# build_pages.py - Generates the complete multi-page corporate website for Ashutosh Build Stone Pvt. Ltd.

import os

HEADER_HTML = """  <!-- STICKY HEADER & NAVBAR WRAPPER -->
  <div class="sticky top-0 z-50 shadow-md">
    
    <!-- TOP CORPORATE CREDENTIALS & DIRECT CALL BAR -->
    <header class="bg-brand-dark text-slate-200 border-b border-slate-800 text-[11px] sm:text-xs py-1.5 px-3 sm:px-6">
      <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-y-1.5 gap-x-4">
        
        <!-- Corporate Reg Badges -->
        <div class="flex items-center flex-wrap gap-x-3 gap-y-1 font-medium whitespace-nowrap">
          <span class="inline-flex items-center gap-1 text-amber-400 font-bold">
            <i class="fa-solid fa-certificate text-[11px]"></i> Govt. Approved Contractor
          </span>
          <span class="text-slate-600 hidden sm:inline">|</span>
          <span class="text-slate-300 hidden md:inline">
            <strong class="text-white">CIN:</strong> U43299GJ2025PTC159486
          </span>
          <span class="text-slate-600 hidden lg:inline">|</span>
          <span class="text-slate-300 hidden lg:inline">
            <strong class="text-white">PAN:</strong> ABCCA2752K &nbsp;|&nbsp; <strong class="text-white">TAN:</strong> AHMA32297G
          </span>
        </div>

        <!-- Direct Key Contacts -->
        <div class="flex items-center gap-2 sm:gap-3 font-semibold ml-auto whitespace-nowrap">
          <a href="tel:7623998398" class="inline-flex items-center gap-1.5 bg-slate-800/90 hover:bg-slate-700 text-amber-300 border border-amber-500/30 px-2.5 py-1 rounded-full transition-colors text-[11px] sm:text-xs">
            <i class="fa-solid fa-phone text-[10px]"></i>
            <span>Alpesh Chauhan: <strong class="text-white">+91 76239 98398</strong></span>
          </a>
          <a href="tel:7878999033" class="inline-flex items-center gap-1.5 bg-amber-500 hover:bg-amber-400 text-slate-950 px-2.5 py-1 rounded-full transition-colors font-bold shadow-sm text-[11px] sm:text-xs">
            <i class="fa-solid fa-phone text-[10px]"></i>
            <span>Bhagirath Sinh: <strong class="text-slate-950">+91 78789 99033</strong></span>
          </a>
        </div>

      </div>
    </header>

    <!-- MAIN NAVIGATION BAR -->
    <nav class="bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm transition-all">
      <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16 sm:h-[72px]">
          
          <!-- Brand Logo & Identity -->
          <a href="index.html" class="flex items-center gap-2.5 sm:gap-3 flex-shrink-0 group py-1">
            <div class="relative w-10 h-10 sm:w-12 sm:h-12 bg-white p-1 rounded-xl shadow-sm border border-slate-200 flex items-center justify-center overflow-hidden flex-shrink-0 group-hover:scale-105 transition-transform">
              <img src="assets/images/logo-transparent.png" alt="Ashutosh Build Stone Logo" class="w-full h-full object-contain">
            </div>
            <div class="flex flex-col justify-center flex-shrink-0">
              <div class="flex items-center gap-1.5 whitespace-nowrap">
                <span class="text-lg sm:text-2xl font-black font-industrial uppercase tracking-wide text-brand-navy leading-none">
                  ASHUTOSH BUILD STONE
                </span>
                <span class="text-[9px] sm:text-[10px] font-extrabold bg-blue-900 text-amber-400 px-1.5 py-0.5 rounded leading-none uppercase tracking-wider">
                  PVT. LTD.
                </span>
              </div>
              <p class="text-[9px] sm:text-[10px] font-bold text-slate-500 uppercase tracking-widest mt-1 whitespace-nowrap leading-none">
                Aggregate • Black Trap • Sand Production
              </p>
            </div>
          </a>

          <!-- Desktop Navigation Links -->
          <div class="hidden lg:flex items-center gap-3 xl:gap-5 text-[13px] xl:text-sm font-bold text-slate-700 whitespace-nowrap">
            <a href="index.html" class="nav-item-home hover:text-amber-600 transition-colors py-1">Home</a>
            <a href="about.html" class="nav-item-about hover:text-amber-600 transition-colors py-1">About Us</a>
            <a href="products.html" class="nav-item-products hover:text-amber-600 transition-colors py-1">Products</a>
            <a href="plant.html" class="nav-item-plant hover:text-amber-600 transition-colors py-1">Machinery</a>
            <a href="contracting.html" class="nav-item-contracting hover:text-amber-600 transition-colors py-1">Govt. Contracting</a>
            <a href="calculator.html" class="nav-item-calculator text-blue-700 hover:text-blue-900 transition-colors py-1 flex items-center gap-1">
              <i class="fa-solid fa-calculator text-amber-500 text-xs"></i>
              <span>Estimator</span>
            </a>
            <a href="gallery.html" class="nav-item-gallery hover:text-amber-600 transition-colors py-1">Gallery</a>
            <a href="contact.html" class="nav-item-contact hover:text-amber-600 transition-colors py-1">Contact</a>
          </div>

          <!-- Action CTAs -->
          <div class="hidden sm:flex items-center gap-2 xl:gap-2.5 flex-shrink-0 whitespace-nowrap">
            <a href="https://wa.me/917878999033?text=Hello%20Ashutosh%20Build%20Stone%20Pvt.%20Ltd.,%20I%20am%20interested%20in%20your%20aggregates%20and%20sand%20supply." target="_blank" class="inline-flex items-center gap-1.5 bg-[#25D366] hover:bg-[#20ba59] text-white px-3 py-2 rounded-lg font-bold text-xs shadow-sm transition-all hover:scale-105">
              <i class="fa-brands fa-whatsapp text-sm"></i>
              <span>WhatsApp</span>
            </a>
            <button onclick="openQuoteModal('General Inquiry')" class="inline-flex items-center gap-1.5 bg-brand-navy hover:bg-blue-900 text-white px-3.5 py-2 rounded-lg font-bold text-xs shadow-sm transition-all hover:scale-105 border-b-2 border-amber-500">
              <i class="fa-solid fa-file-invoice text-amber-400 text-xs"></i>
              <span>Get Quote</span>
            </button>
          </div>

          <!-- Mobile / Tablet Menu Toggle Button -->
          <button id="mobile-menu-btn" class="lg:hidden p-2 rounded-lg text-slate-700 hover:text-brand-navy hover:bg-slate-100 focus:outline-none flex-shrink-0 ml-2">
            <i class="fa-solid fa-bars text-xl"></i>
          </button>

        </div>
      </div>

      <!-- Mobile Dropdown Menu -->
      <div id="mobile-menu" class="hidden lg:hidden bg-white border-b border-slate-200 px-4 pt-2 pb-6 shadow-xl">
        <div class="flex flex-col gap-2.5 font-bold text-sm text-slate-800">
          <a href="index.html" class="py-2 border-b border-slate-100 hover:text-amber-600" onclick="closeMobileMenu()">Home</a>
          <a href="about.html" class="py-2 border-b border-slate-100 hover:text-amber-600" onclick="closeMobileMenu()">About Ashutosh Build Stone</a>
          <a href="products.html" class="py-2 border-b border-slate-100 hover:text-amber-600" onclick="closeMobileMenu()">Products & Aggregates</a>
          <a href="plant.html" class="py-2 border-b border-slate-100 hover:text-amber-600" onclick="closeMobileMenu()">Plant & Machinery</a>
          <a href="contracting.html" class="py-2 border-b border-slate-100 hover:text-amber-600" onclick="closeMobileMenu()">Govt. Approved Contracting</a>
          <a href="calculator.html" class="py-2 border-b border-slate-100 text-blue-700 flex items-center gap-1.5" onclick="closeMobileMenu()">
            <i class="fa-solid fa-calculator text-amber-500"></i> Material Estimator Calculator
          </a>
          <a href="gallery.html" class="py-2 border-b border-slate-100 hover:text-amber-600" onclick="closeMobileMenu()">Photo Gallery</a>
          <a href="contact.html" class="py-2 hover:text-amber-600" onclick="closeMobileMenu()">Contact & Location</a>
          
          <div class="pt-3 flex flex-col gap-2">
            <button onclick="closeMobileMenu(); openQuoteModal('General Inquiry');" class="w-full text-center bg-brand-navy text-white py-2.5 rounded-lg font-bold text-xs flex items-center justify-center gap-2 border-b-2 border-amber-500 shadow-sm">
              <i class="fa-solid fa-file-invoice text-amber-400"></i> Get Instant Quote
            </button>
            <a href="tel:7878999033" class="w-full text-center bg-amber-500 text-slate-950 py-2.5 rounded-lg font-bold text-xs flex items-center justify-center gap-2 shadow-sm">
              <i class="fa-solid fa-phone"></i> Call Bhagirath Sinh: 7878999033
            </a>
            <a href="tel:7623998398" class="w-full text-center bg-slate-800 text-amber-300 py-2.5 rounded-lg font-bold text-xs flex items-center justify-center gap-2 shadow-sm">
              <i class="fa-solid fa-phone"></i> Call Alpesh Chauhan: 7623998398
            </a>
            <a href="https://wa.me/917878999033" target="_blank" class="w-full text-center bg-[#25D366] text-white py-2.5 rounded-lg font-bold text-xs flex items-center justify-center gap-2 shadow-sm">
              <i class="fa-brands fa-whatsapp text-base"></i> WhatsApp Order Desk
            </a>
          </div>
        </div>
      </div>
    </nav>
  </div>"""

