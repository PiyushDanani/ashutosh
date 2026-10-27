# generate_remaining_expanded.py
# Generates products.html, plant.html, contracting.html, calculator.html, gallery.html, and contact.html with deep SEO, GEO & AEO.

import os
from build_ultimate_site import build_head
from generate_ultimate_multipage import (
    BASE_URL, COMPANY_NAME, CIN, PAN, TAN,
    PHONE_BHAGIRATH, PHONE_BHAGIRATH_RAW, PHONE_ALPESH, PHONE_ALPESH_RAW,
    ADDRESS, LATITUDE, LONGITUDE,
    get_global_schema, get_header_nav, get_geo_ai_factsheet, get_aeo_faq_component
)
from build_pages import FOOTER_HTML, get_page_banner

# ==========================================
# 2. PRODUCTS PAGE
# ==========================================
def build_expanded_products():
    faqs = [
        (
            "What is the difference between M-Sand and P-Sand?",
            "Manufactured Sand (M-Sand) is graded according to IS 383 Zone II (0-4.75mm) and is specifically engineered for concrete structural elements like slabs, columns, and beams to provide maximum compressive strength. Plaster Sand (P-Sand) is micro-screened to IS 383 Zone IV (0-2.36mm), double-washed to eliminate silt, and tailored specifically for smooth, crack-free internal and external wall plastering."
        ),
        (
            "What is the crushing value and flakiness index of your 20mm aggregate?",
            "Our 20mm Black Trap Aggregate achieves an Aggregate Crushing Value of under 18% (exceeding standard IS 383 threshold of 30%) and a Flakiness & Elongation Index of under 15%. This cubical geometric shape ensures dense packing, minimal voids, and reduced cement slurry demand in high-grade RCC concrete."
        ),
        (
            "What grades of Ready-Mix Concrete (RMC) are available for site dispatch?",
            "We supply standard and high-performance RMC concrete grades including M15, M20, M25, M30, M35, and M40. Every batch is mixed using automated PLC batching technology with guaranteed on-site slump retention and delivered via transit mixers across the Bhavnagar and Talaja region."
        ),
        (
            "How does Ashutosh Build Stone ensure zero mud or silt in washed sand?",
            "We use a cutting-edge CDE-class hydrocyclone washing plant. Slurry is pumped under pressure into hydrocyclone cones where centrifugal force separates heavier clean sand particles from lightweight silt and clay micro-fines. The clean sand is then dewatered on high-frequency polyurethane screens, guaranteeing silt content under 3%."
        ),
        (
            "Can I order custom blended GSB or WMM aggregate mixes for road work?",
            "Yes, we produce Granular Sub-Base (GSB) and Wet Mix Macadam (WMM) strictly adhering to Ministry of Road Transport and Highways (MoRTH) Section 400 specifications. We supply pre-blended, optimum moisture content aggregates for national and state highway base layers."
        )
    ]

    schema = get_global_schema(
        f"Products & Technical Specifications | {COMPANY_NAME}",
        "Technical catalogue of Black Trap Aggregates (10mm, 20mm, 40mm), M-Sand, Plaster Sand, GSB, and RMC Concrete complying with IS 383:2016.",
        f"{BASE_URL}/products.html",
        "ItemPage",
        faqs
    )

    head = build_head(
        "Products & Specifications | Ashutosh Build Stone Pvt. Ltd.",
        "IS 383:2016 Certified Black Trap Aggregates (10mm, 20mm, 40mm), Washed M-Sand, Plaster Sand, GSB, and RMC Concrete in Bhavnagar, Gujarat.",
        "20mm Aggregate Bhavnagar, 10mm Grit Talaja, M-Sand Supplier Gujarat, Plaster Sand Borda, 40mm Ballast, RMC Batching Plant Bhavnagar, GSB Road Base, Stone Crusher Price List",
        f"{BASE_URL}/products.html",
        schema
    )

    nav = get_header_nav("products")
    banner = get_page_banner(
        "Products & Technical Specifications",
        "IS 383:2016 Certified Black Trap Basalt Aggregates, Eco-Friendly Washed M-Sand & Ready-Mix Concrete",
        "Products"
    )
    factsheet = get_geo_ai_factsheet("Products & Materials")
    faqs_html = get_aeo_faq_component(faqs, "Product Technical & Ordering FAQs (AEO)")

    content = f"""{head}
{nav}
{factsheet}
{banner}

  <!-- PRODUCTS CATALOG & SPECIFICATIONS SECTION -->
  <section class="py-16 sm:py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Filter Bar -->
      <div class="flex flex-wrap items-center justify-center gap-2 mb-12">
        <button class="filter-btn active bg-brand-navy text-white px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold shadow-sm transition-all" data-filter="all">All Materials</button>
        <button class="filter-btn bg-white text-slate-700 hover:bg-slate-200 px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold shadow-sm transition-all" data-filter="aggregates">Black Trap Aggregates</button>
        <button class="filter-btn bg-white text-slate-700 hover:bg-slate-200 px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold shadow-sm transition-all" data-filter="sand">Washed M-Sand & P-Sand</button>
        <button class="filter-btn bg-white text-slate-700 hover:bg-slate-200 px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold shadow-sm transition-all" data-filter="infrastructure">RMC & Road Sub-Base</button>
      </div>

      <!-- Products Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-20">

        <!-- Product 1: 20mm Aggregate -->
        <div class="product-card card-hover bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="aggregates">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/aggregate-20mm-hd.jpeg" alt="20mm Black Trap Aggregate" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" width="1376" height="768">
            <span class="absolute top-3 left-3 bg-amber-500 text-slate-950 font-black text-xs px-3 py-1 rounded shadow uppercase">20 MM JELLY</span>
            <span class="absolute top-3 right-3 bg-brand-navy/90 text-white text-[11px] font-bold px-2.5 py-1 rounded backdrop-blur-sm">IS 383 Coarse</span>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between">
            <div>
              <h3 class="text-2xl font-bold font-industrial uppercase text-brand-navy">20mm Black Trap Aggregate (Kapchi)</h3>
              <p class="text-xs text-slate-500 mt-2 leading-relaxed">
                The primary aggregate for Reinforced Cement Concrete (RCC). Cubical shape with minimal flakiness index for slabs, columns, beams, bridge decks, and heavy civil structures.
              </p>
              
              <div class="mt-4 pt-4 border-t border-slate-100 space-y-2 text-xs text-slate-700">
                <div class="flex justify-between"><span class="text-slate-400">Standard Size:</span><span class="font-bold">20 mm Graded</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Crushing Value:</span><span class="font-bold text-emerald-600">&lt; 18% (High Strength)</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Flakiness Index:</span><span class="font-bold text-emerald-600">&lt; 15% (Cubical Shape)</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Specific Gravity:</span><span class="font-bold">2.85+</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Water Absorption:</span><span class="font-bold">&lt; 1.0%</span></div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-2">
              <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%2020mm%20Black%20Trap%20Aggregate" target="_blank" rel="noopener noreferrer" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-xl text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-xl text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 2: 10mm Grit -->
        <div class="product-card card-hover bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="aggregates">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/aggregate-10mm-hd.jpeg" alt="10mm Grit Aggregate" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" width="1376" height="768">
            <span class="absolute top-3 left-3 bg-blue-600 text-white font-black text-xs px-3 py-1 rounded shadow uppercase">10 MM GRIT</span>
            <span class="absolute top-3 right-3 bg-brand-navy/90 text-white text-[11px] font-bold px-2.5 py-1 rounded backdrop-blur-sm">Chipping</span>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between">
            <div>
              <h3 class="text-2xl font-bold font-industrial uppercase text-brand-navy">10mm Black Trap Grit / Chipping</h3>
              <p class="text-xs text-slate-500 mt-2 leading-relaxed">
                Precision-screened angular grit for asphalt road carpeting, concrete paver blocks, ready-mix design blends, screeds, and precast concrete components.
              </p>
              
              <div class="mt-4 pt-4 border-t border-slate-100 space-y-2 text-xs text-slate-700">
                <div class="flex justify-between"><span class="text-slate-400">Standard Size:</span><span class="font-bold">10 mm Graded</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Screening:</span><span class="font-bold text-emerald-600">Triple Deck Washed</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Dust Content:</span><span class="font-bold text-emerald-600">&lt; 1.0% (Clean)</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Applications:</span><span class="font-bold">Asphalt, Paver, Precast</span></div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-2">
              <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%2010mm%20Grit" target="_blank" rel="noopener noreferrer" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-xl text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-xl text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 3: 40mm Ballast -->
        <div class="product-card card-hover bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="aggregates">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/aggregate-40mm-hd.jpeg" alt="40mm Coarse Aggregate Ballast" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" width="1376" height="768">
            <span class="absolute top-3 left-3 bg-slate-800 text-white font-black text-xs px-3 py-1 rounded shadow uppercase">40 MM BALLAST</span>
            <span class="absolute top-3 right-3 bg-brand-navy/90 text-white text-[11px] font-bold px-2.5 py-1 rounded backdrop-blur-sm">Mass Concrete</span>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between">
            <div>
              <h3 class="text-2xl font-bold font-industrial uppercase text-brand-navy">40mm Coarse Aggregate / Ballast</h3>
              <p class="text-xs text-slate-500 mt-2 leading-relaxed">
                High-density, heavy-duty basalt aggregates for massive machine foundations, retaining walls, ground soling, road sub-bases, and railway track ballast.
              </p>
              
              <div class="mt-4 pt-4 border-t border-slate-100 space-y-2 text-xs text-slate-700">
                <div class="flex justify-between"><span class="text-slate-400">Standard Size:</span><span class="font-bold">40 mm Graded</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Impact Value:</span><span class="font-bold text-emerald-600">&lt; 15%</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Rock Density:</span><span class="font-bold">High Density Basalt</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Applications:</span><span class="font-bold">Foundation, Soling, Railway</span></div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-2">
              <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%2040mm%20Aggregate" target="_blank" rel="noopener noreferrer" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-xl text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-xl text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 4: M-Sand -->
        <div class="product-card card-hover bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="sand">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/manufactured-sand-m-sand-hd.jpeg" alt="Manufactured Sand M-Sand" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" width="1376" height="768">
            <span class="absolute top-3 left-3 bg-cyan-600 text-white font-black text-xs px-3 py-1 rounded shadow uppercase">M-SAND (WASHED)</span>
            <span class="absolute top-3 right-3 bg-emerald-600 text-white text-[11px] font-bold px-2.5 py-1 rounded backdrop-blur-sm">Zone II</span>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between">
            <div>
              <h3 class="text-2xl font-bold font-industrial uppercase text-brand-navy">Hydro-Washed Manufactured Sand (M-Sand)</h3>
              <p class="text-xs text-slate-500 mt-2 leading-relaxed">
                Eco-friendly, hydrocyclone desilted sand engineered to replace river sand. Gives 15-20% higher compressive strength, lower cement consumption, and zero organic silt.
              </p>
              
              <div class="mt-4 pt-4 border-t border-slate-100 space-y-2 text-xs text-slate-700">
                <div class="flex justify-between"><span class="text-slate-400">Grading Zone:</span><span class="font-bold text-emerald-600">IS 383 Zone II Compliant</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Silt & Clay Content:</span><span class="font-bold text-emerald-600">&lt; 3% (Lab Verified)</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Particle Geometry:</span><span class="font-bold">Cubical & Sharp Granules</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Strength Gain:</span><span class="font-bold text-emerald-600">+15% over River Sand</span></div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-2">
              <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%20Washed%20M-Sand" target="_blank" rel="noopener noreferrer" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-xl text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-xl text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 5: P-Sand -->
        <div class="product-card card-hover bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="sand">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/plaster-sand-fine-hd.jpeg" alt="Plaster Sand Fine Grade" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" width="1376" height="768">
            <span class="absolute top-3 left-3 bg-purple-600 text-white font-black text-xs px-3 py-1 rounded shadow uppercase">P-SAND (PLASTER)</span>
            <span class="absolute top-3 right-3 bg-brand-navy/90 text-white text-[11px] font-bold px-2.5 py-1 rounded backdrop-blur-sm">Crack-Free</span>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between">
            <div>
              <h3 class="text-2xl font-bold font-industrial uppercase text-brand-navy">Plastering Sand (P-Sand / Fine Sand)</h3>
              <p class="text-xs text-slate-500 mt-2 leading-relaxed">
                Double-washed and micro-screened fine sand designed for crack-free internal and external wall plastering. Provides smooth trowel workability and high adhesion.
              </p>
              
              <div class="mt-4 pt-4 border-t border-slate-100 space-y-2 text-xs text-slate-700">
                <div class="flex justify-between"><span class="text-slate-400">Grading Zone:</span><span class="font-bold text-purple-600">IS 383 Zone IV / Fine</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Clay / Mud Content:</span><span class="font-bold text-emerald-600">0% (Nil)</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Surface Finish:</span><span class="font-bold">Super Smooth & Crack-Free</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Applications:</span><span class="font-bold">Internal/External Wall Plaster</span></div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-2">
              <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%20Plaster%20Sand%20(P-Sand)" target="_blank" rel="noopener noreferrer" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-xl text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-xl text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 6: RMC Concrete -->
        <div class="product-card card-hover bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="infrastructure">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/rmc-batching-plant-hd.jpeg" alt="RMC Batching Plant" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" width="1376" height="768">
            <span class="absolute top-3 left-3 bg-red-600 text-white font-black text-xs px-3 py-1 rounded shadow uppercase">RMC CONCRETE</span>
            <span class="absolute top-3 right-3 bg-brand-navy/90 text-white text-[11px] font-bold px-2.5 py-1 rounded backdrop-blur-sm">Batching Plant</span>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between">
            <div>
              <h3 class="text-2xl font-bold font-industrial uppercase text-brand-navy">Ready-Mix Concrete (RMC) Solutions</h3>
              <p class="text-xs text-slate-500 mt-2 leading-relaxed">
                Computerized PLC batching plant concrete formulated from M15 to M40 grades, transported directly to your project site via our rapid transit mixer fleet.
              </p>
              
              <div class="mt-4 pt-4 border-t border-slate-100 space-y-2 text-xs text-slate-700">
                <div class="flex justify-between"><span class="text-slate-400">Available Grades:</span><span class="font-bold">M15, M20, M25, M30, M35, M40</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Control System:</span><span class="font-bold">Automated PLC Weighing</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Slump Retention:</span><span class="font-bold text-emerald-600">Guaranteed On-Site</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Fleet:</span><span class="font-bold">Dedicated Transit Mixers</span></div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-2">
              <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%20Ready%20Mix%20Concrete%20(RMC)" target="_blank" rel="noopener noreferrer" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-xl text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-xl text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 7: GSB Road Base -->
        <div class="product-card card-hover bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="infrastructure">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/road-base-gsb-hd.jpeg" alt="Granular Sub Base GSB" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" width="1376" height="768">
            <span class="absolute top-3 left-3 bg-emerald-700 text-white font-black text-xs px-3 py-1 rounded shadow uppercase">GSB / WMM</span>
            <span class="absolute top-3 right-3 bg-brand-navy/90 text-white text-[11px] font-bold px-2.5 py-1 rounded backdrop-blur-sm">MoRTH Spec</span>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between">
            <div>
              <h3 class="text-2xl font-bold font-industrial uppercase text-brand-navy">Granular Sub Base (GSB) & WMM</h3>
              <p class="text-xs text-slate-500 mt-2 leading-relaxed">
                MoRTH compliant dense-graded crushed stone aggregate mix for national highways, state expressways, industrial park floors, and logistics warehouse base layers.
              </p>
              
              <div class="mt-4 pt-4 border-t border-slate-100 space-y-2 text-xs text-slate-700">
                <div class="flex justify-between"><span class="text-slate-400">MoRTH Standard:</span><span class="font-bold">Table 400-1 / 400-2</span></div>
                <div class="flex justify-between"><span class="text-slate-400">California Bearing Ratio:</span><span class="font-bold text-emerald-600">CBR &gt; 30%</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Compaction:</span><span class="font-bold text-emerald-600">Optimum Proctor Density</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Applications:</span><span class="font-bold">Roadways, Pavements, Logistics</span></div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-2">
              <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%20GSB%20Road%20Base" target="_blank" rel="noopener noreferrer" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-xl text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-xl text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 8: Quarry Rubble & Soling -->
        <div class="product-card card-hover bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="infrastructure">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/aggregate-40mm-hd.jpeg" alt="Quarry Rubble and Soling" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" width="1376" height="768">
            <span class="absolute top-3 left-3 bg-stone-700 text-white font-black text-xs px-3 py-1 rounded shadow uppercase">SOLING STONE</span>
            <span class="absolute top-3 right-3 bg-brand-navy/90 text-white text-[11px] font-bold px-2.5 py-1 rounded backdrop-blur-sm">Heavy Basalt</span>
          </div>
          <div class="p-6 flex-1 flex flex-col justify-between">
            <div>
              <h3 class="text-2xl font-bold font-industrial uppercase text-brand-navy">Quarry Rubble & Soling Stone</h3>
              <p class="text-xs text-slate-500 mt-2 leading-relaxed">
                Heavy, high-density black trap basalt rocks for foundation soling, gravity retaining walls, coastal armor, check dams, and embankment protection.
              </p>
              
              <div class="mt-4 pt-4 border-t border-slate-100 space-y-2 text-xs text-slate-700">
                <div class="flex justify-between"><span class="text-slate-400">Rock Origin:</span><span class="font-bold">Igneous Black Trap</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Specific Gravity:</span><span class="font-bold">2.90+ (Heavy Weight)</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Weather Resistance:</span><span class="font-bold text-emerald-600">Zero Degradation</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Applications:</span><span class="font-bold">Retaining Walls, Dikes, Soling</span></div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-2">
              <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%20Quarry%20Rubble%20Soling" target="_blank" rel="noopener noreferrer" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-xl text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-xl text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 9: Bulk Turnkey Supply -->
        <div class="product-card card-hover bg-gradient-to-br from-brand-navy to-slate-900 rounded-3xl overflow-hidden border border-slate-700 text-white shadow-xl flex flex-col justify-between p-7" data-category="all">
          <div>
            <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-2xl mb-4">
              <i class="fa-solid fa-dolly"></i>
            </div>
            <span class="text-xs font-bold text-amber-400 uppercase tracking-widest">Turnkey Procurement</span>
            <h3 class="text-2xl font-bold font-industrial uppercase mt-1">All Building Material Suppliers</h3>
            <p class="text-xs text-slate-300 mt-2 leading-relaxed">
              Complete civil construction material supply to contractors, real estate developers, highway tenders, and government infrastructure projects across Gujarat.
            </p>

            <ul class="mt-5 space-y-2 text-xs text-slate-300">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-400"></i> Wholesale factory-direct pricing</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-400"></i> 10-wheeler and 12-wheeler bulk dumpers</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-emerald-400"></i> GST tax invoice and digital weighment slip</li>
            </ul>
          </div>

          <div class="mt-6 pt-4 border-t border-slate-700/80">
            <a href="tel:{PHONE_BHAGIRATH_RAW}" class="w-full bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-3 px-4 rounded-xl flex items-center justify-center gap-2 text-sm transition-transform active:scale-95">
              <i class="fa-solid fa-phone"></i> Inquire Project Supply
            </a>
          </div>
        </div>

      </div>

      <!-- COMPARISON TABLE: M-SAND VS NATURAL RIVER SAND -->
      <div class="bg-white rounded-3xl p-8 sm:p-10 shadow-lg border border-slate-200 mb-16">
        <div class="max-w-3xl mb-8">
          <span class="text-xs font-bold text-amber-600 uppercase tracking-widest">Engineering Comparison</span>
          <h3 class="text-2xl sm:text-3xl font-black font-industrial uppercase text-brand-navy mt-1">
            Why Modern Engineers Choose Hydro-Washed M-Sand Over River Sand
          </h3>
          <p class="text-slate-600 text-xs sm:text-sm mt-1">
            Manufactured Sand is recommended by the Bureau of Indian Standards (IS 383:2016) for modern concrete construction.
          </p>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs sm:text-sm border-collapse">
            <thead>
              <tr class="bg-brand-navy text-white font-industrial uppercase text-base">
                <th class="p-3.5 rounded-l-xl">Technical Parameter</th>
                <th class="p-3.5 bg-amber-500 text-slate-950">Ashutosh Hydro-Washed M-Sand</th>
                <th class="p-3.5 rounded-r-xl">Ordinary River Sand</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 text-slate-700">
              <tr class="hover:bg-slate-50">
                <td class="p-3.5 font-bold">Compressive Strength</td>
                <td class="p-3.5 font-bold text-emerald-600 bg-amber-50/50">15% - 20% Higher Strength</td>
                <td class="p-3.5 text-slate-500">Standard / Variable</td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3.5 font-bold">Silt & Clay Impurities</td>
                <td class="p-3.5 font-bold text-emerald-600 bg-amber-50/50">&lt; 3% (Hydrocyclone Washed)</td>
                <td class="p-3.5 text-red-600">7% - 15% (High Silt Risk)</td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3.5 font-bold">Particle Shape & Bonding</td>
                <td class="p-3.5 font-bold text-slate-900 bg-amber-50/50">Cubical & Angular (Optimal Cement Interlocking)</td>
                <td class="p-3.5 text-slate-500">Rounded / Sub-rounded (Lower Interlocking)</td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3.5 font-bold">Organic & Chemical Matter</td>
                <td class="p-3.5 font-bold text-emerald-600 bg-amber-50/50">0% (Nil Organics)</td>
                <td class="p-3.5 text-red-600">Often contains roots, marine salts & dirt</td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3.5 font-bold">Year-Round Availability</td>
                <td class="p-3.5 font-bold text-slate-900 bg-amber-50/50">365 Days Uninterrupted Production</td>
                <td class="p-3.5 text-slate-500">Monsoon mining bans & erratic supply</td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3.5 font-bold">Environmental Impact</td>
                <td class="p-3.5 font-bold text-emerald-600 bg-amber-50/50">Eco-Friendly ("Save Water, River Sand")</td>
                <td class="p-3.5 text-red-600">Damages riverbeds & water tables</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TECHNICAL SPECIFICATIONS DATA TABLE -->
      <div class="bg-white rounded-3xl p-8 sm:p-10 shadow-lg border border-slate-200">
        <h3 class="text-2xl font-black font-industrial uppercase text-brand-navy mb-4">
          Laboratory Test Values & Physical Parameters (IS 383:2016 Compliant)
        </h3>
        
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs sm:text-sm border-collapse">
            <thead>
              <tr class="bg-slate-800 text-white font-industrial uppercase text-sm">
                <th class="p-3 rounded-l-lg">Material Grade</th>
                <th class="p-3">Specific Gravity</th>
                <th class="p-3">Crushing Value</th>
                <th class="p-3">Impact Value</th>
                <th class="p-3">Water Absorption</th>
                <th class="p-3 rounded-r-lg">Grading Standard</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 text-slate-700">
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-bold text-brand-navy">20 mm Black Trap Aggregate</td>
                <td class="p-3">2.85 - 2.88</td>
                <td class="p-3">&lt; 18%</td>
                <td class="p-3">&lt; 16%</td>
                <td class="p-3">&lt; 1.0%</td>
                <td class="p-3 font-semibold text-emerald-600">IS 383 Coarse</td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-bold text-brand-navy">10 mm Black Trap Grit</td>
                <td class="p-3">2.82 - 2.85</td>
                <td class="p-3">&lt; 19%</td>
                <td class="p-3">&lt; 17%</td>
                <td class="p-3">&lt; 1.2%</td>
                <td class="p-3 font-semibold text-emerald-600">IS 383 Coarse Chipping</td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-bold text-brand-navy">40 mm Ballast Stone</td>
                <td class="p-3">2.88 - 2.92</td>
                <td class="p-3">&lt; 16%</td>
                <td class="p-3">&lt; 14%</td>
                <td class="p-3">&lt; 0.8%</td>
                <td class="p-3 font-semibold text-emerald-600">IS 383 / Railway Ballast</td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-bold text-brand-navy">Washed M-Sand</td>
                <td class="p-3">2.65 - 2.70</td>
                <td class="p-3">N/A</td>
                <td class="p-3">N/A</td>
                <td class="p-3">&lt; 2.5%</td>
                <td class="p-3 font-semibold text-emerald-600">IS 383 Zone II</td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-bold text-brand-navy">Washed P-Sand</td>
                <td class="p-3">2.60 - 2.65</td>
                <td class="p-3">N/A</td>
                <td class="p-3">N/A</td>
                <td class="p-3">&lt; 2.8%</td>
                <td class="p-3 font-semibold text-emerald-600">IS 383 Zone IV / Fine</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </section>

  <script>
    const filterButtons = document.querySelectorAll('.filter-btn');
    const productCards = document.querySelectorAll('.product-card');

    filterButtons.forEach(button => {{
      button.addEventListener('click', () => {{
        filterButtons.forEach(btn => {{
          btn.classList.remove('active', 'bg-brand-navy', 'text-white');
          btn.classList.add('bg-white', 'text-slate-700');
        }});
        button.classList.add('active', 'bg-brand-navy', 'text-white');
        button.classList.remove('bg-white', 'text-slate-700');

        const filter = button.getAttribute('data-filter');
        productCards.forEach(card => {{
          if (filter === 'all' || card.getAttribute('data-category') === filter) {{
            card.style.display = 'flex';
          }} else {{
            card.style.display = 'none';
          }}
        }});
      }});
    }});
  </script>

{faqs_html}

{FOOTER_HTML}
</body>
</html>"""

    with open('products.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("products.html generated with expanded authority.")

build_expanded_products()

# ==========================================
# 3. PLANT & MACHINERY PAGE
# ==========================================
def build_expanded_plant():
    faqs = [
        (
            "What is the daily processing capacity of the Borda crushing plant?",
            "Our primary and secondary crushing lines operate at a combined throughput exceeding 150 Metric Tons Per Hour (TPH), producing more than 1,500 Metric Tons of graded black trap aggregates and hydro-washed sands per operating day."
        ),
        (
            "How does the hydrocyclone sand washer recycle process water?",
            "Our sand washing unit is integrated with a closed-loop water treatment system comprising high-rate thickeners, flocculant dosing units, and settling ponds. Up to 90% of process water is clarified and recycled back into the washing circuit, preventing groundwater wastage."
        ),
        (
            "How does the electronic weighbridge ensure zero billing discrepancy?",
            "We operate a fully computerized 100-Ton electronic weighbridge with automated tare-weight sensors and CCTV verification. Every tipper truck receives a digitally printed weighment slip detailing gross weight, tare weight, net weight, timestamp, and material grade."
        ),
        (
            "Can corporate clients schedule an in-person plant inspection?",
            "Yes, we welcome structural engineers, government PWD inspectors, real estate project heads, and road contractors to inspect our quarry benches, crushing machinery, sieve grading laboratory, and hydrocyclone desilter by contacting Mr. Bhagirath Sinh Sarviya at +91 78789 99033."
        )
    ]

    schema = get_global_schema(
        f"Plant, Machinery & Technology | {COMPANY_NAME}",
        "Technical breakdown of the 1,500 MT/Day basalt stone crushing, hydrocyclone sand washing, and RMC batching plant in Borda, Talaja, Bhavnagar.",
        f"{BASE_URL}/plant.html",
        "WebPage",
        faqs
    )

    head = build_head(
        "Plant & Machinery | Ashutosh Build Stone Pvt. Ltd.",
        "Advanced stone crushing plant, hydrocyclone sand washing desilter, RMC batching tower, and computerized weighbridge in Borda, Talaja, Bhavnagar.",
        "Stone Crusher Plant Talaja, Hydrocyclone Sand Washer Gujarat, RMC Batching Plant Bhavnagar, 100 Ton Weighbridge Borda, Basalt Quarry Mining Gujarat",
        f"{BASE_URL}/plant.html",
        schema
    )

    nav = get_header_nav("plant")
    banner = get_page_banner(
        "Plant, Machinery & Technology",
        "High-Capacity Basalt Crushing, Hydrocyclone Sand Washing & Computerized Concrete Batching Setup",
        "Plant & Machinery"
    )
    factsheet = get_geo_ai_factsheet("Plant & Machinery")
    faqs_html = get_aeo_faq_component(faqs, "Plant Engineering & Capacity FAQs (AEO)")

    content = f"""{head}
{nav}
{factsheet}
{banner}

  <!-- PLANT & MACHINERY OVERVIEW -->
  <section class="py-16 sm:py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-16">
        <div class="lg:col-span-6 space-y-6">
          <span class="inline-flex items-center gap-2 bg-amber-100 text-amber-800 font-bold px-3.5 py-1 rounded-full text-xs uppercase tracking-wider">
            <i class="fa-solid fa-gears"></i> Heavy Industrial Infrastructure
          </span>
          <h2 class="text-3xl sm:text-5xl font-black font-industrial uppercase text-brand-navy leading-tight">
            Engineered For High Output, Zero Downtime & Micro-Graded Precision
          </h2>
          <p class="speakable-summary text-slate-600 leading-relaxed text-sm sm:text-base">
            Located on Gopnath Road, Borda (Talaja), our industrial infrastructure is engineered to process raw basalt boulders into micro-graded aggregates and hydro-washed sands at a continuous throughput exceeding <strong>1,500 Metric Tons every day</strong>.
          </p>
          <p class="text-slate-600 leading-relaxed text-sm sm:text-base">
            Equipped with multi-stage cone crushers, variable frequency vibrating screens, automated sand hydrocyclones, and computerized RMC silos, we control every micron of material grading from quarry extraction to final site discharge.
          </p>

          <div class="grid grid-cols-2 gap-4 pt-2">
            <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
              <div class="text-2xl font-black font-industrial text-amber-500">150+ TPH</div>
              <div class="text-xs font-bold text-slate-700">Crushing Output</div>
              <div class="text-[11px] text-slate-500">Continuous feed system</div>
            </div>
            <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
              <div class="text-2xl font-black font-industrial text-blue-600">90% Recycle</div>
              <div class="text-xs font-bold text-slate-700">Process Water</div>
              <div class="text-[11px] text-slate-500">Closed-loop desilter</div>
            </div>
          </div>
        </div>

        <div class="lg:col-span-6">
          <div class="rounded-3xl overflow-hidden shadow-2xl border-4 border-slate-100">
            <img src="assets/images/sand-washing-crusher-plant-hd.jpeg" alt="Sand Washing Crusher Facility" class="w-full h-96 object-cover" width="1376" height="768">
          </div>
        </div>
      </div>

      <!-- MACHINERY EQUIPMENT BREAKDOWN -->
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="text-xs font-bold text-amber-600 uppercase tracking-widest">Key Assets</span>
        <h3 class="text-3xl sm:text-4xl font-black font-industrial uppercase text-brand-navy mt-1">
          Our Advanced Plant Units & Machinery Fleet
        </h3>
        <p class="text-slate-600 text-sm mt-1">High-performance machines maintaining consistency across every truckload.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-20">
        
        <!-- Asset 1 -->
        <div class="bg-slate-50 rounded-3xl p-6 border border-slate-200 card-hover flex flex-col justify-between">
          <div>
            <div class="h-48 rounded-2xl overflow-hidden mb-4 bg-slate-200">
              <img src="assets/images/quarry-crushing-facility-hd.jpeg" alt="Crushing Unit" class="w-full h-full object-cover">
            </div>
            <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Multi-Stage Jaw & Cone Crushers</h4>
            <p class="text-xs text-slate-600 mt-2 leading-relaxed">
              Heavy hydraulic jaw crushers handle primary rock breaking, followed by high-speed cone crushers producing cubical, stress-free stone particles without micro-fissures.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-200 text-xs font-bold text-amber-600">
            <i class="fa-solid fa-check-circle mr-1"></i> Superior Cubical Shape
          </div>
        </div>

        <!-- Asset 2 -->
        <div class="bg-slate-50 rounded-3xl p-6 border border-slate-200 card-hover flex flex-col justify-between">
          <div>
            <div class="h-48 rounded-2xl overflow-hidden mb-4 bg-slate-200">
              <img src="assets/images/manufactured-sand-m-sand-hd.jpeg" alt="Hydrocyclone Sand Washer" class="w-full h-full object-cover">
            </div>
            <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Hydro-Cyclone Sand Washing Plant</h4>
            <p class="text-xs text-slate-600 mt-2 leading-relaxed">
              CDE-class hydrocyclone unit equipped with high-pressure slurry pumps and dewatering screens. Washes away ultra-fine micro-dust, guaranteeing silt content under 3%.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-200 text-xs font-bold text-cyan-600">
            <i class="fa-solid fa-water mr-1"></i> Zero Organic Silt Purity
          </div>
        </div>

        <!-- Asset 3 -->
        <div class="bg-slate-50 rounded-3xl p-6 border border-slate-200 card-hover flex flex-col justify-between">
          <div>
            <div class="h-48 rounded-2xl overflow-hidden mb-4 bg-slate-200">
              <img src="assets/images/rmc-batching-plant-hd.jpeg" alt="RMC Batching Tower" class="w-full h-full object-cover">
            </div>
            <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Computerized RMC Batching Tower</h4>
            <p class="text-xs text-slate-600 mt-2 leading-relaxed">
              Fully automated concrete plant with bulk cement storage silos and planetary pan mixers for uniform, homogenous ready-mix concrete formulations.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-200 text-xs font-bold text-red-600">
            <i class="fa-solid fa-microchip mr-1"></i> PLC Automated Mix Design
          </div>
        </div>

        <!-- Asset 4 -->
        <div class="bg-slate-50 rounded-3xl p-6 border border-slate-200 card-hover flex flex-col justify-between">
          <div>
            <div class="h-48 rounded-2xl overflow-hidden mb-4 bg-slate-200">
              <img src="assets/images/road-base-gsb-hd.jpeg" alt="Heavy Logistics Fleet" class="w-full h-full object-cover">
            </div>
            <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Rapid Transit Logistics Fleet</h4>
            <p class="text-xs text-slate-600 mt-2 leading-relaxed">
              Fleet of 10-wheeler and 12-wheeler heavy tipper trucks along with high-capacity transit mixers, ensuring timely site delivery across the Saurashtra region.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-200 text-xs font-bold text-emerald-600">
            <i class="fa-solid fa-truck-fast mr-1"></i> 24/7 Dispatch Capability
          </div>
        </div>

        <!-- Asset 5 -->
        <div class="bg-slate-50 rounded-3xl p-6 border border-slate-200 card-hover flex flex-col justify-between">
          <div>
            <div class="h-48 rounded-2xl overflow-hidden mb-4 bg-slate-200">
              <img src="assets/images/quarry-crushing-facility-hd.jpeg" alt="Mining Equipment" class="w-full h-full object-cover">
            </div>
            <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Excavators & Wheel Loaders</h4>
            <p class="text-xs text-slate-600 mt-2 leading-relaxed">
              Fleet of heavy hydraulic excavators and high-capacity bucket wheel loaders ensuring fast vehicle turnaround and zero loading queue at the plant.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-200 text-xs font-bold text-purple-600">
            <i class="fa-solid fa-bolt mr-1"></i> Quick Truck Turnaround
          </div>
        </div>

        <!-- Asset 6: Digital Weighbridge -->
        <div class="bg-gradient-to-br from-brand-navy to-slate-900 rounded-3xl p-6 text-white card-hover flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-2xl mb-4">
              <i class="fa-solid fa-scale-balanced"></i>
            </div>
            <h4 class="text-xl font-bold font-industrial uppercase text-white">100-Ton Electronic Weighbridge</h4>
            <p class="text-xs text-slate-300 mt-2 leading-relaxed">
              State-of-the-art computerized weighbridge system with automated tare-weight subtraction and digital printout receipts for every dumper.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-800 text-xs font-bold text-amber-400">
            <i class="fa-solid fa-stamp mr-1"></i> 100% Weight Transparency
          </div>
        </div>

      </div>

      <!-- Factory Visit CTA -->
      <div class="bg-amber-500 rounded-3xl p-8 sm:p-10 text-slate-950 flex flex-col md:flex-row items-center justify-between gap-6 shadow-xl">
        <div>
          <span class="text-xs font-black uppercase tracking-widest bg-slate-950 text-white px-3 py-1 rounded-full">Inspection Welcome</span>
          <h3 class="text-2xl sm:text-3xl font-black font-industrial uppercase mt-2">Book a Plant Visit & Material Inspection</h3>
          <p class="text-xs sm:text-sm font-medium mt-1">Engineers, contractors, and project managers are invited to visit our Borda (Talaja) plant for live testing.</p>
        </div>
        <div class="flex gap-3 flex-shrink-0">
          <a href="tel:{PHONE_BHAGIRATH_RAW}" class="bg-slate-950 hover:bg-slate-800 text-white font-bold px-6 py-3.5 rounded-xl text-xs sm:text-sm shadow-md transition-all flex items-center gap-2">
            <i class="fa-solid fa-phone"></i> Call Bhagirath Sinh
          </a>
        </div>
      </div>

    </div>
  </section>

{faqs_html}

{FOOTER_HTML}
</body>
</html>"""

    with open('plant.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("plant.html generated with expanded authority.")

build_expanded_plant()

# ==========================================
# 4. CONTRACTING PAGE
# ==========================================
def build_expanded_contracting():
    faqs = [
        (
            "What categories of civil works does Ashutosh Build Stone execute?",
            "As a certified Government Approved Building Contractor, we execute national and state highway flexible/rigid pavements, Granular Sub-Base (GSB), Wet Mix Macadam (WMM), industrial machine foundations, earthwork grading, retaining structures, and coastal sea-wall rock armor."
        ),
        (
            "Does Ashutosh Build Stone provide complete GST tax invoices for tenders?",
            "Yes, we are 100% tax compliant with regular GST registration, PAN (ABCCA2752K), and TAN (AHMA32297G). All supplies and contracting billings are accompanied by formal GST e-way bills and computerized weighbridge slips."
        ),
        (
            "What machinery does your contracting wing deploy on site?",
            "Our civil contracting division deploys a fleet of hydraulic excavators (JCB & Tata Hitachi), vibratory soil compactors (10-12 Ton rollers), motor graders, water tankers, wheel loaders, and 10/12-wheeler heavy tipper trucks."
        ),
        (
            "How can government departments or EPC contractors invite tender bids?",
            "EPC contractors and municipal departments can forward tender documents and BOQs directly to Director Alpesh Chauhan at +91 76239 98398 or initiate contact through our commercial WhatsApp desk."
        )
    ]

    schema = get_global_schema(
        f"Govt. Approved Building Contractor | {COMPANY_NAME}",
        "Government Approved Building Contractor specializing in highway road construction, industrial foundations, and bulk infrastructure procurement in Gujarat.",
        f"{BASE_URL}/contracting.html",
        "WebPage",
        faqs
    )

    head = build_head(
        "Govt. Contracting | Ashutosh Build Stone Pvt. Ltd.",
        "Certified Government Approved Building Contractor for highway construction, industrial foundations, and civil infrastructure across Gujarat.",
        "Govt Approved Contractor Gujarat, Highway Road Construction Bhavnagar, PWD Contractor Talaja, Industrial Earthworks Alang, Civil Infrastructure Gujarat",
        f"{BASE_URL}/contracting.html",
        schema
    )

    nav = get_header_nav("contracting")
    banner = get_page_banner(
        "Govt. Approved Building Contractor",
        "Executing Highway Development, Industrial Earthworks, Retaining Structures & Bulk Material Supply",
        "Civil Contracting"
    )
    factsheet = get_geo_ai_factsheet("Civil Contracting")
    faqs_html = get_aeo_faq_component(faqs, "Government Contracting & Tender FAQs (AEO)")

    content = f"""{head}
{nav}
{factsheet}
{banner}

  <!-- CONTRACTING SERVICES SECTION -->
  <section class="py-16 sm:py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Top Credentials Overview -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-16">
        <div class="lg:col-span-7 space-y-6">
          <span class="inline-flex items-center gap-2 bg-amber-100 text-amber-800 font-bold px-3.5 py-1 rounded-full text-xs uppercase tracking-wider">
            <i class="fa-solid fa-landmark"></i> Official Government Approval
          </span>
          <h2 class="text-3xl sm:text-5xl font-black font-industrial uppercase text-brand-navy leading-tight">
            Certified Civil Engineering Partner For Gujarat's Major Infrastructure
          </h2>
          <p class="speakable-summary text-slate-600 leading-relaxed text-sm sm:text-base">
            <strong>ASHUTOSH BUILD STONE PVT. LTD.</strong> possesses certified government contractor credentials, enabling us to tender, execute, and deliver road construction, heavy industrial foundations, and civil infrastructure projects for government bodies and private conglomerates.
          </p>
          <p class="text-slate-600 leading-relaxed text-sm sm:text-base">
            With our own captive basalt quarries, stone crushers, sand washing units, and heavy earthmoving machinery, we provide seamless turnkey execution without third-party material bottlenecks or price fluctuations.
          </p>

          <div class="pt-2 flex flex-wrap gap-4">
            <a href="tel:{PHONE_ALPESH_RAW}" class="inline-flex items-center gap-2 bg-brand-navy hover:bg-blue-900 text-white font-bold px-6 py-3.5 rounded-xl text-xs sm:text-sm shadow-md transition-all">
              <i class="fa-solid fa-phone text-amber-400"></i>
              <span>Consult Alpesh Chauhan (Sales & Tenders)</span>
            </a>
            <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}?text=Hello,%20I%20am%20inquiring%20about%20civil%20contracting%20services%20from%20Ashutosh%20Build%20Stone%20Pvt.%20Ltd." target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-[#25D366] hover:bg-[#20ba59] text-white font-bold px-6 py-3.5 rounded-xl text-xs sm:text-sm shadow-md transition-all">
              <i class="fa-brands fa-whatsapp text-lg"></i>
              <span>WhatsApp Tender Inquiry</span>
            </a>
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="bg-slate-50 border border-slate-200 rounded-3xl p-6 sm:p-8 shadow-lg space-y-5">
            <h4 class="text-xs font-bold text-amber-600 uppercase tracking-widest border-b border-slate-200 pb-3">Contractor Specifications</h4>
            <div class="space-y-3 text-xs sm:text-sm text-slate-700">
              <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                <span class="text-slate-500">Corporate Status:</span>
                <span class="font-bold text-brand-navy">Private Limited</span>
              </div>
              <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                <span class="text-slate-500">CIN Registration:</span>
                <span class="font-mono font-bold text-amber-600">{CIN}</span>
              </div>
              <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                <span class="text-slate-500">GST Compliance:</span>
                <span class="font-bold text-emerald-600">Full Regular GST Billing</span>
              </div>
              <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                <span class="text-slate-500">Geographic Coverage:</span>
                <span class="font-bold text-brand-navy">Bhavnagar, Amreli, Surat, All Gujarat</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-500">Key Execution:</span>
                <span class="font-bold text-brand-navy">Roads, Earthworks, Bulk Aggregates</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- CONTRACTING SERVICES CARDS -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm card-hover">
          <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-600 flex items-center justify-center text-2xl mb-4">
            <i class="fa-solid fa-road"></i>
          </div>
          <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Road & Highway Construction</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Execution of Granular Sub-Base (GSB), Wet Mix Macadam (WMM), Bituminous Macadam, and complete culvert structural work for PWD, State Highways, and NHAI packages.
          </p>
        </div>

        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm card-hover">
          <div class="w-12 h-12 rounded-xl bg-blue-500/10 text-blue-600 flex items-center justify-center text-2xl mb-4">
            <i class="fa-solid fa-industry"></i>
          </div>
          <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Industrial Earthworks & Grading</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Large-scale site leveling, ground compaction, heavy equipment footing excavation, storm drainage systems, and industrial factory flooring bases.
          </p>
        </div>

        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm card-hover">
          <div class="w-12 h-12 rounded-xl bg-cyan-500/10 text-cyan-600 flex items-center justify-center text-2xl mb-4">
            <i class="fa-solid fa-ship"></i>
          </div>
          <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Port & Maritime Protection Works</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Supplying and installing heavy basalt rock armor for coastal sea walls, breakwaters, and harbor infrastructure in the Alang and Bhavnagar coastal belt.
          </p>
        </div>

        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm card-hover">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 text-emerald-600 flex items-center justify-center text-2xl mb-4">
            <i class="fa-solid fa-bridge"></i>
          </div>
          <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Bridge & Culvert Substructures</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Heavy mass concrete pourings, abutment foundation stones, pier construction, and approach road earthwork with laboratory certified aggregate grading.
          </p>
        </div>

        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm card-hover">
          <div class="w-12 h-12 rounded-xl bg-purple-500/10 text-purple-600 flex items-center justify-center text-2xl mb-4">
            <i class="fa-solid fa-city"></i>
          </div>
          <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Mega Real Estate Procurement</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Dedicated long-term supply contracts for residential townships, commercial complexes, and industrial warehouses with guaranteed fixed delivery timelines.
          </p>
        </div>

        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm card-hover">
          <div class="w-12 h-12 rounded-xl bg-stone-500/10 text-stone-700 flex items-center justify-center text-2xl mb-4">
            <i class="fa-solid fa-mountain"></i>
          </div>
          <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Quarry Mining & Crushing Contracts</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Contract mining, on-site mobile crushing, screening operations, and overburden removal using our fleet of excavators and dumpers.
          </p>
        </div>
      </div>

    </div>
  </section>

{faqs_html}

{FOOTER_HTML}
</body>
</html>"""

    with open('contracting.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("contracting.html generated with expanded authority.")

build_expanded_contracting()

# ==========================================
# 5. CALCULATOR PAGE
# ==========================================
def build_expanded_calculator():
    faqs = [
        (
            "What is 1 Brass in civil construction and how many Metric Tons does it equal?",
            "In Gujarat civil construction, 1 Brass is equal to 100 Cubic Feet (approx. 2.83 Cubic Meters). For Black Trap 20mm aggregate, 1 Brass weighs approximately 4.5 to 4.8 Metric Tons depending on stone density and moisture. For M-Sand, 1 Brass weighs approximately 4.6 to 4.9 Metric Tons."
        ),
        (
            "How do I calculate the aggregate and sand needed for a 1,000 sq.ft RCC roof slab?",
            "For a standard 1,000 sq.ft residential roof slab with 5 inches (0.42 ft) thickness, total concrete volume is approximately 417 Cu.Ft (approx. 4.17 Brass or 11.8 m³). Under standard M20 mix design (1:1.5:3), you will require approximately 6.5 Tons of M-Sand and 13.5 Tons of 20mm Black Trap Aggregate."
        ),
        (
            "How many tipper or dumper truckloads are needed for my order?",
            "A standard 10-wheeler dumper carries roughly 18 to 22 Metric Tons (approx. 4 to 4.5 Brass), while a heavy 12-wheeler multi-axle tipper carries between 28 and 32 Metric Tons (approx. 6 to 7 Brass)."
        ),
        (
            "Can I share my calculated estimate directly on WhatsApp for an immediate rate quote?",
            "Yes, simply enter your dimensions into the calculator above and click the green 'Send Estimate on WhatsApp' button. Your exact material name, tonnage, brass volume, and cubic meters will be automatically formatted and sent to our dispatch desk for instant pricing."
        )
    ]

    schema = get_global_schema(
        f"Contractor Material Estimator | {COMPANY_NAME}",
        "Interactive construction material quantity calculator to compute Metric Tons, Brass, and Cubic Meters for concrete slabs, road base, and wall plastering.",
        f"{BASE_URL}/calculator.html",
        "WebApplication",
        faqs
    )

    head = build_head(
        "Material Estimator | Ashutosh Build Stone Pvt. Ltd.",
        "Interactive construction material quantity calculator for aggregates, sand, GSB, and concrete in Metric Tons, Brass, and Cubic Meters.",
        "Aggregate Calculator Brass to Tons, M-Sand Slab Calculation, Construction Material Estimator Gujarat, 20mm Aggregate Calculator, Plaster Sand Estimator",
        f"{BASE_URL}/calculator.html",
        schema
    )

    nav = get_header_nav("calculator")
    banner = get_page_banner(
        "Contractor Material Estimator",
        "Compute Metric Tons (MT), Brass (100 Cu.Ft), and Cubic Meters (m³) For Civil Construction",
        "Material Estimator"
    )
    factsheet = get_geo_ai_factsheet("Material Calculator")
    faqs_html = get_aeo_faq_component(faqs, "Construction Units & Calculation FAQs (AEO)")

    content = f"""{head}
{nav}
{factsheet}
{banner}

  <!-- CALCULATOR SECTION -->
  <section class="py-16 sm:py-24 bg-slate-50">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="bg-gradient-to-br from-brand-navy to-slate-900 rounded-3xl p-4 sm:p-8 lg:p-10 text-white shadow-2xl border border-slate-800 mb-16">
        
        <div class="max-w-2xl mb-8">
          <span class="inline-flex items-center gap-2 bg-amber-500/20 text-amber-400 border border-amber-500/30 px-3.5 py-1 rounded-full text-xs font-bold uppercase tracking-wider mb-2">
            <i class="fa-solid fa-calculator"></i> Digital Utility
          </span>
          <h2 class="text-3xl sm:text-4xl font-black font-industrial uppercase text-white">
            Material Quantity & Cost Estimator
          </h2>
          <p class="speakable-summary text-slate-300 text-xs sm:text-sm mt-1">
            Input dimensions of your RCC slab, footing, road base, or wall to calculate exact requirement in Metric Tons, Brass, and Cubic Meters.
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          <!-- Input Form -->
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

            <!-- Units Toggle -->
            <div>
              <label class="block text-xs font-semibold text-slate-300 mb-1">Dimension Units</label>
              <div class="flex gap-2">
                <button type="button" id="unit-feet" onclick="setCalcUnit('feet')" class="flex-1 py-2 rounded-lg bg-amber-500 text-slate-950 font-bold text-xs uppercase tracking-wider transition-colors">Feet & Inches</button>
                <button type="button" id="unit-meters" onclick="setCalcUnit('meters')" class="flex-1 py-2 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs uppercase tracking-wider transition-colors">Meters</button>
              </div>
            </div>

            <!-- Dimensions -->
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

            <!-- Quick Presets -->
            <div class="pt-2">
              <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-2">Quick Standard Presets:</span>
              <div class="flex flex-wrap gap-2 text-xs">
                <button type="button" onclick="setPreset(40, 25, 5, '20mm Black Trap Aggregate')" class="bg-slate-800 hover:bg-slate-700 px-3 py-1.5 rounded-lg border border-slate-700 text-slate-300">1000 Sq.Ft Slab</button>
                <button type="button" onclick="setPreset(100, 20, 8, 'GSB / WMM Road Base')" class="bg-slate-800 hover:bg-slate-700 px-3 py-1.5 rounded-lg border border-slate-700 text-slate-300">Road Base Layer</button>
                <button type="button" onclick="setPreset(50, 20, 0.75, 'Plaster Sand (P-Sand)')" class="bg-slate-800 hover:bg-slate-700 px-3 py-1.5 rounded-lg border border-slate-700 text-slate-300">Wall Plaster Area</button>
              </div>
            </div>
          </div>

          <!-- Output Box -->
          <div class="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-2xl p-6 flex flex-col justify-between">
            <div>
              <h4 class="text-xs font-bold text-amber-400 uppercase tracking-widest mb-4">Estimated Material</h4>
              
              <div class="space-y-4">
                <div class="bg-slate-900/90 rounded-xl p-4 border border-slate-700 flex items-center justify-between">
                  <div>
                    <span class="text-xs text-slate-400">Estimated Weight:</span>
                    <div class="text-3xl font-black font-industrial text-amber-400" id="res-tons">28.3 MT</div>
                  </div>
                  <span class="text-xs font-bold bg-amber-500/20 text-amber-300 px-2 py-1 rounded">Metric Tons</span>
                </div>

                <div class="bg-slate-900/90 rounded-xl p-4 border border-slate-700 flex items-center justify-between">
                  <div>
                    <span class="text-xs text-slate-400">Brass (100 Cu.Ft):</span>
                    <div class="text-3xl font-black font-industrial text-cyan-400" id="res-brass">6.25 Brass</div>
                  </div>
                  <span class="text-xs font-bold bg-cyan-500/20 text-cyan-300 px-2 py-1 rounded">Local Unit</span>
                </div>

                <div class="bg-slate-900/90 rounded-xl p-4 border border-slate-700 flex items-center justify-between">
                  <div>
                    <span class="text-xs text-slate-400">Volume:</span>
                    <div class="text-xl font-bold font-industrial text-slate-200" id="res-cu-m">17.7 m³ (625 Cu.Ft)</div>
                  </div>
                  <span class="text-xs text-slate-400">Volume</span>
                </div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-700">
              <button onclick="sendCalculatedQuote()" class="w-full bg-[#25D366] hover:bg-[#20ba59] text-white font-bold py-3.5 px-4 rounded-xl flex items-center justify-center gap-2 text-sm transition-transform active:scale-95 shadow-md">
                <i class="fa-brands fa-whatsapp text-lg"></i> Send Estimate on WhatsApp
              </button>
            </div>
          </div>

        </div>

      </div>

      <!-- STANDARD CONCRETE MIX RATIOS TABLE -->
      <div class="bg-white rounded-3xl p-8 sm:p-10 shadow-lg border border-slate-200">
        <h3 class="text-2xl font-black font-industrial uppercase text-brand-navy mb-4">
          Standard IS 456 Concrete Mix Design Ratios Reference
        </h3>
        <p class="text-xs sm:text-sm text-slate-600 mb-6">Use this guideline table to cross-check nominal mix volume proportions per cubic meter of concrete.</p>
        
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs sm:text-sm border-collapse">
            <thead>
              <tr class="bg-slate-800 text-white font-industrial uppercase text-sm">
                <th class="p-3.5 rounded-l-lg">Grade</th>
                <th class="p-3.5">Proportion (Cement : Sand : Aggregate)</th>
                <th class="p-3.5">Characteristic Strength</th>
                <th class="p-3.5 rounded-r-lg">Recommended Structural Use</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 text-slate-700">
              <tr class="hover:bg-slate-50">
                <td class="p-3.5 font-bold text-brand-navy">M15</td>
                <td class="p-3.5">1 : 2 : 4</td>
                <td class="p-3.5">15 N/mm² @ 28 Days</td>
                <td class="p-3.5">PCC, Leveling course, Footpath</td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3.5 font-bold text-brand-navy">M20</td>
                <td class="p-3.5">1 : 1.5 : 3</td>
                <td class="p-3.5">20 N/mm² @ 28 Days</td>
                <td class="p-3.5">Standard RCC Slabs, Beams, Columns</td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3.5 font-bold text-brand-navy">M25</td>
                <td class="p-3.5">1 : 1 : 2</td>
                <td class="p-3.5">25 N/mm² @ 28 Days</td>
                <td class="p-3.5">Heavy Foundations, Water Tanks, Retaining Walls</td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3.5 font-bold text-brand-navy">M30 / M35</td>
                <td class="p-3.5">Design Mix (Automated RMC)</td>
                <td class="p-3.5">30 - 35 N/mm² @ 28 Days</td>
                <td class="p-3.5">High-Rise Buildings, Bridge Piers, Industrial Floors</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </section>

  <script>
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

    function setPreset(l, w, d, mat) {{
      setCalcUnit('feet');
      document.getElementById('calc-len').value = l;
      document.getElementById('calc-wid').value = w;
      document.getElementById('calc-dep').value = d;
      const select = document.getElementById('calc-material');
      for (let i = 0; i < select.options.length; i++) {{
        if (select.options[i].value === mat) {{
          select.selectedIndex = i;
          break;
        }}
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

{faqs_html}

{FOOTER_HTML}
</body>
</html>"""

    with open('calculator.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("calculator.html generated with expanded authority.")

build_expanded_calculator()


# ==========================================
# 6. GALLERY PAGE
# ==========================================
def build_expanded_gallery():
    gallery_items = [
        ("assets/images/sand-washing-crusher-plant-hd.jpeg", "Primary Multi-Stage Crushing & Sand Washing Plant", "Machinery", "High-capacity cone crusher and hydrocyclone desilter unit operating in daylight."),
        ("assets/images/manufactured-sand-m-sand-hd.jpeg", "Hydro-Cyclone Washed Sand Conical Stockpiles", "Sand Washing", "Pure silt-free manufactured sand produced in Zone II grading for RCC slabs."),
        ("assets/images/aggregate-20mm-hd.jpeg", "20mm Black Trap Aggregate - Sharp Cubical Shape", "Aggregates", "Macro shot showing clean fracture faces and minimal flakiness index <15%."),
        ("assets/images/aggregate-10mm-hd.jpeg", "10mm Fine Black Trap Grit & Chipping", "Aggregates", "Uniformly graded angular grit for asphalt road carpeting and paver blocks."),
        ("assets/images/aggregate-40mm-hd.jpeg", "40mm Coarse Aggregate Ballast for Mass Concrete", "Aggregates", "Heavy-duty basalt stones for railway ballast and foundation footings."),
        ("assets/images/plaster-sand-fine-hd.jpeg", "Washed Fine Plaster Sand (P-Sand)", "Sand Washing", "Double-washed Zone IV fine sand for mirror-finish, crack-free plastering."),
        ("assets/images/rmc-batching-plant-hd.jpeg", "Ready-Mix Concrete Computerized Batching Tower", "RMC", "Automated cement storage silos and planetary pan mixers with transit mixers."),
        ("assets/images/quarry-crushing-facility-hd.jpeg", "Aerial View of Open Pit Basalt Quarry & Benches", "Quarry", "Active mining benches with excavators, dumpers, and primary crushing bridges."),
        ("assets/images/road-base-gsb-hd.jpeg", "Granular Sub-Base (GSB) Stockpiles for Road Works", "Roads", "Dense-graded road base material conforming to MoRTH specifications."),
        ("assets/images/company-banner.jpeg", "Official Corporate Registration Banner", "Corporate", "Official display board displaying CIN, PAN, TAN, address, and phone numbers."),
        ("assets/images/poster-nirmaan-aasan.jpeg", "Marketing Poster: हमारे साथ, निर्माण बने आसान", "Marketing", "Official company marketing banner featuring high-rise infrastructure."),
        ("assets/images/poster-sapno-ki-raksha.jpeg", "Marketing Poster: निर्माण मटेरियल जो करे आपके सपनों की रक्षा", "Marketing", "Corporate marketing visual highlighting durability and strength.")
    ]

    faqs = [
        (
            "Are the gallery photos taken at the actual Borda plant?",
            "Yes, our gallery displays actual field operations, heavy machinery setups, quarry extraction benches, and high-definition material samples from our Borda (Talaja) manufacturing plant."
        ),
        (
            "Can clients request high-resolution test certificates alongside material photos?",
            "Yes, test reports for Sieve Analysis (IS 383:2016), Aggregate Crushing Value, Impact Value, Silt Content, and Flakiness Index are provided digitally or with dispatched weighbridge slips."
        )
    ]

    schema = get_global_schema(
        f"Visual Photo Gallery | {COMPANY_NAME}",
        "High-definition photograph gallery showcasing the basalt quarry, crushing plant, hydrocyclone washer, and aggregates of Ashutosh Build Stone Pvt. Ltd.",
        f"{BASE_URL}/gallery.html",
        "ImageGallery",
        faqs
    )

    head = build_head(
        "Photo Gallery | Ashutosh Build Stone Pvt. Ltd.",
        "High-resolution photos of stone crushing machinery, washed M-sand stockpiles, 20mm aggregates, and transit mixer fleet in Bhavnagar, Gujarat.",
        "Stone Crusher Photos Bhavnagar, M-Sand Plant Pictures Gujarat, 20mm Jelly Photos, Quarry Mining Images Talaja",
        f"{BASE_URL}/gallery.html",
        schema
    )

    nav = get_header_nav("gallery")
    banner = get_page_banner(
        "Visual Photo Gallery",
        "High-Definition Visual Tour of Our Quarry Operations, Crushing Plants, Sand Washing & Delivery Fleet",
        "Gallery"
    )
    factsheet = get_geo_ai_factsheet("Photo Gallery")
    faqs_html = get_aeo_faq_component(faqs, "Media & Photo Verification FAQs (AEO)")

    gallery_cards = ""
    for img, caption, cat, desc in gallery_items:
        gallery_cards += f"""
        <div class="gallery-item relative rounded-3xl overflow-hidden shadow-sm border border-slate-200 group cursor-pointer h-72 bg-slate-100" onclick="openLightbox('{img}', '{caption}')">
          <img src="{img}" alt="{caption}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" loading="lazy">
          <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/20 to-transparent opacity-90 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-5">
            <span class="text-[10px] font-bold text-amber-400 uppercase tracking-widest">{cat}</span>
            <div class="text-sm sm:text-base font-bold text-white mt-0.5">{caption}</div>
            <p class="text-[11px] text-slate-300 mt-1 line-clamp-1">{desc}</p>
          </div>
          <div class="absolute top-4 right-4 w-9 h-9 rounded-full bg-black/50 text-white flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
            <i class="fa-solid fa-expand text-xs"></i>
          </div>
        </div>
        """

    content = f"""{head}
{nav}
{factsheet}
{banner}

  <!-- GALLERY GRID SECTION -->
  <section class="py-16 sm:py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-2xl mx-auto mb-12">
        <span class="text-xs font-bold text-amber-600 uppercase tracking-widest">Field Photos</span>
        <h2 class="text-3xl sm:text-4xl font-black font-industrial uppercase text-brand-navy mt-1">
          Explore Our Operations
        </h2>
        <p class="speakable-summary text-slate-600 text-sm mt-1">Click on any image to open the full-screen high-definition lightbox preview with detailed captions.</p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {gallery_cards}
      </div>

    </div>
  </section>

{faqs_html}

{FOOTER_HTML}
</body>
</html>"""

    with open('gallery.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("gallery.html generated with expanded authority.")

build_expanded_gallery()


# ==========================================
# 7. CONTACT PAGE
# ==========================================
def build_expanded_contact():
    faqs = [
        (
            "What are the direct mobile phone numbers for order booking?",
            "You can contact our Directors directly: Mr. Bhagirath Sinh Sarviya at +91 78789 99033 (Plant Management & Logistics) or Alpesh Chauhan at +91 76239 98398 (Sales & Government Tenders)."
        ),
        (
            "What is the exact plant address and GPS location?",
            "The plant and registered office is located at Gopnath Road, At. Borda, Tal. Talaja, Dist. Bhavnagar, Gujarat - 364130, India. GPS Coordinates: Latitude 21.2850° N, Longitude 72.0850° E."
        ),
        (
            "What regions and cities does Ashutosh Build Stone supply to?",
            "We provide continuous fleet delivery across Bhavnagar, Talaja, Alang Ship Recycling Yard, Mahuva, Palitana, Sihor, Amreli, Ghogha, and major infrastructure corridors across Gujarat."
        ),
        (
            "What are the plant operational hours for tipper loading?",
            "Office inquiries are active Monday to Sunday from 7:00 AM to 8:00 PM. For active road contracts, government tenders, and mega infrastructure projects, our crushing plant and weighbridge operate 24/7."
        )
    ]

    schema = get_global_schema(
        f"Contact Us & Plant Location | {COMPANY_NAME}",
        "Get in touch with Directors Bhagirath Sinh Sarviya and Alpesh Chauhan at Ashutosh Build Stone Pvt. Ltd. in Borda, Talaja, Bhavnagar.",
        f"{BASE_URL}/contact.html",
        "ContactPage",
        faqs
    )

    head = build_head(
        "Contact Us | Ashutosh Build Stone Pvt. Ltd.",
        "Official phone numbers, plant address, and Google Map directions for Ashutosh Build Stone Pvt. Ltd. in Borda, Talaja, Bhavnagar, Gujarat.",
        "Ashutosh Build Stone Contact, Bhagirath Sinh Phone Number, Alpesh Chauhan Mobile, Stone Crusher Near Me Talaja, Bhavnagar Aggregate Supplier Address",
        f"{BASE_URL}/contact.html",
        schema
    )

    nav = get_header_nav("contact")
    banner = get_page_banner(
        "Contact Us & Plant Location",
        "Connect Directly with Directors for Bulk Inquiries, Commercial Orders & Site Visits",
        "Contact"
    )
    factsheet = get_geo_ai_factsheet("Contact & Location")
    faqs_html = get_aeo_faq_component(faqs, "Location, Transport & Order FAQs (AEO)")

    content = f"""{head}
{nav}
{factsheet}
{banner}

  <!-- CONTACT & LOCATION SECTION -->
  <section class="py-16 sm:py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start mb-16">
        
        <!-- Left Column: Contact Cards & Info -->
        <div class="lg:col-span-5 space-y-6">
          
          <!-- Key Contact 1: Bhagirath Sinh -->
          <div class="bg-white rounded-3xl p-6 sm:p-7 shadow-md border-l-4 border-amber-500">
            <div class="flex items-center justify-between mb-3">
              <span class="text-xs font-bold uppercase tracking-wider text-amber-600 bg-amber-50 px-2.5 py-1 rounded">Director / Key Contact</span>
              <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}" target="_blank" rel="noopener noreferrer" class="text-emerald-600 hover:text-emerald-700 text-2xl" title="Chat on WhatsApp">
                <i class="fa-brands fa-whatsapp"></i>
              </a>
            </div>
            <h3 class="text-2xl font-black text-brand-navy">Mr. Bhagirath Sinh Sarviya</h3>
            <p class="text-xs text-slate-500 mt-1">Plant Operations, Weighbridge & Regional Supply Dispatch</p>
            
            <div class="mt-5 pt-3 border-t border-slate-100 flex items-center justify-between">
              <a href="tel:{PHONE_BHAGIRATH_RAW}" class="inline-flex items-center gap-2 text-base font-black text-brand-navy hover:text-amber-600">
                <i class="fa-solid fa-phone text-amber-500"></i> {PHONE_BHAGIRATH}
              </a>
              <a href="tel:{PHONE_BHAGIRATH_RAW}" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs px-3.5 py-1.5 rounded-xl shadow-sm">
                Call Direct
              </a>
            </div>
          </div>

          <!-- Key Contact 2: Alpesh Chauhan -->
          <div class="bg-white rounded-3xl p-6 sm:p-7 shadow-md border-l-4 border-blue-600">
            <div class="flex items-center justify-between mb-3">
              <span class="text-xs font-bold uppercase tracking-wider text-blue-600 bg-blue-50 px-2.5 py-1 rounded">Director / Key Contact</span>
              <a href="https://wa.me/{PHONE_ALPESH_RAW}" target="_blank" rel="noopener noreferrer" class="text-emerald-600 hover:text-emerald-700 text-2xl" title="Chat on WhatsApp">
                <i class="fa-brands fa-whatsapp"></i>
              </a>
            </div>
            <h3 class="text-2xl font-black text-brand-navy">Alpesh Chauhan</h3>
            <p class="text-xs text-slate-500 mt-1">Corporate Client Accounts, Tenders, Billing & Quotations</p>
            
            <div class="mt-5 pt-3 border-t border-slate-100 flex items-center justify-between">
              <a href="tel:{PHONE_ALPESH_RAW}" class="inline-flex items-center gap-2 text-base font-black text-brand-navy hover:text-blue-600">
                <i class="fa-solid fa-phone text-blue-600"></i> {PHONE_ALPESH}
              </a>
              <a href="tel:{PHONE_ALPESH_RAW}" class="bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs px-3.5 py-1.5 rounded-xl shadow-sm">
                Call Direct
              </a>
            </div>
          </div>

          <!-- Official Details -->
          <div class="bg-white rounded-3xl p-6 sm:p-7 shadow-md space-y-4 text-xs sm:text-sm text-slate-700">
            <div class="flex items-start gap-3">
              <i class="fa-solid fa-location-dot text-amber-500 text-base mt-1 flex-shrink-0"></i>
              <div>
                <strong class="text-brand-navy block">Crusher Plant & Registered Office:</strong>
                <span class="text-slate-600">{ADDRESS}</span>
              </div>
            </div>

            <div class="flex items-center gap-3">
              <i class="fa-solid fa-id-card text-blue-600 text-base flex-shrink-0"></i>
              <div><strong>CIN:</strong> {CIN}</div>
            </div>

            <div class="flex items-center gap-3">
              <i class="fa-solid fa-file-invoice text-emerald-600 text-base flex-shrink-0"></i>
              <div><strong>PAN:</strong> {PAN} &nbsp;|&nbsp; <strong>TAN:</strong> {TAN}</div>
            </div>

            <div class="flex items-center gap-3">
              <i class="fa-solid fa-clock text-amber-500 text-base flex-shrink-0"></i>
              <div><strong>Hours:</strong> Mon - Sun: 7:00 AM - 8:00 PM (24/7 for active projects)</div>
            </div>
          </div>

          <!-- Travel Distances -->
          <div class="bg-slate-100 rounded-3xl p-5 border border-slate-200 text-xs">
            <span class="font-bold text-slate-800 block mb-2 uppercase tracking-wider">Transport Connectivity From Plant:</span>
            <div class="grid grid-cols-2 gap-2 text-slate-600">
              <div>• Talaja Town: ~12 km</div>
              <div>• Alang Shipyard: ~25 km</div>
              <div>• Bhavnagar City: ~65 km</div>
              <div>• Mahuva City: ~45 km</div>
            </div>
          </div>

        </div>

        <!-- Right Column: Inquiry Form & Map -->
        <div class="lg:col-span-7 space-y-6">
          
          <div class="bg-white rounded-3xl p-6 sm:p-8 shadow-md border border-slate-200">
            <h3 class="text-2xl font-bold font-industrial uppercase text-brand-navy mb-1">
              Send Your Construction Requirements
            </h3>
            <p class="text-xs text-slate-500 mb-6">Receive factory-direct rates within 10 minutes on WhatsApp or phone.</p>

            <form onsubmit="handleContactPageForm(event)" class="space-y-4">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-700 mb-1">Your Full Name *</label>
                  <input type="text" id="contact-name" required placeholder="Enter your name" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-slate-900 text-sm focus:outline-none focus:border-amber-500">
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-700 mb-1">Phone Number *</label>
                  <input type="tel" id="contact-phone" required placeholder="Enter 10-digit mobile number" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-slate-900 text-sm focus:outline-none focus:border-amber-500">
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-700 mb-1">Material Required</label>
                  <select id="contact-material" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2.5 text-slate-900 text-sm focus:outline-none focus:border-amber-500">
                    <option value="20mm Black Trap Aggregate">20mm Aggregate (Jelly)</option>
                    <option value="10mm Black Trap Grit">10mm Grit (Chipping)</option>
                    <option value="40mm Coarse Aggregate">40mm Ballast / Coarse</option>
                    <option value="Manufactured Sand (M-Sand)">Manufactured Sand (M-Sand)</option>
                    <option value="Plaster Sand (P-Sand)">Plaster Sand (P-Sand)</option>
                    <option value="Ready Mix Concrete (RMC)">Ready Mix Concrete (RMC)</option>
                    <option value="GSB / WMM Road Base">GSB / WMM Road Base</option>
                    <option value="Govt. Civil Tender Supply">Govt. Civil Tender Supply</option>
                  </select>
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-700 mb-1">Site Delivery Location</label>
                  <input type="text" id="contact-site" placeholder="e.g. Talaja, Bhavnagar, Mahuva" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-slate-900 text-sm focus:outline-none focus:border-amber-500">
                </div>
              </div>

              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Project Details / Message</label>
                <textarea id="contact-msg" rows="3" placeholder="Mention total estimated tons or brass, site condition, date of delivery..." class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-slate-900 text-sm focus:outline-none focus:border-amber-500"></textarea>
              </div>

              <button type="submit" class="w-full bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-bold py-3.5 px-6 rounded-xl flex items-center justify-center gap-2 text-base transition-transform active:scale-95 shadow-md">
                <i class="fa-solid fa-paper-plane"></i>
                <span>Send Requirement Direct via WhatsApp</span>
              </button>
            </form>
          </div>

          <!-- Embedded Map -->
          <div class="bg-white rounded-3xl p-3 shadow-md border border-slate-200 overflow-hidden">
            <div class="flex items-center justify-between px-3 py-2 text-xs font-bold text-slate-700">
              <span><i class="fa-solid fa-map-pin text-red-500 mr-1.5"></i> Location: Borda, Talaja, Dist. Bhavnagar</span>
              <a href="https://maps.google.com/?q={LATITUDE},{LONGITUDE}" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:underline">Open in Google Maps</a>
            </div>
            <div class="h-80 w-full rounded-2xl overflow-hidden border border-slate-200">
              <iframe 
                title="Ashutosh Build Stone Location Map"
                src="https://maps.google.com/maps?q=Borda,Talaja,Bhavnagar,Gujarat&t=&z=13&ie=UTF8&iwloc=&output=embed" 
                class="w-full h-full border-0" 
                allowfullscreen="" 
                loading="lazy">
              </iframe>
            </div>
          </div>

        </div>

      </div>

    </div>
  </section>

  <script>
    function handleContactPageForm(e) {{
      e.preventDefault();
      const name = document.getElementById('contact-name').value;
      const phone = document.getElementById('contact-phone').value;
      const mat = document.getElementById('contact-material').value;
      const site = document.getElementById('contact-site').value;
      const msg = document.getElementById('contact-msg').value;

      const text = `*New Website Inquiry - Ashutosh Build Stone Pvt. Ltd.*\\n\\n*Client Name:* ${{name}}\\n*Contact No:* ${{phone}}\\n*Material:* ${{mat}}\\n*Site Location:* ${{site}}\\n*Message:* ${{msg}}\\n\\nPlease provide rate quote and delivery schedule.`;
      const url = `https://wa.me/{PHONE_BHAGIRATH_RAW}?text=${{encodeURIComponent(text)}}`;
      window.open(url, '_blank');
    }}
  </script>

{faqs_html}

{FOOTER_HTML}
</body>
</html>"""

    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("contact.html generated with expanded authority.")

build_expanded_contact()
