# generate_index_page.py
import json
from build_ultimate_site import build_head
from generate_ultimate_multipage import (
    BASE_URL, COMPANY_NAME, CIN, PAN, TAN,
    PHONE_BHAGIRATH, PHONE_BHAGIRATH_RAW, PHONE_ALPESH, PHONE_ALPESH_RAW,
    ADDRESS, LATITUDE, LONGITUDE,
    get_global_schema, get_header_nav, get_geo_ai_factsheet, get_aeo_faq_component
)
from build_pages import FOOTER_HTML

index_faqs = [
    (
        "Where is Ashutosh Build Stone Pvt. Ltd. plant located?",
        "Our high-capacity stone crushing and sand washing plant is located on Gopnath Road, At. Borda, Tal. Talaja, Dist. Bhavnagar, Gujarat - 364130, India. We are conveniently situated ~12 km from Talaja, ~25 km from Alang Shipyard, and ~65 km from Bhavnagar City, enabling fast site delivery."
    ),
    (
        "What products does Ashutosh Build Stone manufacture?",
        "We manufacture IS 383:2016 certified 20mm Black Trap Aggregate (Kapchi / Jelly), 10mm Grit / Chipping, 40mm Coarse Aggregate Ballast, Hydro-Washed Manufactured Sand (M-Sand - Zone II), Plaster Sand (P-Sand - Zone IV), Granular Sub-Base (GSB), WMM, Quarry Rubble, and Ready Mix Concrete (RMC) from M15 to M40 grades."
    ),
    (
        "Why is your Manufactured Sand (M-Sand) superior to river sand?",
        "Our M-Sand is produced through state-of-the-art CDE hydrocyclone washing which eliminates micro-dust and keeps silt content under 3% (compared to 7-15% in river sand). Its cubical, sharp-edged geometry creates 15% to 20% higher bonding strength with cement, lowers water demand, and avoids harmful organic matter."
    ),
    (
        "Is Ashutosh Build Stone a Government Approved Building Contractor?",
        "Yes, Ashutosh Build Stone Pvt. Ltd. (CIN: U43299GJ2025PTC159486) is a certified Government Approved Building Contractor. We execute highway construction, PWD road projects, industrial civil earthworks, and bulk material supply for government infrastructure across Gujarat."
    ),
    (
        "What is the daily production capacity of your plant?",
        "Our Borda (Talaja) plant has an uninterrupted daily production capacity of over 1,500 Metric Tons (MT) of crushed basalt stone aggregates and hydro-washed sands, supported by captive basalt quarries, multiple screening decks, and a dedicated transport fleet."
    ),
    (
        "How can I request an instant price quotation or place a bulk order?",
        "You can directly call our Directors: Mr. Bhagirath Sinh Sarviya at +91 78789 99033 (Plant & Supply) or Alpesh Chauhan at +91 76239 98398 (Sales & Tenders). You can also click the WhatsApp button on our website for instant dispatch rates within 10 minutes."
    )
]

schema = get_global_schema(
    "Ashutosh Build Stone Pvt. Ltd. | Aggregate, Black Trap & Sand Production | Govt. Approved Contractor",
    "Leading Manufacturer of Black Trap Aggregates (10mm, 20mm, 40mm), Washed M-Sand, Plaster Sand, GSB, and Govt. Approved Contractor in Bhavnagar, Gujarat.",
    f"{BASE_URL}/index.html",
    "WebPage",
    index_faqs
)

head = build_head(
    "Ashutosh Build Stone Pvt. Ltd. | Aggregate, Black Trap & Sand Production",
    "Leading Manufacturer of Black Trap Aggregates (10mm, 20mm, 40mm), Washed M-Sand, Plaster Sand, GSB, and Govt. Approved Contractor in Bhavnagar, Gujarat.",
    "Ashutosh Build Stone, Black Trap Aggregate, M-Sand Bhavnagar, Stone Crusher Talaja, 20mm Jelly, 10mm Grit, 40mm Aggregate, Plaster Sand Gujarat, Govt Approved Contractor, RMC Batching Plant Borda",
    f"{BASE_URL}/index.html",
    schema
)

nav = get_header_nav("home")
factsheet = get_geo_ai_factsheet("Home")
faqs_html = get_aeo_faq_component(index_faqs, "Frequently Asked Questions (AEO & AI Voice Search)")

