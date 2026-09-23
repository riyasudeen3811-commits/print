import os

# 1. Update index.html
with open("/Users/riyasudeen/Documents/clien web/xerox/index.html") as f:
    html = f.read()

# Replace src="/hero-bg.jpg" with src="/hero-bg.png?v=2"
html = html.replace('src="/hero-bg.jpg"', 'src="/hero-bg.png?v=2"')
html = html.replace('src="hero-bg.jpg"', 'src="/hero-bg.png?v=2"')

with open("/Users/riyasudeen/Documents/clien web/xerox/index.html", "w") as f:
    f.write(html)

# 2. Update premium-animations.css
with open("/Users/riyasudeen/Documents/clien web/xerox/premium-animations.css") as f:
    anim = f.read()

anim_fix = """
/* ═══ HERO IMAGE FULL VISIBILITY & SHARPNESS ═══ */
.hero {
  position: relative;
  width: 100%;
  min-height: clamp(460px, 70vh, 750px) !important;
  background: #0b0f19 !important;
  overflow: hidden !important;
  display: flex !important;
  align-items: flex-end !important;
  justify-content: center !important;
}

.hero-bg {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  width: 100% !important;
  height: 100% !important;
  z-index: 1 !important;
}

.hero-bg img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center !important;
  opacity: 1 !important;
  visibility: visible !important;
  filter: brightness(1) contrast(1) !important;
  transform: none !important;
}

.hero-overlay {
  position: absolute !important;
  inset: 0 !important;
  background: linear-gradient(to top, rgba(11, 15, 25, 0.75) 0%, rgba(11, 15, 25, 0.15) 30%, transparent 60%) !important;
  z-index: 2 !important;
  pointer-events: none !important;
}

.hero-film-grain, .hero-vignette, .hero-light-leak {
  display: none !important;
}
"""

if ".hero-bg img" in anim:
    anim += "\n\n" + anim_fix
else:
    anim += "\n\n" + anim_fix

with open("/Users/riyasudeen/Documents/clien web/xerox/premium-animations.css", "w") as f:
    f.write(anim)

# 3. Update styles.css
with open("/Users/riyasudeen/Documents/clien web/xerox/styles.css") as f:
    css = f.read()

css += "\n\n.hero-bg img { opacity: 1 !important; visibility: visible !important; object-fit: cover !important; }\n"

with open("/Users/riyasudeen/Documents/clien web/xerox/styles.css", "w") as f:
    f.write(css)

print("Applied Hero visibility fixes successfully")
