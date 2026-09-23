import os

with open("/Users/riyasudeen/Documents/clien web/xerox/styles.css") as f:
    css = f.read()

marquee_css = """
/* ═══ HERO BOTTOM RUNNING MARQUEE BANNER ═══ */
.hero-services-marquee {
  background: #0b0f19;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  overflow: hidden;
  padding: 14px 0;
  position: relative;
  z-index: 20;
  box-shadow: 0 6px 24px rgba(0,0,0,0.4);
}

.hero-marquee-track {
  display: flex;
  width: max-content;
  animation: heroMarqueeScroll 28s linear infinite;
}

.hero-services-marquee:hover .hero-marquee-track {
  animation-play-state: paused;
}

@keyframes heroMarqueeScroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

.hero-marquee-content {
  display: flex;
  align-items: center;
  gap: 28px;
  padding: 0 14px;
}

.marquee-item {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #e2e8f0;
  white-space: nowrap;
  font-size: 0.92rem;
  font-weight: 600;
  padding: 8px 18px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-full);
  transition: var(--transition);
}

.marquee-item:hover {
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  border-color: var(--primary);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37,99,235,0.4);
}

.m-icon {
  font-size: 1.15rem;
}

.m-label {
  letter-spacing: 0.02em;
}
"""

if ".hero-services-marquee" not in css:
    css += "\n\n" + marquee_css

with open("/Users/riyasudeen/Documents/clien web/xerox/styles.css", "w") as f:
    f.write(css)

print("Appended marquee CSS to styles.css")
