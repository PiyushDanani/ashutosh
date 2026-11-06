# check_exact_css.py
import re
import subprocess
import os

test_html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
<div id="wrapper"></div>
<script>
fetch('index.html')
  .then(r => r.text())
  .then(html => {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const modal = doc.getElementById('festive-modal');
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.appendChild(modal);
    
    setTimeout(() => {
      const card = modal.querySelector('div');
      const b = card.getBoundingClientRect();
      const mb = modal.getBoundingClientRect();
      console.log('MODAL_METRICS:' + JSON.stringify({
        windowInnerWidth: window.innerWidth,
        modal: { x: mb.x, width: mb.width },
        card: { x: b.x, width: b.width, right: b.right, left: b.left },
        cardComputedWidth: window.getComputedStyle(card).width,
        cardComputedMaxWidth: window.getComputedStyle(card).maxWidth
      }));
    }, 500);
  });
</script>
</body>
</html>
"""

with open('test_metrics.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_url = "file:///" + os.path.abspath("test_metrics.html").replace("\\", "/")

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--window-size=390,844",
    "--virtual-time-budget=2000",
    "--enable-logging=stderr",
    "--v=1",
    html_url
]

res = subprocess.run(cmd, capture_output=True, text=True)
for line in (res.stdout + res.stderr).splitlines():
    if 'MODAL_METRICS' in line:
        print(line)

os.remove('test_metrics.html')