FOOTER_HTML = """  <!-- CORPORATE FOOTER -->
  <footer class="bg-brand-dark text-slate-400 text-xs border-t border-slate-800 pt-16 pb-24 lg:pb-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        
        <!-- Company Identity -->
        <div class="space-y-4">
          <div class="flex items-center gap-3">
            <img src="assets/images/logo-transparent.png" alt="Ashutosh Build Stone" class="w-12 h-12 object-contain bg-white p-1 rounded-lg">
            <div>
              <div class="text-lg font-black font-industrial uppercase text-white tracking-wide">
                ASHUTOSH BUILD STONE
              </div>
              <div class="text-[10px] font-bold text-amber-400">PVT. LTD.</div>
            </div>
          </div>
          <p class="text-xs text-slate-400 leading-relaxed">
            Govt. Approved Building Contractor & High-Capacity Aggregate / Sand Manufacturer in Bhavnagar, Gujarat.
          </p>
          <div class="p-3 bg-slate-900/90 rounded-lg border border-slate-800 text-[11px] space-y-1">
            <div><strong class="text-slate-300">CIN:</strong> U43299GJ2025PTC159486</div>
            <div><strong class="text-slate-300">PAN:</strong> ABCCA2752K | <strong class="text-slate-300">TAN:</strong> AHMA32297G</div>
          </div>
        </div>

        <!-- Quick Links -->
        <div class="space-y-3">
          <h4 class="text-sm font-bold uppercase text-white tracking-wider border-b border-slate-800 pb-2">Navigation</h4>
          <ul class="space-y-2">
            <li><a href="index.html" class="hover:text-amber-400 transition-colors">Home</a></li>
            <li><a href="about.html" class="hover:text-amber-400 transition-colors">About Us</a></li>
            <li><a href="products.html" class="hover:text-amber-400 transition-colors">Products & Specifications</a></li>
            <li><a href="plant.html" class="hover:text-amber-400 transition-colors">Plant & Machinery</a></li>
            <li><a href="contracting.html" class="hover:text-amber-400 transition-colors">Govt. Building Contracting</a></li>
            <li><a href="calculator.html" class="hover:text-amber-400 transition-colors">Material Quantity Calculator</a></li>
            <li><a href="gallery.html" class="hover:text-amber-400 transition-colors">Photo Gallery</a></li>
            <li><a href="contact.html" class="hover:text-amber-400 transition-colors">Contact & Location</a></li>
          </ul>
        </div>

        <!-- Products Range -->
        <div class="space-y-3">
          <h4 class="text-sm font-bold uppercase text-white tracking-wider border-b border-slate-800 pb-2">Products Supply</h4>
          <ul class="space-y-2">
            <li><a href="products.html" class="hover:text-amber-400 transition-colors">20mm Black Trap Aggregate (Jelly)</a></li>
            <li><a href="products.html" class="hover:text-amber-400 transition-colors">10mm Fine Grit / Chipping</a></li>
            <li><a href="products.html" class="hover:text-amber-400 transition-colors">40mm Ballast Coarse Stone</a></li>
            <li><a href="products.html" class="hover:text-amber-400 transition-colors">Manufactured Sand (M-Sand - Washed)</a></li>
            <li><a href="products.html" class="hover:text-amber-400 transition-colors">Plaster Sand (P-Sand - Fine Grade)</a></li>
            <li><a href="products.html" class="hover:text-amber-400 transition-colors">Granular Sub Base (GSB) & WMM</a></li>
            <li><a href="products.html" class="hover:text-amber-400 transition-colors">Ready Mix Concrete (RMC)</a></li>
          </ul>
        </div>

        <!-- Direct Contacts -->
        <div class="space-y-3">
          <h4 class="text-sm font-bold uppercase text-white tracking-wider border-b border-slate-800 pb-2">Key Personnel</h4>
          <div class="space-y-3">
            <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800">
              <span class="text-[10px] font-bold text-amber-400 block uppercase">Plant & Operations:</span>
              <a href="tel:7878999033" class="text-sm font-bold text-white hover:text-amber-400 block">
                Mr. Bhagirath Sinh Sarviya
              </a>
              <span class="text-xs text-amber-300 font-semibold">+91 78789 99033</span>
            </div>

            <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800">
              <span class="text-[10px] font-bold text-amber-400 block uppercase">Sales & Billing:</span>
              <a href="tel:7623998398" class="text-sm font-bold text-white hover:text-amber-400 block">
                Alpesh Chauhan
              </a>
              <span class="text-xs text-amber-300 font-semibold">+91 76239 98398</span>
            </div>

            <p class="text-[11px] text-slate-400 pt-1">
              <i class="fa-solid fa-location-dot text-amber-400 mr-1"></i> Gopnath Road, Borda, Talaja, Bhavnagar - 364130
            </p>
          </div>
        </div>

      </div>

      <div class="pt-8 border-t border-slate-800/80 flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-slate-400">
        <div>
          © 2026 <strong>ASHUTOSH BUILD STONE PVT. LTD.</strong> All Rights Reserved.
        </div>
        <div class="flex items-center gap-4">
          <span class="text-amber-400 font-hindi-motto font-bold">"हमारे साथ, निर्माण बने आसान"</span>
          <span>•</span>
          <span class="text-slate-400">IS 383:2016 Compliant</span>
        </div>
      </div>

    </div>
  </footer>

  <!-- FLOATING BOTTOM ACTION BAR FOR MOBILE -->
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

  <!-- FLOATING DESKTOP WHATSAPP BADGE -->
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
  </a>

  <!-- POPUP QUOTE MODAL -->
  <div id="quote-modal" class="fixed inset-0 z-50 bg-black/80 hidden items-center justify-center p-4 backdrop-blur-sm" onclick="closeQuoteModal()">
    <div class="relative max-w-lg w-full bg-slate-900 rounded-2xl p-6 sm:p-7 border border-slate-700 shadow-2xl text-white" onclick="event.stopPropagation()">
      <button onclick="closeQuoteModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white p-2 text-xl leading-none">
        <i class="fa-solid fa-xmark"></i>
      </button>

      <div class="mb-5 border-b border-slate-800 pb-3">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-2">
          <i class="fa-solid fa-file-invoice"></i> Fast Quotation Desk
        </span>
        <h3 class="text-2xl font-bold font-industrial uppercase mt-1">Request Price Quote</h3>
        <p class="text-xs text-slate-400">Direct factory dispatch pricing from Borda, Talaja plant</p>
      </div>

      <form onsubmit="handleModalQuote(event)" class="space-y-3.5 text-sm">
        <div>
          <label class="block text-xs font-semibold text-slate-300 mb-1">Your Name / Firm Name *</label>
          <input type="text" id="modal-name" required placeholder="Enter name or company" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-3.5 py-2 text-white text-sm focus:outline-none focus:border-amber-400">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-300 mb-1">Mobile Number *</label>
            <input type="tel" id="modal-phone" required placeholder="10-digit number" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-3.5 py-2 text-white text-sm focus:outline-none focus:border-amber-400">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-300 mb-1">Select Material</label>
            <select id="modal-material" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-2.5 py-2 text-white text-sm focus:outline-none focus:border-amber-400">
              <option value="20mm Black Trap Aggregate">20mm Aggregate (Jelly)</option>
              <option value="10mm Black Trap Grit">10mm Grit (Chipping)</option>
              <option value="40mm Coarse Ballast">40mm Ballast / Coarse</option>
              <option value="Manufactured Sand (M-Sand)">Manufactured Sand (M-Sand)</option>
              <option value="Plaster Sand (P-Sand)">Plaster Sand (P-Sand)</option>
              <option value="GSB / WMM Road Base">GSB / WMM Road Base</option>
              <option value="Ready Mix Concrete (RMC)">Ready Mix Concrete (RMC)</option>
              <option value="All Materials Bulk Supply">All Materials Bulk</option>
            </select>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-300 mb-1">Estimated Quantity</label>
            <input type="text" id="modal-quantity" placeholder="e.g. 50 MT / 5 Brass" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-3.5 py-2 text-white text-sm focus:outline-none focus:border-amber-400">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-300 mb-1">Site Delivery Location</label>
            <input type="text" id="modal-location" placeholder="e.g. Talaja, Bhavnagar" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-3.5 py-2 text-white text-sm focus:outline-none focus:border-amber-400">
          </div>
        </div>

        <button type="submit" class="w-full bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-3 px-4 rounded-xl flex items-center justify-center gap-2 text-sm transition-transform active:scale-95 shadow-md mt-2">
          <i class="fa-brands fa-whatsapp text-lg"></i>
          <span>Get Quote on WhatsApp</span>
        </button>

        <div class="pt-2 text-center text-xs text-slate-400">
          Or call directly: <a href="tel:7878999033" class="text-amber-400 font-bold hover:underline">7878999033</a> / <a href="tel:7623998398" class="text-amber-400 font-bold hover:underline">7623998398</a>
        </div>
      </form>
    </div>
  </div>

  <!-- LIGHTBOX MODAL FOR GALLERY PREVIEW -->
  <div id="lightbox-modal" class="fixed inset-0 z-50 bg-black/90 hidden items-center justify-center p-4 backdrop-blur-sm" onclick="closeLightbox()">
    <div class="relative max-w-4xl w-full bg-slate-900 rounded-2xl overflow-hidden border border-slate-700 shadow-2xl" onclick="event.stopPropagation()">
      <button onclick="closeLightbox()" class="absolute top-4 right-4 z-10 text-white bg-slate-800/80 hover:bg-slate-700 p-2.5 rounded-full text-lg w-10 h-10 flex items-center justify-center">
        <i class="fa-solid fa-xmark"></i>
      </button>
      <div class="max-h-[75vh] flex items-center justify-center bg-black/60 p-2">
        <img id="lightbox-img" src="" alt="Enlarged view" class="max-h-[70vh] w-auto max-w-full object-contain rounded-lg">
      </div>
      <div class="p-4 bg-slate-900 border-t border-slate-800 flex items-center justify-between">
        <div id="lightbox-caption" class="text-sm font-bold text-white"></div>
        <a href="tel:7878999033" class="text-xs bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold px-3 py-1.5 rounded-lg">
          Inquire Now
        </a>
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
      mobileMenuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
      });
    }

    function closeMobileMenu() {
      if (mobileMenu) mobileMenu.classList.add('hidden');
    }

    // Modal Quote Handlers
    function openQuoteModal(defaultMaterial) {
      const modal = document.getElementById('quote-modal');
      if (!modal) return;
      modal.classList.remove('hidden');
      modal.classList.add('flex');
      if (defaultMaterial && defaultMaterial !== 'General Inquiry') {
        const matSelect = document.getElementById('modal-material');
        if (matSelect) matSelect.value = defaultMaterial;
      }
    }

    function closeQuoteModal() {
      const modal = document.getElementById('quote-modal');
      if (!modal) return;
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }

    function handleModalQuote(e) {
      e.preventDefault();
      const name = document.getElementById('modal-name').value;
      const phone = document.getElementById('modal-phone').value;
      const mat = document.getElementById('modal-material').value;
      const qty = document.getElementById('modal-quantity').value || 'To be discussed';
      const loc = document.getElementById('modal-location').value || 'Bhavnagar area';

      const text = `*Instant Quote Request - Ashutosh Build Stone Pvt. Ltd.*\\n\\n*Name:* ${name}\\n*Phone:* ${phone}\\n*Material:* ${mat}\\n*Quantity:* ${qty}\\n*Site Location:* ${loc}\\n\\nPlease share price quote.`;
      const url = `https://wa.me/917878999033?text=${encodeURIComponent(text)}`;
      window.open(url, '_blank');
      closeQuoteModal();
    }

    // Lightbox Modal for Gallery
    function openLightbox(src, caption) {
      const img = document.getElementById('lightbox-img');
      const cap = document.getElementById('lightbox-caption');
      const modal = document.getElementById('lightbox-modal');
      if (img && cap && modal) {
        img.src = src;
        cap.innerText = caption;
        modal.classList.remove('hidden');
        modal.classList.add('flex');
      }
    }

    function closeLightbox() {
      const modal = document.getElementById('lightbox-modal');
      if (modal) {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }
    }
  </script>"""

