# apply_mobile_overflow_fixes.py
import re
import os

# 1. Update build_ultimate_site.py
with open("build_ultimate_site.py", "r", encoding="utf-8") as f:
    bus = f.read()

# Replace style block
old_bus_style_pattern = re.compile(
    r'<style>\s*body\s*\{\{.*?\}\}\s*\.font-industrial',
    re.DOTALL
)

new_bus_style = """<style>
    *, *::before, *::after {{
      box-sizing: border-box;
    }}
    html, body {{
      font-family: 'Outfit', sans-serif;
      background-color: #f8fafc;
      color: #1e293b;
      overflow-x: hidden !important;
      max-width: 100% !important;
      width: 100% !important;
      position: relative;
      touch-action: pan-y;
      -webkit-overflow-scrolling: touch;
    }}
    img, video, canvas, svg {{
      max-width: 100%;
      height: auto;
    }}
    .font-industrial"""

bus, count1 = old_bus_style_pattern.subn(new_bus_style, bus)
with open("build_ultimate_site.py", "w", encoding="utf-8") as f:
    f.write(bus)
print(f"Updated build_ultimate_site.py: {count1} replacements")

# 2. Update generate_ultimate_multipage.py
with open("generate_ultimate_multipage.py", "r", encoding="utf-8") as f:
    gum = f.read()

# Replace header bar
old_header_pattern = re.compile(
    r'<!-- TOP CORPORATE CREDENTIALS & DIRECT CALL BAR -->.*?<!-- MAIN NAVIGATION BAR -->',
    re.DOTALL
)

new_header = """<!-- TOP CORPORATE CREDENTIALS & DIRECT CALL BAR -->
    <header class="bg-brand-dark text-slate-200 border-b border-slate-800 text-[11px] sm:text-xs py-1.5 px-3 sm:px-6 overflow-hidden">
      <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-y-1.5 gap-x-2 sm:gap-x-4">
        
        <!-- Corporate Reg Badges -->
        <div class="flex items-center flex-wrap gap-x-2 sm:gap-x-3 gap-y-1 font-medium">
          <span class="inline-flex items-center gap-1 text-amber-400 font-bold whitespace-nowrap">
            <i class="fa-solid fa-certificate text-[11px]"></i> Govt. Approved Contractor
          </span>
          <span class="text-slate-600 hidden sm:inline">|</span>
          <span class="text-slate-300 hidden md:inline whitespace-nowrap">
            <strong class="text-white">CIN:</strong> {CIN}
          </span>
          <span class="text-slate-600 hidden lg:inline">|</span>
          <span class="text-slate-300 hidden lg:inline whitespace-nowrap">
            <strong class="text-white">PAN:</strong> {PAN} &nbsp;|&nbsp; <strong class="text-white">TAN:</strong> {TAN}
          </span>
        </div>

        <!-- Direct Key Contacts -->
        <div class="flex flex-wrap items-center gap-1.5 sm:gap-3 font-semibold ml-auto">
          <a href="tel:{PHONE_ALPESH_RAW}" class="inline-flex items-center gap-1 bg-slate-800/90 hover:bg-slate-700 text-amber-300 border border-amber-500/30 px-2 sm:px-2.5 py-1 rounded-full transition-colors text-[10px] sm:text-xs whitespace-nowrap">
            <i class="fa-solid fa-phone text-[9px] sm:text-[10px]"></i>
            <span><span class="hidden xs:inline">Alpesh: </span><strong class="text-white">{PHONE_ALPESH}</strong></span>
          </a>
          <a href="tel:{PHONE_BHAGIRATH_RAW}" class="inline-flex items-center gap-1 bg-amber-500 hover:bg-amber-400 text-slate-950 px-2 sm:px-2.5 py-1 rounded-full transition-colors font-bold shadow-sm text-[10px] sm:text-xs whitespace-nowrap">
            <i class="fa-solid fa-phone text-[9px] sm:text-[10px]"></i>
            <span><span class="hidden xs:inline">Bhagirath: </span><strong class="text-slate-950">{PHONE_BHAGIRATH}</strong></span>
          </a>
        </div>

      </div>
    </header>

    <!-- MAIN NAVIGATION BAR -->"""

gum, count2 = old_header_pattern.subn(new_header, gum)

# Replace brand logo anchor
old_logo_pattern = re.compile(
    r'<!-- Brand Logo & Identity \(Strictly Single Line\) -->\s*<a href="index\.html".*?</a>',
    re.DOTALL
)

