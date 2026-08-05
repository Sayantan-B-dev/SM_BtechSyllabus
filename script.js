const PREFIX = "";
const pdfRoot = "3rdSem/PROJECTS/PYTHON/docx/FinalWeeklyReport/pdf";

const u = (p) => encodeURI(p);
const pagePdf = (week, kind, page) =>
  `${u(`${PREFIX}${pdfRoot}/split`)}/Week${week}/${kind}/page-${String(page).padStart(2, "0")}.pdf`;

function openViewer(title, src) {
  window.open(u(src), "_blank", "noopener");
}

async function downloadPrintPages(week, title, pages) {
  try {
    const merged = await PDFLib.PDFDocument.create();
    for (const p of pages) {
      const resp = await fetch(pagePdf(week, "print", p));
      if (!resp.ok) throw new Error(`Failed to load page ${p}`);
      const src = await PDFLib.PDFDocument.load(await resp.arrayBuffer());
      const copied = await merged.copyPages(src, src.getPageIndices());
      copied.forEach(cp => merged.addPage(cp));
    }
    const bytes = await merged.save();
    const blob = new Blob([bytes], { type: "application/pdf" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `Week${week}_${title.replace(/\s+/g, "_")}_Print_Pages.pdf`;
    a.click();
    URL.revokeObjectURL(url);
  } catch (e) {
    alert("Merge failed: " + e.message);
  }
}

document.addEventListener("DOMContentLoaded", async () => {
  const root = document.getElementById("cards");

  let weeks;
  try {
    const resp = await fetch("weeks.json");
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    weeks = (await resp.json()).weeks;
  } catch (e) {
    root.innerHTML = `<p class="no-data">weeks.json not found. Run <code>node split.js</code> in the pdf folder to generate the week data.</p>`;
    return;
  }

  weeks.forEach(w => {
    const handwrite = [];
    for (let p = 1; p <= w.total; p++) if (!w.print.includes(p)) handwrite.push(p);

    const card = document.createElement("article");
    card.className = "card";

    const head = document.createElement("header");
    head.className = "card-head";
    const h = document.createElement("h2");
    h.innerHTML = `Week ${w.n} <span class="card-sub">· ${w.title}</span>`;
    const badge = document.createElement("span");
    badge.className = "pages-badge";
    badge.textContent = `${w.total} pages`;
    head.append(h, badge);

    const rows = document.createElement("div");
    rows.className = "rows";

    const mkRow = (kind, label, pages) => {
      const row = document.createElement("div");
      row.className = `row ${kind}`;
      const lbl = document.createElement("div");
      lbl.className = "row-label";
      lbl.textContent = label;
      const chips = document.createElement("div");
      chips.className = "chips";
      pages.forEach(p => {
        const chip = document.createElement("button");
        chip.className = "page-chip";
        chip.textContent = p;
        chip.title = `Page ${p}`;
        chip.addEventListener("click", () =>
          openViewer(`Week ${w.n} · ${label} · Page ${p}`, pagePdf(w.n, kind, p)));
        chips.appendChild(chip);
      });
      row.append(lbl, chips);
      if (kind === "print") {
        const dl = document.createElement("button");
        dl.className = "download-print";
        dl.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>Download Printing Pages`;
        dl.addEventListener("click", () => downloadPrintPages(w.n, w.title, w.print));
        row.appendChild(dl);
      }
      rows.appendChild(row);
    };

    mkRow("print", "Print Pages", w.print);
    mkRow("handwrite", "Handwrite Only", handwrite);

    const openBtn = document.createElement("button");
    openBtn.className = "open-full";
    openBtn.textContent = "Open Full PDF";
    openBtn.addEventListener("click", () =>
      openViewer(`Week ${w.n} · Full Report (${w.total} pages)`, u(w.original)));
    const foot = document.createElement("div");
    foot.className = "row-footer";
    const listSpan = document.createElement("span");
    listSpan.innerHTML = `Print: <b>${w.print.join(", ")}</b> · Handwrite: <b>${handwrite.join(", ")}</b>`;
    foot.appendChild(listSpan);

    card.append(head, openBtn, rows, foot);
    root.appendChild(card);
  });
});
