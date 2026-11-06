# generate_subpages.py - Generates all 7 subpages for Ashutosh Build Stone Pvt. Ltd.

from build_pages import get_page_head, get_page_banner, highlight_nav, HEADER_HTML, FOOTER_HTML

def create_about_page():
    nav = highlight_nav(HEADER_HTML, 'about')
    banner = get_page_banner(
        "About Ashutosh Build Stone Pvt. Ltd.",
        "Pioneering Sustainable Manufactured Sand & Certified Black Trap Aggregates in Gujarat",
        "About Us"
    )
    
    content = f"""{get_page_head("About Us", "Learn about Ashutosh Build Stone Pvt. Ltd. - Govt. Approved Contractor, Black Trap Aggregate & M-Sand Manufacturer in Borda, Talaja, Bhavnagar.")}
{nav}
{banner}

  <!-- ABOUT DETAILED SECTION -->
  <section class="py-16 sm:py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Top Grid: Story & Visuals -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-16">
        
        <!-- Left: Image Presentation -->
        <div class="lg:col-span-5 space-y-6">
          <div class="rounded-2xl overflow-hidden shadow-xl border-4 border-slate-100 group">
            <img src="assets/images/quarry-crushing-facility-hd.jpeg" alt="Basalt Quarry Facility" class="w-full h-80 object-cover group-hover:scale-105 transition-transform duration-700">
            <div class="p-4 bg-brand-navy text-white flex justify-between items-center">
              <div>
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Facility Location</span>
                <div class="text-base font-bold">Borda, Tal. Talaja, Dist. Bhavnagar</div>
              </div>
              <span class="bg-amber-500 text-slate-950 text-xs font-black px-2.5 py-1 rounded">1500+ MT/Day</span>
            </div>
          </div>

          <!-- Standee Posters from Reference -->
          <div class="grid grid-cols-2 gap-4">
            <div class="rounded-xl overflow-hidden shadow border border-slate-200 bg-slate-50 p-2 text-center">
              <img src="assets/images/poster-nirmaan-aasan.jpeg" alt="हमारे साथ, निर्माण बने आसान" class="w-full h-60 object-contain rounded-lg">
              <p class="text-xs font-bold text-slate-700 mt-2 font-hindi-motto">हमारे साथ, निर्माण बने आसान</p>
            </div>
            <div class="rounded-xl overflow-hidden shadow border border-slate-200 bg-slate-50 p-2 text-center">
              <img src="assets/images/poster-sapno-ki-raksha.jpeg" alt="निर्माण मटेरियल जो करे आपके सपनों की रक्षा" class="w-full h-60 object-contain rounded-lg">
              <p class="text-xs font-bold text-slate-700 mt-2 font-hindi-motto">सपनों की रक्षा</p>
            </div>
          </div>
        </div>

        <!-- Right: Story -->
        <div class="lg:col-span-7 space-y-6">
          <span class="inline-flex items-center gap-2 bg-amber-100 text-amber-800 font-bold px-3 py-1 rounded-full text-xs uppercase tracking-wider">
            <i class="fa-solid fa-landmark"></i> Corporate Legacy & Commitment
          </span>
          <h2 class="text-3xl sm:text-4xl font-black font-industrial uppercase text-brand-navy leading-tight">
            Delivering Industrial Excellence, Ecological Responsibility & Civil Strength
          </h2>
          <p class="text-slate-600 leading-relaxed text-sm sm:text-base">
            <strong>ASHUTOSH BUILD STONE PVT. LTD.</strong> is an officially registered private limited corporate entity and government-approved building contractor operating in Borda, Talaja (Dist. Bhavnagar, Gujarat). Established with an ambition to revolutionize construction raw material standards, our facility integrates heavy-duty mechanized basalt quarrying with advanced 3-stage cone crushing and hydro-cyclone sand washing technologies.
          </p>
          <p class="text-slate-600 leading-relaxed text-sm sm:text-base">
            Under our guiding emblem motto <strong>"SAVE WATER, RIVER SAND"</strong>, we champion the transition from destructive riverbed dredging to precision-engineered <strong>Manufactured Sand (M-Sand)</strong> and <strong>Plaster Sand (P-Sand)</strong>. Our products provide superior concrete compressive strengths, optimal grading curves, and guaranteed zero clay or organic contamination.
          </p>

          <!-- Key Metrics Grid -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-3">
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
              <div class="text-2xl font-black font-industrial text-amber-500">1,500+ MT</div>
              <div class="text-[11px] font-bold text-slate-600 uppercase">Daily Output</div>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
              <div class="text-2xl font-black font-industrial text-blue-600">IS 383:2016</div>
              <div class="text-[11px] font-bold text-slate-600 uppercase">BIS Quality</div>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
              <div class="text-2xl font-black font-industrial text-emerald-600">&lt; 3%</div>
              <div class="text-[11px] font-bold text-slate-600 uppercase">Silt Content</div>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
              <div class="text-2xl font-black font-industrial text-purple-600">100%</div>
              <div class="text-[11px] font-bold text-slate-600 uppercase">Accurate Weight</div>
            </div>
          </div>
        </div>

      </div>

      <!-- Official Corporate Credentials Card -->
      <div class="bg-gradient-to-r from-brand-navy to-slate-900 rounded-3xl p-8 sm:p-10 text-white shadow-xl mb-16 border border-slate-800">
        <div class="flex flex-col md:flex-row items-center justify-between gap-6 pb-6 border-b border-slate-800">
          <div>
            <span class="text-xs font-bold text-amber-400 uppercase tracking-widest">Government Verified Entity</span>
            <h3 class="text-2xl sm:text-3xl font-black font-industrial uppercase mt-1">Official Corporate Disclosures</h3>
          </div>
          <span class="bg-amber-500 text-slate-950 font-black text-xs px-4 py-2 rounded-full uppercase tracking-wider">Govt. Approved Building Contractor</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 pt-6 text-sm">
          <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
            <span class="text-xs text-slate-400 block">Corporate Identification No. (CIN)</span>
            <span class="text-base font-bold text-amber-300 font-mono mt-1 block">U43299GJ2025PTC159486</span>
          </div>

          <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
            <span class="text-xs text-slate-400 block">Permanent Account Number (PAN)</span>
            <span class="text-base font-bold text-white font-mono mt-1 block">ABCCA2752K</span>
          </div>

          <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
            <span class="text-xs text-slate-400 block">Tax Deduction Account (TAN)</span>
            <span class="text-base font-bold text-white font-mono mt-1 block">AHMA32297G</span>
          </div>

          <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
            <span class="text-xs text-slate-400 block">Registered Works Location</span>
            <span class="text-xs font-bold text-slate-200 mt-1 block">Gopnath Road, Borda, Talaja, Bhavnagar - 364130</span>
          </div>
        </div>
      </div>

      <!-- Promoters & Leadership Spotlight -->
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="text-xs font-bold text-amber-600 uppercase tracking-widest">Direct Leadership</span>
        <h2 class="text-3xl sm:text-4xl font-black font-industrial uppercase text-brand-navy mt-1">
          Meet Our Directors & Management
        </h2>
        <p class="text-slate-600 text-sm mt-2">Personal accountability, decades of civil contracting experience, and customer-first service.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto mb-16">
        
        <!-- Leader 1: Bhagirath Sinh -->
        <div class="bg-white rounded-2xl p-7 shadow-lg border-t-4 border-amber-500 card-hover flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="bg-amber-100 text-amber-800 text-xs font-bold px-3 py-1 rounded-full uppercase">Director & Operations</span>
              <a href="https://wa.me/917878999033" target="_blank" class="text-emerald-500 hover:text-emerald-600 text-2xl"><i class="fa-brands fa-whatsapp"></i></a>
            </div>
            <h3 class="text-2xl font-black text-brand-navy">Mr. Bhagirath Sinh Sarviya</h3>
            <p class="text-xs text-slate-500 mt-1">Oversees quarry extraction, crushing plant performance, weighbridge verification, and regional transit logistics.</p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
            <a href="tel:7878999033" class="text-base font-bold text-brand-navy hover:text-amber-600 flex items-center gap-2">
              <i class="fa-solid fa-phone text-amber-500"></i> +91 78789 99033
            </a>
            <a href="tel:7878999033" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs px-4 py-2 rounded-lg shadow-sm">
              Call Direct
            </a>
          </div>
        </div>

        <!-- Leader 2: Alpesh Chauhan -->
        <div class="bg-white rounded-2xl p-7 shadow-lg border-t-4 border-blue-600 card-hover flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="bg-blue-100 text-blue-800 text-xs font-bold px-3 py-1 rounded-full uppercase">Director & Sales</span>
              <a href="https://wa.me/917623998398" target="_blank" class="text-emerald-500 hover:text-emerald-600 text-2xl"><i class="fa-brands fa-whatsapp"></i></a>
            </div>
            <h3 class="text-2xl font-black text-brand-navy">Alpesh Chauhan</h3>
            <p class="text-xs text-slate-500 mt-1">Leads corporate client relationships, government contracting tenders, bulk material contracts, and commercial billing.</p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
            <a href="tel:7623998398" class="text-base font-bold text-brand-navy hover:text-blue-600 flex items-center gap-2">
              <i class="fa-solid fa-phone text-blue-600"></i> +91 76239 98398
            </a>
            <a href="tel:7623998398" class="bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs px-4 py-2 rounded-lg shadow-sm">
              Call Direct
            </a>
          </div>
        </div>

      </div>

      <!-- Banner Presentation -->
      <div class="rounded-2xl overflow-hidden shadow-sm border border-slate-200 p-4 bg-slate-50">
        <img src="assets/images/company-banner.jpeg" alt="Ashutosh Build Stone Pvt. Ltd. Corporate Banner" class="w-full h-auto object-contain rounded-xl">
      </div>

    </div>
  </section>

{FOOTER_HTML}
</body>
</html>"""

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("about.html generated.")


