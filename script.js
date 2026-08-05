const base = "3rdSem/PROJECTS/PYTHON/docx/FinalWeeklyReport/pdf";
const splitRoot = base + "/split";

const weeks = [
  { n: 1, total: 6, title: "Student Grade Management System", print: [1, 3, 4, 6] },
  { n: 2, total: 8, title: "Electricity Bill Calculator & ATM Simulator", print: [1, 4, 5, 6, 8] },
  { n: 3, total: 9, title: "Bank, Hotel & Library Systems", print: [1, 3, 5, 7, 9] },
  { n: 4, total: 7, title: "Password Strength & Email Validation", print: [1, 3, 5, 7] }
];

const originals = {
  1: `${base}/Week1_(print 1,3,4,6 pages)_Student_Grade_Management_System_Report.pdf`,
  2: `${base}/Week2_(print 1,4,5,6,8 pages)_Electricity_Bill_Calculator_and_ATM_Simulator_Report.pdf`,
  3: `${base}/Week3_(print 1,3,5,7,9 pages)_Combined_Report_Bank_Hotel_Library.pdf`,
  4: `${base}/Week4_(print 1,3,5,7 pages)_Password_Strength_Email_Validation_Report.pdf`
};

const u = (p) => encodeURI(p);
const pagePdf = (week, kind, page) =>
  `${u(splitRoot)}/Week${week}/${kind}/page-${String(page).padStart(2, "0")}.pdf`;

function openViewer(title, src) {
  const viewer = document.getElementById("viewer");
  const frame = document.getElementById("viewer-frame");
  document.getElementById("viewer-title").textContent = title;
  frame.src = u(src);
  viewer.classList.add("open");
  frame.scrollTo(0, 0);
}

function closeViewer() {
  document.getElementById("viewer").classList.remove("open");
  document.getElementById("viewer-frame").src = "about:blank";
}

document.addEventListener("DOMContentLoaded", () => {
  const root = document.getElementById("cards");

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
      rows.appendChild(row);
    };

    mkRow("print", "Print Pages", w.print);
    mkRow("handwrite", "Handwrite Only", handwrite);

    const foot = document.createElement("div");
    foot.className = "row-footer";
    const openBtn = document.createElement("button");
    openBtn.className = "open-full";
    openBtn.textContent = "Open Full PDF";
    openBtn.addEventListener("click", () =>
      openViewer(`Week ${w.n} · Full Report (${w.total} pages)`, originals[w.n]));
    const listSpan = document.createElement("span");
    listSpan.innerHTML = `Print: <b>${w.print.join(", ")}</b> · Handwrite: <b>${handwrite.join(", ")}</b>`;
    foot.append(openBtn, listSpan);

    card.append(head, rows, foot);
    root.appendChild(card);
  });

  document.getElementById("viewer-close").addEventListener("click", closeViewer);
});
