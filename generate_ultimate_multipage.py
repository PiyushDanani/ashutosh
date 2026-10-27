# generate_ultimate_multipage.py
# Generates the ultimate, expanded corporate multi-page website with deep SEO + GEO + AEO integration.

import os
import json

BASE_URL = "https://ashutoshbuildstone.com" # Canonical base
COMPANY_NAME = "Ashutosh Build Stone Pvt. Ltd."
CIN = "U43299GJ2025PTC159486"
PAN = "ABCCA2752K"
TAN = "AHMA32297G"
PHONE_BHAGIRATH = "+91 78789 99033"
PHONE_BHAGIRATH_RAW = "7878999033"
PHONE_ALPESH = "+91 76239 98398"
PHONE_ALPESH_RAW = "7623998398"
ADDRESS = "Gopnath Road, At. Borda, Tal. Talaja, Dist. Bhavnagar, Gujarat - 364130, India"
LATITUDE = 21.2850
LONGITUDE = 72.0850

# Global JSON-LD Schema Generator for SEO, GEO and AEO
def get_global_schema(page_title, page_description, page_url, page_type="WebPage", faqs=None):
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["LocalBusiness", "GeneralContractor", "Corporation"],
                "@id": f"{BASE_URL}/#corporation",
                "name": COMPANY_NAME,
                "legalName": COMPANY_NAME,
                "url": BASE_URL,
                "logo": f"{BASE_URL}/assets/images/logo-transparent.png",
                "image": f"{BASE_URL}/assets/images/sand-washing-crusher-plant-hd.jpeg",
                "description": "Govt. Approved Building Contractor & Leading Manufacturer of Black Trap Aggregates (10mm, 20mm, 40mm), Hydro-Washed M-Sand, Plaster Sand, GSB, and Ready Mix Concrete in Bhavnagar, Gujarat.",
                "telephone": PHONE_BHAGIRATH,
                "priceRange": "$$",
                "currenciesAccepted": "INR",
                "paymentAccepted": "Cash, Bank Transfer, Cheque, RTGS, NEFT",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Gopnath Road, At. Borda",
                    "addressLocality": "Talaja",
                    "addressRegion": "Gujarat",
                    "postalCode": "364130",
                    "addressCountry": "IN"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": LATITUDE,
                    "longitude": LONGITUDE
                },
                "openingHoursSpecification": [
                    {
                        "@type": "OpeningHoursSpecification",
                        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                        "opens": "07:00",
                        "closes": "20:00"
                    }
                ],
                "founder": [
                    {
                        "@type": "Person",
                        "name": "Mr. Bhagirath Sinh Sarviya",
                        "jobTitle": "Director & Plant Head",
                        "telephone": PHONE_BHAGIRATH
                    },
                    {
                        "@type": "Person",
                        "name": "Alpesh Chauhan",
                        "jobTitle": "Director & Sales Head",
                        "telephone": PHONE_ALPESH
                    }
                ],
                "taxID": PAN,
                "identifier": [
                    {
                        "@type": "PropertyValue",
                        "name": "CIN",
                        "value": CIN
                    },
                    {
                        "@type": "PropertyValue",
                        "name": "PAN",
                        "value": PAN
                    },
                    {
                        "@type": "PropertyValue",
                        "name": "TAN",
                        "value": TAN
                    }
                ],
                "areaServed": [
                    {"@type": "AdministrativeArea", "name": "Bhavnagar"},
                    {"@type": "AdministrativeArea", "name": "Talaja"},
                    {"@type": "AdministrativeArea", "name": "Alang"},
                    {"@type": "AdministrativeArea", "name": "Mahuva"},
                    {"@type": "AdministrativeArea", "name": "Palitana"},
                    {"@type": "AdministrativeArea", "name": "Sihor"},
                    {"@type": "AdministrativeArea", "name": "Gujarat"}
                ],
                "hasOfferCatalog": {
                    "@type": "OfferCatalog",
                    "name": "Construction Materials Catalog",
                    "itemListElement": [
                        {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "20mm Black Trap Aggregate (Kapchi / Jelly)"}},
                        {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "10mm Black Trap Grit / Chipping"}},
                        {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "40mm Coarse Aggregate Ballast"}},
                        {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Hydro-Washed Manufactured Sand (M-Sand - Zone II)"}},
                        {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Plaster Sand (P-Sand - Zone IV Fine)"}},
                        {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Granular Sub-Base (GSB) & WMM Road Base"}},
                        {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Ready Mix Concrete (RMC) M15 to M40"}}
                    ]
                }
            },
            {
                "@type": page_type,
                "@id": page_url,
                "url": page_url,
                "name": page_title,
                "description": page_description,
                "isPartOf": {
                    "@type": "WebSite",
                    "@id": f"{BASE_URL}/#website",
                    "url": BASE_URL,
                    "name": COMPANY_NAME,
                    "inLanguage": ["en", "hi", "gu"]
                },
                "speakable": {
                    "@type": "SpeakableSpecification",
                    "cssSelector": [".speakable-summary", ".aeo-answer", ".geo-factsheet"]
                }
            }
        ]
    }

    if faqs:
        faq_schema = {
            "@type": "FAQPage",
            "@id": f"{page_url}#faq",
            "mainEntity": []
        }
        for q, a in faqs:
            faq_schema["mainEntity"].append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            })
        schema["@graph"].append(faq_schema)

    return json.dumps(schema, indent=2, ensure_ascii=False)