new_logo = """<!-- Brand Logo & Identity (Responsive Single Line) -->
          <a href="index.html" class="flex items-center gap-2 sm:gap-3 min-w-0 max-w-[calc(100%-55px)] lg:max-w-none group py-1" title="{COMPANY_NAME}">
            <div class="relative w-9 h-9 sm:w-12 sm:h-12 bg-white p-1 rounded-xl shadow-sm border border-slate-200 flex items-center justify-center overflow-hidden flex-shrink-0 group-hover:scale-105 transition-transform">
              <img src="assets/images/logo-transparent.png" alt="Ashutosh Build Stone Logo" class="w-full h-full object-contain" width="48" height="48">
            </div>
            <div class="flex flex-col justify-center min-w-0">
              <div class="flex items-center gap-1 sm:gap-1.5">
                <span class="text-base sm:text-xl lg:text-2xl font-black font-industrial uppercase tracking-tight sm:tracking-wide text-brand-navy leading-none truncate">
                  ASHUTOSH BUILD STONE
                </span>
                <span class="text-[8px] sm:text-[10px] font-extrabold bg-blue-900 text-amber-400 px-1 sm:px-1.5 py-0.5 rounded leading-none uppercase tracking-wider flex-shrink-0">
                  PVT. LTD.
                </span>
              </div>
              <p class="text-[8px] sm:text-[10px] font-bold text-slate-500 uppercase tracking-wider sm:tracking-widest mt-0.5 sm:mt-1 leading-none truncate">
                Aggregate &bull; Black Trap &bull; Sand Production
              </p>
            </div>
          </a>"""

gum, count3 = old_logo_pattern.subn(new_logo, gum)

# Replace get_geo_ai_factsheet
old_geo_pattern = re.compile(
    r'def get_geo_ai_factsheet\(page_context="General"\):.*?return f\"\"\"(.*?)\"\"\"',
    re.DOTALL
)

new_geo_func = '''def get_geo_ai_factsheet(page_context="General"):
    return f"""  <!-- GEO & AEO KNOWLEDGE CAPSULE (GENERATIVE AI ENGINE CITATION BLOCK) -->
  <aside class="geo-factsheet bg-slate-900 border-y border-slate-800 py-3.5 px-3 sm:px-6 text-slate-300 text-xs overflow-hidden">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-start md:items-center justify-between gap-2.5 sm:gap-3">
      <div class="flex items-center gap-2 text-amber-400 font-bold uppercase tracking-wider text-[11px] sm:whitespace-nowrap">
        <i class="fa-solid fa-brain"></i>
        <span>Generative Engine / Factual Entity Record</span>
      </div>
      <div class="flex flex-wrap items-center gap-x-3 sm:gap-x-4 gap-y-1 text-[11px] text-slate-400 break-words">
        <span><strong>Legal Name:</strong> {COMPANY_NAME}</span>
        <span>&bull;</span>
        <span><strong>CIN:</strong> {CIN}</span>
        <span>&bull;</span>
        <span><strong>Headquarters:</strong> Borda, Talaja, Bhavnagar, Gujarat (Pin: 364130)</span>
        <span>&bull;</span>
        <span><strong>Standard:</strong> IS 383:2016 Compliant</span>
        <span>&bull;</span>
        <span><strong>Daily Throughput:</strong> 1,500+ MT Crushed Basalt & Washed Sand</span>
      </div>
      <div class="text-[11px] text-amber-300 font-semibold sm:whitespace-nowrap md:ml-auto">
        <i class="fa-solid fa-shield-check text-emerald-400 mr-1"></i> Verified Corporate Profile
      </div>
    </div>
  </aside>"""'''

gum, count4 = old_geo_pattern.subn(new_geo_func, gum)

with open("generate_ultimate_multipage.py", "w", encoding="utf-8") as f:
    f.write(gum)
print(f"Updated generate_ultimate_multipage.py: header={count2}, logo={count3}, geo={count4}")

# 3. Update build_pages.py
with open("build_pages.py", "r", encoding="utf-8") as f:
    bp = f.read()

# Replace mobile bottom action bar
old_mobile_bar_pattern = re.compile(
    r'<!-- FLOATING BOTTOM ACTION BAR FOR MOBILE -->.*?<!-- FLOATING DESKTOP WHATSAPP BADGE -->',
    re.DOTALL
)

