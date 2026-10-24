/* ══════════════════════════════════════════════════════════════════
   MADHA PRINTS — Ultra-Premium Engine (Inspired by theprintguy24.com)
   ══════════════════════════════════════════════════════════════════ */

const products = [
  // Category 1: Offset Printing
  { id:'offset-letterpad', title:'Letter Pad', category:'offset', tag:'🖨️ Offset', desc:'Professional corporate letter pads and executive stationery on premium paper stocks.', img:'letterheads.jpg' },
  { id:'offset-brooches', title:'Brooches & Lapel Pins', category:'offset', tag:'🖨️ Offset / Metal', desc:'Custom printed metal lapel pins, event brooches, and badge buttons with vibrant offset colors.', img:'brooches-pins.jpg' },
  { id:'offset-vouchers', title:'Vouchers & Receipts', category:'offset', tag:'🖨️ Offset / Perforated', desc:'Custom corporate gift vouchers, payment vouchers, and discount coupon books with serial numbering.', img:'bill-books.jpg' },
  { id:'offset-billbooks', title:'All Bill Books', category:'offset', tag:'⭐ Essential', desc:'GST tax invoices, delivery challans, estimate books, and day books with carbonless copies.', img:'bill-books.jpg' },
  { id:'offset-envelopes', title:'Envelop Cover Printing', category:'offset', tag:'🖨️ Stationery', desc:'Standard and custom-sized business envelope printing with window and peel-and-seal gumming.', img:'envelopes.jpg' },
  { id:'offset-invitations', title:'All Invitations', category:'offset', tag:'👑 Luxury', desc:'Wedding invitations, corporate celebration invites, and ceremony cards with offset detailing.', img:'invitations.jpg' },

  // Category 2: Screen Printing
  { id:'screen-bags', title:'Bag Printing', category:'screen', tag:'🎨 Screen Print', desc:'Custom screen-printed carry bags, tote bags, and shopping bags with bold, long-lasting prints.', img:'printed-bags.jpg' },
  { id:'screen-invitations', title:'Screen Printed Invitations', category:'screen', tag:'🎨 Handcrafted', desc:'Invitations screen-printed with metallic inks, textured finishes, and traditional aesthetics.', img:'invitations.jpg' },

  // Category 3: Digital Printing
  { id:'digital-visiting-cards', title:'Visiting Cards', category:'digital', tag:'⭐ Bestseller', desc:'Premium business visiting cards on 350+ GSM art card, matte velvet lamination, and spot UV.', img:'business-cards.jpg' },
  { id:'digital-foil-cards', title:'Gold & Silver Foil Visiting Cards', category:'digital', tag:'✨ Luxury Foil', desc:'Metallic gold and silver foil stamped business cards with tactile embossed detailing.', img:'foil-visiting-cards.jpg' },

  // Category: Stamps & Seals (Featured)
  { id:'stamp-normal', title:'Normal Rubber Stamp', category:'stamps', tag:'🔖 Classic Seal', desc:'Custom wooden handle rubber stamps with sharp vulcanized text for official seals, signatures, and addresses.', img:'normal-stamp.jpg' },
  { id:'stamp-self-ink', title:'Self Inking Stamp', category:'stamps', tag:'⭐ Automatic Ink', desc:'High-speed self-inking stamps with built-in ink pad, leakproof casing, and crisp impressions in blue, black, or red.', img:'self-ink-stamp.jpg' },

  { id:'digital-invitations', title:'Digital Invitations', category:'digital', tag:'⚡ Express', desc:'Express digital color invitation printing for urgent parties, weddings, and corporate meetups.', img:'invitations.jpg' },
  { id:'digital-letterpad', title:'Digital Letter Pad', category:'digital', tag:'⚡ Digital', desc:'Short-run on-demand digital letterhead and memo pad printing with sharp color consistency.', img:'letterheads.jpg' },
  { id:'digital-brooches', title:'Digital Brooches', category:'digital', tag:'📌 Badges', desc:'High-resolution full-color digitally printed brooches and pin badges with glossy protective finish.', img:'brooches-pins.jpg' },
  { id:'digital-id-cards', title:'ID Card', category:'digital', tag:'🪪 High Security', desc:'Corporate employee and student ID cards with high-definition photo, barcodes, and QR codes.', img:'id-cards.jpg' },
  { id:'digital-lanyards', title:'ID Card Rope Printing', category:'digital', tag:'🎀 Branded', desc:'Custom printed satin and polyester neck lanyards/ropes with company logo and swivel hooks.', img:'lanyard-rope.jpg' },
  { id:'digital-pvc-cards', title:'PVC Cards', category:'digital', tag:'💎 Smart Plastic', desc:'Heavy-duty PVC plastic cards for privilege clubs, loyalty rewards, gym passes, and RFID cards.', img:'pvc-cards.jpg' },
  { id:'digital-metallic-stickers', title:'Sticker Sheet Printing (Gold, Silver, Transparent)', category:'digital', tag:'🏷️ Waterproof', desc:'Premium metallic gold, silver chrome, and clear transparent waterproof vinyl sticker sheets.', img:'metallic-stickers.jpg' },

  // Category 4: Sublimation Printing
  { id:'sublimation-mug', title:'(Personalised) Mug', category:'sublimation', tag:'🔥 Personalized', desc:'Custom ceramic photo mugs, magic heat-reveal mugs, two-tone mugs, and corporate drinkware.', img:'mug-printing.jpg' },
  { id:'sublimation-keychain', title:'Key Chain', category:'sublimation', tag:'🔑 Custom Shapes', desc:'Personalized sublimation printed key chains in metal, acrylic, and MDF with dual-sided photos.', img:'keychains.jpg' },
  { id:'sublimation-tshirt', title:'T.Shirt (Sublimation / DTF Printing)', category:'sublimation', tag:'👕 Trending', desc:'Vibrant full-color sublimation and DTF printed round-neck and polo t-shirts for teams and events.', img:'tshirt-printing.jpg' },
  { id:'sublimation-flags', title:'Flags', category:'sublimation', tag:'🚩 Corporate', desc:'Custom printed corporate desk table flags with chrome stands and outdoor feather flags.', img:'flags.jpg' },
  { id:'sublimation-pillow', title:'Pillow', category:'sublimation', tag:'🛋️ Keepsake', desc:'Personalized photo cushions, memory pillows, and custom home decor cushion covers.', img:'pillow-cover.jpg' },
  { id:'sublimation-id-400', title:'ID Card 400 GSM', category:'sublimation', tag:'🪪 Heavy Duty', desc:'Ultra-stout 400 GSM heavy-duty laminated sublimation ID cards offering superior rigidity.', img:'pvc-cards.jpg' },

  // Category 5: Sticker Digital Cutting
  { id:'digital-sticker-cutting', title:'Sticker Digital Cutting (Customized 13x19)', category:'digital', tag:'✂️ Plotter 13×19', desc:'Precision computerized plotter die-cutting on 13×19 sticker sheets in any custom shape.', img:'sticker-cutting.jpg' },

  // Category 6: Photo Print
  { id:'photo-passport', title:'Pass Port Size Photo', category:'photo', tag:'📸 6 Colour Studio', desc:'Express biometric passport size, visa size, and stamp size photo prints with studio lighting.', img:'passport-photos.jpg' },
  { id:'photo-frames', title:'Photo Frame – All Size', category:'photo', tag:'🖼️ All Sizes', desc:'Premium wooden and acrylic photo frames in all standard and custom dimensions with 6-colour prints.', img:'photo-frames.jpg' },

  // Category 7: Banner Printing & Signage
  { id:'banner-flex', title:'Banner Printing', category:'signage', tag:'🪧 Large Format', desc:'Heavy-duty outdoor flex banner printing for storefront promotions, road shows, and events.', img:'flex-printing.jpg' },
  { id:'banner-backlight', title:'Back Light & Front Light', category:'signage', tag:'💡 Illuminated', desc:'Backlit flex for glow sign boxes and opaque frontlit flex banners for illuminated shop fascias.', img:'backlight-boards.jpg' },
  { id:'banner-led', title:'LED Boards', category:'signage', tag:'💡 3D Acrylic', desc:'Bright acrylic 3D LED channel letters, programmable LED moving message displays, and neon signs.', img:'led-boards.jpg' },
  { id:'banner-standee', title:'Standing Board', category:'signage', tag:'🧍 Roll-up Standee', desc:'Portable aluminum roll-up standees, easel display boards, and outdoor standing signage.', img:'standing-boards.jpg' },
  { id:'banner-foamboard', title:'Foam Board printing', category:'signage', tag:'🪟 Sunboard', desc:'Direct printed lightweight rigid foam board (sunboard) for exhibition booths and menu boards.', img:'foam-board.jpg' },
  { id:'banner-uv', title:'UV Printing', category:'signage', tag:'🔮 Flatbed Direct', desc:'Flatbed UV direct ink printing on acrylic, ceramic tiles, wood, glass, metal, and composite sheets.', img:'uv-printing.jpg' },

  // Category 8: Binding
  { id:'binding-spiral', title:'Spiral Binding', category:'binding', tag:'🔗 Wire-O', desc:'Flexible plastic spiral and metal wire-o coil binding with transparent acetate protective covers.', img:'spiral-binding.jpg' },
  { id:'binding-soft', title:'Soft Binding', category:'binding', tag:'📕 Perfect Bound', desc:'Clean, professional thermal soft cover binding for manuals, company portfolios, and reports.', img:'soft-binding.jpg' },
  { id:'binding-hard', title:'Hard Binding', category:'binding', tag:'📗 Gold Embossed', desc:'Deluxe rexine hardcover book binding with embossed gold foil lettering on face and spine.', img:'hard-binding.jpg' },
  { id:'binding-project', title:'Project Binding', category:'binding', tag:'📚 College Viva', desc:'Student project report and degree thesis binding strictly meeting university standards.', img:'project-binding.jpg' },

  // Category 9: Designing
  { id:'designing-studio', title:'Designing', category:'designing', tag:'🎨 Creative Studio', desc:'Professional graphic designing for logos, business cards, banners, invitations, and packaging.', img:'graphic-design.jpg' },
];


