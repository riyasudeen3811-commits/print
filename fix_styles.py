import os

css_content = """/* ══════════════════════════════════════════════════════════════════
   ADHA PRINTS — Inspired by theprintguy24.com (Ultra-Premium Theme)
   ══════════════════════════════════════════════════════════════════ */

:root {
  --primary: #2563eb;
  --primary-hover: #1d4ed8;
  --primary-dark: #1e3a8a;
  --secondary: #0d9488;
  --accent: #f59e0b;
  --whatsapp: #25D366;
  --whatsapp-dark: #128C7E;
  
  --bg-dark: #0f172a;
  --bg-card-dark: #1e293b;
  --bg-light: #f8fafc;
  --bg-white: #ffffff;
  
  --text-dark: #0f172a;
  --text-muted: #64748b;
  --text-light: #94a3b8;
  --text-white: #ffffff;
  
  --border-light: #e2e8f0;
  --border-dark: #334155;
  
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 24px;
  --radius-full: 9999px;
  
  --shadow-sm: 0 2px 8px rgba(0,0,0,0.04);
  --shadow-md: 0 10px 30px rgba(0,0,0,0.08);
  --shadow-lg: 0 20px 50px rgba(0,0,0,0.15);
  
  --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  color: var(--text-dark);
  background-color: #ffffff;
  -webkit-font-smoothing: antialiased;
}

body {
  overflow-x: hidden;
  position: relative;
  line-height: 1.6;
}

a {
  color: inherit;
  text-decoration: none;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

.container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 24px;
}

.section-padding {
  padding: 80px 0;
}

h1, h2, h3, h4, h5, h6 {
  font-family: 'Outfit', sans-serif;
  font-weight: 700;
  color: var(--text-dark);
  line-height: 1.25;
}

.section-title {
  font-size: clamp(2rem, 3.8vw, 2.75rem);
  letter-spacing: -0.02em;
  margin-bottom: 12px;
}

.section-subtitle {
  font-size: clamp(1rem, 1.4vw, 1.15rem);
  color: var(--text-muted);
  max-width: 680px;
  margin: 0 auto 40px;
}

.text-center { text-align: center; }

.accent-line {
  width: 48px;
  height: 4px;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  border-radius: 4px;
  margin: 0 auto 16px;
}

/* Scroll Progress Bar */
.scroll-progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: linear-gradient(90deg, #2563eb, #0d9488, #f59e0b);
  z-index: 9999;
  width: 0%;
  transition: width 0.1s ease-out;
}

/* ═══ TOP ANNOUNCEMENT BAR ═══ */
.top-announcement-bar {
  background: #0f172a;
  color: #f8fafc;
  font-size: 0.85rem;
  padding: 8px 0;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.top-announcement-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}

.highlight-code {
  background: linear-gradient(135deg, #f59e0b, #ef4444);
  color: #fff;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
}

.top-announcement-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.top-link {
  color: #94a3b8;
  transition: var(--transition);
}

.top-link:hover { color: #fff; }
.whatsapp-top { color: var(--whatsapp); font-weight: 600; }
.sep { color: #334155; }

/* ═══ MAIN HEADER & SEARCH BAR ═══ */
.site-header {
  position: sticky;
  top: 0;
  background: #ffffff;
  z-index: 1000;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
  transition: var(--transition);
}

.header-main {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 16px 24px;
}

.site-logo {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-mark {
  width: 44px;
  height: 44px;
  background: linear-gradient(135deg, #2563eb, #0d9488);
  color: #fff;
  font-weight: 900;
  font-size: 1.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(37,99,235,0.3);
}

.logo-text-group {
  display: flex;
  flex-direction: column;
}

.brand-name {
  font-family: 'Outfit', sans-serif;
  font-size: 1.45rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #0f172a;
}

.brand-accent { color: var(--primary); }

.brand-sub {
  font-size: 0.72rem;
  color: var(--text-muted);
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

/* Header Search Container (Fixed Typing Text Overlay) */
.header-search-container {
  flex: 1;
  max-width: 520px;
  position: relative;
}

.search-input-wrapper {
  display: flex;
  align-items: center;
  background: #f1f5f9;
  border: 2px solid #e2e8f0;
  border-radius: var(--radius-full);
  padding: 4px 6px 4px 16px;
  position: relative;
  transition: var(--transition);
}

.search-input-wrapper:focus-within {
  background: #fff;
  border-color: var(--primary);
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.15);
}

.search-icon-fixed {
  color: #64748b;
  display: flex;
  align-items: center;
  margin-right: 8px;
}

.header-search-input {
  width: 100%;
  border: none;
  outline: none;
  background: transparent;
  font-size: 0.95rem;
  padding: 8px 0;
  color: #0f172a;
  z-index: 2;
  position: relative;
}

.search-placeholder-label {
  position: absolute;
  left: 42px;
  color: #64748b;
  font-size: 0.92rem;
  pointer-events: none;
  transition: opacity 0.2s ease;
  z-index: 1;
}

.search-typing-text {
  color: var(--primary);
  font-weight: 700;
}

/* When input has focus or text, hide typing placeholder */
.header-search-input:focus ~ .search-placeholder-label,
.header-search-input:not(:placeholder-shown) ~ .search-placeholder-label {
  opacity: 0 !important;
  visibility: hidden !important;
}

.search-submit-btn {
  background: var(--primary);
  color: #fff;
  border: none;
  padding: 8px 20px;
  border-radius: var(--radius-full);
  font-weight: 600;
  font-size: 0.88rem;
  cursor: pointer;
  transition: var(--transition);
  z-index: 3;
}

.search-submit-btn:hover {
  background: var(--primary-hover);
}

/* Search Dropdown */
.search-results-dropdown {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  right: 0;
  background: #ffffff;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--border-light);
  max-height: 360px;
  overflow-y: auto;
  z-index: 1100;
  display: none;
}

.search-results-dropdown.active {
  display: block;
}

.search-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-bottom: 1px solid #f1f5f9;
  cursor: pointer;
  transition: var(--transition);
}

.search-item:hover {
  background: #f8fafc;
}

.search-item img {
  width: 44px;
  height: 44px;
  object-fit: cover;
  border-radius: 8px;
}

.search-item-info h5 {
  font-size: 0.92rem;
  font-weight: 600;
}

.search-item-info p {
  font-size: 0.8rem;
  color: var(--text-muted);
}

/* Header Right Actions */
.header-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

.account-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #f1f5f9;
  border: none;
  padding: 10px 18px;
  border-radius: var(--radius-full);
  font-weight: 600;
  font-size: 0.9rem;
  color: #0f172a;
  cursor: pointer;
  transition: var(--transition);
}

.account-btn:hover {
  background: #e2e8f0;
  color: var(--primary);
}

.header-wa-btn {
  padding: 10px 20px !important;
  font-size: 0.9rem !important;
  border-radius: var(--radius-full) !important;
}

/* Sub Nav Menu */
.sub-nav {
  background: #f8fafc;
  border-top: 1px solid #e2e8f0;
  border-bottom: 1px solid #e2e8f0;
}

.sub-nav-inner {
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 32px;
  list-style: none;
  overflow-x: auto;
  white-space: nowrap;
  padding: 12px 0;
}

.nav-link {
  font-size: 0.92rem;
  font-weight: 600;
  color: #334155;
  transition: var(--transition);
  position: relative;
  padding: 4px 0;
}

.nav-link:hover { color: var(--primary); }

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--primary);
  transition: var(--transition);
}

.nav-link:hover::after { width: 100%; }

.nav-item-highlight .nav-link {
  color: var(--secondary);
  font-weight: 700;
}

/* Mobile Menu Button */
.mobile-menu-btn {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 4px;
}

.mobile-menu-btn span {
  width: 24px;
  height: 2.5px;
  background: #0f172a;
  border-radius: 2px;
  transition: var(--transition);
}

.mobile-menu {
  position: fixed;
  top: 0;
  right: -100%;
  width: 80%;
  max-width: 320px;
  height: 100vh;
  background: #ffffff;
  z-index: 2000;
  box-shadow: -10px 0 30px rgba(0,0,0,0.15);
  display: flex;
  flex-direction: column;
  padding: 80px 32px 32px;
  gap: 20px;
  transition: right 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.mobile-menu.active { right: 0; }

.mobile-menu a {
  font-size: 1.1rem;
  font-weight: 600;
  color: #0f172a;
  padding-bottom: 12px;
  border-bottom: 1px solid #f1f5f9;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-weight: 600;
  font-size: 0.95rem;
  padding: 12px 26px;
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: var(--transition);
  border: none;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  color: #ffffff;
  box-shadow: 0 4px 14px rgba(37,99,235,0.35);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(37,99,235,0.45);
}

.btn-whatsapp {
  background: linear-gradient(135deg, var(--whatsapp), var(--whatsapp-dark));
  color: #ffffff;
  box-shadow: 0 4px 14px rgba(37,211,102,0.35);
}

.btn-whatsapp:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(37,211,102,0.45);
}

.btn-outline-light {
  background: rgba(255,255,255,0.15);
  color: #ffffff;
  border: 1px solid rgba(255,255,255,0.3);
  backdrop-filter: blur(8px);
}

.btn-outline-light:hover {
  background: #ffffff;
  color: #0f172a;
}

.btn-outline-dark {
  background: transparent;
  color: var(--primary);
  border: 1.5px solid var(--primary);
}

.btn-outline-dark:hover {
  background: var(--primary);
  color: #ffffff;
}

/* ═══ 5 FEATURE HIGHLIGHTS BAR ═══ */
.features-bar-section {
  background: #ffffff;
  padding: 24px 0;
  border-bottom: 1px solid var(--border-light);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px 16px;
  background: #f8fafc;
  border-radius: var(--radius-md);
  border: 1px solid #e2e8f0;
  transition: var(--transition);
}

.feature-item:hover {
  transform: translateY(-3px);
  border-color: var(--primary);
  box-shadow: var(--shadow-sm);
}

.feature-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: rgba(37, 99, 235, 0.1);
  color: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.feature-text {
  display: flex;
  flex-direction: column;
}

.feature-text strong {
  font-size: 0.92rem;
  font-weight: 700;
  color: #0f172a;
}

.feature-text span {
  font-size: 0.78rem;
  color: var(--text-muted);
}

/* ═══ PROMO BANNERS GRID ═══ */
.promo-banners-section {
  background: #f8fafc;
}

.banners-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
}

.banner-card {
  position: relative;
  border-radius: var(--radius-lg);
  overflow: hidden;
  background-size: cover;
  background-position: center;
  padding: 40px;
  min-height: 280px;
  display: flex;
  align-items: flex-end;
  box-shadow: var(--shadow-md);
  transition: var(--transition);
}

.banner-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.banner-large { grid-column: span 8; min-height: 360px; }
.banner-tall { grid-column: span 4; min-height: 360px; }
.banner-wide { grid-column: span 12; min-height: 220px; }

.banner-content {
  position: relative;
  z-index: 2;
  color: #ffffff;
  max-width: 580px;
}

.banner-tag {
  display: inline-block;
  background: rgba(255,255,255,0.2);
  backdrop-filter: blur(10px);
  padding: 4px 12px;
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  margin-bottom: 12px;
  text-transform: uppercase;
}

.banner-title {
  font-size: clamp(1.5rem, 2.5vw, 2.1rem);
  color: #ffffff;
  margin-bottom: 10px;
}

.banner-desc {
  font-size: 0.95rem;
  color: rgba(255,255,255,0.85);
  margin-bottom: 20px;
}

.banner-btn {
  padding: 10px 22px !important;
  font-size: 0.88rem !important;
}

/* ═══ POPULAR CATEGORIES CAROUSEL ═══ */
.popular-categories-section { background: #ffffff; }

.animated-heading-wrapper { margin-bottom: 12px; }

.animated-title {
  font-size: clamp(2rem, 3.8vw, 2.75rem);
  font-weight: 800;
}

.highlight-underline {
  position: relative;
  display: inline-block;
  color: var(--primary);
}

.highlight-underline svg {
  position: absolute;
  bottom: -10px;
  left: 0;
  width: 100%;
  height: 18px;
  stroke: var(--accent);
  stroke-width: 8;
  fill: none;
}

.categories-carousel-wrapper { margin-top: 40px; }

.categories-grid-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 24px;
}

.category-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: var(--transition);
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
}

.category-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-md);
  border-color: var(--primary);
}

.category-card-img {
  position: relative;
  width: 100%;
  height: 200px;
  overflow: hidden;
  background: #f1f5f9;
}

.category-card-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.category-card:hover .category-card-img img {
  transform: scale(1.08);
}

.category-badge {
  position: absolute;
  top: 14px;
  right: 14px;
  background: rgba(15, 23, 42, 0.75);
  backdrop-filter: blur(8px);
  color: #fff;
  padding: 4px 10px;
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 600;
}

.category-card-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.category-title { font-size: 1.15rem; margin-bottom: 8px; }

.category-desc {
  font-size: 0.88rem;
  color: var(--text-muted);
  margin-bottom: 16px;
  flex: 1;
}

.category-explore {
  font-size: 0.85rem !important;
  padding: 8px 16px !important;
  align-self: flex-start;
}

/* ═══ POPULAR PRINTING — CONTINUOUS MARQUEE ═══ */
.featured-marquee-section {
  background: #f8fafc;
  overflow: hidden;
}

.filter-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 32px;
}

.filter-btn {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  padding: 8px 20px;
  border-radius: var(--radius-full);
  font-weight: 600;
  font-size: 0.88rem;
  color: #334155;
  cursor: pointer;
  transition: var(--transition);
}

.filter-btn.active, .filter-btn:hover {
  background: var(--primary);
  color: #ffffff;
  border-color: var(--primary);
  box-shadow: 0 4px 12px rgba(37,99,235,0.25);
}

.featured-slider-wrapper {
  overflow: hidden;
  width: 100%;
  position: relative;
  padding: 10px 0;
}

.featured-marquee-track {
  display: flex;
  width: max-content;
  gap: 24px;
  animation: marqueeTrackLoop 30s linear infinite;
}

.featured-slider-wrapper:hover .featured-marquee-track {
  animation-play-state: paused;
}

@keyframes marqueeTrackLoop {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

.featured-slider {
  display: flex;
  gap: 24px;
}

.featured-card {
  width: 280px;
  flex-shrink: 0;
  background: #ffffff;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-light);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.featured-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-md);
}

.featured-card-img {
  position: relative;
  width: 100%;
  height: 180px;
  overflow: hidden;
  background: #f1f5f9;
}

.featured-card-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.featured-card:hover .featured-card-img img {
  transform: scale(1.06);
}

.featured-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  background: var(--primary);
  color: #fff;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 0.72rem;
  font-weight: 700;
}

.featured-card-content { padding: 16px; }

.featured-card-content h4 { font-size: 1.05rem; margin-bottom: 6px; }

.featured-card-content p {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-bottom: 14px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* ═══ ALL PRODUCTS GRID ═══ */
.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 28px;
}

.product-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
}

.product-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-md);
  border-color: var(--primary);
}

.product-card-image {
  position: relative;
  width: 100%;
  height: 210px;
  overflow: hidden;
  background: #f1f5f9;
}

.product-card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.product-card:hover .product-card-image img {
  transform: scale(1.08);
}

.product-tag {
  position: absolute;
  top: 12px;
  left: 12px;
  background: rgba(15, 23, 42, 0.8);
  backdrop-filter: blur(8px);
  color: #fff;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 700;
}

.product-card-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.product-card-title { font-size: 1.15rem; margin-bottom: 8px; }

.product-card-desc {
  font-size: 0.88rem;
  color: var(--text-muted);
  margin-bottom: 18px;
  flex: 1;
}

/* ═══ PROCESS STEPS SHOWCASE ═══ */
.process-showcase { background: #ffffff; }

.process-steps-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}

.process-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-md);
  padding: 32px 24px;
  position: relative;
  transition: var(--transition);
}

.process-card:hover {
  transform: translateY(-6px);
  border-color: var(--primary);
  background: #ffffff;
  box-shadow: var(--shadow-md);
}

.step-num {
  font-family: 'Outfit', sans-serif;
  font-size: 2.5rem;
  font-weight: 900;
  color: rgba(37,99,235,0.15);
  position: absolute;
  top: 16px;
  right: 20px;
}

.step-icon { font-size: 2.2rem; margin-bottom: 16px; }

.process-card h3 { font-size: 1.15rem; margin-bottom: 8px; }

.process-card p { font-size: 0.88rem; color: var(--text-muted); }

/* ═══ TRANSFORMATION BEFORE/AFTER SLIDER (Fixed Responsiveness) ═══ */
.transformation-section { background: #f8fafc; }

.comparison-container {
  position: relative;
  width: 100%;
  max-width: 900px;
  height: 440px;
  margin: 0 auto;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-lg);
  user-select: none;
  cursor: ew-resize;
}

.comparison-after, .comparison-before {
  position: absolute;
  inset: 0;
}

.comparison-after img, .comparison-before img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.comparison-before {
  width: 50%;
  overflow: hidden;
  border-right: 2px solid #ffffff;
  z-index: 2;
}

.comp-badge {
  position: absolute;
  top: 20px;
  padding: 6px 14px;
  border-radius: var(--radius-full);
  font-size: 0.8rem;
  font-weight: 700;
  backdrop-filter: blur(10px);
  z-index: 5;
}

.badge-after { right: 20px; background: rgba(37,99,235,0.85); color: #fff; }
.badge-before { left: 20px; background: rgba(15,23,42,0.85); color: #fff; }

.comparison-slider {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 4px;
  background: #ffffff;
  transform: translateX(-50%);
  z-index: 10;
}

.slider-handle {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 40px;
  height: 40px;
  background: #ffffff;
  color: #0f172a;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  box-shadow: 0 4px 14px rgba(0,0,0,0.3);
}

/* ═══ CALCULATOR ═══ */
.calculator-section { background: #ffffff; }

.calculator-card {
  background: linear-gradient(135deg, #0f172a, #1e293b);
  border-radius: var(--radius-lg);
  padding: 48px;
  color: #ffffff;
  box-shadow: var(--shadow-lg);
}

.calculator-card .section-title { color: #ffffff; }
.calculator-card .section-subtitle { color: #94a3b8; }

.calc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 24px;
  margin-bottom: 32px;
}

.calc-group { display: flex; flex-direction: column; gap: 8px; }

.calc-label {
  font-size: 0.9rem;
  font-weight: 600;
  color: #cbd5e1;
}

.calc-select {
  background: #1e293b;
  border: 1px solid #334155;
  color: #ffffff;
  padding: 12px 16px;
  border-radius: var(--radius-md);
  font-size: 0.95rem;
  outline: none;
  transition: var(--transition);
}

.calc-select:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(37,99,235,0.3);
}

.calc-action-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 20px;
  padding-top: 24px;
  border-top: 1px solid #334155;
}

.calc-info-note span { color: #94a3b8; font-size: 0.9rem; }

/* ═══ ABOUT STORE ═══ */
.about-section { background: #f8fafc; }

.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
}

.about-lead {
  font-size: 1.1rem;
  font-weight: 600;
  color: #334155;
  margin-bottom: 16px;
}

.store-info-box {
  margin-top: 32px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.info-item {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  background: #ffffff;
  padding: 14px 18px;
  border-radius: var(--radius-md);
  border: 1px solid #e2e8f0;
}

.info-icon { font-size: 1.3rem; }

.about-image-card {
  position: relative;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-lg);
}

.experience-badge {
  position: absolute;
  bottom: 24px;
  left: 24px;
  background: rgba(15,23,42,0.85);
  backdrop-filter: blur(10px);
  color: #ffffff;
  padding: 14px 24px;
  border-radius: var(--radius-md);
  display: flex;
  flex-direction: column;
}

.exp-number {
  font-family: 'Outfit', sans-serif;
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--accent);
}

.exp-label { font-size: 0.8rem; font-weight: 600; }

/* ═══ FOOTER & FLOATING WHATSAPP ═══ */
.site-footer {
  background: #0f172a;
  color: #94a3b8;
  padding-top: 64px;
}

.footer-inner {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.2fr;
  gap: 40px;
  padding-bottom: 48px;
  border-bottom: 1px solid #1e293b;
}

.footer-logo {
  font-family: 'Outfit', sans-serif;
  font-size: 1.5rem;
  font-weight: 800;
  color: #ffffff;
  margin-bottom: 14px;
}

.footer-desc { font-size: 0.88rem; margin-bottom: 20px; line-height: 1.6; }
.footer-contact p { font-size: 0.85rem; margin-bottom: 8px; }

.footer-col h4 {
  color: #ffffff;
  font-size: 1.05rem;
  margin-bottom: 20px;
}

.footer-col ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.footer-col ul a { font-size: 0.88rem; transition: var(--transition); }
.footer-col ul a:hover { color: #ffffff; padding-left: 4px; }

.hours-text { font-size: 0.88rem; margin-bottom: 10px; }

.footer-pay-badges {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 16px;
}

.pay-tag {
  background: #1e293b;
  color: #cbd5e1;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
}

.footer-bottom { padding: 24px 0; font-size: 0.85rem; }

.bottom-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
}

.back-to-top {
  background: #1e293b;
  color: #ffffff;
  border: none;
  padding: 8px 16px;
  border-radius: var(--radius-full);
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
}

.back-to-top:hover { background: var(--primary); }

/* Floating WhatsApp */
.floating-whatsapp {
  position: fixed;
  bottom: 28px;
  right: 28px;
  width: 58px;
  height: 58px;
  background: var(--whatsapp);
  color: #ffffff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 24px rgba(37,211,102,0.45);
  z-index: 1500;
  transition: var(--transition);
  animation: pulseWa 2s infinite;
}

.floating-whatsapp:hover { transform: scale(1.1); }

.floating-tooltip {
  position: absolute;
  right: 70px;
  background: #0f172a;
  color: #ffffff;
  padding: 6px 14px;
  border-radius: var(--radius-full);
  font-size: 0.8rem;
  font-weight: 600;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: var(--transition);
}

.floating-whatsapp:hover .floating-tooltip { opacity: 1; }

@keyframes pulseWa {
  0% { box-shadow: 0 0 0 0 rgba(37,211,102,0.6); }
  70% { box-shadow: 0 0 0 16px rgba(37,211,102,0); }
  100% { box-shadow: 0 0 0 0 rgba(37,211,102,0); }
}

/* Modals */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(15,23,42,0.75);
  backdrop-filter: blur(8px);
  z-index: 3000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}

.modal-overlay.active {
  opacity: 1;
  pointer-events: auto;
}

.modal-card {
  background: #ffffff;
  border-radius: var(--radius-lg);
  width: 100%;
  max-width: 440px;
  padding: 36px;
  position: relative;
  box-shadow: var(--shadow-lg);
}

.modal-close {
  position: absolute;
  top: 18px;
  right: 18px;
  background: #f1f5f9;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  cursor: pointer;
}

.modal-subtitle {
  font-size: 0.88rem;
  color: var(--text-muted);
  margin-bottom: 20px;
}

.form-group { margin-bottom: 16px; }

.form-group label {
  display: block;
  font-size: 0.85rem;
  font-weight: 600;
  margin-bottom: 6px;
}

.form-input {
  width: 100%;
  padding: 10px 14px;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  outline: none;
  font-size: 0.92rem;
}

.form-input:focus { border-color: var(--primary); }

.full-width-btn { width: 100%; margin-top: 10px; }

.modal-tabs {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
  border-bottom: 1px solid #e2e8f0;
}

.modal-tab {
  background: none;
  border: none;
  padding: 8px 16px;
  font-weight: 700;
  color: var(--text-muted);
  cursor: pointer;
}

.modal-tab.active {
  color: var(--primary);
  border-bottom: 2px solid var(--primary);
}

.modal-tab-content { display: none; }
.modal-tab-content.active { display: block; }

/* Responsive Adjustments */
@media (max-width: 1024px) {
  .banner-large, .banner-tall, .banner-wide { grid-column: span 12; }
  .about-grid, .footer-inner { grid-template-columns: 1fr; }
  .header-search-container { max-width: 300px; }
}

@media (max-width: 768px) {
  .header-search-container { display: none; }
  .nav-menu { display: none; }
  .mobile-menu-btn { display: flex; }
  .top-announcement-right { display: none; }
  .top-announcement-inner { justify-content: center; text-align: center; }
  .comparison-container { height: 280px; }
}
"""

with open("/Users/riyasudeen/Documents/clien web/xerox/styles.css", "w") as f:
    f.write(css_content)

print("Fixed styles.css")