body = f"""{head}
{nav}
{factsheet}

  <!-- HERO SECTION -->
  <section id="home" class="relative bg-brand-navy min-h-[640px] lg:min-h-[720px] flex items-center text-white overflow-hidden">
    <div class="absolute inset-0 z-0">
      <img src="assets/images/sand-washing-crusher-plant-hd.jpeg" alt="Crushing and Sand Washing Facility" class="w-full h-full object-cover object-center filter brightness-[0.28] scale-105 transform hover:scale-100 transition-transform duration-1000" width="1376" height="768">
      <div class="absolute inset-0 hero-gradient"></div>
    </div>

    <div class="absolute inset-0 bg-[radial-gradient(#ffffff0a_1px,transparent_1px)] [background-size:24px_24px] pointer-events-none opacity-40"></div>

    <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-24">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Hero Text Content -->
        <div class="lg:col-span-7 space-y-6">
          <div class="flex flex-wrap items-center gap-2.5">
            <span class="inline-flex items-center gap-1.5 bg-amber-500/20 text-amber-300 border border-amber-500/40 px-3.5 py-1 rounded-full text-xs font-bold uppercase tracking-wider backdrop-blur-sm">
              <i class="fa-solid fa-award"></i> Govt. Approved Building Contractor
            </span>
            <span class="inline-flex items-center gap-1.5 bg-blue-500/20 text-blue-300 border border-blue-500/40 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider backdrop-blur-sm">
              <i class="fa-solid fa-shield-halved"></i> IS 383:2016 Compliant
            </span>
          </div>

          <div>
            <h2 class="text-amber-400 font-hindi-motto text-2xl sm:text-3xl font-extrabold tracking-wide drop-shadow-md mb-2">
              "हमारे साथ, निर्माण बने आसान"
            </h2>
            <h1 class="text-4xl sm:text-5xl lg:text-6xl font-black font-industrial tracking-wide uppercase leading-tight text-white drop-shadow-lg">
              ASHUTOSH BUILD STONE <span class="text-amber-400">PVT. LTD.</span>
            </h1>
            <p class="text-lg sm:text-xl font-medium text-slate-300 mt-2 font-hindi-motto">
              "निर्माण मटेरियल जो करे आपके सपनों की रक्षा"
            </p>
          </div>

          <p class="speakable-summary text-base sm:text-lg text-slate-300 max-w-2xl leading-relaxed">
            Gujarat's trusted high-capacity production facility for <strong>Black Trap Aggregates (10mm, 20mm, 40mm)</strong>, 
            eco-friendly <strong>Manufactured Sand (M-Sand)</strong>, Plaster Sand, GSB, and Ready-Mix Concrete. 
            Engineered for unmatched compressive strength and bulk on-time site delivery.
          </p>

          <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 pt-2">
            <div class="bg-slate-900/70 border border-slate-700/80 p-3 rounded-lg backdrop-blur-sm">
              <i class="fa-solid fa-water text-cyan-400 text-lg mb-1 block"></i>
              <div class="text-sm font-bold text-white">Save Water & Sand</div>
              <div class="text-[11px] text-slate-400">Hydro-Washed Purity</div>
            </div>
            <div class="bg-slate-900/70 border border-slate-700/80 p-3 rounded-lg backdrop-blur-sm">
              <i class="fa-solid fa-weight-hanging text-amber-400 text-lg mb-1 block"></i>
              <div class="text-sm font-bold text-white">100% Accurate Weight</div>
              <div class="text-[11px] text-slate-400">Digital Weighbridge</div>
            </div>
            <div class="bg-slate-900/70 border border-slate-700/80 p-3 rounded-lg backdrop-blur-sm col-span-2 sm:col-span-1">
              <i class="fa-solid fa-truck-fast text-emerald-400 text-lg mb-1 block"></i>
              <div class="text-sm font-bold text-white">Fleet Logistics</div>
              <div class="text-[11px] text-slate-400">Direct Site Delivery</div>
            </div>
          </div>

          <div class="flex flex-wrap items-center gap-4 pt-4">
            <a href="tel:{PHONE_BHAGIRATH_RAW}" class="inline-flex items-center justify-center gap-2.5 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black px-7 py-4 rounded-xl text-base shadow-lg shadow-amber-500/25 transition-all transform hover:-translate-y-0.5">
              <i class="fa-solid fa-phone-volume text-lg"></i>
              <span>Call Bhagirath Sinh</span>
            </a>
            <a href="tel:{PHONE_ALPESH_RAW}" class="inline-flex items-center justify-center gap-2.5 bg-slate-800 hover:bg-slate-700 text-amber-300 font-bold px-6 py-4 rounded-xl text-base border border-amber-500/40 shadow-lg transition-all transform hover:-translate-y-0.5">
              <i class="fa-solid fa-phone text-lg"></i>
              <span>Call Alpesh Chauhan</span>
            </a>
            <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}?text=Namaste,%20I%20need%20a%20quotation%20for%20Black%20Trap%20Aggregates%20/%20Sand%20from%20Ashutosh%20Build%20Stone%20Pvt.%20Ltd." target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2 bg-[#25D366] hover:bg-[#20ba59] text-white font-bold px-6 py-4 rounded-xl text-base shadow-lg shadow-emerald-600/30 transition-all transform hover:-translate-y-0.5">
              <i class="fa-brands fa-whatsapp text-xl"></i>
              <span>WhatsApp Order</span>
            </a>
          </div>

          <div class="pt-4 text-xs text-slate-400 border-t border-slate-800/80 flex flex-wrap gap-y-2 gap-x-6 items-center">
            <span><i class="fa-solid fa-location-dot text-amber-400 mr-1.5"></i> Plant: {ADDRESS}</span>
            <span><i class="fa-solid fa-truck-ramp-box text-blue-400 mr-1.5"></i> Daily Bulk Supply Across Gujarat</span>
          </div>
        </div>

        <!-- Hero Right Column: Fast Quote Card -->
        <div class="lg:col-span-5 space-y-6">
          <div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-6 sm:p-7 shadow-2xl backdrop-blur-md relative overflow-hidden">
            <div class="absolute top-0 right-0 w-28 h-28 bg-amber-500/10 rounded-full blur-2xl"></div>
            
            <div class="border-b border-slate-700 pb-4 mb-5">
              <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span> Live Factory Direct Desk
              </span>
              <h3 class="text-2xl font-bold font-industrial uppercase text-white tracking-wide mt-1">
                Instant Price Quote & Dispatch
              </h3>
              <p class="text-xs text-slate-400">Fill details for direct quote on WhatsApp or Call within 10 minutes</p>
            </div>

            <form id="hero-quote-form" onsubmit="handleHeroQuote(event)" class="space-y-4 text-sm">
              <div>
                <label class="block text-xs font-semibold text-slate-300 mb-1">Your Name / Company Name</label>
                <input type="text" id="quote-name" required placeholder="e.g. Ramesh Patel / ABC Infra" class="w-full bg-slate-800/90 border border-slate-600 rounded-lg px-3.5 py-2.5 text-white placeholder-slate-500 focus:outline-none focus:border-amber-400 text-sm">
              </div>

              <div class="grid grid-cols-2 gap-3">
                <div>
                  <label class="block text-xs font-semibold text-slate-300 mb-1">Phone Number</label>
                  <input type="tel" id="quote-phone" required placeholder="e.g. 9876543210" class="w-full bg-slate-800/90 border border-slate-600 rounded-lg px-3.5 py-2.5 text-white placeholder-slate-500 focus:outline-none focus:border-amber-400 text-sm">
                </div>
                <div>
                  <label class="block text-xs font-semibold text-slate-300 mb-1">Required Material</label>
                  <select id="quote-material" class="w-full bg-slate-800/90 border border-slate-600 rounded-lg px-3 py-2.5 text-white focus:outline-none focus:border-amber-400 text-sm">
                    <option value="20mm Black Trap Aggregate">20mm Aggregate (Jelly)</option>
                    <option value="10mm Black Trap Grit">10mm Grit (Chipping)</option>
                    <option value="40mm Coarse Aggregate">40mm Ballast / Coarse</option>
                    <option value="Manufactured Sand (M-Sand)">Manufactured Sand (M-Sand)</option>
                    <option value="Plaster Sand (P-Sand)">Plaster Sand (P-Sand)</option>
                    <option value="GSB / WMM Road Base">GSB / WMM Road Base</option>
                    <option value="Ready Mix Concrete (RMC)">Ready Mix Concrete (RMC)</option>
                    <option value="Quarry Rubble / Soling">Quarry Rubble / Soling Stone</option>
                    <option value="All Building Materials">All Building Materials</option>
                  </select>
                </div>
              </div>

              <div class="grid grid-cols-2 gap-3">
                <div>
                  <label class="block text-xs font-semibold text-slate-300 mb-1">Approx. Quantity</label>
                  <input type="text" id="quote-quantity" placeholder="e.g. 100 MT / 5 Brass" class="w-full bg-slate-800/90 border border-slate-600 rounded-lg px-3.5 py-2.5 text-white placeholder-slate-500 focus:outline-none focus:border-amber-400 text-sm">
                </div>
                <div>
                  <label class="block text-xs font-semibold text-slate-300 mb-1">Delivery Site Location</label>
                  <input type="text" id="quote-location" placeholder="e.g. Bhavnagar / Talaja" class="w-full bg-slate-800/90 border border-slate-600 rounded-lg px-3.5 py-2.5 text-white placeholder-slate-500 focus:outline-none focus:border-amber-400 text-sm">
                </div>
              </div>

              <button type="submit" class="w-full bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-bold py-3 px-4 rounded-xl flex items-center justify-center gap-2 shadow-lg transition-transform active:scale-95 text-base">
                <i class="fa-solid fa-paper-plane"></i>
                <span>Submit & Get WhatsApp Quote</span>
              </button>
            </form>

            <div class="mt-4 pt-3 border-t border-slate-800 text-center">
              <span class="text-xs text-slate-400">Direct Owner Helpline: 
                <a href="tel:{PHONE_BHAGIRATH_RAW}" class="text-amber-400 font-bold hover:underline">{PHONE_BHAGIRATH_RAW}</a> | 
                <a href="tel:{PHONE_ALPESH_RAW}" class="text-amber-400 font-bold hover:underline">{PHONE_ALPESH_RAW}</a>
              </span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- KEY STATS COUNTER -->
  <section class="bg-brand-dark border-y border-slate-800 py-8 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
        <div class="p-4 border-r border-slate-800/80 last:border-none">
          <div class="text-3xl sm:text-4xl lg:text-5xl font-black font-industrial text-amber-400 tracking-wider">1,500+</div>
          <div class="text-xs sm:text-sm font-semibold text-slate-300 uppercase tracking-wider mt-1">Metric Ton Daily Capacity</div>
          <div class="text-[11px] text-slate-500">Uninterrupted Production</div>
        </div>
        <div class="p-4 border-r border-slate-800/80 last:border-none">
          <div class="text-3xl sm:text-4xl lg:text-5xl font-black font-industrial text-cyan-400 tracking-wider">100%</div>
          <div class="text-xs sm:text-sm font-semibold text-slate-300 uppercase tracking-wider mt-1">Hydro-Washed Sand</div>
          <div class="text-[11px] text-slate-500">Zero Silt & Impurities</div>
        </div>
        <div class="p-4 border-r border-slate-800/80 last:border-none">
          <div class="text-3xl sm:text-4xl lg:text-5xl font-black font-industrial text-emerald-400 tracking-wider">IS 383</div>
          <div class="text-xs sm:text-sm font-semibold text-slate-300 uppercase tracking-wider mt-1">Bureau of Indian Standards</div>
          <div class="text-[11px] text-slate-500">Tested Quality Grades</div>
        </div>
        <div class="p-4">
          <div class="text-3xl sm:text-4xl lg:text-5xl font-black font-industrial text-amber-400 tracking-wider">24 / 7</div>
          <div class="text-xs sm:text-sm font-semibold text-slate-300 uppercase tracking-wider mt-1">Dedicated Fleet Delivery</div>
          <div class="text-[11px] text-slate-500">Transit Mixers & Tippers</div>
        </div>
      </div>
    </div>
  </section>

  <!-- OFFICIAL CORPORATE BANNER & CREDENTIALS -->
  <section class="py-6 bg-slate-100 border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white rounded-2xl shadow-sm border border-slate-200 p-3 sm:p-5 overflow-hidden">
        <div class="flex flex-col md:flex-row items-center justify-between gap-4">
          <div class="w-full md:w-3/4">
            <img src="assets/images/company-banner.jpeg" alt="Ashutosh Build Stone Pvt. Ltd. Official Banner" class="w-full h-auto rounded-xl object-contain shadow-sm border border-slate-100" width="1600" height="276">
          </div>
          <div class="w-full md:w-1/4 bg-slate-50 rounded-xl p-4 border border-slate-200/70 text-center flex flex-col justify-center">
            <span class="text-xs font-bold text-amber-600 uppercase tracking-widest">Official Registration</span>
            <div class="text-sm font-extrabold text-brand-navy mt-1">CIN: {CIN}</div>
            <div class="text-xs text-slate-600 mt-1">Govt. Approved Building Contractor & Material Supplier</div>
            <div class="mt-3 pt-3 border-t border-slate-200 flex justify-center gap-2">
              <a href="tel:{PHONE_BHAGIRATH_RAW}" class="text-xs font-bold bg-amber-500 text-slate-950 px-3 py-1.5 rounded-lg hover:bg-amber-400">
                <i class="fa-solid fa-phone"></i> Call Plant
              </a>
              <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}" target="_blank" rel="noopener noreferrer" class="text-xs font-bold bg-emerald-600 text-white px-3 py-1.5 rounded-lg hover:bg-emerald-500">
                <i class="fa-brands fa-whatsapp"></i> Chat
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- QUICK MULTI-PAGE NAVIGATION CARDS (EXPLORE OUR FULL ECOSYSTEM) -->
  <section class="py-14 bg-white border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="text-xs font-bold text-amber-600 uppercase tracking-widest">Corporate Architecture</span>
        <h2 class="text-2xl sm:text-3xl font-black font-industrial uppercase text-brand-navy mt-1">Explore Our Full Corporate Sections</h2>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3 sm:gap-4">
        <a href="about.html" class="p-3 sm:p-4 bg-slate-50 hover:bg-amber-50 rounded-2xl border border-slate-200 hover:border-amber-400 transition-all text-center group">
          <div class="w-10 h-10 rounded-xl bg-amber-500/10 text-amber-600 group-hover:bg-amber-500 group-hover:text-slate-950 flex items-center justify-center text-lg mx-auto mb-2 transition-colors">
            <i class="fa-solid fa-building"></i>
          </div>
          <div class="text-xs font-bold text-slate-800">About Us</div>
          <div class="text-[10px] text-slate-500">Story & Promoters</div>
        </a>

        <a href="products.html" class="p-3 sm:p-4 bg-slate-50 hover:bg-amber-50 rounded-2xl border border-slate-200 hover:border-amber-400 transition-all text-center group">
          <div class="w-10 h-10 rounded-xl bg-blue-500/10 text-blue-600 group-hover:bg-blue-600 group-hover:text-white flex items-center justify-center text-lg mx-auto mb-2 transition-colors">
            <i class="fa-solid fa-cubes"></i>
          </div>
          <div class="text-xs font-bold text-slate-800">Products & Specs</div>
          <div class="text-[10px] text-slate-500">Aggregates & Sand</div>
        </a>

        <a href="plant.html" class="p-3 sm:p-4 bg-slate-50 hover:bg-amber-50 rounded-2xl border border-slate-200 hover:border-amber-400 transition-all text-center group">
          <div class="w-10 h-10 rounded-xl bg-cyan-500/10 text-cyan-600 group-hover:bg-cyan-600 group-hover:text-white flex items-center justify-center text-lg mx-auto mb-2 transition-colors">
            <i class="fa-solid fa-gears"></i>
          </div>
          <div class="text-xs font-bold text-slate-800">Plant & Tech</div>
          <div class="text-[10px] text-slate-500">1500+ MT/Day Setup</div>
        </a>

        <a href="contracting.html" class="p-3 sm:p-4 bg-slate-50 hover:bg-amber-50 rounded-2xl border border-slate-200 hover:border-amber-400 transition-all text-center group">
          <div class="w-10 h-10 rounded-xl bg-emerald-500/10 text-emerald-600 group-hover:bg-emerald-600 group-hover:text-white flex items-center justify-center text-lg mx-auto mb-2 transition-colors">
            <i class="fa-solid fa-road"></i>
          </div>
          <div class="text-xs font-bold text-slate-800">Govt. Contracting</div>
          <div class="text-[10px] text-slate-500">Roads & Foundations</div>
        </a>

        <a href="calculator.html" class="p-3 sm:p-4 bg-slate-50 hover:bg-amber-50 rounded-2xl border border-slate-200 hover:border-amber-400 transition-all text-center group">
          <div class="w-10 h-10 rounded-xl bg-purple-500/10 text-purple-600 group-hover:bg-purple-600 group-hover:text-white flex items-center justify-center text-lg mx-auto mb-2 transition-colors">
            <i class="fa-solid fa-calculator"></i>
          </div>
          <div class="text-xs font-bold text-slate-800">Estimator Tool</div>
          <div class="text-[10px] text-slate-500">Tons, Brass & Cu.M</div>
        </a>

        <a href="contact.html" class="p-3 sm:p-4 bg-slate-50 hover:bg-amber-50 rounded-2xl border border-slate-200 hover:border-amber-400 transition-all text-center group">
          <div class="w-10 h-10 rounded-xl bg-red-500/10 text-red-600 group-hover:bg-red-600 group-hover:text-white flex items-center justify-center text-lg mx-auto mb-2 transition-colors">
            <i class="fa-solid fa-location-dot"></i>
          </div>
          <div class="text-xs font-bold text-slate-800">Contact & Map</div>
          <div class="text-[10px] text-slate-500">Direct Plant Location</div>
        </a>
      </div>
    </div>
  </section>

  <!-- EMBEDDED CONTRACTOR ESTIMATOR TOOL -->
  <section class="py-16 bg-slate-50 border-b border-slate-200">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-gradient-to-br from-brand-navy to-slate-900 rounded-3xl p-4 sm:p-8 lg:p-10 text-white shadow-2xl border border-slate-800">
        <div class="max-w-2xl mb-8">
          <span class="inline-flex items-center gap-2 bg-amber-500/20 text-amber-400 border border-amber-500/30 px-3.5 py-1 rounded-full text-xs font-bold uppercase tracking-wider mb-2">
            <i class="fa-solid fa-calculator"></i> Live Contractor Estimator
          </span>
          <h2 class="text-2xl sm:text-3xl lg:text-4xl font-black font-industrial uppercase text-white">
            Material Quantity & Brass / Ton Estimator
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm mt-1">
            Calculate exact material requirements for slabs, foundations, road base, and civil construction in Brass, Metric Tons (MT), or Cubic Meters.
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-7 space-y-4">
            <div>
              <label class="block text-xs font-semibold text-slate-300 mb-1">Select Construction Material</label>
              <select id="calc-material" onchange="calculateMaterial()" class="w-full bg-slate-800 border border-slate-600 rounded-xl px-4 py-3 text-white text-sm focus:outline-none focus:border-amber-400">
                <option value="20mm Black Trap Aggregate" data-density="1.60">20mm Black Trap Aggregate (RCC Slab / Beam)</option>
                <option value="10mm Black Trap Grit" data-density="1.55">10mm Black Trap Grit (Chipping / Paver)</option>
                <option value="40mm Coarse Aggregate" data-density="1.65">40mm Coarse Aggregate (Foundation / Ballast)</option>
                <option value="Manufactured Sand (M-Sand)" data-density="1.65">Manufactured Sand (M-Sand - Washed)</option>
                <option value="Plaster Sand (P-Sand)" data-density="1.60">Plaster Sand (P-Sand - Fine Plastering)</option>
                <option value="GSB / WMM Road Base" data-density="2.10">GSB / WMM Road Sub-Base</option>
                <option value="Quarry Rubble / Soling" data-density="1.75">Quarry Rubble / Soling Stone</option>
              </select>
            </div>

            <div>
              <label class="block text-xs font-semibold text-slate-300 mb-1">Input Dimension Units</label>
              <div class="flex gap-2">
                <button type="button" id="unit-feet" onclick="setCalcUnit('feet')" class="flex-1 py-2 rounded-lg bg-amber-500 text-slate-950 font-bold text-xs uppercase tracking-wider transition-colors">Feet & Inches</button>
                <button type="button" id="unit-meters" onclick="setCalcUnit('meters')" class="flex-1 py-2 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs uppercase tracking-wider transition-colors">Meters</button>
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
              <div class="min-w-0">
                <label id="label-len" class="block text-xs font-semibold text-slate-300 mb-1">Length (Feet)</label>
                <input type="number" id="calc-len" value="50" min="1" step="any" oninput="calculateMaterial()" class="w-full bg-slate-800 border border-slate-600 rounded-xl px-3 py-2.5 text-white text-sm focus:outline-none focus:border-amber-400">
              </div>
              <div class="min-w-0">
                <label id="label-wid" class="block text-xs font-semibold text-slate-300 mb-1">Width (Feet)</label>
                <input type="number" id="calc-wid" value="30" min="1" step="any" oninput="calculateMaterial()" class="w-full bg-slate-800 border border-slate-600 rounded-xl px-3 py-2.5 text-white text-sm focus:outline-none focus:border-amber-400">
              </div>
              <div class="min-w-0">
                <label id="label-dep" class="block text-xs font-semibold text-slate-300 mb-1">Thickness (Inches)</label>
                <input type="number" id="calc-dep" value="5" min="0.1" step="any" oninput="calculateMaterial()" class="w-full bg-slate-800 border border-slate-600 rounded-xl px-3 py-2.5 text-white text-sm focus:outline-none focus:border-amber-400">
              </div>
            </div>

            <p class="text-[11px] text-slate-400">
              <i class="fa-solid fa-circle-info text-amber-400 mr-1"></i> 1 Brass = 100 Cubic Feet (approx. 4.5 to 5.0 Metric Tons based on stone density).
            </p>
          </div>

          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-2xl p-6 flex flex-col justify-between">
            <div>
              <h4 class="text-xs font-bold text-amber-400 uppercase tracking-widest mb-4">Estimated Output</h4>
              <div class="space-y-4">
                <div class="bg-slate-900/90 rounded-xl p-4 border border-slate-700 flex items-center justify-between">
                  <div>
                    <span class="text-xs text-slate-400">Estimated Weight:</span>
                    <div class="text-2xl sm:text-3xl font-black font-industrial text-amber-400" id="res-tons">28.3 MT</div>
                  </div>
                  <span class="text-xs font-bold bg-amber-500/20 text-amber-300 px-2 py-1 rounded">Metric Tons</span>
                </div>

                <div class="bg-slate-900/90 rounded-xl p-4 border border-slate-700 flex items-center justify-between">
                  <div>
                    <span class="text-xs text-slate-400">Brass (100 Cu.Ft):</span>
                    <div class="text-2xl sm:text-3xl font-black font-industrial text-cyan-400" id="res-brass">6.25 Brass</div>
                  </div>
                  <span class="text-xs font-bold bg-cyan-500/20 text-cyan-300 px-2 py-1 rounded">Local Unit</span>
                </div>

                <div class="bg-slate-900/90 rounded-xl p-4 border border-slate-700 flex items-center justify-between">
                  <div>
                    <span class="text-xs text-slate-400">Volume:</span>
                    <div class="text-xl font-bold font-industrial text-slate-200" id="res-cu-m">17.7 m³ (625 Cu.Ft)</div>
                  </div>
                  <span class="text-xs text-slate-400">Total Volume</span>
                </div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-700">
              <button onclick="sendCalculatedQuote()" class="w-full bg-[#25D366] hover:bg-[#20ba59] text-white font-bold py-3 px-4 rounded-xl flex items-center justify-center gap-2 text-sm transition-transform active:scale-95 shadow-md">
                <i class="fa-brands fa-whatsapp text-lg"></i> Send Estimate on WhatsApp
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

{faqs_html}

{FOOTER_HTML}

  <script>
    function handleHeroQuote(e) {{
      e.preventDefault();
      const name = document.getElementById('quote-name').value;
      const phone = document.getElementById('quote-phone').value;
      const material = document.getElementById('quote-material').value;
      const qty = document.getElementById('quote-quantity').value || 'To be discussed';
      const loc = document.getElementById('quote-location').value || 'Bhavnagar area';

      const text = `*New Website Inquiry - Ashutosh Build Stone Pvt. Ltd.*\\n\\n*Name:* ${{name}}\\n*Phone:* ${{phone}}\\n*Material Needed:* ${{material}}\\n*Quantity:* ${{qty}}\\n*Site Location:* ${{loc}}\\n\\nPlease provide rate quote and delivery schedule.`;
      const url = `https://wa.me/{PHONE_BHAGIRATH_RAW}?text=${{encodeURIComponent(text)}}`;
      window.open(url, '_blank');
    }}

    let currentUnit = 'feet';
    function setCalcUnit(unit) {{
      currentUnit = unit;
      const btnFeet = document.getElementById('unit-feet');
      const btnMeters = document.getElementById('unit-meters');
      const lblLen = document.getElementById('label-len');
      const lblWid = document.getElementById('label-wid');
      const lblDep = document.getElementById('label-dep');
      const lenInput = document.getElementById('calc-len');
      const widInput = document.getElementById('calc-wid');
      const depInput = document.getElementById('calc-dep');

      if (unit === 'feet') {{
        btnFeet.classList.replace('bg-slate-800', 'bg-amber-500');
        btnFeet.classList.replace('text-slate-300', 'text-slate-950');
        btnMeters.classList.replace('bg-amber-500', 'bg-slate-800');
        btnMeters.classList.replace('text-slate-950', 'text-slate-300');

        lblLen.innerText = 'Length (Feet)';
        lblWid.innerText = 'Width (Feet)';
        lblDep.innerText = 'Thickness (Inches)';
        lenInput.value = 50;
        widInput.value = 30;
        depInput.value = 5;
      }} else {{
        btnMeters.classList.replace('bg-slate-800', 'bg-amber-500');
        btnMeters.classList.replace('text-slate-300', 'text-slate-950');
        btnFeet.classList.replace('bg-amber-500', 'bg-slate-800');
        btnFeet.classList.replace('text-slate-950', 'text-slate-300');

        lblLen.innerText = 'Length (Meters)';
        lblWid.innerText = 'Width (Meters)';
        lblDep.innerText = 'Thickness (Meters)';
        lenInput.value = 15;
        widInput.value = 10;
        depInput.value = 0.15;
      }}
      calculateMaterial();
    }}

    function calculateMaterial() {{
      const materialSelect = document.getElementById('calc-material');
      const selectedOption = materialSelect.options[materialSelect.selectedIndex];
      const density = parseFloat(selectedOption.getAttribute('data-density')) || 1.6;

      const l = parseFloat(document.getElementById('calc-len').value) || 0;
      const w = parseFloat(document.getElementById('calc-wid').value) || 0;
      const d = parseFloat(document.getElementById('calc-dep').value) || 0;

      let volumeCuM = 0;
      let volumeCuFt = 0;

      if (currentUnit === 'feet') {{
        volumeCuFt = l * w * (d / 12);
        volumeCuM = volumeCuFt * 0.0283168;
      }} else {{
        volumeCuM = l * w * d;
        volumeCuFt = volumeCuM * 35.3147;
      }}

      const brass = volumeCuFt / 100;
      const metricTons = volumeCuM * density;

      document.getElementById('res-tons').innerText = metricTons.toFixed(1) + ' MT';
      document.getElementById('res-brass').innerText = brass.toFixed(2) + ' Brass';
      document.getElementById('res-cu-m').innerText = volumeCuM.toFixed(1) + ' m³ (' + volumeCuFt.toFixed(0) + ' Cu.Ft)';
    }}

    function sendCalculatedQuote() {{
      const material = document.getElementById('calc-material').value;
      const tons = document.getElementById('res-tons').innerText;
      const brass = document.getElementById('res-brass').innerText;
      const volume = document.getElementById('res-cu-m').innerText;

      const text = `Hello Ashutosh Build Stone Pvt. Ltd., I calculated my requirement on your website:\\n\\n*Material:* ${{material}}\\n*Estimated Weight:* ${{tons}}\\n*Local Units:* ${{brass}}\\n*Volume:* ${{volume}}\\n\\nPlease share your best rate and dispatch availability.`;
      const url = `https://wa.me/{PHONE_BHAGIRATH_RAW}?text=${{encodeURIComponent(text)}}`;
      window.open(url, '_blank');
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      calculateMaterial();
    }});
  </script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(body)

print("index.html generated with deep SEO + GEO + AEO integration.")