const typingKeywords = [
  "Normal Rubber Stamps",
  "Self Inking Stamps",
  "Offset Printing",
  "Visiting cards",
  "Gold & Silver Foil Cards",
  "All Bill Books & Receipts",
  "Screen Bag Printing",
  "Custom Mug Printing",
  "T-Shirt Sublimation & DTF",
  "Sticker Digital Cutting 13x19",
  "Passport Size Photos",
  "Photo Frames All Sizes",
  "LED Boards & Backlight",
  "Roll-up Standing Boards",
  "UV Printing on Acrylic & Wood",
  "Thesis & Project Binding",
  "ID Card Rope Printing",
  "Graphic Designing"
];

document.addEventListener('DOMContentLoaded', () => {

  /* ═══ 1. ANIMATED TYPING SEARCH PLACEHOLDER ═══ */
  const typingEl = document.getElementById('typing-text');
  const searchInput = document.getElementById('search-input');
  const searchDropdown = document.getElementById('search-dropdown');
  let wordIdx = 0, charIdx = 0, isDeleting = false;

  function typeEffect() {
    if (!typingEl) return;
    const currentWord = typingKeywords[wordIdx];
    if (isDeleting) {
      typingEl.textContent = currentWord.substring(0, charIdx - 1);
      charIdx--;
    } else {
      typingEl.textContent = currentWord.substring(0, charIdx + 1);
      charIdx++;
    }

    let delay = isDeleting ? 60 : 120;
    if (!isDeleting && charIdx === currentWord.length) {
      delay = 2000;
      isDeleting = true;
    } else if (isDeleting && charIdx === 0) {
      isDeleting = false;
      wordIdx = (wordIdx + 1) % typingKeywords.length;
      delay = 400;
    }
    setTimeout(typeEffect, delay);
  }
  typeEffect();

  /* Search Input Filter & Dropdown */
  if (searchInput && searchDropdown) {
    searchInput.addEventListener('input', e => {
      const q = e.target.value.toLowerCase().trim();
      if (!q) {
        searchDropdown.classList.remove('active');
        return;
      }
      const matches = products.filter(p => p.title.toLowerCase().includes(q) || p.desc.toLowerCase().includes(q));
      if (matches.length > 0) {
        searchDropdown.innerHTML = matches.map(p => `
          <div class="search-item" data-title="${p.title}">
            <img src="${p.img}" alt="${p.title}" />
            <div class="search-item-info">
              <h5>${p.title}</h5>
              <p>${p.tag} • ${p.desc.substring(0, 45)}...</p>
            </div>
          </div>
        `).join('');
        searchDropdown.classList.add('active');

        searchDropdown.querySelectorAll('.search-item').forEach(item => {
          item.addEventListener('click', () => {
            const t = item.dataset.title;
            const modalReq = document.getElementById('modal-requirement');
            if (modalReq) modalReq.value = `Inquiry for ${t}`;
            document.getElementById('quote-modal')?.classList.add('active');
            searchDropdown.classList.remove('active');
          });
        });
      } else {
        searchDropdown.innerHTML = '<div style="padding:16px;text-align:center;color:#64748b;font-size:0.9rem;">No matching print services found.</div>';
        searchDropdown.classList.add('active');
      }
    });

    document.addEventListener('click', e => {
      if (!e.target.closest('.header-search-container')) {
        searchDropdown.classList.remove('active');
      }
    });
  }


  /* ═══ 3. RENDER PRODUCTS GRID & MARQUEE ═══ */
  const productsGrid = document.getElementById('products-grid');
  const featuredSlider = document.getElementById('featured-slider');
  const featuredSliderDup = document.getElementById('featured-slider-dup');

  function renderProducts(filter = 'all') {
    let filtered = products;
    if (filter === 'bestseller') filtered = products.filter(p => p.tag.includes('Bestseller') || p.tag.includes('Essential') || p.tag.includes('Luxury') || p.category === 'stamps');
    else if (filter !== 'all') filtered = products.filter(p => p.category === filter);

    // Update Products Grid
    if (productsGrid) {
      productsGrid.style.opacity = '1';
      productsGrid.style.transform = 'none';
      productsGrid.innerHTML = filtered.map(p => `
        <div class="product-card visible" data-id="${p.id}">
          <div class="product-card-image">
            <img src="${p.img}" alt="${p.title}" decoding="async" width="600" height="400" />
            <span class="product-tag">${p.tag}</span>
            <div class="card-shine"></div>
          </div>
          <div class="product-card-body">
            <h3 class="product-card-title">${p.title}</h3>
            <p class="product-card-desc">${p.desc}</p>
            <button class="btn btn-outline-dark quick-quote-trigger" data-title="${p.title}">
              💬 Get Instant Quote
            </button>
          </div>
        </div>
      `).join('');
      attachModalTriggers();
    }

    // Update Marquee Banner Cards
    const cardHTML = filtered.map(p => `
      <div class="featured-card">
        <div class="featured-card-img">
          <img src="${p.img}" alt="${p.title}" decoding="async" width="600" height="400" />
          <span class="featured-badge">${p.tag}</span>
        </div>
        <div class="featured-card-content">
          <h4>${p.title}</h4>
          <p>${p.desc}</p>
          <button class="btn btn-outline-dark quick-quote-trigger" data-title="${p.title}" style="padding:6px 14px;font-size:0.8rem;width:100%;">Enquire Now →</button>
        </div>
      </div>
    `).join('');

    if (featuredSlider) featuredSlider.innerHTML = cardHTML;
    if (featuredSliderDup) featuredSliderDup.innerHTML = cardHTML;
  }
  renderProducts('all');

  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderProducts(btn.dataset.filter);
    });
  });

  /* ═══ 4. INSTANT QUOTE CALCULATOR ═══ */
  const calcProd = document.getElementById('calc-product');
  const calcQty = document.getElementById('calc-quantity');
  const calcFinish = document.getElementById('calc-finish');
  const calcBtn = document.getElementById('calc-whatsapp-btn');

  function updateCalcUrl() {
    if (!calcBtn) return;
    const p = calcProd ? calcProd.value : 'Business Cards';
    const q = calcQty ? calcQty.value : '500 Units';
    const f = calcFinish ? calcFinish.value : 'Matte Lamination';
    const msg = `Hi Madha Prints, I want a quotation for ${p}, Quantity: ${q}, Finish: ${f}. Please guide me with pricing.`;
    calcBtn.href = `https://wa.me/919790779720?text=${encodeURIComponent(msg)}`;
  }
  if (calcProd) calcProd.addEventListener('change', updateCalcUrl);
  if (calcQty) calcQty.addEventListener('change', updateCalcUrl);
  if (calcFinish) calcFinish.addEventListener('change', updateCalcUrl);
  updateCalcUrl();

  /* ═══ 5. MODAL HANDLERS ═══ */
  const quoteModal = document.getElementById('quote-modal');
  const quoteClose = document.getElementById('modal-close-btn');
  const quoteForm = document.getElementById('modal-quote-form');
  const modalReq = document.getElementById('modal-requirement');

  function attachModalTriggers() {
    document.querySelectorAll('.quick-quote-trigger').forEach(btn => {
      btn.addEventListener('click', e => {
        e.preventDefault();
        const title = btn.dataset.title;
        if (title && modalReq) modalReq.value = `Quotation request for ${title}`;
        quoteModal?.classList.add('active');
      });
    });
  }

  if (quoteClose && quoteModal) {
    quoteClose.addEventListener('click', () => quoteModal.classList.remove('active'));
    quoteModal.addEventListener('click', e => { if (e.target === quoteModal) quoteModal.classList.remove('active'); });
  }

  if (quoteForm) {
    quoteForm.addEventListener('submit', e => {
      e.preventDefault();
      const n = document.getElementById('modal-name')?.value || '';
      const p = document.getElementById('modal-phone')?.value || '';
      const r = modalReq?.value || '';
      const text = `Hi Madha Prints, my name is ${n} (${p}). I need a quote for: ${r}.`;
      window.open(`https://wa.me/919790779720?text=${encodeURIComponent(text)}`, '_blank');
      quoteModal?.classList.remove('active');
    });
  }

  /* Account Modal Handler */
  const accModal = document.getElementById('account-modal');
  const accTrigger = document.getElementById('account-modal-trigger');
  const accClose = document.getElementById('account-modal-close');

  if (accTrigger && accModal) {
    accTrigger.addEventListener('click', () => accModal.classList.add('active'));
  }
  if (accClose && accModal) {
    accClose.addEventListener('click', () => accModal.classList.remove('active'));
    accModal.addEventListener('click', e => { if (e.target === accModal) accModal.classList.remove('active'); });
  }

  /* Account Modal Tabs */
  document.querySelectorAll('.modal-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      document.querySelectorAll('.modal-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.modal-tab-content').forEach(c => c.classList.remove('active'));
      tab.classList.add('active');
      const targetId = `tab-${tab.dataset.tab}`;
      document.getElementById(targetId)?.classList.add('active');
    });
  });

  /* ═══ 6. BEFORE / AFTER COMPARISON SLIDER & SAMPLE SWITCHER ═══ */
  const comp = document.getElementById('comparison');
  const compBefore = document.getElementById('comparison-before');
  const compSlider = document.getElementById('comparison-slider');
  const compImgBefore = document.getElementById('comp-img-before');
  const compImgAfter = document.getElementById('comp-img-after');

  if (comp && compBefore && compSlider) {
    let dragging = false;
    const setPercent = p => {
      p = Math.max(0.05, Math.min(0.95, p));
      compBefore.style.width = (p * 100) + '%';
      compSlider.style.left = (p * 100) + '%';
    };
    const update = x => {
      const r = comp.getBoundingClientRect();
      setPercent((x - r.left) / r.width);
    };

    comp.addEventListener('mousedown', e => { dragging = true; update(e.clientX); });
    window.addEventListener('mouseup', () => dragging = false);
    comp.addEventListener('mousemove', e => { if (dragging) update(e.clientX); });
    comp.addEventListener('touchstart', () => dragging = true);
    window.addEventListener('touchend', () => dragging = false);
    comp.addEventListener('touchmove', e => { if (dragging && e.touches[0]) update(e.touches[0].clientX); });

    // Comparison Presets Buttons (10%, 50%, 90%)
    document.querySelectorAll('.comp-preset-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.comp-preset-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const pos = parseFloat(btn.dataset.pos || '50') / 100;
        setPercent(pos);
      });
    });

    // Sample Product Switcher
    document.querySelectorAll('.sample-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.sample-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const beforeImg = btn.dataset.before;
        const afterImg = btn.dataset.after;
        if (beforeImg && compImgBefore) compImgBefore.src = beforeImg;
        if (afterImg && compImgAfter) compImgAfter.src = afterImg;
      });
    });
  }

  /* ═══ 7. SCROLL REVEAL OBSERVER ═══ */
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) entry.target.classList.add('visible');
    });
  }, { threshold: 0.08 });
  document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .stagger-children').forEach(el => revealObserver.observe(el));

  /* ═══ 8. SCROLL PROGRESS & BACK TO TOP ═══ */
  const progressBar = document.getElementById('scroll-progress');
  const btt = document.getElementById('back-to-top');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const h = document.documentElement.scrollHeight - window.innerHeight;
    if (progressBar) progressBar.style.width = ((scrollY / h) * 100) + '%';
  }, { passive: true });

  if (btt) btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ═══ 9. MOBILE MENU DRAWER & BACKDROP OVERLAY ═══ */
  const mobileMenuBtns = document.querySelectorAll('.mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileOverlay = document.getElementById('mobile-menu-overlay');
  const mobileClose = document.getElementById('mobile-menu-close');

  function openMobileMenu() {
    mobileMenu?.classList.add('active');
    mobileOverlay?.classList.add('active');
    mobileMenuBtns.forEach(b => b.classList.add('active'));
    document.body.classList.add('menu-open');
  }

  function closeMobileMenu() {
    mobileMenu?.classList.remove('active');
    mobileOverlay?.classList.remove('active');
    mobileMenuBtns.forEach(b => b.classList.remove('active'));
    document.body.classList.remove('menu-open');
  }

  mobileMenuBtns.forEach(btn => {
    btn.addEventListener('click', e => {
      e.stopPropagation();
      if (mobileMenu?.classList.contains('active')) closeMobileMenu();
      else openMobileMenu();
    });
  });

  if (mobileClose) mobileClose.addEventListener('click', closeMobileMenu);
  if (mobileOverlay) mobileOverlay.addEventListener('click', closeMobileMenu);
  document.querySelectorAll('.mobile-menu a').forEach(l => l.addEventListener('click', closeMobileMenu));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMobileMenu(); });

  /* ═══ 10. MOBILE DRAWER QUICK SEARCH ═══ */
  const drawerSearchInput = document.getElementById('mobile-drawer-search');
  const drawerSearchResults = document.getElementById('mobile-search-results');
  if (drawerSearchInput && drawerSearchResults) {
    drawerSearchInput.addEventListener('input', e => {
      const q = e.target.value.toLowerCase().trim();
      if (!q) {
        drawerSearchResults.innerHTML = '';
        drawerSearchResults.classList.remove('active');
        return;
      }
      const matches = products.filter(p => p.title.toLowerCase().includes(q) || p.desc.toLowerCase().includes(q));
      if (matches.length > 0) {
        drawerSearchResults.innerHTML = matches.slice(0, 6).map(p => `
          <div class="mobile-search-item" data-title="${p.title}">
            <img src="${p.img}" alt="${p.title}" />
            <div class="mobile-search-meta">
              <h6>${p.title}</h6>
              <span>${p.tag}</span>
            </div>
            <a href="https://wa.me/919790779720?text=${encodeURIComponent('Hi Madha Prints, I want a quote for ' + p.title)}" target="_blank" class="mobile-search-wa-btn">💬 Quote</a>
          </div>
        `).join('');
        drawerSearchResults.classList.add('active');
      } else {
        drawerSearchResults.innerHTML = '<div class="mobile-search-empty">No matching products found.</div>';
        drawerSearchResults.classList.add('active');
      }
    });
  }

  /* ═══ 11. HERO HOTSPOTS TOUCH & TAP SUPPORT ═══ */
  const hotspots = document.querySelectorAll('.hero-hotspot');
  if (hotspots.length) {
    hotspots.forEach(spot => {
      spot.addEventListener('click', e => {
        if (e.target.closest('.popover-cta')) return;
        e.stopPropagation();
        const isActive = spot.classList.contains('active');
        hotspots.forEach(s => s.classList.remove('active'));
        if (!isActive) spot.classList.add('active');
      });
    });
    document.addEventListener('click', () => {
      hotspots.forEach(s => s.classList.remove('active'));
    });
  }

  /* ═══ 12. DOCK QUICK QUOTE TRIGGER ═══ */
  const dockQuoteTrigger = document.getElementById('dock-quote-trigger');
  if (dockQuoteTrigger) {
    dockQuoteTrigger.addEventListener('click', e => {
      e.preventDefault();
      const modalReq = document.getElementById('modal-requirement');
      if (modalReq) modalReq.value = 'General Instant Print Quotation Request';
      document.getElementById('quote-modal')?.classList.add('active');
    });
  }

  /* ═══ 13. COPY BUTTONS FEEDBACK ═══ */
  document.querySelectorAll('[data-copy]').forEach(btn => {
    btn.addEventListener('click', () => {
      const text = btn.dataset.copy;
      if (navigator.clipboard && text) {
        navigator.clipboard.writeText(text).then(() => {
          const original = btn.innerHTML;
          btn.innerHTML = '✓ Copied!';
          btn.classList.add('copied');
          setTimeout(() => {
            btn.innerHTML = original;
            btn.classList.remove('copied');
          }, 2000);
        });
      }
    });
  });

  const btnCopyAddress = document.getElementById('btn-copy-contact-address');
  if (btnCopyAddress) {
    btnCopyAddress.addEventListener('click', () => {
      const address = "No: 4/353, 4th Street, Dr. Puratchi Thalaivi Main Road, MGR Nagar, Kottivakkam, Chennai – 600 041. (Near SRP Tools)";
      if (navigator.clipboard) {
        navigator.clipboard.writeText(address).then(() => {
          const orig = btnCopyAddress.innerText;
          btnCopyAddress.innerText = '✓ Copied Address!';
          setTimeout(() => btnCopyAddress.innerText = orig, 2000);
        });
      }
    });
  }
});
