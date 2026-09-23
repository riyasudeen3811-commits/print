import os

js_content = """/* ══════════════════════════════════════════════════════════════════
   ADHA PRINTS — Ultra-Premium Engine (Inspired by theprintguy24.com)
   ══════════════════════════════════════════════════════════════════ */

const products = [
  { id:'business-cards', title:'Business Cards (Visiting Cards)', category:'corporate', tag:'⭐ Bestseller', desc:'Art, Matte, Velvet Soft Touch, Gold Foil Stamping, Spot UV & Metallic cards.', img:'/business-cards.jpg' },
  { id:'letterheads', title:'Letterheads & Envelopes', category:'corporate', tag:'Corporate', desc:'Executive letterheads & branded envelopes on 100 GSM sunshine paper stock.', img:'/letterheads.jpg' },
  { id:'brochures', title:'Brochures & Catalogs', category:'marketing', tag:'🔥 Popular', desc:'Bi-fold, tri-fold & multi-page brochures with vibrant CMYK color fidelity.', img:'/brochures.jpg' },
  { id:'flyers', title:'Flyers & Pamphlets', category:'marketing', tag:'⚡ 24h Express', desc:'Promotional flyers, leaflets & handbills for corporate events & marketing.', img:'/flyers.jpg' },
  { id:'invitations', title:'Invitations & Greeting Cards', category:'events', tag:'Specialty', desc:'Wedding cards, event invitations & greeting cards with foil embossing.', img:'/invitations.jpg' },
  { id:'stickers', title:'Custom Stickers & Labels', category:'events', tag:'Waterproof', desc:'Art paper, Glossy, Synthetic, Waterproof Vinyl & Die-Cut product labels.', img:'/stickers.jpg' },
  { id:'id-cards', title:'ID Cards & Lanyards', category:'corporate', tag:'High Security', desc:'PVC employee ID cards, student badges & custom printed satin lanyards.', img:'/id-cards.jpg' },
  { id:'offset-printing', title:'Offset & Flex Signage', category:'custom', tag:'Bulk Master', desc:'Large-format flex banners, star flex, standees & offset commercial printing.', img:'/offset-printing.jpg' },
  { id:'binding', title:'Book & Thesis Binding', category:'custom', tag:'Professional', desc:'Spiral, wire-o, softcover & hardcover thesis book binding with golden foil text.', img:'/binding.jpg' }
];

const popularCategories = [
  { title:'Visiting Cards', desc:'Art, Matte, Velvet, Spot UV & Metallic Foil', count:'12+ Options', img:'/business-cards.jpg', filter:'corporate' },
  { title:'Stickers & Labels', desc:'Waterproof Vinyl, Synthetic & Die-Cut', count:'10+ Options', img:'/stickers.jpg', filter:'events' },
  { title:'Brochures & Flyers', desc:'Bi-fold, Tri-fold & Promotional Leaflets', count:'8+ Options', img:'/brochures.jpg', filter:'marketing' },
  { title:'Flex & Signage', desc:'Star Flex, Standees & Foam Board', count:'6+ Options', img:'/offset-printing.jpg', filter:'custom' },
  { title:'ID Cards & Lanyards', desc:'PVC Cards & Custom Satin Lanyards', count:'5+ Options', img:'/id-cards.jpg', filter:'corporate' },
  { title:'Thesis Book Binding', desc:'Hardcover, Softcover & Golden Foil Text', count:'7+ Options', img:'/binding.jpg', filter:'custom' }
];

const typingKeywords = [
  "Visiting cards",
  "Custom Stickers",
  "Brochures & Pamphlets",
  "PVC ID Cards",
  "Flex Banners",
  "Thesis Book Binding",
  "Letterheads & Envelopes"
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

  /* ═══ 2. RENDER POPULAR CATEGORIES CAROUSEL ═══ */
  const popCatGrid = document.getElementById('popular-categories-grid');
  if (popCatGrid) {
    popCatGrid.innerHTML = popularCategories.map(c => `
      <div class="category-card">
        <div class="category-card-img">
          <img src="${c.img}" alt="${c.title}" loading="lazy" decoding="async" />
          <span class="category-badge">${c.count}</span>
        </div>
        <div class="category-card-body">
          <h3 class="category-title">${c.title}</h3>
          <p class="category-desc">${c.desc}</p>
          <a href="#cards" class="btn btn-outline-dark category-explore" data-filter="${c.filter}">View Options →</a>
        </div>
      </div>
    `).join('');

    popCatGrid.querySelectorAll('.category-explore').forEach(btn => {
      btn.addEventListener('click', e => {
        const filter = btn.dataset.filter;
        if (filter) renderProducts(filter);
      });
    });
  }

  /* ═══ 3. RENDER PRODUCTS GRID & FILTERS ═══ */
  const productsGrid = document.getElementById('products-grid');
  function renderProducts(filter = 'all') {
    if (!productsGrid) return;
    let filtered = products;
    if (filter === 'bestseller') filtered = products.filter(p => p.tag.includes('Bestseller') || p.tag.includes('Popular'));
    else if (filter !== 'all') filtered = products.filter(p => p.category === filter);

    productsGrid.style.opacity = '0';
    productsGrid.style.transform = 'translateY(15px)';
    setTimeout(() => {
      productsGrid.innerHTML = filtered.map(p => `
        <div class="product-card" data-id="${p.id}">
          <div class="product-card-image">
            <img src="${p.img}" alt="${p.title}" loading="lazy" decoding="async" />
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
      productsGrid.style.opacity = '1';
      productsGrid.style.transform = 'translateY(0)';
      attachModalTriggers();
    }, 200);
  }
  renderProducts('all');

  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderProducts(btn.dataset.filter);
    });
  });

  /* ═══ 4. MARQUEE BANNER POPULATE ═══ */
  const featuredSlider = document.getElementById('featured-slider');
  const featuredSliderDup = document.getElementById('featured-slider-dup');
  const cardHTML = products.map(p => `
    <div class="featured-card">
      <div class="featured-card-img">
        <img src="${p.img}" alt="${p.title}" loading="lazy" decoding="async" />
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

  /* ═══ 5. INSTANT QUOTE CALCULATOR ═══ */
  const calcProd = document.getElementById('calc-product');
  const calcQty = document.getElementById('calc-quantity');
  const calcFinish = document.getElementById('calc-finish');
  const calcBtn = document.getElementById('calc-whatsapp-btn');

  function updateCalcUrl() {
    if (!calcBtn) return;
    const p = calcProd ? calcProd.value : 'Business Cards';
    const q = calcQty ? calcQty.value : '500 Units';
    const f = calcFinish ? calcFinish.value : 'Matte Lamination';
    const msg = `Hi Adha Prints, I want a quotation for ${p}, Quantity: ${q}, Finish: ${f}. Please guide me with pricing.`;
    calcBtn.href = `https://wa.me/919790779720?text=${encodeURIComponent(msg)}`;
  }
  if (calcProd) calcProd.addEventListener('change', updateCalcUrl);
  if (calcQty) calcQty.addEventListener('change', updateCalcUrl);
  if (calcFinish) calcFinish.addEventListener('change', updateCalcUrl);
  updateCalcUrl();

  /* ═══ 6. MODAL HANDLERS ═══ */
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
      const text = `Hi Adha Prints, my name is ${n} (${p}). I need a quote for: ${r}.`;
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

  /* ═══ 7. BEFORE / AFTER COMPARISON SLIDER ═══ */
  const comp = document.getElementById('comparison');
  const compBefore = document.getElementById('comparison-before');
  const compSlider = document.getElementById('comparison-slider');
  if (comp && compBefore && compSlider) {
    let dragging = false;
    const update = x => {
      const r = comp.getBoundingClientRect();
      let p = (x - r.left) / r.width;
      p = Math.max(0.05, Math.min(0.95, p));
      compBefore.style.width = (p * 100) + '%';
      compSlider.style.left = (p * 100) + '%';
    };
    comp.addEventListener('mousedown', e => { dragging = true; update(e.clientX); });
    window.addEventListener('mouseup', () => dragging = false);
    comp.addEventListener('mousemove', e => { if (dragging) update(e.clientX); });
    comp.addEventListener('touchstart', () => dragging = true);
    window.addEventListener('touchend', () => dragging = false);
    comp.addEventListener('touchmove', e => { if (dragging && e.touches[0]) update(e.touches[0].clientX); });
  }

  /* ═══ 8. SCROLL REVEAL OBSERVER ═══ */
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) entry.target.classList.add('visible');
    });
  }, { threshold: 0.08 });
  document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .stagger-children').forEach(el => revealObserver.observe(el));

  /* ═══ 9. SCROLL PROGRESS & BACK TO TOP ═══ */
  const progressBar = document.getElementById('scroll-progress');
  const btt = document.getElementById('back-to-top');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const h = document.documentElement.scrollHeight - window.innerHeight;
    if (progressBar) progressBar.style.width = ((scrollY / h) * 100) + '%';
  }, { passive: true });

  if (btt) btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ═══ 10. MOBILE MENU ═══ */
  const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('active');
    });
    mobileMenu.querySelectorAll('a').forEach(l => l.addEventListener('click', () => mobileMenu.classList.remove('active')));
  }
});
"""

with open("/Users/riyasudeen/Documents/clien web/xerox/src/main.js", "w") as f:
    f.write(js_content)

print("Updated src/main.js successfully")
