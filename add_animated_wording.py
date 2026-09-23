import os

# 1. Update index.html
with open("/Users/riyasudeen/Documents/clien web/xerox/index.html") as f:
    html = f.read()

hero_start = '<section class="hero" id="home">'
hero_end = '</section>'

pos_start = html.find(hero_start)
pos_end = html.find(hero_end, pos_start)

new_hero_html = """<section class="hero" id="home">
      <div class="hero-bg">
        <img src="/hero-bg.png?v=5" alt="Adha Prints — Product Showcase" fetchpriority="high" decoding="async" width="1024" height="575" />
      </div>
      <div class="hero-overlay"></div>
      
      <!-- Animated Wording Overlay -->
      <div class="hero-animated-wording-container">
        <div class="hero-handwritten-tag">Your One Stop Printing Partner</div>
        
        <div class="hero-brand-group">
          <h1 class="hero-title-main">
            <span class="animated-word word-1">PRINT YOUR BRAND.</span>
            <span class="animated-word word-2 gradient-shimmer-text">MAKE IT REMEMBERED.</span>
          </h1>
          <p class="hero-animated-sub">High-quality printing solutions for businesses, events, education and everyday needs.</p>
        </div>

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
    </section>"""

updated_html = html[:pos_start] + new_hero_html + html[pos_end+len(hero_end):]

with open("/Users/riyasudeen/Documents/clien web/xerox/index.html", "w") as f:
    f.write(updated_html)

# 2. Update premium-animations.css with Animated Wording CSS
with open("/Users/riyasudeen/Documents/clien web/xerox/premium-animations.css") as f:
    anim = f.read()

wording_css = """
/* ═══ ANIMATED WORDING OVERLAY ═══ */
.hero-animated-wording-container {
  position: relative;
  z-index: 10;
  width: 100%;
  max-width: 1280px;
  padding: 60px 24px 40px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: clamp(500px, 80vh, 800px);
}

.hero-handwritten-tag {
  align-self: flex-end;
  font-family: 'Caveat', cursive;
  font-size: clamp(1.8rem, 3.2vw, 2.6rem);
  color: #fbbf24;
  text-shadow: 0 4px 20px rgba(0,0,0,0.8), 0 0 12px rgba(251,191,36,0.6);
  opacity: 0;
  animation: handwritingFade 1.2s 0.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes handwritingFade {
  0% { opacity: 0; transform: translateY(-15px) rotate(-3deg) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) rotate(-2deg) scale(1); }
}

.hero-brand-group {
  max-width: 720px;
}

.hero-title-main {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-bottom: 16px;
}

.animated-word {
  display: block;
  font-family: 'Outfit', sans-serif;
  font-weight: 900;
  font-size: clamp(2.2rem, 4.8vw, 4.2rem);
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.word-1 {
  color: #ffffff;
  text-shadow: 0 4px 30px rgba(0,0,0,0.9);
  opacity: 0;
  animation: wordSlideLeft 0.9s 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.word-2 {
  opacity: 0;
  animation: wordSlideRight 0.9s 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.gradient-shimmer-text {
  background: linear-gradient(90deg, #ec4899, #f59e0b, #3b82f6, #ec4899);
  background-size: 300% 100%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: wordSlideRight 0.9s 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards, gradientLiquid 6s ease-in-out infinite alternate !important;
}

@keyframes wordSlideLeft {
  0% { opacity: 0; transform: translateX(-40px); }
  100% { opacity: 1; transform: translateX(0); }
}

@keyframes wordSlideRight {
  0% { opacity: 0; transform: translateX(40px); }
  100% { opacity: 1; transform: translateX(0); }
}

@keyframes gradientLiquid {
  0% { background-position: 0% 50%; }
  100% { background-position: 100% 50%; }
}

.hero-animated-sub {
  font-size: clamp(1rem, 1.5vw, 1.25rem);
  color: #f1f5f9;
  text-shadow: 0 2px 14px rgba(0,0,0,0.9);
  max-width: 580px;
  line-height: 1.5;
  opacity: 0;
  animation: fadeInSub 0.8s 0.9s forwards;
}

@keyframes fadeInSub {
  0% { opacity: 0; transform: translateY(20px); }
  100% { opacity: 1; transform: translateY(0); }
}
"""

if ".hero-animated-wording-container" not in anim:
    anim += "\n\n" + wording_css

with open("/Users/riyasudeen/Documents/clien web/xerox/premium-animations.css", "w") as f:
    f.write(anim)

print("Updated index.html and premium-animations.css with animated wording overlay")
