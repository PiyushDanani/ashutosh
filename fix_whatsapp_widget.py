# fix_whatsapp_widget.py
import re
import os

OLD_BADGE_PATTERN = re.compile(
    r'<!-- FLOATING DESKTOP WHATSAPP BADGE -->\s*<a\s+href="https://wa\.me/917878999033[^>]*>.*?</a>',
    re.DOTALL
)

NEW_BADGE_HTML = """<!-- FLOATING DESKTOP WHATSAPP BADGE -->
  <a href="https://wa.me/917878999033?text=Namaste,%20I%20am%20inquiring%20about%20materials%20from%20Ashutosh%20Build%20Stone%20Pvt.%20Ltd." target="_blank" rel="noopener noreferrer" class="hidden md:flex fixed bottom-6 left-6 z-50 items-center gap-2.5 bg-[#25D366] hover:bg-[#20ba59] text-white pl-3.5 pr-4 py-3 rounded-full shadow-xl hover:shadow-2xl transition-all duration-300 transform hover:scale-105 border-2 border-white/20 group" title="Direct WhatsApp Order Desk" aria-label="Direct WhatsApp Order Desk">
    <span class="relative flex items-center justify-center">
      <i class="fa-brands fa-whatsapp text-2xl"></i>
      <span class="absolute -top-1 -right-1 flex h-2.5 w-2.5">
        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-white opacity-75"></span>
        <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-200"></span>
      </span>
    </span>
    <div class="flex flex-col text-left leading-tight">
      <span class="text-[10px] font-semibold text-emerald-100 uppercase tracking-wider">Direct Dispatch</span>
      <span class="text-xs font-bold whitespace-nowrap text-white">WhatsApp Order Desk</span>
    </div>
  </a>"""

PULSE_CALL_CSS = """    .pulse-call {
      animation: pulseAnimation 2s infinite;
    }
    @keyframes pulseAnimation {
      0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.6); }
      70% { box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
      100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
    }"""

CLEAN_PULSE_CSS = """    .pulse-call {
      transition: transform 0.2s ease;
    }"""

files_to_update = [
    "index.html",
    "about.html",
    "products.html",
    "plant.html",
    "contracting.html",
    "calculator.html",
    "gallery.html",
    "contact.html",
]

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, count = OLD_BADGE_PATTERN.subn(NEW_BADGE_HTML, content)
        if PULSE_CALL_CSS in new_content:
            new_content = new_content.replace(PULSE_CALL_CSS, CLEAN_PULSE_CSS)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}: replaced badge count = {count}")

# Also update build_pages.py
if os.path.exists("build_pages.py"):
    with open("build_pages.py", 'r', encoding='utf-8') as f:
        bp_content = f.read()
    bp_content, count = OLD_BADGE_PATTERN.subn(NEW_BADGE_HTML, bp_content)
    with open("build_pages.py", 'w', encoding='utf-8') as f:
        f.write(bp_content)
    print(f"Updated build_pages.py: replaced badge count = {count}")

# Also update build_ultimate_site.py
if os.path.exists("build_ultimate_site.py"):
    with open("build_ultimate_site.py", 'r', encoding='utf-8') as f:
        bus_content = f.read()
    old_css_bus = """    .pulse-call {{
      animation: pulseAnimation 2s infinite;
    }}
    @keyframes pulseAnimation {{
      0% {{ box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.6); }}
      70% {{ box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }}
    }}"""
    new_css_bus = """    .pulse-call {{
      transition: transform 0.2s ease;
    }}"""
    if old_css_bus in bus_content:
        bus_content = bus_content.replace(old_css_bus, new_css_bus)
        with open("build_ultimate_site.py", 'w', encoding='utf-8') as f:
            f.write(bus_content)
        print("Updated build_ultimate_site.py pulse css")

print("All files updated successfully.")
