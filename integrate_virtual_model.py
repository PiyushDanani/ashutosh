# integrate_virtual_model.py
import re
import os

WIDGET_HTML = """  <!-- VIRTUAL ASSISTANT MODEL & WHATSAPP INTERACTIVE WIDGET (APPEARS AFTER 4 SECONDS) -->
  <div id="virtual-model-widget" class="fixed bottom-14 md:bottom-0 left-2 sm:left-6 z-50 flex flex-col-reverse sm:flex-row items-start sm:items-end gap-2 sm:gap-3 pointer-events-none transition-all duration-700 ease-out transform translate-y-[130%] opacity-0 max-w-[95vw] sm:max-w-none" aria-label="Live Customer Support Desk">
    
    <!-- Model Half-Character Cutout & WhatsApp Icon -->
    <div class="relative pointer-events-auto flex flex-col items-center flex-shrink-0">
      
      <!-- Speech / Audio Control Pill -->
      <button id="model-voice-btn" onclick="toggleVoiceAudio()" class="absolute -top-3 left-1/2 -translate-x-1/2 z-20 bg-amber-500 hover:bg-amber-400 text-slate-950 font-black text-[10px] px-2.5 py-1 rounded-full shadow-lg border border-amber-300 flex items-center gap-1.5 whitespace-nowrap cursor-pointer transition-transform hover:scale-105" title="Click to listen / replay voice">
        <i id="model-audio-icon" class="fa-solid fa-volume-high text-xs text-slate-950"></i>
        <span id="model-audio-text">Voice On</span>
      </button>

      <!-- Half Character Image Container -->
      <div class="relative w-24 sm:w-36 md:w-44 h-auto cursor-pointer filter drop-shadow-[0_12px_24px_rgba(0,0,0,0.35)] transition-transform duration-300 hover:scale-105" onclick="reopenModelSpeech()">
        <img src="assets/images/virtual-assistant-model.png" alt="Pooja - Ashutosh Build Stone Live Support Executive" class="w-full h-auto object-contain block select-none pointer-events-none" width="350" height="450">
        
        <!-- WhatsApp Icon Badge positioned on model's lower side -->
        <a href="https://wa.me/917878999033?text=Hello%20Ashutosh%20Build%20Stone%20Pvt.%20Ltd.,%20I%20am%20interested%20in%20instant%20material%20quotation%20and%20rates." target="_blank" rel="noopener noreferrer" class="absolute -bottom-1 -right-1 sm:right-1 bg-[#25D366] hover:bg-[#20ba59] text-white w-9 h-9 sm:w-12 sm:h-12 rounded-full flex items-center justify-center text-lg sm:text-2xl shadow-xl border-2 border-white transition-all transform hover:scale-110" title="Chat on WhatsApp" aria-label="Chat on WhatsApp">
          <i class="fa-brands fa-whatsapp"></i>
        </a>
      </div>
    </div>

    <!-- Speech Chat Bubble -->
    <div id="model-speech-bubble" class="pointer-events-auto bg-white/95 backdrop-blur-md rounded-2xl p-3.5 sm:p-5 shadow-2xl border border-slate-200/90 text-slate-800 w-[280px] sm:w-[340px] mb-1 sm:mb-6 relative">
      
      <!-- Close / Dismiss Button -->
      <button onclick="dismissModelAssistant()" class="absolute -top-2.5 -right-2.5 bg-slate-800 hover:bg-slate-950 text-white rounded-full w-6 h-6 flex items-center justify-center text-xs shadow-md transition-colors" title="Close" aria-label="Close Assistant">
        <i class="fa-solid fa-xmark"></i>
      </button>

      <!-- Assistant Header with Live Status -->
      <div class="flex items-center gap-2 mb-2 pb-2 border-b border-slate-100">
        <span class="relative flex h-2.5 w-2.5">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
        </span>
        <div class="leading-tight">
          <div class="text-xs font-bold text-slate-900 flex items-center gap-1">
            <span>Pooja Sharma</span>
            <span class="text-[9px] bg-blue-100 text-blue-800 font-extrabold px-1.5 py-0.5 rounded">Support Desk</span>
          </div>
          <div class="text-[10px] text-slate-500">Ashutosh Build Stone Pvt. Ltd.</div>
        </div>
      </div>

      <!-- Spoken Message Text -->
      <p id="model-speech-text" class="text-xs sm:text-[13px] font-medium text-slate-700 leading-relaxed">
        "Hello! Welcome to <strong>Ashutosh Build Stone</strong>. How may I help you today? We are available live on WhatsApp for instant price rates and dispatch!"
      </p>

      <!-- Action Buttons inside Bubble -->
      <div class="mt-3 flex flex-col sm:flex-row gap-2">
        <a href="https://wa.me/917878999033?text=Hello%20Ashutosh%20Build%20Stone%20Pvt.%20Ltd.,%20I%20am%20interested%20in%20instant%20material%20quotation%20and%20rates." target="_blank" rel="noopener noreferrer" class="flex-1 bg-[#25D366] hover:bg-[#20ba59] text-white font-bold py-2 px-3 rounded-xl text-xs flex items-center justify-center gap-1.5 shadow-md transition-transform hover:scale-102">
          <i class="fa-brands fa-whatsapp text-sm"></i>
          <span>Chat on WhatsApp</span>
        </a>
        <a href="tel:7878999033" class="bg-brand-navy hover:bg-slate-800 text-amber-300 font-bold py-2 px-2.5 rounded-xl text-xs flex items-center justify-center gap-1 border border-amber-500/30 shadow-sm transition-colors whitespace-nowrap">
          <i class="fa-solid fa-phone text-[10px]"></i>
          <span>Call Plant</span>
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
    <button onclick="reopenModelSpeech()" class="flex items-center gap-2.5 bg-[#25D366] hover:bg-[#20ba59] text-white pl-2 pr-4 py-2 rounded-full shadow-xl hover:shadow-2xl transition-all duration-300 transform hover:scale-105 border-2 border-white/30 cursor-pointer">
      <div class="w-9 h-9 rounded-full overflow-hidden border border-white/60 bg-white flex-shrink-0">
        <img src="assets/images/virtual-assistant-model.png" alt="Support" class="w-full h-full object-cover">
      </div>
      <div class="flex flex-col text-left leading-tight">
        <span class="text-[9px] font-semibold text-emerald-100 uppercase tracking-wider">Live WhatsApp</span>
        <span class="text-xs font-bold whitespace-nowrap text-white">Ask Pooja (Support)</span>
      </div>
    </button>
  </div>

  <!-- Hidden Audio Element for Pre-Recorded Voice -->
  <audio id="virtual-model-audio" preload="auto">
    <source src="assets/audio/welcome-voice.wav" type="audio/wav">
  </audio>"""

