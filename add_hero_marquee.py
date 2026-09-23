import os

with open("/Users/riyasudeen/Documents/clien web/xerox/index.html") as f:
    html = f.read()

hero_section_end = "</section>"
# Find first </section> which ends hero
hero_idx = html.find(hero_section_end)

marquee_banner_html = """
    <!-- ═══ HERO BOTTOM RUNNING MARQUEE BANNER (Icon Strip) ═══ -->
    <div class="hero-services-marquee">
      <div class="hero-marquee-track">
        <div class="hero-marquee-content">
          <div class="marquee-item"><span class="m-icon">💳</span> <span class="m-label">Business Cards</span></div>
          <div class="marquee-item"><span class="m-icon">✉️</span> <span class="m-label">Letterhead</span></div>
          <div class="marquee-item"><span class="m-icon">📬</span> <span class="m-label">Envelopes</span></div>
          <div class="marquee-item"><span class="m-icon">📄</span> <span class="m-label">Pamphlets</span></div>
          <div class="marquee-item"><span class="m-icon">📖</span> <span class="m-label">Brochures</span></div>
          <div class="marquee-item"><span class="m-icon">📑</span> <span class="m-label">Flyers</span></div>
          <div class="marquee-item"><span class="m-icon">📜</span> <span class="m-label">Hand Bits</span></div>
          <div class="marquee-item"><span class="m-icon">💌</span> <span class="m-label">Invitations</span></div>
          <div class="marquee-item"><span class="m-icon">🏷️</span> <span class="m-label">Stickers</span></div>
          <div class="marquee-item"><span class="m-icon">🖨️</span> <span class="m-label">Offset Printing</span></div>
          <div class="marquee-item"><span class="m-icon">🎨</span> <span class="m-label">Multi Colour Printing</span></div>
          <div class="marquee-item"><span class="m-icon">🖼️</span> <span class="m-label">Screen Printing</span></div>
          <div class="marquee-item"><span class="m-icon">📚</span> <span class="m-label">All type of Binding</span></div>
          <div class="marquee-item"><span class="m-icon">🪪</span> <span class="m-label">Id Card</span></div>
          <div class="marquee-item"><span class="m-icon">💻</span> <span class="m-label">D.T.P</span></div>
        </div>
        <!-- Duplicated content for seamless 100% loop -->
        <div class="hero-marquee-content" aria-hidden="true">
          <div class="marquee-item"><span class="m-icon">💳</span> <span class="m-label">Business Cards</span></div>
          <div class="marquee-item"><span class="m-icon">✉️</span> <span class="m-label">Letterhead</span></div>
          <div class="marquee-item"><span class="m-icon">📬</span> <span class="m-label">Envelopes</span></div>
          <div class="marquee-item"><span class="m-icon">📄</span> <span class="m-label">Pamphlets</span></div>
          <div class="marquee-item"><span class="m-icon">📖</span> <span class="m-label">Brochures</span></div>
          <div class="marquee-item"><span class="m-icon">📑</span> <span class="m-label">Flyers</span></div>
          <div class="marquee-item"><span class="m-icon">📜</span> <span class="m-label">Hand Bits</span></div>
          <div class="marquee-item"><span class="m-icon">💌</span> <span class="m-label">Invitations</span></div>
          <div class="marquee-item"><span class="m-icon">🏷️</span> <span class="m-label">Stickers</span></div>
          <div class="marquee-item"><span class="m-icon">🖨️</span> <span class="m-label">Offset Printing</span></div>
          <div class="marquee-item"><span class="m-icon">🎨</span> <span class="m-label">Multi Colour Printing</span></div>
          <div class="marquee-item"><span class="m-icon">🖼️</span> <span class="m-label">Screen Printing</span></div>
          <div class="marquee-item"><span class="m-icon">📚</span> <span class="m-label">All type of Binding</span></div>
          <div class="marquee-item"><span class="m-icon">🪪</span> <span class="m-label">Id Card</span></div>
          <div class="marquee-item"><span class="m-icon">💻</span> <span class="m-label">D.T.P</span></div>
        </div>
      </div>
    </div>
"""

new_html = html[:hero_idx+9] + marquee_banner_html + html[hero_idx+9:]

with open("/Users/riyasudeen/Documents/clien web/xerox/index.html", "w") as f:
    f.write(new_html)

print("Added Hero Services Marquee Banner under Hero section")
