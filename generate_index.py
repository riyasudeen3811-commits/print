import os

html_content = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Adha Prints — Business Cards, Flyers, Stickers & Custom Printing | Chennai</title>
    <meta name="description" content="Order custom business cards, flyers, banners, stickers, ID cards & book binding online at Adha Prints. Fast turnaround & doorstep delivery across Chennai." />
    <meta name="keywords" content="Adha Prints, printing services Kottivakkam, printing shop Chennai, business cards Chennai, brochure printing, flyer printing, ID card printing, offset printing Chennai, screen printing, thesis binding Kottivakkam, DTP services Chennai" />
    <meta name="author" content="Adha Prints" />
    <meta name="robots" content="index, follow, max-image-preview:large" />
    <link rel="canonical" href="http://localhost:5173/" />
    
    <!-- Geo Meta Tags for Local SEO in Chennai -->
    <meta name="geo.region" content="IN-TN" />
    <meta name="geo.placename" content="Chennai, Kottivakkam" />
    <meta name="geo.position" content="12.96;80.265" />
    <meta name="ICBM" content="12.96, 80.265" />
    
    <!-- Open Graph / Social Media Meta Tags -->
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Adha Prints — Neighbourhood Print Store" />
    <meta property="og:title" content="Business Cards, Flyers & Custom Printing | Adha Prints Chennai" />
    <meta property="og:description" content="Order custom business cards, flyers, banners & stickers online. Fast turnaround, doorstep delivery across Chennai. Get an instant quote at Adha Prints." />
    <meta property="og:image" content="http://localhost:5173/hero-bg.jpg" />
    <meta property="og:url" content="http://localhost:5173/" />
    <meta property="og:locale" content="en_IN" />

    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Business Cards, Flyers & Custom Printing | Adha Prints" />
    <meta name="twitter:description" content="High-quality printing solutions for businesses, events, education and everyday needs in Chennai." />
    <meta name="twitter:image" content="http://localhost:5173/hero-bg.jpg" />

    <!-- Performance & Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload" href="/hero-bg.jpg" as="image" fetchpriority="high">
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800;900&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/premium-animations.css">
    
    <!-- JSON-LD LocalBusiness Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "PrintShop",
      "name": "Adha Prints",
      "image": "http://localhost:5173/hero-bg.jpg",
      "@id": "http://localhost:5173/#organization",
      "url": "http://localhost:5173/",
      "telephone": "+919790779720",
      "email": "madhaprints@gmail.com",
      "priceRange": "₹",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "No: 4/353, 4th Street, Dr. Puratchi Thalaivi Main Road, MGR Nagar, Kottivakkam",
        "addressLocality": "Chennai",
        "addressRegion": "Tamil Nadu",
        "postalCode": "600041",
        "addressCountry": "IN"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 12.96,
        "longitude": 80.265
      },
      "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
        "opens": "09:00",
        "closes": "20:00"
      },
      "sameAs": ["https://wa.me/919790779720"]
    }
    </script>
  </head>
  <body>
    <div class="scroll-progress-bar" id="scroll-progress"></div>

    <!-- ═══ TOP ANNOUNCEMENT BAR ═══ -->
    <div class="top-announcement-bar">
      <div class="container top-announcement-inner">
        <span class="announcement-text">🎉 Use code <strong class="highlight-code">PRINT10</strong> on first order | Doorstep Delivery across Chennai</span>
        <div class="top-announcement-right">
          <a href="tel:+919790779720" class="top-link">📞 +91 97907 79720</a>
          <span class="sep">|</span>
          <a href="https://wa.me/919790779720?text=Hi%20Adha%20Prints%2C%20I%20need%20a%20quotation." class="top-link whatsapp-top" target="_blank">💬 WhatsApp Support</a>
        </div>
      </div>
    </div>

    <!-- ═══ MAIN HEADER ═══ -->
    <header class="site-header" id="navbar">
      <div class="container header-main">
        <!-- Logo -->
        <a href="#" class="site-logo">
          <div class="logo-mark">AP</div>
          <div class="logo-text-group">
            <span class="brand-name">ADHA<span class="brand-accent"> PRINTS</span></span>
            <span class="brand-sub">Neighbourhood Print Store</span>
          </div>
        </a>

        <!-- Animated Typing Search Bar -->
        <div class="header-search-container">
          <form class="header-search-form" id="search-form" onsubmit="return false;">
            <div class="search-input-wrapper">
              <span class="search-icon-fixed">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              </span>
              <span class="search-placeholder-label">Search for <span class="search-typing-text" id="typing-text">Visiting cards</span></span>
              <input type="text" class="header-search-input" id="search-input" aria-label="Search products" autocomplete="off" />
              <button type="submit" class="search-submit-btn" id="search-btn">
                <span>Search</span>
              </button>
            </div>
          </form>
          <div class="search-results-dropdown" id="search-dropdown"></div>
        </div>

        <!-- Header Right Actions -->
        <div class="header-actions">
          <button class="account-btn" id="account-modal-trigger">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            <span class="account-label">Sign In</span>
          </button>
          
          <a href="https://wa.me/919790779720?text=Hi%20Adha%20Prints%2C%20I%20want%20to%20get%20an%20instant%20quote." class="btn btn-whatsapp header-wa-btn" target="_blank">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            <span>Quote</span>
          </a>

          <div class="mobile-menu-btn" id="mobile-menu-btn">
            <span></span><span></span><span></span>
          </div>
        </div>
      </div>

      <!-- Navigation Bar -->
      <nav class="sub-nav">
        <div class="container sub-nav-inner">
          <ul class="nav-menu">
            <li class="nav-item"><a href="#cards" class="nav-link">Cards & Stationery</a></li>
            <li class="nav-item"><a href="#marketing" class="nav-link">Marketing & Flyers</a></li>
            <li class="nav-item"><a href="#stickers" class="nav-link">Stickers & Labels</a></li>
            <li class="nav-item"><a href="#signage" class="nav-link">Signage & Apparel</a></li>
            <li class="nav-item"><a href="#binding" class="nav-link">ID & Thesis Binding</a></li>
            <li class="nav-item nav-item-highlight"><a href="#calculator" class="nav-link">⚡ Instant Quote Calculator</a></li>
          </ul>
        </div>
      </nav>
    </header>

    <!-- Mobile Menu Drawer -->
    <div class="mobile-menu" id="mobile-menu">
      <a href="#home">Home</a>
      <a href="#cards">Cards & Stationery</a>
      <a href="#marketing">Marketing & Flyers</a>
      <a href="#stickers">Stickers & Labels</a>
      <a href="#signage">Signage & Apparel</a>
      <a href="#binding">ID & Thesis Binding</a>
      <a href="#calculator">Instant Calculator</a>
      <a href="#contact">Contact Us</a>
      <a href="https://wa.me/919790779720?text=Hi%20Adha%20Prints%2C%20I%20need%20a%20quotation." class="btn btn-primary" target="_blank">Get Instant Quote</a>
    </div>

    <!-- ═══ HERO SECTION — CINEMATIC ULTRA-PREMIUM ═══ -->
    <section class="hero" id="home">
      <div class="hero-bg">
        <img src="/hero-bg.jpg" alt="Adha Prints — Heidelberg & Offset Product Showcase" fetchpriority="high" decoding="async" />
      </div>
      <div class="hero-film-grain"></div>
      <div class="hero-overlay"></div>
      
      <!-- Particles -->
      <div class="particles cinematic-particles">
        <div class="particle"></div><div class="particle"></div><div class="particle"></div>
        <div class="particle"></div><div class="particle"></div><div class="particle"></div>
      </div>

      <!-- Hero Content Container -->
      <div class="hero-content hero-content-imageonly">
        <div class="hero-bottom-cta">
          <a href="#cards" class="btn btn-primary hero-cta-btn">
            Explore Printing Services <span class="arrow">→</span>
          </a>
          <a href="https://wa.me/919790779720?text=Hi%20Adha%20Prints%2C%20I%20need%20a%20quotation%20for%20my%20business." class="btn btn-whatsapp hero-cta-btn" target="_blank">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            WhatsApp Instant Quote
          </a>
        </div>
      </div>
    </section>

    <!-- ═══ 5 FEATURE HIGHLIGHTS BAR (as in theprintguy24.com) ═══ -->
    <section class="features-bar-section">
      <div class="container">
        <div class="features-grid">
          <div class="feature-item">
            <div class="feature-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
            </div>
            <div class="feature-text">
              <strong>Bulk Order Discounts</strong>
              <span>Enquire on WhatsApp & get up to 50% off</span>
            </div>
          </div>

          <div class="feature-item">
            <div class="feature-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            </div>
            <div class="feature-text">
              <strong>Store & Pickup</strong>
              <span>Store in Kottivakkam, Chennai</span>
            </div>
          </div>

          <div class="feature-item">
            <div class="feature-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
            </div>
            <div class="feature-text">
              <strong>Free Fast Delivery</strong>
              <span>Express doorstep shipping with tracking</span>
            </div>
          </div>

          <div class="feature-item">
            <div class="feature-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <div class="feature-text">
              <strong>100% Quality Assurance</strong>
              <span>High precision Heidelberg CMYK printing</span>
            </div>
          </div>

          <div class="feature-item">
            <div class="feature-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>
            </div>
            <div class="feature-text">
              <strong>Custom Specs Enquiries</strong>
              <span>Instant direct WhatsApp quotation</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══ PROMO CATEGORY BANNERS (3-Column Grid like theprintguy24.com) ═══ -->
    <section class="promo-banners-section section-padding">
      <div class="container">
        <div class="banners-grid">
          <!-- Main Banner 1 -->
          <div class="banner-card banner-large" style="background-image: linear-gradient(135deg, rgba(15, 23, 42, 0.85), rgba(30, 58, 138, 0.7)), url('/business-cards.jpg');">
            <div class="banner-content">
              <span class="banner-tag">BESTSELLER COLLECTION</span>
              <h3 class="banner-title">Visiting Cards & Business Stationery</h3>
              <p class="banner-desc">Art, Matte, Mirror, Ivory, Metallic, Spot UV, Foil Stamped & Velvet Soft Touch Cards.</p>
              <a href="#cards" class="btn btn-primary banner-btn">Explore Collection →</a>
            </div>
          </div>

          <!-- Banner 2 -->
          <div class="banner-card banner-tall" style="background-image: linear-gradient(135deg, rgba(15, 23, 42, 0.85), rgba(88, 28, 135, 0.7)), url('/stickers.jpg');">
            <div class="banner-content">
              <span class="banner-tag">WATERPROOF & DIE-CUT</span>
              <h3 class="banner-title">Custom Stickers & Product Labels</h3>
              <p class="banner-desc">Art paper, Glossy, Matte, Synthetic, Transparent & Metallic Foil Stickers.</p>
              <a href="#stickers" class="btn btn-outline-light banner-btn">View Stickers →</a>
            </div>
          </div>

          <!-- Banner 3 Stacked -->
          <div class="banner-card banner-wide" style="background-image: linear-gradient(135deg, rgba(15, 23, 42, 0.85), rgba(6, 78, 59, 0.7)), url('/flyers.jpg');">
            <div class="banner-content">
              <span class="banner-tag">MARKETING & SIGNAGE</span>
              <h3 class="banner-title">Banners, Flyers & Corporate ID</h3>
              <p class="banner-desc">High resolution flex banners, standees, brochures, satin lanyards & T-shirts.</p>
              <a href="#marketing" class="btn btn-outline-light banner-btn">Order Banners →</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══ POPULAR CATEGORIES CAROUSEL SECTION (Underline Title + Carousel) ═══ -->
    <section class="popular-categories-section section-padding" id="categories">
      <div class="container">
        <div class="text-center reveal">
          <div class="animated-heading-wrapper">
            <h2 class="animated-title">
              Popular <span class="highlight-underline">Categories<svg viewBox="0 0 500 150" preserveAspectRatio="none"><path d="M5.5 125.883C149.207 118.384 329.838 103.383 495.5 125.883"></path></svg></span>
            </h2>
          </div>
          <p class="section-subtitle">Browse through our most ordered printing categories with instant customization.</p>
        </div>

        <div class="categories-carousel-wrapper">
          <div class="categories-grid-cards" id="popular-categories-grid">
            <!-- Dynamically Rendered by JS -->
          </div>
        </div>
      </div>
    </section>

    <!-- ═══ POPULAR PRINTING — AUTO-RUNNING MARQUEE BANNER (User Request) ═══ -->
    <section class="featured-marquee-section section-padding" id="popular">
      <div class="container">
        <div class="text-center reveal">
          <div class="accent-line"></div>
          <h2 class="section-title">Popular Printing</h2>
          <p class="section-subtitle">Our most requested printing services — continuous high speed production.</p>
        </div>

        <!-- Filter Buttons -->
        <div class="filter-container reveal">
          <button class="filter-btn active" data-filter="all">All Printing</button>
          <button class="filter-btn" data-filter="bestseller">⭐ Bestsellers</button>
          <button class="filter-btn" data-filter="corporate">🏢 Business Stationery</button>
          <button class="filter-btn" data-filter="marketing">📣 Marketing & Flyers</button>
          <button class="filter-btn" data-filter="events">🎉 Events & Cards</button>
          <button class="filter-btn" data-filter="custom">✂️ Binding & Special</button>
        </div>

        <!-- Continuous Running Marquee Track -->
        <div class="featured-slider-wrapper">
          <div class="featured-marquee-track">
            <div class="featured-slider" id="featured-slider">
              <!-- Cards injected by JS -->
            </div>
            <div class="featured-slider" id="featured-slider-dup" aria-hidden="true">
              <!-- Duplicated Cards injected by JS -->
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══ ALL PRODUCTS GRID ═══ -->
    <section class="products-section section-padding" id="cards">
      <div class="container">
        <div class="text-center reveal">
          <div class="accent-line"></div>
          <h2 class="section-title">Complete Printing Solutions</h2>
          <p class="section-subtitle">Explore our full catalog of premium print options tailored for business & everyday needs.</p>
        </div>
        <div class="products-grid stagger-children" id="products-grid">
          <!-- Cards injected by JS -->
        </div>
      </div>
    </section>

    <!-- ═══ FROM IDEA TO PRINT (PROCESS FLOW) ═══ -->
    <section class="process-showcase section-padding">
      <div class="container">
        <div class="text-center reveal">
          <div class="accent-line"></div>
          <h2 class="section-title">From Idea to Print</h2>
          <p class="section-subtitle">Our streamlined 4-step process ensures flawless production every single time.</p>
        </div>
        <div class="process-steps-grid stagger-children">
          <div class="process-card">
            <div class="step-num">01</div>
            <div class="step-icon">📋</div>
            <h3>Choose Product</h3>
            <p>Select your desired item, size, paper weight (GSM), and quantity.</p>
          </div>

          <div class="process-card">
            <div class="step-num">02</div>
            <div class="step-icon">🎨</div>
            <h3>Upload or Design</h3>
            <p>Send your PDF/AI print-ready file or request our in-house DTP design service.</p>
          </div>

          <div class="process-card">
            <div class="step-num">03</div>
            <div class="step-icon">🖨️</div>
            <h3>Instant Proof & Print</h3>
            <p>Approve digital proof before offset / digital printing on Heidelberg machinery.</p>
          </div>

          <div class="process-card">
            <div class="step-num">04</div>
            <div class="step-icon">🚚</div>
            <h3>Doorstep Delivery</h3>
            <p>Receive carefully packaged finished prints delivered straight to your door across Chennai.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══ SEE THE TRANSFORMATION (BEFORE/AFTER SLIDER) ═══ -->
    <section class="transformation-section section-padding">
      <div class="container">
        <div class="text-center reveal">
          <div class="accent-line"></div>
          <h2 class="section-title">See the Transformation</h2>
          <p class="section-subtitle">Slide to compare raw digital artwork with our ultra-premium printed product output.</p>
        </div>

        <div class="comparison-container reveal" id="comparison">
          <div class="comparison-after">
            <img src="/business-cards.jpg" alt="Finished Printed Velvet Spot UV Card" />
            <span class="comp-badge badge-after">✨ Finished Printed Output</span>
          </div>
          <div class="comparison-before" id="comparison-before">
            <img src="/letterheads.jpg" alt="Raw Digital Artwork File" />
            <span class="comp-badge badge-before">💻 Raw Digital File</span>
          </div>
          <div class="comparison-slider" id="comparison-slider">
            <div class="slider-handle">↔</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══ INSTANT QUOTE CALCULATOR ═══ -->
    <section class="calculator-section section-padding" id="calculator">
      <div class="container">
        <div class="calculator-card reveal">
          <div class="calc-header text-center">
            <div class="accent-line"></div>
            <h2 class="section-title">Instant Specifications & Quote Helper</h2>
            <p class="section-subtitle">Customize paper GSM, lamination, and size — then send specs straight to WhatsApp for instant order confirmation.</p>
          </div>

          <div class="calc-grid">
            <div class="calc-group">
              <label class="calc-label" for="calc-product">Select Product Type</label>
              <select class="calc-select" id="calc-product">
                <option value="Business Cards">Visiting Cards (350 GSM Art / Velvet / Spot UV)</option>
                <option value="Brochures">Brochures & Catalogs (170 GSM Gloss / Matte)</option>
                <option value="Flyers & Handbills">Flyers & Pamphlets (A4 / A5 - 130 GSM)</option>
                <option value="Stickers & Labels">Custom Stickers & Waterproof Labels</option>
                <option value="ID Cards & Lanyards">PVC ID Cards & Satin Printed Lanyards</option>
                <option value="Thesis & Book Binding">Book Binding (Hardcover / Softcover / Spiral)</option>
                <option value="Flex & Banners">Signage, Flex Banners & Rollup Standee</option>
              </select>
            </div>

            <div class="calc-group">
              <label class="calc-label" for="calc-quantity">Select Quantity</label>
              <select class="calc-select" id="calc-quantity">
                <option value="100 Units">100 Units</option>
                <option value="250 Units">250 Units</option>
                <option value="500 Units" selected>500 Units (Popular)</option>
                <option value="1000 Units">1,000 Units (Best Value)</option>
                <option value="2000+ Bulk Units">2,000+ Bulk Units (Wholesale Rate)</option>
              </select>
            </div>

            <div class="calc-group">
              <label class="calc-label" for="calc-finish">Paper Finish & Lamination</label>
              <select class="calc-select" id="calc-finish">
                <option value="Matte Lamination">Premium Matte Finish</option>
                <option value="Gloss Lamination">High Gloss UV Finish</option>
                <option value="Velvet Soft Touch">Velvet Soft Touch</option>
                <option value="Spot UV + Matte">Spot UV + Matte Lamination</option>
                <option value="Metallic Gold Foil Stamping">Gold Foil Stamping</option>
              </select>
            </div>
          </div>

          <div class="calc-action-bar">
            <div class="calc-info-note">
              <span>⚡ Direct WhatsApp Assistant will prepare your exact specifications instantly.</span>
            </div>
            <a id="calc-whatsapp-btn" href="https://wa.me/919790779720?text=Hi%20Adha%20Prints%2C%20I%20want%20to%20order%20500%20Business%20Cards%20with%20Matte%20Lamination." target="_blank" class="btn btn-primary calc-submit-btn">
              💬 Order Specs via WhatsApp →
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══ ABOUT & STORE LOCATION ═══ -->
    <section class="about-section section-padding" id="about">
      <div class="container">
        <div class="about-grid">
          <div class="about-text reveal-left">
            <div class="accent-line"></div>
            <h2 class="section-title">Your Trusted Neighbourhood Print Store in Chennai</h2>
            <p class="about-lead">Adha Prints delivers high-precision printing solutions using state-of-the-art offset and digital technology for businesses, startups, educational institutions, and individuals.</p>
            <p>From executive visiting cards and vibrant marketing flyers to custom waterproof stickers, thesis binding, and corporate signage — we ensure crisp color accuracy, fast turnaround times, and affordable wholesale pricing.</p>
            
            <div class="store-info-box">
              <div class="info-item">
                <div class="info-icon">📍</div>
                <div>
                  <strong>Store Location</strong>
                  <p>No: 4/353, 4th Street, Dr. Puratchi Thalaivi Main Road, MGR Nagar, Kottivakkam, Chennai - 600 041</p>
                </div>
              </div>
              <div class="info-item">
                <div class="info-icon">🕒</div>
                <div>
                  <strong>Operating Hours</strong>
                  <p>Monday – Saturday: 9:00 AM – 8:00 PM</p>
                </div>
              </div>
              <div class="info-item">
                <div class="info-icon">📞</div>
                <div>
                  <strong>Contact & Enquiries</strong>
                  <p>Phone: +91 97907 79720 | Email: madhaprints@gmail.com</p>
                </div>
              </div>
            </div>
          </div>

          <div class="about-image-card reveal-right">
            <img src="/offset-printing.jpg" alt="Adha Prints Offset Machine & Quality Check" />
            <div class="experience-badge">
              <span class="exp-number">100%</span>
              <span class="exp-label">Quality Guaranteed</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══ FOOTER ═══ -->
    <footer class="site-footer" id="contact">
      <div class="container footer-inner">
        <div class="footer-col brand-col">
          <div class="footer-logo">ADHA<span class="logo-accent"> PRINTS</span></div>
          <p class="footer-desc">Neighbourhood print store delivering high quality offset, digital, and custom print solutions across Chennai.</p>
          <div class="footer-contact">
            <p>📍 No: 4/353, 4th Street, Dr. Puratchi Thalaivi Main Road, MGR Nagar, Kottivakkam, Chennai - 600 041</p>
            <p>📞 <a href="tel:+919790779720">+91 97907 79720</a></p>
            <p>✉️ <a href="mailto:madhaprints@gmail.com">madhaprints@gmail.com</a></p>
          </div>
        </div>

        <div class="footer-col">
          <h4>Popular Printing</h4>
          <ul>
            <li><a href="#cards">Business Cards</a></li>
            <li><a href="#stickers">Custom Stickers & Labels</a></li>
            <li><a href="#marketing">Brochures & Flyers</a></li>
            <li><a href="#signage">Flex Banners & Standees</a></li>
            <li><a href="#binding">Book & Thesis Binding</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#categories">Popular Categories</a></li>
            <li><a href="#calculator">Instant Specifications</a></li>
            <li><a href="#about">About Our Store</a></li>
            <li><a href="https://wa.me/919790779720" target="_blank">WhatsApp Support</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Store Hours</h4>
          <p class="hours-text"><strong>Mon - Sat:</strong> 9:00 AM – 8:00 PM</p>
          <p class="hours-text"><strong>Sunday:</strong> On Call / Appointment</p>
          <div class="footer-pay-badges">
            <span class="pay-tag">GPay / PhonePe</span>
            <span class="pay-tag">UPI</span>
            <span class="pay-tag">Cards Accepted</span>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="container bottom-inner">
          <p>© 2026 Adha Prints. All Rights Reserved. Designed & Developed with Ultra-Premium Quality.</p>
          <button class="back-to-top" id="back-to-top" aria-label="Back to top">↑ Top</button>
        </div>
      </div>
    </footer>

    <!-- ═══ FLOATING WHATSAPP BUTTON ═══ -->
    <a href="https://wa.me/919790779720?text=Hi%20Adha%20Prints%2C%20I%20want%20to%20place%20an%20order." class="floating-whatsapp" target="_blank" aria-label="Chat on WhatsApp">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
      <span class="floating-tooltip">Need Help? Chat on WhatsApp</span>
    </a>

    <!-- ═══ MODAL FOR SIGN IN / LOGIN ═══ -->
    <div class="modal-overlay" id="account-modal">
      <div class="modal-card">
        <button class="modal-close" id="account-modal-close">✕</button>
        <div class="modal-tabs">
          <button class="modal-tab active" data-tab="login">Login</button>
          <button class="modal-tab" data-tab="register">Register</button>
        </div>
        <div class="modal-tab-content active" id="tab-login">
          <h3>Welcome Back to Adha Prints</h3>
          <form onsubmit="event.preventDefault(); alert('Logged in successfully!'); document.getElementById('account-modal').classList.remove('active');">
            <div class="form-group">
              <label>Email or Phone Number</label>
              <input type="text" required placeholder="Enter your email or phone" class="form-input" />
            </div>
            <div class="form-group">
              <label>Password</label>
              <input type="password" required placeholder="Enter password" class="form-input" />
            </div>
            <button type="submit" class="btn btn-primary full-width-btn">Login to Account</button>
          </form>
        </div>
        <div class="modal-tab-content" id="tab-register">
          <h3>Create an Account</h3>
          <form onsubmit="event.preventDefault(); alert('Account created successfully!'); document.getElementById('account-modal').classList.remove('active');">
            <div class="form-group">
              <label>Full Name</label>
              <input type="text" required placeholder="Enter your name" class="form-input" />
            </div>
            <div class="form-group">
              <label>Email Address</label>
              <input type="email" required placeholder="Enter your email" class="form-input" />
            </div>
            <div class="form-group">
              <label>Mobile Number</label>
              <input type="tel" required placeholder="Enter phone number" class="form-input" />
            </div>
            <button type="submit" class="btn btn-primary full-width-btn">Register Account</button>
          </form>
        </div>
      </div>
    </div>

    <!-- ═══ MODAL FOR QUICK QUOTE ═══ -->
    <div class="modal-overlay" id="quote-modal">
      <div class="modal-card">
        <button class="modal-close" id="modal-close-btn">✕</button>
        <h3>Request Instant Print Quote</h3>
        <p class="modal-subtitle">Submit your requirement and our Kottivakkam print expert will contact you immediately.</p>
        <form id="modal-quote-form">
          <div class="form-group">
            <label>Your Name</label>
            <input type="text" id="modal-name" required placeholder="Enter full name" class="form-input" />
          </div>
          <div class="form-group">
            <label>Phone / WhatsApp Number</label>
            <input type="tel" id="modal-phone" required placeholder="Enter mobile number" class="form-input" />
          </div>
          <div class="form-group">
            <label>Print Service Needed</label>
            <input type="text" id="modal-requirement" required placeholder="e.g. 500 Business Cards" class="form-input" />
          </div>
          <button type="submit" class="btn btn-primary full-width-btn">Submit Quote Request →</button>
        </form>
      </div>
    </div>

    <script src="/src/main.js"></script>
  </body>
</html>
"""

with open("/Users/riyasudeen/Documents/clien web/xerox/index.html", "w") as f:
    f.write(html_content)

print("Generated index.html successfully")