WIDGET_JS = """
    // ==========================================
    // VIRTUAL ASSISTANT MODEL & AUDIO LOGIC
    // ==========================================
    let modelAudio = null;
    let hasInteracted = false;
    let isSpeaking = false;
    let modelDismissed = false;

    // Detect user interaction anywhere on page to unlock browser audio policy
    const unlockAudio = () => {
      hasInteracted = true;
      document.removeEventListener('click', unlockAudio);
      document.removeEventListener('touchstart', unlockAudio);
    };
    document.addEventListener('click', unlockAudio, { once: true });
    document.addEventListener('touchstart', unlockAudio, { once: true });

    // After 4 Seconds, slide model up and play greeting
    window.addEventListener('load', () => {
      setTimeout(() => {
        showVirtualAssistant();
      }, 4000);
    });

    function showVirtualAssistant() {
      if (modelDismissed) return;
      const widget = document.getElementById('virtual-model-widget');
      const reopenPill = document.getElementById('reopen-assistant-pill');
      if (widget) {
        widget.classList.remove('translate-y-[130%]', 'opacity-0');
        widget.classList.add('translate-y-0', 'opacity-100');
        if (reopenPill) reopenPill.classList.add('hidden');
        
        // Play Welcome Audio
        playWelcomeVoice();
      }
    }

    function playWelcomeVoice() {
      modelAudio = document.getElementById('virtual-model-audio');
      if (!modelAudio) return;

      modelAudio.currentTime = 0;
      const promise = modelAudio.play();
      
      const icon = document.getElementById('model-audio-icon');
      const txt = document.getElementById('model-audio-text');

      if (promise !== undefined) {
        promise.then(() => {
          isSpeaking = true;
          if (icon) {
            icon.className = 'fa-solid fa-volume-high text-xs text-slate-950 animate-bounce';
          }
          if (txt) txt.innerText = 'Voice Playing';
          
          modelAudio.onended = () => {
            isSpeaking = false;
            if (icon) icon.className = 'fa-solid fa-volume-high text-xs text-slate-950';
            if (txt) txt.innerText = 'Replay Voice';
          };
        }).catch(err => {
          console.log('Autoplay restriction (will play on tap):', err);
          isSpeaking = false;
          if (icon) icon.className = 'fa-solid fa-volume-xmark text-xs text-slate-950';
          if (txt) txt.innerText = 'Tap to Listen 🔊';

          // Try SpeechSynthesis fallback
          trySpeechSynthesisFallback();
        });
      }
    }

    function trySpeechSynthesisFallback() {
      if ('speechSynthesis' in window && hasInteracted) {
        const text = "Hello! Welcome to Ashutosh Build Stone. How may I help you today? We are available live on WhatsApp for instant price rates and dispatch.";
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.rate = 1.0;
        utterance.pitch = 1.1;
        const voices = window.speechSynthesis.getVoices();
        const femaleVoice = voices.find(v => v.name.includes('Female') || v.name.includes('Zira') || v.name.includes('Google UK English Female') || v.lang.includes('en-IN') || v.lang.includes('en-US'));
        if (femaleVoice) utterance.voice = femaleVoice;
        window.speechSynthesis.speak(utterance);
      }
    }

    function toggleVoiceAudio() {
      modelAudio = document.getElementById('virtual-model-audio');
      const icon = document.getElementById('model-audio-icon');
      const txt = document.getElementById('model-audio-text');

      if (modelAudio) {
        if (!modelAudio.paused && !modelAudio.ended) {
          modelAudio.pause();
          isSpeaking = false;
          if (icon) icon.className = 'fa-solid fa-volume-xmark text-xs text-slate-950';
          if (txt) txt.innerText = 'Listen Voice';
        } else {
          modelAudio.currentTime = 0;
          modelAudio.play().then(() => {
            isSpeaking = true;
            if (icon) icon.className = 'fa-solid fa-volume-high text-xs text-slate-950 animate-bounce';
            if (txt) txt.innerText = 'Playing Voice';
          }).catch(e => {
            trySpeechSynthesisFallback();
          });
        }
      }
    }

    function dismissModelAssistant() {
      modelDismissed = true;
      const widget = document.getElementById('virtual-model-widget');
      const reopenPill = document.getElementById('reopen-assistant-pill');
      if (widget) {
        widget.classList.add('translate-y-[130%]', 'opacity-0');
        widget.classList.remove('translate-y-0', 'opacity-100');
      }
      if (reopenPill) {
        reopenPill.classList.remove('hidden');
      }
      if (modelAudio && !modelAudio.paused) {
        modelAudio.pause();
      }
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
    }

    function reopenModelSpeech() {
      modelDismissed = false;
      const widget = document.getElementById('virtual-model-widget');
      const reopenPill = document.getElementById('reopen-assistant-pill');
      if (widget) {
        widget.classList.remove('translate-y-[130%]', 'opacity-0');
        widget.classList.add('translate-y-0', 'opacity-100');
      }
      if (reopenPill) {
        reopenPill.classList.add('hidden');
      }
      playWelcomeVoice();
    }
"""

with open("build_pages.py", "r", encoding="utf-8") as f:
    bp = f.read()

# Replace existing widget block in build_pages.py
widget_regex = re.compile(
    r'<!-- VIRTUAL ASSISTANT MODEL & WHATSAPP INTERACTIVE WIDGET \(APPEARS AFTER 4 SECONDS\) -->.*?<!-- Hidden Audio Element for Pre-Recorded Voice -->\s*<audio id="virtual-model-audio"[^>]*>.*?</audio>',
    re.DOTALL
)

if widget_regex.search(bp):
    bp = widget_regex.sub(WIDGET_HTML, bp)
    print("build_pages.py: Updated widget HTML with responsive layout.")

# Check JS
js_regex = re.compile(
    r'// ==========================================\s*// VIRTUAL ASSISTANT MODEL & AUDIO LOGIC.*?function reopenModelSpeech\(\) \{.*?\}\s*',
    re.DOTALL
)

if js_regex.search(bp):
    bp = js_regex.sub(WIDGET_JS, bp)
    print("build_pages.py: Updated widget JS.")

with open("build_pages.py", "w", encoding="utf-8") as f:
    f.write(bp)

print("Updated build_pages.py successfully.")
