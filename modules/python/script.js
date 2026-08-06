const PREFIX = "../../";
const pdfRoot = "3rdSem/PROJECTS/PYTHON/docx/FinalWeeklyReport/pdf";
const docxRoot = "3rdSem/PROJECTS/PYTHON/docx/FinalWeeklyReport/docx";
const GH_FALLBACK = "Sayantan-B-dev/SM_BtechSyllabus";

const u = (p) => encodeURI(p);
const pagePdf = (week, kind, page) =>
  `${u(`${PREFIX}${pdfRoot}/split`)}/Week${week}/${kind}/page-${String(page).padStart(2, "0")}.pdf`;

function openViewer(title, src) {
  window.open(u(src), "_blank", "noopener");
}

async function downloadPrintPages(week, title, pages) {
  if (!pages || !pages.length) return;
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

function weekNoOf(name) {
  const m = name.match(/^Week(\d+)/i);
  return m ? parseInt(m[1], 10) : null;
}

function deriveTitle(name) {
  let t = name.replace(/\.(pdf|docx)$/i, "");
  t = t.replace(/^Week\d+_/, "");
  t = t.replace(/_?\(print\s+[\d,\s]+\s+pages?\)/i, "");
  t = t.replace(/_Report$/i, "");
  return t.split("_").filter(Boolean).join(" ");
}

function ghRepo() {
  try {
    if (location.protocol === "file:") return null;
    const host = location.hostname.toLowerCase();
    if (host === "localhost" || host === "127.0.0.1") return null;
    if (host.endsWith("github.io")) {
      const user = host.split(".")[0];
      const seg = location.pathname.split("/").filter(Boolean);
      const repo = seg.find(s => s !== user);
      if (repo) return `${user}/${repo}`;
    }
  } catch (e) {}
  return GH_FALLBACK;
}

function renderDocxMenu(weeks, docxMap) {
  const docxMenu = document.getElementById("docx-menu");
  docxMenu.innerHTML = "";
  weeks.forEach(w => {
    const name = docxMap && docxMap.get(w.n);
    let docxPath;
    if (name) {
      docxPath = `${docxRoot}/${name}`;
    } else if (w.original) {
      docxPath = w.original.replace(/\/pdf\//, "/docx/").replace(/\.pdf$/i, ".docx");
    } else {
      return;
    }
    const row = document.createElement("a");
    row.className = "docx-row";
    row.href = PREFIX + docxPath;
    row.download = docxPath.split("/").pop();
    row.innerHTML = `<span class="docx-name">Week ${w.n} · ${w.title}</span><span class="docx-dl">Download</span>`;
    docxMenu.appendChild(row);
  });
}

function renderAll(weeks, docxMap) {
  const root = document.getElementById("cards");
  root.innerHTML = "";
  weeks.slice().sort((a, b) => a.n - b.n).forEach(w => {
    if (!w.original) return;

    const card = document.createElement("article");
    card.className = "card";

    const head = document.createElement("header");
    head.className = "card-head";
    const h = document.createElement("h2");
    h.innerHTML = `Week ${w.n} <span class="card-sub">· ${w.title}</span>`;
    const badge = document.createElement("span");
    badge.className = "pages-badge";
    badge.textContent = w.total ? `${w.total} pages` : "Plan pending";
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
        dl.innerHTML = `<svg class="dl-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><svg class="dl-spin" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M21 12a9 9 0 1 1-6.219-8.56"/></svg><span class="dl-label">Download Printing Pages</span>`;
        dl.addEventListener("click", async () => {
          if (dl.disabled) return;
          const label = dl.querySelector(".dl-label");
          const started = Date.now();
          dl.disabled = true;
          dl.classList.add("loading");
          label.textContent = "Merging Pages…";
          await downloadPrintPages(w.n, w.title, w.print);
          const elapsed = Date.now() - started;
          if (elapsed < 2000) await new Promise(r => setTimeout(r, 2000 - elapsed));
          dl.classList.remove("loading");
          dl.disabled = false;
          label.textContent = "Download Printing Pages";
        });
        row.appendChild(dl);
      }
      rows.appendChild(row);
    };

    if (w.print && w.total) {
      const handwrite = [];
      for (let p = 1; p <= w.total; p++) if (!w.print.includes(p)) handwrite.push(p);
      mkRow("print", "Print Pages", w.print);
      mkRow("handwrite", "Handwrite Only", handwrite);
    } else {
      const row = document.createElement("div");
      row.className = "row";
      const lbl = document.createElement("div");
      lbl.className = "row-label";
      lbl.textContent = "Print plan";
      const note = document.createElement("div");
      note.className = "plan-note";
      note.innerHTML = `New PDF detected on GitHub — run <code>node split.js</code> in the pdf folder to generate the print plan.`;
      row.append(lbl, note);
      rows.appendChild(row);
    }

    const openBtn = document.createElement("button");
    openBtn.className = "open-full";
    openBtn.textContent = "Open Full PDF";
    openBtn.addEventListener("click", () =>
      openViewer(`Week ${w.n} · Full Report (${w.total ? w.total : "?"} pages)`, PREFIX + w.original));

    const foot = document.createElement("div");
    foot.className = "row-footer";
    const listSpan = document.createElement("span");
    listSpan.innerHTML = w.print && w.total
      ? `Print: <b>${w.print.join(", ")}</b> · Handwrite: <b>${[...Array(w.total)].map((_, i) => i + 1).filter(p => !w.print.includes(p)).join(", ")}</b>`
      : `<span class="muted">Auto-detected — plan not generated yet.</span>`;
    foot.appendChild(listSpan);

    card.append(head, openBtn, rows, foot);
    root.appendChild(card);
  });
  renderDocxMenu(weeks, docxMap);
}

