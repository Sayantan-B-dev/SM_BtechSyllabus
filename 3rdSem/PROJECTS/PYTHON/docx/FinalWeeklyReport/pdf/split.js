const fs = require("fs");
const path = require("path");
const { PDFDocument } = require("pdf-lib");

const PDF_DIR = __dirname;

function findRepoRoot(dir) {
  let cur = dir;
  while (true) {
    if (fs.existsSync(path.join(cur, ".git"))) return cur;
    const up = path.dirname(cur);
    if (up === cur) throw new Error("Could not locate repo root from " + dir);
    cur = up;
  }
}

const REPO_ROOT = findRepoRoot(PDF_DIR);
const PDF_REL = path.relative(REPO_ROOT, PDF_DIR).split(path.sep).join("/");
const WEEKS_JSON = path.join(REPO_ROOT, "modules", "python", "weeks.json");

function parsePrintFromName(name) {
  const m = name.match(/\(print\s+([\d,\s]+)\s+pages?\)/i);
  if (!m) return null;
  return m[1].split(",").map(s => parseInt(s.trim(), 10)).filter(n => !isNaN(n));
}

function deriveTitle(name) {
  let t = name.replace(/\.pdf$/i, "");
  t = t.replace(/^Week\d+_/, "");
  t = t.replace(/_?\(print\s+[\d,\s]+\s+pages?\)/i, "");
  t = t.replace(/_Report$/i, "");
  return t.split("_").filter(Boolean).join(" ");
}

async function main() {
  const files = fs.readdirSync(PDF_DIR).filter(f => /^Week\d+_.*\.pdf$/i.test(f));
  if (!files.length) {
    console.log("No WeekN_*.pdf files found in " + PDF_DIR);
    return;
  }
  files.sort((a, b) => parseInt(a.match(/^Week(\d+)/i)[1], 10) - parseInt(b.match(/^Week(\d+)/i)[1]));

  fs.rmSync(path.join(PDF_DIR, "split"), { recursive: true, force: true });

  const weeks = [];
  for (const f of files) {
    const n = parseInt(f.match(/^Week(\d+)/i)[1], 10);
    const print = parsePrintFromName(f);
    if (!print) {
      console.log(`SKIP ${f}: no '(print ... pages)' info in filename`);
      continue;
    }
    const doc = await PDFDocument.load(fs.readFileSync(path.join(PDF_DIR, f)));
    const total = doc.getPageCount();
    const handwrite = [];
    for (let p = 1; p <= total; p++) if (!print.includes(p)) handwrite.push(p);

    const weekDir = path.join(PDF_DIR, "split", `Week${n}`);
    for (const kind of ["print", "handwrite"]) {
      const kindDir = path.join(weekDir, kind);
      fs.mkdirSync(kindDir, { recursive: true });
      for (const p of (kind === "print" ? print : handwrite)) {
        const out = await PDFDocument.create();
        const [copied] = await out.copyPages(doc, [p - 1]);
        out.addPage(copied);
        fs.writeFileSync(path.join(kindDir, `page-${String(p).padStart(2, "0")}.pdf`), await out.save());
      }
    }

    weeks.push({
      n,
      title: deriveTitle(f),
      total,
      print,
      handwrite,
      original: `${PDF_REL}/${f}`
    });
    console.log(`Week ${n}: ${total} pages -> print [${print}] / handwrite [${handwrite}]`);
  }

  const data = { generated: new Date().toISOString(), pdfRoot: PDF_REL, weeks };
  fs.writeFileSync(WEEKS_JSON, `window.weeksData = ${JSON.stringify(data, null, 2)};\n`);
  console.log(`Wrote ${WEEKS_JSON} (${weeks.length} weeks)`);
}

main().catch(e => { console.error(e); process.exit(1); });
