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
          <h4 class="text-sm font-bold uppercase text-white tracking-wider border-b border-slate-800 pb-2">Key Personnel & Direct Desk</h4>
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

            <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800">
              <span class="text-[10px] font-bold text-amber-400 block uppercase">Official Email Desk:</span>
              <a href="mailto:ashutoshbuild@rediffmail.com" class="text-xs font-semibold text-white hover:text-amber-400 flex items-center gap-1.5 mt-0.5">
                <i class="fa-solid fa-envelope text-amber-400"></i> ashutoshbuild@rediffmail.com
              </a>
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

        <!-- VIRTUAL ASSISTANT MODEL & WHATSAPP INTERACTIVE WIDGET (APPEARS AFTER 4 SECONDS) -->
  <div id="virtual-model-widget" aria-label="Live Customer Support Desk">
    
    <!-- Model Half-Character Cutout & WhatsApp Icon -->
    <div class="relative flex flex-col items-center flex-shrink-0">
      
      <!-- Half Character Image Container -->
      <div class="relative w-28 sm:w-36 md:w-44 h-auto cursor-pointer filter drop-shadow-[0_12px_24px_rgba(0,0,0,0.4)] transition-transform duration-300 hover:scale-105" onclick="reopenModelSpeech()">
        <img src="assets/images/virtual-assistant-model.png" alt="Pooja Sharma - Ashutosh Build Stone Live Support" class="w-full h-auto object-contain block select-none pointer-events-none" width="350" height="450">
        
        <!-- WhatsApp Icon Badge positioned on model's lower side -->
        <a href="https://wa.me/917878999033?text=Namaste%20Ashutosh%20Build%20Stone%20Pvt.%20Ltd.,%20I%20am%20inquiring%20about%20material%20rates%20and%20instant%20dispatch." target="_blank" rel="noopener noreferrer" class="absolute -bottom-1 -right-1 sm:right-1 bg-[#25D366] hover:bg-[#20ba59] text-white w-10 h-10 sm:w-12 sm:h-12 rounded-full flex items-center justify-center text-xl sm:text-2xl shadow-xl border-2 border-white transition-all transform hover:scale-110 pulse-glow" title="Chat on WhatsApp" aria-label="Chat on WhatsApp">
          <i class="fa-brands fa-whatsapp"></i>
        </a>
      </div>
    </div>

    <!-- Speech Chat Bubble -->
    <div id="model-speech-bubble" class="bg-white/95 backdrop-blur-md rounded-2xl p-4 sm:p-5 shadow-2xl border-2 border-amber-400/80 text-slate-800 w-[285px] sm:w-[350px] mb-1 sm:mb-6 relative">
      
      <!-- Close / Dismiss Button (Immediately stops audio and closes popup) -->
      <button onclick="dismissModelAssistant(event)" class="absolute -top-3 -right-3 bg-slate-900 hover:bg-red-600 text-white rounded-full w-7 h-7 flex items-center justify-center text-xs shadow-lg transition-colors border-2 border-white cursor-pointer" title="बंद करें (Close)" aria-label="Close Assistant">
        <i class="fa-solid fa-xmark"></i>
      </button>

      <!-- Assistant Header with Live Status & Speaking Equalizer -->
      <div class="flex items-center justify-between mb-2.5 pb-2 border-b border-slate-100">
        <div class="flex items-center gap-2">
          <span class="relative flex h-2.5 w-2.5">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
          </span>
          <div class="leading-tight">
            <div class="text-xs font-bold text-slate-900 flex items-center gap-1">
              <span>पूजा शर्मा</span>
              <span class="text-[9px] bg-blue-100 text-blue-800 font-extrabold px-1.5 py-0.5 rounded">कस्टमर सपोर्ट</span>
            </div>
            <div class="text-[10px] text-slate-500 font-medium">Ashutosh Build Stone Pvt. Ltd.</div>
          </div>
        </div>

        <!-- Live Voice Speaking Indicator Badge -->
        <div id="live-voice-badge" class="flex items-center gap-1.5 text-[11px] font-bold text-amber-600 bg-amber-50 px-2.5 py-1 rounded-full border border-amber-200 cursor-pointer" onclick="toggleVoiceAudio(event)" title="वॉइस ऑन/ऑफ">
          <span class="flex items-center gap-0.5 h-3">
            <span class="sound-wave-bar"></span>
            <span class="sound-wave-bar" style="animation-delay: 0.2s"></span>
            <span class="sound-wave-bar" style="animation-delay: 0.4s"></span>
          </span>
          <span id="live-voice-text">लाइव वॉइस</span>
        </div>
      </div>

      <!-- Spoken Message Text in Hindi -->
      <p id="model-speech-text" class="text-xs sm:text-[13px] font-semibold text-slate-800 leading-relaxed font-hindi-motto">
        "नमस्ते! आशुतोष बिल्ड स्टोन में आपका स्वागत है। मैं आपकी क्या सहायता कर सकती हूँ? हम वॉट्सऐप पर लाइव उपलब्ध हैं, तुरंत बेस्ट रेट और मटेरियल डिलीवरी के लिए अभी वॉट्सऐप पर संपर्क करें।"
      </p>

      <!-- Action Buttons inside Bubble -->
      <div class="mt-3.5 flex flex-col sm:flex-row gap-2">
        <a href="https://wa.me/917878999033?text=Namaste%20Ashutosh%20Build%20Stone%20Pvt.%20Ltd.,%20I%20am%20inquiring%20about%20material%20rates%20and%20instant%20dispatch." target="_blank" rel="noopener noreferrer" class="flex-1 bg-[#25D366] hover:bg-[#20ba59] text-white font-bold py-2.5 px-3 rounded-xl text-xs flex items-center justify-center gap-1.5 shadow-md transition-transform hover:scale-102">
          <i class="fa-brands fa-whatsapp text-base"></i>
          <span>वॉट्सऐप पर चैट करें</span>
        </a>
        <a href="tel:7878999033" class="bg-brand-navy hover:bg-slate-800 text-amber-300 font-bold py-2.5 px-3 rounded-xl text-xs flex items-center justify-center gap-1 border border-amber-500/30 shadow-sm transition-colors whitespace-nowrap">
          <i class="fa-solid fa-phone text-[10px]"></i>
          <span>कॉल करें</span>
        </a>
      </div>

      <!-- Pointer Arrow pointing to model (Desktop) -->
      <div class="hidden sm:block absolute bottom-6 -left-2 w-0 h-0 border-t-8 border-t-transparent border-r-8 border-r-white border-b-8 border-b-transparent"></div>
      <!-- Pointer Arrow pointing to model (Mobile) -->
      <div class="block sm:hidden absolute -bottom-2 left-8 w-0 h-0 border-l-8 border-l-transparent border-t-8 border-t-white border-r-8 border-r-transparent"></div>
    </div>

  </div>

  <!-- Reopen Floating Trigger Pill (When Model is dismissed) -->
  <div id="reopen-assistant-pill" class="hidden fixed bottom-16 md:bottom-6 left-4 sm:left-6 z-50">
    <button onclick="reopenModelSpeech()" class="flex items-center gap-2.5 bg-[#25D366] hover:bg-[#20ba59] text-white pl-2 pr-4 py-2 rounded-full shadow-xl hover:shadow-2xl transition-all duration-300 transform hover:scale-105 border-2 border-white/40 cursor-pointer">
      <div class="w-9 h-9 rounded-full overflow-hidden border border-white/60 bg-white flex-shrink-0">
        <img src="assets/images/virtual-assistant-model.png" alt="Support" class="w-full h-full object-cover">
      </div>
      <div class="flex flex-col text-left leading-tight">
        <span class="text-[9px] font-semibold text-emerald-100 uppercase tracking-wider">लाइव वॉट्सऐप</span>
        <span class="text-xs font-bold whitespace-nowrap text-white">सहायता चाहिए? (Help)</span>
      </div>
    </button>
  </div>

  <!-- Audio Element for Hindi Voice -->
  <audio id="virtual-model-audio" preload="auto">
    <source src="assets/audio/welcome-voice.mp3" type="audio/mpeg">
  </audio>

  <!-- FESTIVE GREETINGS POPUP MODAL (DHANTERAS, KALI CHAUDAS, DIWALI, NEW YEAR) -->
  <div id="festive-modal" class="fixed inset-0 z-[100] bg-black/85 hidden items-center justify-center px-4 py-6 backdrop-blur-md overflow-y-auto" onclick="closeFestiveModal()">
    <div class="relative w-[92%] sm:w-full sm:max-w-lg max-h-[90vh] overflow-y-auto rounded-3xl p-4 sm:p-7 text-white text-center shadow-2xl border-2 border-amber-400/80 transform transition-all duration-300 my-auto box-border mx-auto" style="background: radial-gradient(circle at top, #1a2942 0%, #07101e 100%);" onclick="event.stopPropagation()">
      
      <!-- Top Decorative Glow Accents -->
      <div class="absolute -top-16 -left-16 w-36 h-36 bg-amber-500/20 rounded-full blur-2xl pointer-events-none"></div>
      <div class="absolute -top-16 -right-16 w-36 h-36 bg-orange-500/20 rounded-full blur-2xl pointer-events-none"></div>
      
      <!-- Close Button (X) -->
      <button onclick="closeFestiveModal()" class="absolute top-3.5 right-3.5 text-slate-400 hover:text-white bg-slate-800/80 hover:bg-slate-700 w-8 h-8 rounded-full flex items-center justify-center text-sm transition-colors z-20 cursor-pointer" title="Close" aria-label="Close Festive Greetings">
        <i class="fa-solid fa-xmark"></i>
      </button>

      <!-- Company Top Badge -->
      <div class="flex items-center justify-center mb-2 px-6">
        <span class="inline-flex items-center gap-1.5 bg-amber-500/15 border border-amber-400/40 text-amber-300 text-[10px] sm:text-[11px] font-bold px-2.5 py-1 rounded-full uppercase tracking-wider max-w-full">
          <i class="fa-solid fa-building text-[9px] sm:text-[10px]"></i>
          <span class="truncate">Ashutosh Build Stone Pvt. Ltd.</span>
        </span>
      </div>

      <!-- Festive Icons & Title Container -->
      <div class="mb-3">
        <div id="festive-icon-container" class="flex items-center justify-center gap-3 text-3xl sm:text-4xl mb-2">
          <span class="inline-block animate-bounce" style="animation-duration: 2s;">🪔</span>
          <span id="festive-main-symbol" class="text-3xl sm:text-4xl drop-shadow-[0_0_15px_rgba(250,204,21,0.6)]">
            <i class="fa-solid fa-coins text-amber-300"></i>
          </span>
          <span class="inline-block animate-bounce" style="animation-duration: 2s; animation-delay: 0.3s;">🪔</span>
        </div>
        <div id="festive-badge" class="text-[11px] sm:text-xs font-black uppercase tracking-widest text-amber-400 mb-1">
          शुभकामना संदेश
        </div>
        <h2 id="festive-title" class="text-2xl sm:text-3xl font-black font-hindi-motto text-amber-300 tracking-wide drop-shadow-md">
          शुभ धनतेरस
        </h2>
        <div id="festive-english-title" class="text-xs sm:text-sm font-bold tracking-widest uppercase text-slate-300 mt-0.5">
          Happy Dhanteras 2026
        </div>
        <div id="festive-subtitle" class="text-[11px] sm:text-xs text-amber-200/90 font-medium mt-1">
          धन, धान्य, उत्तम स्वास्थ्य और समृद्धि का पावन पर्व
        </div>
      </div>

      <!-- Golden Divider -->
      <div class="flex items-center justify-center gap-2 my-2.5">
        <div class="h-[1px] w-12 bg-gradient-to-r from-transparent via-amber-400 to-transparent"></div>
        <span class="text-amber-400 text-xs">✦ 🪔 ✦</span>
        <div class="h-[1px] w-12 bg-gradient-to-r from-transparent via-amber-400 to-transparent"></div>
      </div>

      <!-- Festive Blessing Message Body -->
      <p id="festive-message" class="text-xs sm:text-sm font-medium text-slate-200 leading-relaxed font-hindi-motto px-1 sm:px-3">
        आशुतोष बिल्ड स्टोन प्रा. लि. परिवार की ओर से आपको एवं आपके परिवार को पावन पर्व धनतेरस की हार्दिक शुभकामनाएं।
      </p>

      <!-- Directors Wishes Box -->
      <div class="mt-3.5 p-3 rounded-2xl bg-slate-900/85 border border-amber-500/30 text-left">
        <div class="text-[10px] font-bold text-amber-400 uppercase tracking-wider mb-1.5 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-0.5">
          <span>हार्दिक शुभकामनाओं सहित</span>
          <span class="text-[9px] text-slate-400">Borda • Talaja • Bhavnagar</span>
        </div>
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5 text-xs text-slate-200">
          <div class="leading-tight">
            <span class="font-bold text-white block sm:inline">श्री भागीरथ सिंह सरवैया</span>
            <span class="text-[11px] text-slate-400 sm:ml-1">(Mo. 78789 99033)</span>
          </div>
          <div class="leading-tight">
            <span class="font-bold text-white block sm:inline">श्री अल्पेश चौहान</span>
            <span class="text-[11px] text-slate-400 sm:ml-1">(Mo. 76239 98398)</span>
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="mt-4 flex flex-col sm:flex-row gap-2">
        <button onclick="closeFestiveModal()" class="w-full sm:flex-1 bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-400 hover:to-yellow-400 text-slate-950 font-black py-2.5 sm:py-3 px-3 rounded-xl text-xs sm:text-sm flex items-center justify-center gap-1.5 shadow-lg transition-transform active:scale-95 cursor-pointer">
          <span>शुभकामनाएं स्वीकार करें / Continue</span>
          <i class="fa-solid fa-arrow-right text-xs"></i>
        </button>
        <a id="festive-whatsapp-btn" href="https://wa.me/917878999033" target="_blank" rel="noopener noreferrer" class="w-full sm:w-auto bg-[#25D366] hover:bg-[#20ba59] text-white font-bold py-2.5 sm:py-3 px-3.5 rounded-xl text-xs sm:text-sm flex items-center justify-center gap-1.5 shadow-lg transition-transform active:scale-95">
          <i class="fa-brands fa-whatsapp text-base"></i>
          <span>WhatsApp पर बधाई दें</span>
        </a>
      </div>

    </div>
  </div>

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

    
    
    
    // ==========================================
    // VIRTUAL ASSISTANT MODEL & AUTO-START AUDIO LOGIC
    // ==========================================
    let modelAudio = null;
    let audioPlaying = false;
    let modelDismissed = false;

    function getAudioElement() {
      if (!modelAudio) {
        modelAudio = document.getElementById('virtual-model-audio');
      }
      return modelAudio;
    }

    // Pre-unlock audio context on user presence
    function unlockAudioContext() {
      const audio = getAudioElement();
      if (!audio) return;
      const playPromise = audio.play();
      if (playPromise !== undefined) {
        playPromise.then(() => {
          audio.pause();
          audio.currentTime = 0;
        }).catch(() => {});
      }
    }

    ['click', 'pointerdown', 'touchstart', 'keydown'].forEach(evt => {
      document.addEventListener(evt, unlockAudioContext, { once: true, capture: true });
    });

    // ==========================================
    // FESTIVE POPUP SYSTEM (DHANTERAS, KALI CHAUDAS, DIWALI, NEW YEAR)
    // ==========================================
    const FESTIVAL_CONFIG = {
      dhanteras: {
        badge: "धनतेरस महापर्व मंगलकामना",
        hindiTitle: "शुभ धनतेरस",
        englishTitle: "Happy Dhanteras 2026",
        subtitle: "धन, धान्य, उत्तम स्वास्थ्य और समृद्धि का पावन पर्व",
        message: "आशुतोष बिल्ड स्टोन प्रा. लि. परिवार की ओर से आपको एवं आपके परिवार को पावन पर्व धनतेरस की हार्दिक शुभकामनाएं। भगवान धन्वंतरि एवं माँ लक्ष्मी की कृपा से आपका जीवन सुख, शांति, आरोग्य और व्यापारिक प्रगति से परिपूर्ण रहे।",
        iconHtml: '<i class="fa-solid fa-coins text-amber-300 drop-shadow-[0_0_12px_rgba(250,204,21,0.8)]"></i>',
        waText: "नमस्कार भागीरथ सिंह जी / अल्पेश जी, आप को और आशुतोष बिल्ड स्टोन प्रा. लि. परिवार को धनतेरस की हार्दिक शुभकामनाएं!"
      },
      kalichaudas: {
        badge: "काली चौदस / रूप चतुर्दशी शुभकामना",
        hindiTitle: "शुभ काली चौदस",
        englishTitle: "Happy Kali Chaudas 2026",
        subtitle: "बुराई पर अच्छाई और अंधकार पर प्रकाश की विजय",
        message: "काली चौदस एवं रूप चतुर्दशी के पावन अवसर पर आशुतोष बिल्ड स्टोन प्रा. लि. की ओर से मंगलमय शुभकामनाएं। माँ महाकाली आपके जीवन से समस्त विघ्न-बाधाओं का नाश कर सुख-शांति और सफलता का मार्ग प्रशस्त करें।",
        iconHtml: '<i class="fa-solid fa-om text-amber-300 drop-shadow-[0_0_12px_rgba(250,204,21,0.8)]"></i>',
        waText: "नमस्कार भागीरथ सिंह जी / अल्पेश जी, आप को और आशुतोष बिल्ड स्टोन परिवार को काली चौदस की हार्दिक शुभकामनाएं!"
      },
      diwali: {
        badge: "दीपावली महापर्व मंगलकामना संदेश",
        hindiTitle: "शुभ दीपावली",
        englishTitle: "Happy Deepawali 2026",
        subtitle: "दीपों का यह महापर्व आपके जीवन को सुख-समृद्धि से आलोकित करे",
        message: "दीपावली के इस पावन एवं प्रकाशमय महापर्व पर आशुतोष बिल्ड स्टोन प्रा. लि. की ओर से आपको एवं आपके संपूर्ण परिवार को हार्दिक शुभकामनाएं। यह दीपोत्सव आपके घर-आँगन में खुशहाली, वैभव, उत्तम स्वास्थ्य और व्यापार में नई ऊंचाइयां लेकर आए।",
        iconHtml: '<i class="fa-solid fa-fire text-amber-300 drop-shadow-[0_0_12px_rgba(250,204,21,0.8)]"></i>',
        waText: "नमस्कार भागीरथ सिंह जी / अल्पेश जी, आप को और आशुतोष बिल्ड स्टोन परिवार को दीपावली की हार्दिक शुभकामनाएं!"
      },
      newyear: {
        badge: "नूतन वर्षाभिनंदन मंगलकामना",
        hindiTitle: "नूतन वर्षाभिनंदन",
        englishTitle: "Happy New Year • साल मुबारक 2026",
        subtitle: "विक्रम संवत नव वर्ष की अशेष हार्दिक शुभकामनाएं",
        message: "नव वर्ष एवं नूतन वर्षाभिनंदन (Bestu Varas) के पावन अवसर पर आशुतोष बिल्ड स्टोन प्रा. लि. की ओर से अशेष शुभकामनाएं। आने वाला नया साल आपके सभी संकल्पों, निर्माण कार्यों और व्यवसाय को नई गति और अपार समृद्धि प्रदान करे।",
        iconHtml: '<i class="fa-solid fa-sun text-amber-300 drop-shadow-[0_0_12px_rgba(250,204,21,0.8)]"></i>',
        waText: "नमस्कार भागीरथ सिंह जी / अल्पेश जी, आप को और आशुतोष बिल्ड स्टोन परिवार को नूतन वर्षाभिनंदन एवं नव वर्ष की हार्दिक शुभकामनाएं!"
      }
    };

    let activeFestivalKey = null;

    function getActiveFestival() {
      // 1. URL parameter override for preview & testing: ?festive=dhanteras / kalichaudas / diwali / newyear
      const urlParams = new URLSearchParams(window.location.search);
      const param = (urlParams.get('festive') || '').toLowerCase().trim();
      if (param) {
        if (param === 'dhanteras') return 'dhanteras';
        if (param === 'kalichaudas' || param === 'kali_chaudas' || param === 'chaudas') return 'kalichaudas';
        if (param === 'diwali' || param === 'deepawali' || param === 'dipawali') return 'diwali';
        if (param === 'newyear' || param === 'nutanvarsh' || param === 'saalmubarak') return 'newyear';
      }

      // 2. Strict Date Detection (Year: 2026, Month: 10 [November in 0-indexed JS])
      const today = new Date();
      const yr = today.getFullYear();
      const mo = today.getMonth(); // 10 is November in JS (0=Jan ... 10=Nov)
      const dt = today.getDate();

      if (yr === 2026 && mo === 10) {
        if (dt === 6) return 'dhanteras';
        if (dt === 7) return 'kalichaudas';
        if (dt === 8 || dt === 9) return 'diwali';
        if (dt === 10) return 'newyear';
      }

      return null;
    }

    function initFestivePopup() {
      const festKey = getActiveFestival();
      if (!festKey || !FESTIVAL_CONFIG[festKey]) {
        // No festival active today: start standard 4-second virtual assistant trigger
        initAssistantTrigger();
        return;
      }

      activeFestivalKey = festKey;
      const data = FESTIVAL_CONFIG[festKey];

      const titleEl = document.getElementById('festive-title');
      const engTitleEl = document.getElementById('festive-english-title');
      const badgeEl = document.getElementById('festive-badge');
      const subEl = document.getElementById('festive-subtitle');
      const msgEl = document.getElementById('festive-message');
      const symEl = document.getElementById('festive-main-symbol');
      const waBtn = document.getElementById('festive-whatsapp-btn');

      if (titleEl) titleEl.innerText = data.hindiTitle;
      if (engTitleEl) engTitleEl.innerText = data.englishTitle;
      if (badgeEl) badgeEl.innerText = data.badge;
      if (subEl) subEl.innerText = data.subtitle;
      if (msgEl) msgEl.innerText = data.message;
      if (symEl) symEl.innerHTML = data.iconHtml;
      if (waBtn) {
        waBtn.href = 'https://wa.me/917878999033?text=' + encodeURIComponent(data.waText);
      }

      const sessionKey = 'festive_dismissed_' + festKey;
      const urlHasOverride = new URLSearchParams(window.location.search).has('festive');
      if (!sessionStorage.getItem(sessionKey) || urlHasOverride) {
        const modal = document.getElementById('festive-modal');
        if (modal) {
          modal.classList.remove('hidden');
          modal.classList.add('flex');
        }
      } else {
        // Already dismissed in this session: start assistant trigger
        initAssistantTrigger();
      }
    }

    function closeFestiveModal() {
      const modal = document.getElementById('festive-modal');
      if (modal) {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }
      if (activeFestivalKey) {
        sessionStorage.setItem('festive_dismissed_' + activeFestivalKey, '1');
      }
      // After festive greeting is closed, trigger Virtual Assistant smoothly after 1.5 seconds
      setTimeout(() => {
        showVirtualAssistant();
      }, 1500);
    }

    // 4-Second Timer: Trigger Popup and Auto-Start Audio
    function initAssistantTrigger() {
      setTimeout(() => {
        showVirtualAssistant();
      }, 4000);
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initFestivePopup);
    } else {
      initFestivePopup();
    }

    function showVirtualAssistant() {
      if (modelDismissed) return;
      const widget = document.getElementById('virtual-model-widget');
      const reopenPill = document.getElementById('reopen-assistant-pill');
      if (widget) {
        widget.classList.add('active');
        if (reopenPill) reopenPill.classList.add('hidden');
        
        // Auto-Start Audio immediately with popup
        startAudioNow();

        // If browser paused unmuted autoplay, start on next first interaction anywhere
        const startOnFirstGesture = () => {
          if (!audioPlaying && !modelDismissed) {
            startAudioNow();
          }
          ['click', 'pointerdown', 'touchstart', 'scroll', 'keydown'].forEach(e => {
            window.removeEventListener(e, startOnFirstGesture);
          });
        };
        ['click', 'pointerdown', 'touchstart', 'scroll', 'keydown'].forEach(e => {
          window.addEventListener(e, startOnFirstGesture, { once: true });
        });
      }
    }

    function startAudioNow() {
      const audio = getAudioElement();
      if (!audio || modelDismissed) return;

      audio.currentTime = 0;
      const playPromise = audio.play();
      if (playPromise !== undefined) {
        playPromise.then(() => {
          audioPlaying = true;
          updateVoiceIndicator(true);
          audio.onended = () => {
            audioPlaying = false;
            updateVoiceIndicator(false);
          };
        }).catch(err => {
          console.log('Autoplay deferred until user activation:', err);
        });
      }
    }

    function updateVoiceIndicator(isPlaying) {
      const txt = document.getElementById('live-voice-text');
      if (!txt) return;
      if (isPlaying) {
        txt.innerText = 'आवाज़ चालू है';
      } else {
        txt.innerText = 'दोबारा सुनें';
      }
    }

    function toggleVoiceAudio(event) {
      if (event) event.stopPropagation();
      const audio = getAudioElement();
      if (!audio) return;

      if (!audio.paused && !audio.ended) {
        audio.pause();
        audioPlaying = false;
        updateVoiceIndicator(false);
      } else {
        audio.currentTime = 0;
        audio.play().then(() => {
          audioPlaying = true;
          updateVoiceIndicator(true);
          audio.onended = () => {
            audioPlaying = false;
            updateVoiceIndicator(false);
          };
        }).catch(err => console.log(err));
      }
    }

    // DISMISS: Stops audio immediately and hides popup
    function dismissModelAssistant(event) {
      if (event) event.stopPropagation();
      modelDismissed = true;
      audioPlaying = false;

      const widget = document.getElementById('virtual-model-widget');
      const reopenPill = document.getElementById('reopen-assistant-pill');
      if (widget) {
        widget.classList.remove('active');
      }
      if (reopenPill) {
        reopenPill.classList.remove('hidden');
      }
      
      // Stop audio completely when popup is closed
      const audio = getAudioElement();
      if (audio) {
        audio.pause();
        audio.currentTime = 0;
      }
      updateVoiceIndicator(false);
    }

    // REOPEN: Re-shows popup and restarts voice
    function reopenModelSpeech() {
      modelDismissed = false;
      const widget = document.getElementById('virtual-model-widget');
      const reopenPill = document.getElementById('reopen-assistant-pill');
      if (widget) {
        widget.classList.add('active');
      }
      if (reopenPill) {
        reopenPill.classList.add('hidden');
      }
      startAudioNow();
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