async function autoMerge() {
  const repo = ghRepo();
  if (!repo) return;
  try {
    const [pdfRes, docxRes] = await Promise.all([
      fetch(`https://api.github.com/repos/${repo}/contents/${pdfRoot}`, { headers: { Accept: "application/vnd.github+json" } }),
      fetch(`https://api.github.com/repos/${repo}/contents/${docxRoot}`, { headers: { Accept: "application/vnd.github+json" } })
    ]);
    if (!pdfRes.ok && !docxRes.ok) return;
    const pdfList = pdfRes.ok ? await pdfRes.json() : [];
    const docxList = docxRes.ok ? await docxRes.json() : [];
    const pdfNames = pdfList.filter(f => f.type === "file" && /^Week\d+_.*\.pdf$/i.test(f.name)).map(f => f.name);
    const docxNames = docxList.filter(f => f.type === "file" && /^Week\d+_.*\.docx$/i.test(f.name)).map(f => f.name);
    const docxMap = new Map(docxNames.map(n => [weekNoOf(n), n]));

    const weeks = window.weeksData.weeks.slice();
    const known = new Set(weeks.map(w => w.n));
    const newNums = new Set([...pdfNames, ...docxNames].map(weekNoOf).filter(n => n && !known.has(n)));
    for (const n of [...newNums].sort((a, b) => a - b)) {
      const pdfName = pdfNames.find(x => weekNoOf(x) === n);
      const docxName = docxNames.find(x => weekNoOf(x) === n);
      weeks.push({
        n,
        title: pdfName ? deriveTitle(pdfName) : deriveTitle(docxName),
        total: null,
        print: null,
        handwrite: null,
        original: pdfName ? `${pdfRoot}/${pdfName}` : null
      });
    }
    renderAll(weeks, docxMap);
  } catch (e) {}
}

document.addEventListener("DOMContentLoaded", () => {
  const weeks = window.weeksData && window.weeksData.weeks;
  if (!weeks) {
    document.getElementById("cards").innerHTML =
      `<p class="no-data">weeks data not found. Run <code>node split.js</code> in the pdf folder to generate it.</p>`;
    return;
  }

  renderAll(weeks, null);

  const docxWrap = document.getElementById("docx-wrap");
  const docxToggle = document.getElementById("docx-toggle");
  function closeDocx() {
    docxWrap.classList.remove("open");
    docxToggle.setAttribute("aria-expanded", "false");
  }
  docxToggle.addEventListener("click", (e) => {
    e.stopPropagation();
    const open = docxWrap.classList.toggle("open");
    docxToggle.setAttribute("aria-expanded", String(open));
  });
  document.addEventListener("click", closeDocx);
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeDocx();
  });

  autoMerge();
});