new_mobile_bar = """<!-- FLOATING BOTTOM ACTION BAR FOR MOBILE -->
  <div class="fixed bottom-0 left-0 right-0 z-40 bg-brand-dark/95 backdrop-blur-md border-t border-slate-800 px-2 sm:px-3 py-2 sm:py-2.5 flex items-center justify-between gap-1.5 sm:gap-2 md:hidden shadow-2xl max-w-full">
    <a href="tel:7878999033" class="flex-1 min-w-0 bg-amber-500 text-slate-950 font-bold py-2.5 px-1.5 sm:px-2 rounded-lg text-center text-xs flex items-center justify-center gap-1 sm:gap-1.5 shadow-md truncate">
      <i class="fa-solid fa-phone text-[10px] sm:text-xs flex-shrink-0"></i>
      <span class="truncate">Bhagirath Sinh</span>
    </a>
    <a href="tel:7623998398" class="flex-1 min-w-0 bg-slate-800 text-amber-300 border border-amber-500/30 font-bold py-2.5 px-1.5 sm:px-2 rounded-lg text-center text-xs flex items-center justify-center gap-1 sm:gap-1.5 shadow-md truncate">
      <i class="fa-solid fa-phone text-[10px] sm:text-xs flex-shrink-0"></i>
      <span class="truncate">Alpesh Chauhan</span>
    </a>
    <a href="https://wa.me/917878999033" target="_blank" rel="noopener noreferrer" class="w-10 h-10 sm:w-11 sm:h-11 bg-[#25D366] text-white rounded-lg flex items-center justify-center text-lg sm:text-xl shadow-lg flex-shrink-0" title="WhatsApp" aria-label="Chat on WhatsApp">
      <i class="fa-brands fa-whatsapp"></i>
    </a>
  </div>

  <!-- FLOATING DESKTOP WHATSAPP BADGE -->"""

bp, count5 = old_mobile_bar_pattern.subn(new_mobile_bar, bp)

with open("build_pages.py", "w", encoding="utf-8") as f:
    f.write(bp)
print(f"Updated build_pages.py mobile bar: {count5}")

# 4. Update generate_index_page.py
with open("generate_index_page.py", "r", encoding="utf-8") as f:
    gip = f.read()

# Fix estimator padding and grid
gip = gip.replace(
    'p-6 sm:p-10 text-white shadow-2xl border border-slate-800',
    'p-4 sm:p-8 lg:p-10 text-white shadow-2xl border border-slate-800'
)

gip = gip.replace(
    '<div class="grid grid-cols-3 gap-3">\n              <div>\n                <label id="label-len"',
    '<div class="grid grid-cols-1 sm:grid-cols-3 gap-3">\n              <div class="min-w-0">\n                <label id="label-len"'
)
gip = gip.replace(
    '</div>\n              <div>\n                <label id="label-wid"',
    '</div>\n              <div class="min-w-0">\n                <label id="label-wid"'
)
gip = gip.replace(
    '</div>\n              <div>\n                <label id="label-dep"',
    '</div>\n              <div class="min-w-0">\n                <label id="label-dep"'
)

# Fix heading text sizes for mobile
gip = gip.replace(
    'text-3xl font-black font-industrial uppercase text-brand-navy mt-1">Explore Our Full Corporate Sections',
    'text-2xl sm:text-3xl font-black font-industrial uppercase text-brand-navy mt-1">Explore Our Full Corporate Sections'
)

gip = gip.replace(
    'text-3xl sm:text-4xl font-black font-industrial uppercase text-white">\n            Material Quantity & Brass / Ton Estimator',
    'text-2xl sm:text-3xl lg:text-4xl font-black font-industrial uppercase text-white">\n            Material Quantity & Brass / Ton Estimator'
)

# Fix corporate sections cards gap & padding
gip = gip.replace(
    '<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">',
    '<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3 sm:gap-4">'
)
gip = re.sub(
    r'<a href="([^"]+)" class="p-4 bg-slate-50',
    r'<a href="\1" class="p-3 sm:p-4 bg-slate-50',
    gip
)

# Fix volume unit encoding
gip = gip.replace('id="res-cu-m">17.7 mA3 (625 Cu.Ft)</div>', 'id="res-cu-m">17.7 m³ (625 Cu.Ft)</div>')
gip = gip.replace('m³', 'm³')

with open("generate_index_page.py", "w", encoding="utf-8") as f:
    f.write(gip)
print("Updated generate_index_page.py")

# 5. Update generate_remaining_expanded.py
with open("generate_remaining_expanded.py", "r", encoding="utf-8") as f:
    gre = f.read()

# Fix calculator page estimator
gre = gre.replace(
    'p-6 sm:p-10 text-white shadow-2xl border border-slate-800',
    'p-4 sm:p-8 lg:p-10 text-white shadow-2xl border border-slate-800'
)
gre = gre.replace(
    '<div class="grid grid-cols-3 gap-3">\n              <div>\n                <label id="label-len"',
    '<div class="grid grid-cols-1 sm:grid-cols-3 gap-3">\n              <div class="min-w-0">\n                <label id="label-len"'
)
gre = gre.replace(
    '</div>\n              <div>\n                <label id="label-wid"',
    '</div>\n              <div class="min-w-0">\n                <label id="label-wid"'
)
gre = gre.replace(
    '</div>\n              <div>\n                <label id="label-dep"',
    '</div>\n              <div class="min-w-0">\n                <label id="label-dep"'
)

with open("generate_remaining_expanded.py", "w", encoding="utf-8") as f:
    f.write(gre)
print("Updated generate_remaining_expanded.py")

print("All code generation scripts updated successfully.")