def get_page_head(title, description):
    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Ashutosh Build Stone Pvt. Ltd.</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="Ashutosh Build Stone, Black Trap Aggregate, M-Sand, Plaster Sand, Stone Crusher Talaja, Bhavnagar Aggregate Supplier, Borda Crusher Plant, RMC Plant Bhavnagar, 20mm Jelly, 10mm Grit, 40mm Aggregate, Govt Approved Contractor Gujarat">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Teko:wght@500;600;700&family=Noto+Sans+Devanagari:wght@600;700;800&display=swap" rel="stylesheet">

  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              navy: '#0b192c',
              dark: '#07101e',
              deep: '#1e3e62',
              blue: '#0056b3',
              accent: '#f39c12',
              gold: '#e67e22',
              amber: '#ffb703',
              surface: '#f8fafc',
              border: '#e2e8f0',
              gray: '#64748b'
            }}
          }},
          fontFamily: {{
            outfit: ['Outfit', 'sans-serif'],
            teko: ['Teko', 'sans-serif'],
            hindi: ['Noto Sans Devanagari', 'Outfit', 'sans-serif']
          }}
        }}
      }}
    }}
  </script>

  <style>
    body {{
      font-family: 'Outfit', sans-serif;
      background-color: #f8fafc;
      color: #1e293b;
      overflow-x: hidden;
    }}
    .font-industrial {{
      font-family: 'Teko', sans-serif;
      letter-spacing: 0.05em;
    }}
    .font-hindi-motto {{
      font-family: 'Noto Sans Devanagari', sans-serif;
    }}
    .hero-gradient {{
      background: linear-gradient(135deg, rgba(7, 16, 30, 0.95) 0%, rgba(14, 34, 64, 0.88) 50%, rgba(7, 16, 30, 0.92) 100%);
    }}
    .card-hover {{
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .card-hover:hover {{
      transform: translateY(-6px);
      box-shadow: 0 20px 25px -5px rgba(11, 25, 44, 0.15), 0 8px 10px -6px rgba(11, 25, 44, 0.1);
    }}
    .pulse-call {{
      animation: pulseAnimation 2s infinite;
    }}
    @keyframes pulseAnimation {{
      0% {{ box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.6); }}
      70% {{ box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }}
    }}
    ::-webkit-scrollbar {{
      width: 10px;
    }}
    ::-webkit-scrollbar-track {{
      background: #0b192c;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #f59e0b;
      border-radius: 5px;
    }}
  </style>
</head>
<body class="antialiased">
"""

def get_page_banner(title, subtitle, breadcrumb):
    return f"""  <!-- PAGE HERO BANNER -->
  <section class="relative bg-brand-navy py-12 sm:py-16 text-white overflow-hidden border-b border-slate-800">
    <div class="absolute inset-0 z-0">
      <img src="assets/images/sand-washing-crusher-plant-hd.jpeg" alt="Ashutosh Build Stone Plant" class="w-full h-full object-cover filter brightness-[0.22]">
      <div class="absolute inset-0 hero-gradient"></div>
    </div>
    <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center gap-2 text-xs font-bold text-amber-400 uppercase tracking-widest mb-3">
        <a href="index.html" class="hover:underline text-slate-300">Home</a>
        <i class="fa-solid fa-chevron-right text-[10px] text-slate-500"></i>
        <span>{breadcrumb}</span>
      </div>
      <h1 class="text-3xl sm:text-5xl font-black font-industrial uppercase tracking-wide text-white leading-tight">
        {title}
      </h1>
      <p class="text-slate-300 text-sm sm:text-base max-w-2xl mt-2">
        {subtitle}
      </p>
    </div>
  </section>
"""

def highlight_nav(html, page_key):
    # highlight the active nav item
    return html.replace(f'nav-item-{page_key}', f'nav-item-{page_key} text-amber-500 font-black border-b-2 border-amber-500')

print("Base builder prepared.")