def create_products_page():
    nav = highlight_nav(HEADER_HTML, 'products')
    banner = get_page_banner(
        "Products & Technical Specifications",
        "IS 383:2016 Certified Black Trap Aggregates, Eco-Friendly Washed M-Sand, Plaster Sand & RMC Concrete",
        "Products"
    )

    content = f"""{get_page_head("Products & Materials", "High-quality Black Trap Aggregates (10mm, 20mm, 40mm), M-Sand, Plaster Sand, GSB, and RMC Concrete by Ashutosh Build Stone.")}
{nav}
{banner}

  <!-- PRODUCTS CATALOG & SPECS SECTION -->
  <section class="py-16 sm:py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Filter Bar -->
      <div class="flex flex-wrap items-center justify-center gap-2 mb-12">
        <button class="filter-btn active bg-brand-navy text-white px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold shadow-sm transition-all" data-filter="all">All Products</button>
        <button class="filter-btn bg-white text-slate-700 hover:bg-slate-200 px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold shadow-sm transition-all" data-filter="aggregates">Black Trap Aggregates</button>
        <button class="filter-btn bg-white text-slate-700 hover:bg-slate-200 px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold shadow-sm transition-all" data-filter="sand">Washed M-Sand & P-Sand</button>
        <button class="filter-btn bg-white text-slate-700 hover:bg-slate-200 px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold shadow-sm transition-all" data-filter="infrastructure">RMC & Road Materials</button>
      </div>

      <!-- Products Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-20">

        <!-- Product 1: 20mm Aggregate -->
        <div class="product-card card-hover bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="aggregates">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/aggregate-20mm-hd.jpeg" alt="20mm Black Trap Aggregate" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
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
                <div class="flex justify-between"><span class="text-slate-400">Crushing Value:</span><span class="font-bold text-emerald-600">&lt; 18% (Superior Strength)</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Flakiness Index:</span><span class="font-bold text-emerald-600">&lt; 15% (Cubical Shape)</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Specific Gravity:</span><span class="font-bold">2.85+</span></div>
                <div class="flex justify-between"><span class="text-slate-400">Water Absorption:</span><span class="font-bold">&lt; 1.0%</span></div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-2">
              <a href="https://wa.me/917878999033?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%2020mm%20Black%20Trap%20Aggregate" target="_blank" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-lg text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-lg text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 2: 10mm Grit -->
        <div class="product-card card-hover bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="aggregates">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/aggregate-10mm-hd.jpeg" alt="10mm Grit Aggregate" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
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
              <a href="https://wa.me/917878999033?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%2010mm%20Grit" target="_blank" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-lg text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-lg text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 3: 40mm Ballast -->
        <div class="product-card card-hover bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="aggregates">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/aggregate-40mm-hd.jpeg" alt="40mm Coarse Aggregate Ballast" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
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
              <a href="https://wa.me/917878999033?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%2040mm%20Aggregate" target="_blank" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-lg text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-lg text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 4: M-Sand -->
        <div class="product-card card-hover bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="sand">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/manufactured-sand-m-sand-hd.jpeg" alt="Manufactured Sand M-Sand" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
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
              <a href="https://wa.me/917878999033?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%20Washed%20M-Sand" target="_blank" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-lg text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-lg text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 5: P-Sand -->
        <div class="product-card card-hover bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="sand">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/plaster-sand-fine-hd.jpeg" alt="Plaster Sand Fine Grade" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
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
              <a href="https://wa.me/917878999033?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%20Plaster%20Sand%20(P-Sand)" target="_blank" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-lg text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-lg text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 6: RMC Concrete -->
        <div class="product-card card-hover bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="infrastructure">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/rmc-batching-plant-hd.jpeg" alt="RMC Batching Plant" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
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
              <a href="https://wa.me/917878999033?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%20Ready%20Mix%20Concrete%20(RMC)" target="_blank" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-lg text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-lg text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 7: GSB Road Base -->
        <div class="product-card card-hover bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="infrastructure">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/road-base-gsb-hd.jpeg" alt="Granular Sub Base GSB" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
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
              <a href="https://wa.me/917878999033?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%20GSB%20Road%20Base" target="_blank" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-lg text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-lg text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 8: Quarry Rubble & Soling -->
        <div class="product-card card-hover bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm flex flex-col" data-category="infrastructure">
          <div class="relative h-60 overflow-hidden bg-slate-100 group">
            <img src="assets/images/aggregate-40mm-hd.jpeg" alt="Quarry Rubble and Soling" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
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
              <a href="https://wa.me/917878999033?text=Hi%20Ashutosh%20Build%20Stone,%20please%20send%20quote%20for%20Quarry%20Rubble%20Soling" target="_blank" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-3 rounded-lg text-center text-xs transition-colors flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
              </a>
              <a href="calculator.html" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold p-2.5 rounded-lg text-xs" title="Calculate Quantity">
                <i class="fa-solid fa-calculator"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Product 9: Bulk Turnkey Supply -->
        <div class="product-card card-hover bg-gradient-to-br from-brand-navy to-slate-900 rounded-2xl overflow-hidden border border-slate-700 text-white shadow-xl flex flex-col justify-between p-7" data-category="all">
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
            <a href="tel:7878999033" class="w-full bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-3 px-4 rounded-xl flex items-center justify-center gap-2 text-sm transition-transform active:scale-95">
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
    // Product Filter Tabs Logic
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

{FOOTER_HTML}
</body>
</html>"""

    with open('products.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("products.html generated.")


def create_plant_page():
    nav = highlight_nav(HEADER_HTML, 'plant')
    banner = get_page_banner(
        "Plant, Machinery & Technology",
        "High-Capacity Basalt Crushing, Hydrocyclone Sand Washing & Computerized Concrete Batching Setup",
        "Plant & Machinery"
    )

    content = f"""{get_page_head("Plant & Machinery", "Explore the modern stone crushing plant, hydrocyclone sand washer, and RMC batching tower at Ashutosh Build Stone Pvt. Ltd.")}
{nav}
{banner}

  <!-- PLANT & MACHINERY OVERVIEW -->
  <section class="py-16 sm:py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-16">
        <div class="lg:col-span-6 space-y-6">
          <span class="inline-flex items-center gap-2 bg-amber-100 text-amber-800 font-bold px-3 py-1 rounded-full text-xs uppercase tracking-wider">
            <i class="fa-solid fa-gears"></i> Heavy Industry Setup
          </span>
          <h2 class="text-3xl sm:text-5xl font-black font-industrial uppercase text-brand-navy leading-tight">
            Engineered For High Output, Zero Downtime & Precise Grading
          </h2>
          <p class="text-slate-600 leading-relaxed text-sm sm:text-base">
            Located on Gopnath Road, Borda (Talaja), our industrial infrastructure is engineered to process raw basalt boulders into micro-graded aggregates and hydro-washed sands at a throughput exceeding <strong>1,500 Metric Tons every day</strong>.
          </p>
          <p class="text-slate-600 leading-relaxed text-sm sm:text-base">
            Equipped with multi-stage cone crushers, variable frequency vibrating screens, automated sand hydrocyclones, and computerized RMC silos, we control every micron of material grading from quarry extraction to final site discharge.
          </p>

          <div class="grid grid-cols-2 gap-4 pt-2">
            <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
              <div class="text-2xl font-black font-industrial text-amber-500">150+ TPH</div>
              <div class="text-xs font-bold text-slate-700">Crushing Output</div>
              <div class="text-[11px] text-slate-500">Continuous feed system</div>
            </div>
            <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
              <div class="text-2xl font-black font-industrial text-blue-600">90% Recycle</div>
              <div class="text-xs font-bold text-slate-700">Process Water</div>
              <div class="text-[11px] text-slate-500">Closed-loop desilter</div>
            </div>
          </div>
        </div>

        <div class="lg:col-span-6">
          <div class="rounded-3xl overflow-hidden shadow-2xl border-4 border-slate-100">
            <img src="assets/images/sand-washing-crusher-plant-hd.jpeg" alt="Sand Washing Crusher Facility" class="w-full h-96 object-cover">
          </div>
        </div>
      </div>

      <!-- MACHINERY EQUIPMENT BREAKDOWN -->
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="text-xs font-bold text-amber-600 uppercase tracking-widest">Key Assets</span>
        <h3 class="text-3xl sm:text-4xl font-black font-industrial uppercase text-brand-navy mt-1">
          Our Advanced Plant Units
        </h3>
        <p class="text-slate-600 text-sm mt-1">High-performance machines maintaining consistency across every truckload.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-20">
        
        <!-- Asset 1 -->
        <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200 card-hover flex flex-col justify-between">
          <div>
            <div class="h-48 rounded-xl overflow-hidden mb-4 bg-slate-200">
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
        <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200 card-hover flex flex-col justify-between">
          <div>
            <div class="h-48 rounded-xl overflow-hidden mb-4 bg-slate-200">
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
        <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200 card-hover flex flex-col justify-between">
          <div>
            <div class="h-48 rounded-xl overflow-hidden mb-4 bg-slate-200">
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
        <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200 card-hover flex flex-col justify-between">
          <div>
            <div class="h-48 rounded-xl overflow-hidden mb-4 bg-slate-200">
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
        <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200 card-hover flex flex-col justify-between">
          <div>
            <div class="h-48 rounded-xl overflow-hidden mb-4 bg-slate-200">
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
        <div class="bg-gradient-to-br from-brand-navy to-slate-900 rounded-2xl p-6 text-white card-hover flex flex-col justify-between">
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
          <a href="tel:7878999033" class="bg-slate-950 hover:bg-slate-800 text-white font-bold px-6 py-3.5 rounded-xl text-xs sm:text-sm shadow-md transition-all flex items-center gap-2">
            <i class="fa-solid fa-phone"></i> Call Bhagirath Sinh
          </a>
        </div>
      </div>

    </div>
  </section>

{FOOTER_HTML}
</body>
</html>"""

    with open('plant.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("plant.html generated.")


def create_contracting_page():
    nav = highlight_nav(HEADER_HTML, 'contracting')
    banner = get_page_banner(
        "Govt. Approved Building Contractor",
        "Executing Highway Development, Industrial Earthworks, Retaining Structures & Bulk Material Supply",
        "Civil Contracting"
    )

    content = f"""{get_page_head("Civil Contracting", "Govt. Approved Building Contractor services for road construction, industrial foundations, and bulk infrastructure supply in Gujarat.")}
{nav}
{banner}

  <!-- CONTRACTING SERVICES SECTION -->
  <section class="py-16 sm:py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Top Credentials Overview -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-16">
        <div class="lg:col-span-7 space-y-6">
          <span class="inline-flex items-center gap-2 bg-amber-100 text-amber-800 font-bold px-3 py-1 rounded-full text-xs uppercase tracking-wider">
            <i class="fa-solid fa-landmark"></i> Official Government Approval
          </span>
          <h2 class="text-3xl sm:text-5xl font-black font-industrial uppercase text-brand-navy leading-tight">
            Certified Civil Engineering Partner For Gujarat's Major Infrastructure
          </h2>
          <p class="text-slate-600 leading-relaxed text-sm sm:text-base">
            <strong>ASHUTOSH BUILD STONE PVT. LTD.</strong> possesses certified government contractor credentials, enabling us to tender, execute, and deliver road construction, heavy industrial foundations, and civil infrastructure projects for government bodies and private conglomerates.
          </p>
          <p class="text-slate-600 leading-relaxed text-sm sm:text-base">
            With our own captive basalt quarries, stone crushers, sand washing units, and heavy earthmoving machinery, we provide seamless turnkey execution without third-party material bottlenecks or price fluctuations.
          </p>

          <div class="pt-2 flex flex-wrap gap-4">
            <a href="tel:7623998398" class="inline-flex items-center gap-2 bg-brand-navy hover:bg-blue-900 text-white font-bold px-6 py-3.5 rounded-xl text-xs sm:text-sm shadow-md transition-all">
              <i class="fa-solid fa-phone text-amber-400"></i>
              <span>Consult Alpesh Chauhan (Sales & Tenders)</span>
            </a>
            <a href="https://wa.me/917878999033?text=Hello,%20I%20am%20inquiring%20about%20civil%20contracting%20services%20from%20Ashutosh%20Build%20Stone%20Pvt.%20Ltd." target="_blank" class="inline-flex items-center gap-2 bg-[#25D366] hover:bg-[#20ba59] text-white font-bold px-6 py-3.5 rounded-xl text-xs sm:text-sm shadow-md transition-all">
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
                <span class="font-mono font-bold text-amber-600">U43299GJ2025PTC159486</span>
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
        
        <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm card-hover">
          <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-600 flex items-center justify-center text-2xl mb-4">
            <i class="fa-solid fa-road"></i>
          </div>
          <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Road & Highway Construction</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Execution of Granular Sub-Base (GSB), Wet Mix Macadam (WMM), Bituminous Macadam, and complete culvert structural work for PWD, State Highways, and NHAI packages.
          </p>
        </div>

        <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm card-hover">
          <div class="w-12 h-12 rounded-xl bg-blue-500/10 text-blue-600 flex items-center justify-center text-2xl mb-4">
            <i class="fa-solid fa-industry"></i>
          </div>
          <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Industrial Earthworks & Grading</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Large-scale site leveling, ground compaction, heavy equipment footing excavation, storm drainage systems, and industrial factory flooring bases.
          </p>
        </div>

        <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm card-hover">
          <div class="w-12 h-12 rounded-xl bg-cyan-500/10 text-cyan-600 flex items-center justify-center text-2xl mb-4">
            <i class="fa-solid fa-ship"></i>
          </div>
          <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Port & Maritime Protection Works</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Supplying and installing heavy basalt rock armor for coastal sea walls, breakwaters, and harbor infrastructure in the Alang and Bhavnagar coastal belt.
          </p>
        </div>

        <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm card-hover">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 text-emerald-600 flex items-center justify-center text-2xl mb-4">
            <i class="fa-solid fa-bridge"></i>
          </div>
          <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Bridge & Culvert Substructures</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Heavy mass concrete pourings, abutment foundation stones, pier construction, and approach road earthwork with laboratory certified aggregate grading.
          </p>
        </div>

        <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm card-hover">
          <div class="w-12 h-12 rounded-xl bg-purple-500/10 text-purple-600 flex items-center justify-center text-2xl mb-4">
            <i class="fa-solid fa-city"></i>
          </div>
          <h4 class="text-xl font-bold font-industrial uppercase text-brand-navy">Mega Real Estate Procurement</h4>
          <p class="text-xs text-slate-500 mt-2 leading-relaxed">
            Dedicated long-term supply contracts for residential townships, commercial complexes, and industrial warehouses with guaranteed fixed delivery timelines.
          </p>
        </div>

        <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm card-hover">
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

{FOOTER_HTML}
</body>
</html>"""

    with open('contracting.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("contracting.html generated.")


def create_calculator_page():
    nav = highlight_nav(HEADER_HTML, 'calculator')
    banner = get_page_banner(
        "Contractor Material Estimator",
        "Calculate Metric Tons (MT), Brass (100 Cu.Ft), and Cubic Meters (m³) For Civil Construction",
        "Material Estimator"
    )

    content = f"""{get_page_head("Material Estimator", "Interactive construction material quantity calculator for aggregates, sand, GSB, and RMC by Ashutosh Build Stone.")}
{nav}
{banner}

  <!-- CALCULATOR SECTION -->
  <section class="py-16 sm:py-24 bg-slate-50">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="bg-gradient-to-br from-brand-navy to-slate-900 rounded-3xl p-6 sm:p-10 text-white shadow-2xl border border-slate-800">
        
        <div class="max-w-2xl mb-8">
          <span class="inline-flex items-center gap-2 bg-amber-500/20 text-amber-400 border border-amber-500/30 px-3.5 py-1 rounded-full text-xs font-bold uppercase tracking-wider mb-2">
            <i class="fa-solid fa-calculator"></i> Digital Utility
          </span>
          <h2 class="text-3xl sm:text-4xl font-black font-industrial uppercase text-white">
            Material Quantity & Cost Estimator
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm mt-1">
            Input dimensions of your RCC slab, footing, road base, or wall to calculate exact requirement in Metric Tons and Brass.
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
            <div class="grid grid-cols-3 gap-3">
              <div>
                <label id="label-len" class="block text-xs font-semibold text-slate-300 mb-1">Length (Feet)</label>
                <input type="number" id="calc-len" value="50" min="1" step="any" oninput="calculateMaterial()" class="w-full bg-slate-800 border border-slate-600 rounded-xl px-3 py-2.5 text-white text-sm focus:outline-none focus:border-amber-400">
              </div>
              <div>
                <label id="label-wid" class="block text-xs font-semibold text-slate-300 mb-1">Width (Feet)</label>
                <input type="number" id="calc-wid" value="30" min="1" step="any" oninput="calculateMaterial()" class="w-full bg-slate-800 border border-slate-600 rounded-xl px-3 py-2.5 text-white text-sm focus:outline-none focus:border-amber-400">
              </div>
              <div>
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
      const url = `https://wa.me/917878999033?text=${{encodeURIComponent(text)}}`;
      window.open(url, '_blank');
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      calculateMaterial();
    }});
  </script>

{FOOTER_HTML}
</body>
</html>"""

    with open('calculator.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("calculator.html generated.")


def create_gallery_page():
    nav = highlight_nav(HEADER_HTML, 'gallery')
    banner = get_page_banner(
        "Visual Photo Gallery",
        "High-Definition Visual Tour of Our Quarry Operations, Crushing Plants, Sand Washing & Delivery Fleet",
        "Gallery"
    )

    gallery_items = [
        ("assets/images/sand-washing-crusher-plant-hd.jpeg", "Primary Multi-Stage Crushing & Sand Washing Plant", "Machinery"),
        ("assets/images/manufactured-sand-m-sand-hd.jpeg", "Hydro-Cyclone Washed Sand Conical Stockpiles", "Sand Washing"),
        ("assets/images/aggregate-20mm-hd.jpeg", "20mm Black Trap Aggregate - Sharp Cubical Shape", "Aggregates"),
        ("assets/images/aggregate-10mm-hd.jpeg", "10mm Fine Black Trap Grit & Chipping", "Aggregates"),
        ("assets/images/aggregate-40mm-hd.jpeg", "40mm Coarse Aggregate Ballast for Mass Concrete", "Aggregates"),
        ("assets/images/plaster-sand-fine-hd.jpeg", "Washed Fine Plaster Sand (P-Sand)", "Sand Washing"),
        ("assets/images/rmc-batching-plant-hd.jpeg", "Ready-Mix Concrete Computerized Batching Tower", "RMC"),
        ("assets/images/quarry-crushing-facility-hd.jpeg", "Aerial View of Open Pit Basalt Quarry & Benches", "Quarry"),
        ("assets/images/road-base-gsb-hd.jpeg", "Granular Sub-Base (GSB) Stockpiles for Road Works", "Roads"),
        ("assets/images/company-banner.jpeg", "Official Corporate Registration Banner", "Corporate"),
        ("assets/images/poster-nirmaan-aasan.jpeg", "Marketing Poster: हमारे साथ, निर्माण बने आसान", "Marketing"),
        ("assets/images/poster-sapno-ki-raksha.jpeg", "Marketing Poster: निर्माण मटेरियल जो करे आपके सपनों की रक्षा", "Marketing")
    ]

    gallery_html = ""
    for img, caption, cat in gallery_items:
        gallery_html += f"""
        <div class="gallery-item relative rounded-2xl overflow-hidden shadow-sm border border-slate-200 group cursor-pointer h-64 bg-slate-100" onclick="openLightbox('{img}', '{caption}')">
          <img src="{img}" alt="{caption}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-90 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
            <span class="text-[10px] font-bold text-amber-400 uppercase tracking-widest">{cat}</span>
            <div class="text-sm font-bold text-white mt-0.5">{caption}</div>
          </div>
          <div class="absolute top-3 right-3 w-8 h-8 rounded-full bg-black/40 text-white flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
            <i class="fa-solid fa-expand text-xs"></i>
          </div>
        </div>
        """

    content = f"""{get_page_head("Photo Gallery", "High-resolution photos of Ashutosh Build Stone Pvt. Ltd. plant, crushing equipment, aggregates, and logistics.")}
{nav}
{banner}

  <!-- GALLERY GRID SECTION -->
  <section class="py-16 sm:py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-2xl mx-auto mb-12">
        <span class="text-xs font-bold text-amber-600 uppercase tracking-widest">Field Photos</span>
        <h2 class="text-3xl sm:text-4xl font-black font-industrial uppercase text-brand-navy mt-1">
          Explore Our Operations
        </h2>
        <p class="text-slate-600 text-sm mt-1">Click on any image to open the full-screen high-definition lightbox.</p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {gallery_html}
      </div>

    </div>
  </section>

{FOOTER_HTML}
</body>
</html>"""

    with open('gallery.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("gallery.html generated.")


def create_contact_page():
    nav = highlight_nav(HEADER_HTML, 'contact')
    banner = get_page_banner(
        "Contact Us & Plant Location",
        "Connect Directly with Directors for Bulk Inquiries, Commercial Orders & Site Visits",
        "Contact"
    )

    content = f"""{get_page_head("Contact Us", "Contact details, phone numbers, and location map for Ashutosh Build Stone Pvt. Ltd. in Borda, Talaja, Bhavnagar.")}
{nav}
{banner}

  <!-- CONTACT & LOCATION SECTION -->
  <section class="py-16 sm:py-24 bg-slate-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
        
        <!-- Left Column: Contact Cards & Info -->
        <div class="lg:col-span-5 space-y-6">
          
          <!-- Key Contact 1: Bhagirath Sinh -->
          <div class="bg-white rounded-2xl p-6 shadow-md border-l-4 border-amber-500">
            <div class="flex items-center justify-between mb-3">
              <span class="text-xs font-bold uppercase tracking-wider text-amber-600 bg-amber-50 px-2.5 py-1 rounded">Director / Key Contact</span>
              <a href="https://wa.me/917878999033" target="_blank" class="text-emerald-600 hover:text-emerald-700 text-2xl" title="Chat on WhatsApp">
                <i class="fa-brands fa-whatsapp"></i>
              </a>
            </div>
            <h3 class="text-2xl font-black text-brand-navy">Mr. Bhagirath Sinh Sarviya</h3>
            <p class="text-xs text-slate-500 mt-1">Plant Operations, Weighbridge & Regional Supply Dispatch</p>
            
            <div class="mt-5 pt-3 border-t border-slate-100 flex items-center justify-between">
              <a href="tel:7878999033" class="inline-flex items-center gap-2 text-base font-black text-brand-navy hover:text-amber-600">
                <i class="fa-solid fa-phone text-amber-500"></i> +91 78789 99033
              </a>
              <a href="tel:7878999033" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs px-3.5 py-1.5 rounded-lg shadow-sm">
                Call Direct
              </a>
            </div>
          </div>

          <!-- Key Contact 2: Alpesh Chauhan -->
          <div class="bg-white rounded-2xl p-6 shadow-md border-l-4 border-blue-600">
            <div class="flex items-center justify-between mb-3">
              <span class="text-xs font-bold uppercase tracking-wider text-blue-600 bg-blue-50 px-2.5 py-1 rounded">Director / Key Contact</span>
              <a href="https://wa.me/917623998398" target="_blank" class="text-emerald-600 hover:text-emerald-700 text-2xl" title="Chat on WhatsApp">
                <i class="fa-brands fa-whatsapp"></i>
              </a>
            </div>
            <h3 class="text-2xl font-black text-brand-navy">Alpesh Chauhan</h3>
            <p class="text-xs text-slate-500 mt-1">Corporate Client Accounts, Tenders, Billing & Quotations</p>
            
            <div class="mt-5 pt-3 border-t border-slate-100 flex items-center justify-between">
              <a href="tel:7623998398" class="inline-flex items-center gap-2 text-base font-black text-brand-navy hover:text-blue-600">
                <i class="fa-solid fa-phone text-blue-600"></i> +91 76239 98398
              </a>
              <a href="tel:7623998398" class="bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs px-3.5 py-1.5 rounded-lg shadow-sm">
                Call Direct
              </a>
            </div>
          </div>

          <!-- Official Details -->
          <div class="bg-white rounded-2xl p-6 shadow-md space-y-4 text-xs sm:text-sm text-slate-700">
            <div class="flex items-start gap-3">
              <i class="fa-solid fa-location-dot text-amber-500 text-base mt-1 flex-shrink-0"></i>
              <div>
                <strong class="text-brand-navy block">Crusher Plant & Registered Office:</strong>
                <span class="text-slate-600">Gopnath Road, At. Borda, Tal. Talaja, Dist. Bhavnagar, Gujarat - 364130, India</span>
              </div>
            </div>

            <div class="flex items-center gap-3">
              <i class="fa-solid fa-id-card text-blue-600 text-base flex-shrink-0"></i>
              <div><strong>CIN:</strong> U43299GJ2025PTC159486</div>
            </div>

            <div class="flex items-center gap-3">
              <i class="fa-solid fa-file-invoice text-emerald-600 text-base flex-shrink-0"></i>
              <div><strong>PAN:</strong> ABCCA2752K &nbsp;|&nbsp; <strong>TAN:</strong> AHMA32297G</div>
            </div>

            <div class="flex items-center gap-3">
              <i class="fa-solid fa-clock text-amber-500 text-base flex-shrink-0"></i>
              <div><strong>Hours:</strong> Mon - Sun: 7:00 AM - 8:00 PM (24/7 for projects)</div>
            </div>
          </div>

          <!-- Travel Distances -->
          <div class="bg-slate-100 rounded-2xl p-5 border border-slate-200 text-xs">
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
                  <input type="text" id="contact-name" required placeholder="Enter your name" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-slate-900 text-sm focus:outline-none focus:border-amber-500">
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-700 mb-1">Phone Number *</label>
                  <input type="tel" id="contact-phone" required placeholder="Enter 10-digit mobile number" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-slate-900 text-sm focus:outline-none focus:border-amber-500">
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-700 mb-1">Material Required</label>
                  <select id="contact-material" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3 py-2.5 text-slate-900 text-sm focus:outline-none focus:border-amber-500">
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
                  <input type="text" id="contact-site" placeholder="e.g. Talaja, Bhavnagar, Mahuva" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-slate-900 text-sm focus:outline-none focus:border-amber-500">
                </div>
              </div>

              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Project Details / Message</label>
                <textarea id="contact-msg" rows="3" placeholder="Mention total estimated tons or brass, site condition, date of delivery..." class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-slate-900 text-sm focus:outline-none focus:border-amber-500"></textarea>
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
              <a href="https://maps.google.com/?q=Borda,Talaja,Bhavnagar,Gujarat" target="_blank" class="text-blue-600 hover:underline">Open in Google Maps</a>
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
      const url = `https://wa.me/917878999033?text=${{encodeURIComponent(text)}}`;
      window.open(url, '_blank');
    }}
  </script>

{FOOTER_HTML}
</body>
</html>"""

    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("contact.html generated.")

if __name__ == '__main__':
    create_about_page()
    create_products_page()
    create_plant_page()
    create_contracting_page()
    create_calculator_page()
    create_gallery_page()
    create_contact_page()
    print("All 7 subpages generated successfully!")