# Header & Nav with active page highlight
def get_header_nav(active_page="home"):
    def is_active(page):
        return "text-amber-500 font-black border-b-2 border-amber-500" if active_page == page else "hover:text-amber-600 transition-colors"

    return f"""  <!-- STICKY HEADER & NAVBAR WRAPPER (PERFECT SINGLE-LINE ALIGNMENT) -->
  <div class="sticky top-0 z-50 shadow-md">
    
    <!-- TOP CORPORATE CREDENTIALS & DIRECT CALL BAR -->
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

    <!-- MAIN NAVIGATION BAR -->
    <nav class="bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm transition-all" aria-label="Main Navigation">
      <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16 sm:h-[72px]">
          
          <!-- Brand Logo & Identity (Responsive Single Line) -->
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
          </a>

          <!-- Desktop Navigation Links -->
          <div class="hidden lg:flex items-center gap-3 xl:gap-5 text-[13px] xl:text-sm font-bold text-slate-700 whitespace-nowrap">
            <a href="index.html" class="{is_active('home')} py-1">Home</a>
            <a href="about.html" class="{is_active('about')} py-1">About Us</a>
            <a href="products.html" class="{is_active('products')} py-1">Products</a>
            <a href="plant.html" class="{is_active('plant')} py-1">Machinery</a>
            <a href="contracting.html" class="{is_active('contracting')} py-1">Govt. Contracting</a>
            <a href="calculator.html" class="{is_active('calculator')} py-1 flex items-center gap-1">
              <i class="fa-solid fa-calculator text-amber-500 text-xs"></i>
              <span>Estimator</span>
            </a>
            <a href="gallery.html" class="{is_active('gallery')} py-1">Gallery</a>
            <a href="contact.html" class="{is_active('contact')} py-1">Contact</a>
          </div>

          <!-- Action CTAs -->
          <div class="hidden sm:flex items-center gap-2 xl:gap-2.5 flex-shrink-0 whitespace-nowrap">
            <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}?text=Hello%20Ashutosh%20Build%20Stone%20Pvt.%20Ltd.,%20I%20am%20interested%20in%20your%20aggregates%20and%20sand%20supply." target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 bg-[#25D366] hover:bg-[#20ba59] text-white px-3 py-2 rounded-lg font-bold text-xs shadow-sm transition-all hover:scale-105" aria-label="Chat on WhatsApp">
              <i class="fa-brands fa-whatsapp text-sm"></i>
              <span>WhatsApp</span>
            </a>
            <button onclick="openQuoteModal('General Inquiry')" class="inline-flex items-center gap-1.5 bg-brand-navy hover:bg-blue-900 text-white px-3.5 py-2 rounded-lg font-bold text-xs shadow-sm transition-all hover:scale-105 border-b-2 border-amber-500" aria-label="Request Instant Quotation">
              <i class="fa-solid fa-file-invoice text-amber-400 text-xs"></i>
              <span>Get Quote</span>
            </button>
          </div>

          <!-- Mobile / Tablet Menu Toggle Button -->
          <button id="mobile-menu-btn" class="lg:hidden p-2 rounded-lg text-slate-700 hover:text-brand-navy hover:bg-slate-100 focus:outline-none flex-shrink-0 ml-2" aria-label="Toggle navigation menu">
            <i class="fa-solid fa-bars text-xl"></i>
          </button>

        </div>
      </div>

      <!-- Mobile Dropdown Menu -->
      <div id="mobile-menu" class="hidden lg:hidden bg-white border-b border-slate-200 px-4 pt-2 pb-6 shadow-xl">
        <div class="flex flex-col gap-2.5 font-bold text-sm text-slate-800">
          <a href="index.html" class="py-2 border-b border-slate-100 {is_active('home')}" onclick="closeMobileMenu()">Home</a>
          <a href="about.html" class="py-2 border-b border-slate-100 {is_active('about')}" onclick="closeMobileMenu()">About Ashutosh Build Stone</a>
          <a href="products.html" class="py-2 border-b border-slate-100 {is_active('products')}" onclick="closeMobileMenu()">Products & Aggregates</a>
          <a href="plant.html" class="py-2 border-b border-slate-100 {is_active('plant')}" onclick="closeMobileMenu()">Plant & Machinery</a>
          <a href="contracting.html" class="py-2 border-b border-slate-100 {is_active('contracting')}" onclick="closeMobileMenu()">Govt. Approved Contracting</a>
          <a href="calculator.html" class="py-2 border-b border-slate-100 {is_active('calculator')} flex items-center gap-1.5" onclick="closeMobileMenu()">
            <i class="fa-solid fa-calculator text-amber-500"></i> Material Estimator Calculator
          </a>
          <a href="gallery.html" class="py-2 border-b border-slate-100 {is_active('gallery')}" onclick="closeMobileMenu()">Photo Gallery</a>
          <a href="contact.html" class="py-2 {is_active('contact')}" onclick="closeMobileMenu()">Contact & Location</a>
          
          <div class="pt-3 flex flex-col gap-2">
            <button onclick="closeMobileMenu(); openQuoteModal('General Inquiry');" class="w-full text-center bg-brand-navy text-white py-2.5 rounded-lg font-bold text-xs flex items-center justify-center gap-2 border-b-2 border-amber-500 shadow-sm">
              <i class="fa-solid fa-file-invoice text-amber-400"></i> Get Instant Quote
            </button>
            <a href="tel:{PHONE_BHAGIRATH_RAW}" class="w-full text-center bg-amber-500 text-slate-950 py-2.5 rounded-lg font-bold text-xs flex items-center justify-center gap-2 shadow-sm">
              <i class="fa-solid fa-phone"></i> Call Bhagirath Sinh: {PHONE_BHAGIRATH_RAW}
            </a>
            <a href="tel:{PHONE_ALPESH_RAW}" class="w-full text-center bg-slate-800 text-amber-300 py-2.5 rounded-lg font-bold text-xs flex items-center justify-center gap-2 shadow-sm">
              <i class="fa-solid fa-phone"></i> Call Alpesh Chauhan: {PHONE_ALPESH_RAW}
            </a>
            <a href="https://wa.me/{PHONE_BHAGIRATH_RAW}" target="_blank" rel="noopener noreferrer" class="w-full text-center bg-[#25D366] text-white py-2.5 rounded-lg font-bold text-xs flex items-center justify-center gap-2 shadow-sm">
              <i class="fa-brands fa-whatsapp text-base"></i> WhatsApp Order Desk
            </a>
          </div>
        </div>
      </div>
    </nav>
  </div>"""


