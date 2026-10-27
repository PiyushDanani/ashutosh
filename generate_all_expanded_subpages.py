# generate_all_expanded_subpages.py
# Generates massive, highly detailed subpages with SEO, GEO, AEO, and engineering authority.

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
# 1. ABOUT US PAGE
# ==========================================
def build_expanded_about():
    faqs = [
        (
            "What is the corporate structure and legal registration of Ashutosh Build Stone?",
            "Ashutosh Build Stone Pvt. Ltd. is an incorporated private limited company under the Ministry of Corporate Affairs, Government of India. Our Corporate Identity Number (CIN) is U43299GJ2025PTC159486, Permanent Account Number (PAN) is ABCCA2752K, and Tax Deduction Account Number (TAN) is AHMA32297G. We operate in full compliance with Indian mining, environmental, and commercial laws."
        ),
        (
            "What is the geological origin and strength of Saurashtra Black Trap basalt?",
            "Our aggregates are extracted from captive black trap rock quarries in the Deccan Traps volcanic formation of Saurashtra, Gujarat. Black trap basalt is an igneous crystalline rock known for extreme compressive strength, high density (specific gravity 2.85+), exceptionally low water absorption (<1.0%), and superior aggregate crushing values, making it the highest quality structural aggregate in India."
        ),
        (
            "What does the company slogan 'Save Water, River Sand' signify?",
            "'Save Water, River Sand' represents our environmental sustainability charter. Unchecked river sand dredging ruins riverbeds, lowers regional water tables, and degrades water quality. By manufacturing hydro-cyclone washed stone sand (M-Sand), we protect natural river ecosystems while providing builders with 15-20% higher concrete strength and zero silt impurities."
        ),
        (
            "Who are the key promoters leading Ashutosh Build Stone Pvt. Ltd.?",
            "The company is directed by Mr. Bhagirath Sinh Sarviya (Ph: +91 78789 99033), who oversees quarry extraction, crushing mechanics, hydrocyclone desilting, and fleet dispatch; and Alpesh Chauhan (Ph: +91 76239 98398), who leads commercial partnerships, government contracting tenders, billing, and regional sales."
        ),
        (
            "How does the on-site quality testing laboratory verify aggregate compliance?",
            "Our facility houses a dedicated material testing lab adhering to IS 383:2016 and MoRTH standards. Every production batch undergoes motorized sieve shaker analysis for particle gradation, silt content sedimentation testing, flakiness and elongation checks (<15%), and moisture calibration before weighbridge dispatch."
        )
    ]

    schema = get_global_schema(
        f"About Us | {COMPANY_NAME}",
        "Discover the corporate history, leadership, captive basalt quarries, and sustainable sand vision of Ashutosh Build Stone Pvt. Ltd. in Bhavnagar, Gujarat.",
        f"{BASE_URL}/about.html",
        "AboutPage",
        faqs
    )

    head = build_head(
        "About Us | Ashutosh Build Stone Pvt. Ltd.",
        "Corporate legacy, management, captive basalt quarries, and sustainable sand production in Borda, Talaja, Bhavnagar.",
        "About Ashutosh Build Stone, Bhagirath Sinh Sarviya, Alpesh Chauhan, Black Trap Basalt Gujarat, M-Sand Manufacturer Talaja, Stone Crusher Company Bhavnagar, Govt Approved Contractor Profile",
        f"{BASE_URL}/about.html",
        schema
    )

    nav = get_header_nav("about")
    banner = get_page_banner(
        "About Ashutosh Build Stone Pvt. Ltd.",
        "Pioneering Sustainable Manufactured Sand & High-Tensile Black Trap Aggregates Across Gujarat",
        "About Us"
    )
    factsheet = get_geo_ai_factsheet("About Us")
    faqs_html = get_aeo_faq_component(faqs, "Corporate & Geological Inquiries (AEO)")

    content = f"""{head}
{nav}
{factsheet}
{banner}

  <!-- MAIN ABOUT CONTENT -->
  <section class="py-16 sm:py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Top Grid: Corporate Narrative & Media -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-16">
        
        <div class="lg:col-span-6 space-y-6">
          <span class="inline-flex items-center gap-2 bg-amber-100 text-amber-800 font-bold px-3.5 py-1 rounded-full text-xs uppercase tracking-wider">
            <i class="fa-solid fa-mountain"></i> Corporate Profile & Geological Excellence
          </span>
          <h2 class="text-3xl sm:text-5xl font-black font-industrial uppercase text-brand-navy leading-tight">
            Forging Indestructible Infrastructure With Saurashtra's Finest Basalt
          </h2>
          <p class="speakable-summary text-slate-600 leading-relaxed text-sm sm:text-base">
            <strong>ASHUTOSH BUILD STONE PVT. LTD.</strong> is an officially registered enterprise and Government Approved Building Contractor headquartered on Gopnath Road, Borda, Talaja (Dist. Bhavnagar, Gujarat). Established with a mandate to elevate raw construction standards, our industrial setup combines mechanized quarry mining with multi-stage cone crushing and hydro-cyclone sand washing technologies.
          </p>
          <p class="text-slate-600 leading-relaxed text-sm sm:text-base">
            Our raw materials originate from high-density Deccan basalt stone formations. Unlike sedimentary gravel or soft river rocks, black trap basalt is characterized by immense compressive toughness, high specific gravity (2.85+), and near-zero chemical weathering, making it the gold standard for bridges, national highways, mega marine ports, and high-rise RCC frames.
          </p>

          <div class="p-5 bg-slate-50 rounded-2xl border border-slate-200">
            <h4 class="font-bold text-slate-900 text-sm flex items-center gap-2">
              <i class="fa-solid fa-leaf text-emerald-600"></i> The "Save Water, River Sand" Ecological Charter
            </h4>
            <p class="text-xs text-slate-600 mt-2 leading-relaxed">
              Dredging natural rivers devastates aquatic biodiversity, causes severe riverbank erosion, and drains regional groundwater reserves. Our hydro-cyclone manufactured sand (M-Sand) provides a 100% sustainable alternative that completely safeguards river basins while giving structural engineers 15-20% higher concrete bonding strength.
            </p>
          </div>
        </div>

        <div class="lg:col-span-6 space-y-4">
          <div class="rounded-3xl overflow-hidden shadow-2xl border-4 border-slate-100 group">
            <img src="assets/images/quarry-crushing-facility-hd.jpeg" alt="Basalt Quarry and Plant Facility" class="w-full h-80 object-cover group-hover:scale-105 transition-transform duration-700" width="1376" height="768">
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div class="rounded-2xl overflow-hidden shadow border border-slate-200 bg-slate-50 p-2 text-center">
              <img src="assets/images/poster-nirmaan-aasan.jpeg" alt="हमारे साथ, निर्माण बने आसान" class="w-full h-56 object-contain rounded-xl">
              <p class="text-xs font-bold text-slate-800 mt-2 font-hindi-motto">हमारे साथ, निर्माण बने आसान</p>
            </div>
            <div class="rounded-2xl overflow-hidden shadow border border-slate-200 bg-slate-50 p-2 text-center">
              <img src="assets/images/poster-sapno-ki-raksha.jpeg" alt="निर्माण मटेरियल जो करे आपके सपनों की रक्षा" class="w-full h-56 object-contain rounded-xl">
              <p class="text-xs font-bold text-slate-800 mt-2 font-hindi-motto">सपनों की रक्षा</p>
            </div>
          </div>
        </div>

      </div>

      <!-- LEGAL & CORPORATE CREDENTIALS BANNER -->
      <div class="bg-gradient-to-r from-brand-navy to-slate-900 rounded-3xl p-8 sm:p-10 text-white shadow-xl mb-16 border border-slate-800">
        <div class="flex flex-col md:flex-row items-center justify-between gap-6 pb-6 border-b border-slate-800">
          <div>
            <span class="text-xs font-bold text-amber-400 uppercase tracking-widest">Verified Legal Credentials</span>
            <h3 class="text-2xl sm:text-3xl font-black font-industrial uppercase mt-1">Official Corporate Registration Data</h3>
          </div>
          <span class="bg-amber-500 text-slate-950 font-black text-xs px-4 py-2 rounded-full uppercase tracking-wider">Govt. Approved Building Contractor</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 pt-6 text-sm">
          <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
            <span class="text-xs text-slate-400 block">Corporate Identification No. (CIN)</span>
            <span class="text-base font-bold text-amber-300 font-mono mt-1 block">{CIN}</span>
          </div>

          <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
            <span class="text-xs text-slate-400 block">Permanent Account Number (PAN)</span>
            <span class="text-base font-bold text-white font-mono mt-1 block">{PAN}</span>
          </div>

          <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
            <span class="text-xs text-slate-400 block">Tax Deduction Account (TAN)</span>
            <span class="text-base font-bold text-white font-mono mt-1 block">{TAN}</span>
          </div>

          <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700">
            <span class="text-xs text-slate-400 block">Registered Works Location</span>
            <span class="text-xs font-bold text-slate-200 mt-1 block">{ADDRESS}</span>
          </div>
        </div>
      </div>

      <!-- DIRECTORS & PROMOTERS SPOTLIGHT -->
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="text-xs font-bold text-amber-600 uppercase tracking-widest">Executive Leadership</span>
        <h2 class="text-3xl sm:text-4xl font-black font-industrial uppercase text-brand-navy mt-1">
          Direct Leadership & Promoter Accountability
        </h2>
        <p class="text-slate-600 text-sm mt-1">Direct access to decision-makers for commercial quotes, plant visits, and contract execution.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto mb-16">
        
        <!-- Leader 1: Bhagirath Sinh -->
        <div class="bg-white rounded-3xl p-7 shadow-lg border-t-4 border-amber-500 card-hover flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="bg-amber-100 text-amber-800 text-xs font-bold px-3 py-1 rounded-full uppercase">Director / Plant & Fleet Head</span>
              <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}" target="_blank" rel="noopener noreferrer" class="text-emerald-500 hover:text-emerald-600 text-2xl" title="Chat on WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
            </div>
            <h3 class="text-2xl font-black text-brand-navy">Mr. Bhagirath Sinh Sarviya</h3>
            <p class="text-xs text-slate-500 mt-2 leading-relaxed">
              Directs overall production mechanics, captive quarry extraction, hydrocyclone washing efficiency, computerized weighbridge accuracy, and regional tipper logistics dispatch across Bhavnagar and Saurashtra.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
            <a href="tel:{PHONE_BHAGIRATH_RAW}" class="text-base font-bold text-brand-navy hover:text-amber-600 flex items-center gap-2">
              <i class="fa-solid fa-phone text-amber-500"></i> {PHONE_BHAGIRATH}
            </a>
            <a href="tel:{PHONE_BHAGIRATH_RAW}" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs px-4 py-2 rounded-xl shadow-sm">
              Call Direct
            </a>
          </div>
        </div>

        <!-- Leader 2: Alpesh Chauhan -->
        <div class="bg-white rounded-3xl p-7 shadow-lg border-t-4 border-blue-600 card-hover flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="bg-blue-100 text-blue-800 text-xs font-bold px-3 py-1 rounded-full uppercase">Director / Sales & Tenders</span>
              <a href="https://wa.me/{PHONE_ALPESH_RAW}" target="_blank" rel="noopener noreferrer" class="text-emerald-500 hover:text-emerald-600 text-2xl" title="Chat on WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
            </div>
            <h3 class="text-2xl font-black text-brand-navy">Alpesh Chauhan</h3>
            <p class="text-xs text-slate-500 mt-2 leading-relaxed">
              Spearheads government civil contracting tenders, corporate procurement partnerships with RMC ready-mix plants and highway contractors, project billing, and custom client quotation desks.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
            <a href="tel:{PHONE_ALPESH_RAW}" class="text-base font-bold text-brand-navy hover:text-blue-600 flex items-center gap-2">
              <i class="fa-solid fa-phone text-blue-600"></i> {PHONE_ALPESH}
            </a>
            <a href="tel:{PHONE_ALPESH_RAW}" class="bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs px-4 py-2 rounded-xl shadow-sm">
              Call Direct
            </a>
          </div>
        </div>

      </div>

      <!-- OFFICIAL BANNER PRESENTATION -->
      <div class="rounded-3xl overflow-hidden shadow-sm border border-slate-200 p-4 bg-slate-50">
        <img src="assets/images/company-banner.jpeg" alt="Ashutosh Build Stone Pvt. Ltd. Corporate Banner" class="w-full h-auto object-contain rounded-2xl" width="1600" height="276">
      </div>

    </div>
  </section>

{faqs_html}

{FOOTER_HTML}
</body>
</html>"""

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("about.html generated with expanded authority.")

build_expanded_about()
