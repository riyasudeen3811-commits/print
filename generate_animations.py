import os

anim_css = """/* ══════════════════════════════════════════════════════════════════
   ADHA PRINTS — Ultra-Premium Cinematic Animation Layer
   ══════════════════════════════════════════════════════════════════ */

/* Hero Container */
.hero {
  position: relative;
  min-height: 82vh;
  width: 100%;
  overflow: hidden;
  background: #000000;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}

/* Background Image Showcase — Crisp, Bright & Vivid */
.hero-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.hero-bg img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  transform: scale(1.02);
  animation: kenBurnsZoom 24s ease-in-out infinite alternate;
  filter: brightness(1.02) contrast(1.03) saturate(1.04);
}

@keyframes kenBurnsZoom {
  0% { transform: scale(1.02) translate(0, 0); }
  50% { transform: scale(1.06) translate(-8px, -4px); }
  100% { transform: scale(1.03) translate(6px, 4px); }
}

/* Very subtle bottom gradient overlay so text/CTA buttons are legible, while keeping image 100% visible */
.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.75) 0%, rgba(0, 0, 0, 0.2) 30%, transparent 60%);
  z-index: 3;
  pointer-events: none;
}

/* Floating particles */
.cinematic-particles {
  position: absolute;
  inset: 0;
  z-index: 4;
  pointer-events: none;
}

.particle {
  position: absolute;
  width: 3px;
  height: 3px;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 50%;
  box-shadow: 0 0 6px rgba(255, 255, 255, 0.8);
  animation: floatParticle 8s infinite linear;
}

.particle:nth-child(1) { left: 15%; top: 80%; animation-duration: 7s; }
.particle:nth-child(2) { left: 35%; top: 90%; animation-duration: 9s; animation-delay: 1s; }
.particle:nth-child(3) { left: 55%; top: 85%; animation-duration: 6s; animation-delay: 2s; }
.particle:nth-child(4) { left: 75%; top: 95%; animation-duration: 10s; animation-delay: 0.5s; }
.particle:nth-child(5) { left: 85%; top: 75%; animation-duration: 8s; animation-delay: 3s; }

@keyframes floatParticle {
  0% { transform: translateY(0) scale(1); opacity: 0; }
  20% { opacity: 0.8; }
  80% { opacity: 0.8; }
  100% { transform: translateY(-300px) scale(0.4); opacity: 0; }
}

/* Hero Content */
.hero-content-imageonly {
  position: relative;
  z-index: 10;
  width: 100%;
  padding: 0 24px 48px;
  display: flex;
  justify-content: center;
}

.hero-bottom-cta {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  justify-content: center;
}

.hero-cta-btn {
  box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important;
  backdrop-filter: blur(8px);
}

/* Scroll Reveals */
.reveal, .reveal-left, .reveal-right, .stagger-children > * {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.reveal-left { transform: translateX(-40px); }
.reveal-right { transform: translateX(40px); }

.reveal.visible, .reveal-left.visible, .reveal-right.visible, .stagger-children > *.visible {
  opacity: 1;
  transform: translate(0, 0);
}

/* Card Shine Hover Effect */
.card-shine {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 5;
}

/* Cursor Glow */
.cursor-glow {
  position: fixed;
  top: 0;
  left: 0;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(37,99,235,0.08) 0%, rgba(13,148,136,0.03) 40%, transparent 70%);
  pointer-events: none;
  z-index: 999;
  border-radius: 50%;
  transform: translate(-50%, -50%);
}
"""

with open("/Users/riyasudeen/Documents/clien web/xerox/premium-animations.css", "w") as f:
    f.write(anim_css)

print("Updated premium-animations.css successfully")