# GEO Factsheet Component (AI Engines & Perplexity / Gemini love to parse this)
def get_geo_ai_factsheet(page_context="General"):
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
  </aside>"""


# AEO FAQ Accordion Component
def get_aeo_faq_component(faqs, section_title="Frequently Asked Questions & Technical Inquiries"):
    accordion_items = ""
    for idx, (q, a) in enumerate(faqs):
        accordion_items += f"""
        <div class="border border-slate-200 rounded-2xl bg-white overflow-hidden shadow-sm transition-all hover:border-amber-400">
          <button type="button" class="faq-btn w-full px-6 py-4 text-left font-bold text-brand-navy flex items-center justify-between gap-4 text-sm sm:text-base focus:outline-none" onclick="toggleFaq({idx})">
            <span>{q}</span>
            <i id="faq-icon-{idx}" class="fa-solid fa-chevron-down text-slate-400 text-xs transition-transform duration-300"></i>
          </button>
          <div id="faq-ans-{idx}" class="faq-content hidden px-6 pb-5 pt-1 text-slate-600 text-xs sm:text-sm leading-relaxed border-t border-slate-100">
            <div class="aeo-answer p-3 bg-amber-50/60 rounded-xl border border-amber-200/50 mb-2 font-medium text-slate-800">
              {a.split('.')[0] + '.' if '.' in a else a}
            </div>
            <p>{a}</p>
          </div>
        </div>
        """

    return f"""  <!-- AEO ANSWER ENGINE OPTIMIZATION: FAQ ACCORDION SECTION -->
  <section class="py-16 sm:py-20 bg-slate-50 border-t border-slate-200" id="faqs">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="inline-flex items-center gap-2 bg-amber-100 text-amber-800 font-bold px-3 py-1 rounded-full text-xs uppercase tracking-wider mb-2">
          <i class="fa-solid fa-circle-question"></i> Answer Engine Optimization (AEO)
        </span>
        <h2 class="text-3xl sm:text-4xl font-black font-industrial uppercase text-brand-navy">
          {section_title}
        </h2>
        <p class="text-slate-600 text-xs sm:text-sm mt-1">
          Direct, verified answers to common contractor, civil engineer, and procurement inquiries.
        </p>
      </div>

      <div class="space-y-3.5">
        {accordion_items}
      </div>

    </div>
  </section>

  <script>
    function toggleFaq(idx) {{
      const ans = document.getElementById('faq-ans-' + idx);
      const icon = document.getElementById('faq-icon-' + idx);
      if (ans.classList.contains('hidden')) {{
        ans.classList.remove('hidden');
        icon.classList.add('rotate-180', 'text-amber-600');
      }} else {{
        ans.classList.add('hidden');
        icon.classList.remove('rotate-180', 'text-amber-600');
      }}
    }}
  </script>"""

print("SEO/GEO/AEO core frameworks initialized.")
