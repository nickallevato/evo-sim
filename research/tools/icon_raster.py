"""Rasterize docs/img/icon.svg into PNG sizes, a favicon.ico and the 1280x640 social preview.
Needs headless Chrome (puppeteer cache) and ImageMagick (`magick` or `convert`) for the .ico.
    research/.venv/bin/python -I research/tools/icon.py && research/.venv/bin/python -I research/tools/icon_raster.py
"""
import glob, os, shutil, subprocess, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IMG = os.path.join(ROOT, "docs", "img")
CHROME = sorted(glob.glob(os.path.expanduser("~/.cache/puppeteer/chrome-headless-shell/*/*/chrome-headless-shell")))[-1]
icon = open(os.path.join(IMG, "icon.svg")).read()
tmp = tempfile.mkdtemp()

def shot(html, w, h, out):
    page = os.path.join(tmp, "p.html")
    open(page, "w").write(f"<!doctype html><meta charset=utf-8><style>html,body{{margin:0;background:transparent}}</style>{html}")
    subprocess.run([CHROME, "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--default-background-color=00000000",
                    f"--window-size={w},{h}", f"--screenshot={out}", "file://" + page], check=True, capture_output=True)

sized = icon.replace("<svg ", '<svg style="display:block" width="{s}" height="{s}" ', 1)
for s in (16, 32, 48, 64, 180, 512):
    shot(sized.replace("{s}", str(s)), s, s, os.path.join(IMG, f"icon-{s}.png"))

im = shutil.which("magick") or shutil.which("convert")
if im:
    subprocess.run([im] + [os.path.join(IMG, f"icon-{s}.png") for s in (16, 32, 48, 64)] + [os.path.join(IMG, "favicon.ico")], check=True)

social = f"""<div style="width:1280px;height:640px;box-sizing:border-box;padding:0 96px;display:flex;align-items:center;gap:72px;
background:linear-gradient(135deg,#1e293b,#0b1120);font-family:'DejaVu Sans',sans-serif;color:#f8fafc">
{sized.replace("{s}", "360")}
<div><div style="font-size:92px;font-weight:700;letter-spacing:-2px">evo-sim</div>
<div style="font-size:34px;line-height:1.35;color:#cbd5e1;margin-top:18px">An open, two-sided audit of the<br>math for and against evolution,<br>then a simulator you control.</div>
<div style="margin-top:30px;font-size:26px"><span style="color:#f59e0b">&#9632; Day</span>&nbsp;&nbsp;&nbsp;<span style="color:#3b82f6">&#9632; critics</span>&nbsp;&nbsp;&nbsp;<span style="color:#94a3b8">every claim checked</span></div></div></div>"""
shot(social, 1280, 640, os.path.join(IMG, "social-preview.png"))
shutil.rmtree(tmp)
print("wrote icon-{16,32,48,64,180,512}.png", "favicon.ico" if im else "(no ImageMagick: skipped favicon.ico)", "social-preview.png")
