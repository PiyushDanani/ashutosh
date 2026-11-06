
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

      const text = `*Instant Quote Request - Ashutosh Build Stone Pvt. Ltd.*\n\n*Name:* ${name}\n*Phone:* ${phone}\n*Material:* ${mat}\n*Quantity:* ${qty}\n*Site Location:* ${loc}\n\nPlease share price quote.`;
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
  