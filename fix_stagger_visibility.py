import os

# 1. Update premium-animations.css
with open("/Users/riyasudeen/Documents/clien web/xerox/premium-animations.css") as f:
    anim = f.read()

anim_old = """.reveal, .reveal-left, .reveal-right, .stagger-children > * {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.reveal-left { transform: translateX(-40px); }
.reveal-right { transform: translateX(40px); }

.reveal.visible, .reveal-left.visible, .reveal-right.visible, .stagger-children > *.visible {
  opacity: 1;
  transform: translate(0, 0);
}"""

anim_new = """.reveal, .reveal-left, .reveal-right {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.reveal-left { transform: translateX(-40px); }
.reveal-right { transform: translateX(40px); }

.reveal.visible, .reveal-left.visible, .reveal-right.visible, .stagger-children.visible > *, .stagger-children > * {
  opacity: 1 !important;
  transform: translate(0, 0) !important;
}"""

if anim_old in anim:
    anim = anim.replace(anim_old, anim_new)
else:
    anim += "\n\n.stagger-children > * { opacity: 1 !important; transform: none !important; }\n"

with open("/Users/riyasudeen/Documents/clien web/xerox/premium-animations.css", "w") as f:
    f.write(anim)

# 2. Update styles.css
with open("/Users/riyasudeen/Documents/clien web/xerox/styles.css") as f:
    css = f.read()

css += "\n\n/* Ensure all product & process cards are 100% visible */\n.products-grid > *, .process-steps-grid > *, .stagger-children > * {\n  opacity: 1 !important;\n  transform: none !important;\n}\n"

with open("/Users/riyasudeen/Documents/clien web/xerox/styles.css", "w") as f:
    f.write(css)

# 3. Update src/main.js
with open("/Users/riyasudeen/Documents/clien web/xerox/src/main.js") as f:
    js = f.read()

js_old = """    if (productsGrid) {
      productsGrid.style.opacity = '0';
      productsGrid.style.transform = 'translateY(15px)';
      setTimeout(() => {
        productsGrid.innerHTML = filtered.map(p => `
          <div class="product-card" data-id="${p.id}">
            <div class="product-card-image">
              <img src="${p.img}" alt="${p.title}" loading="lazy" decoding="async" width="600" height="400" />
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
      }, 150);
    }"""

js_new = """    if (productsGrid) {
      productsGrid.style.opacity = '1';
      productsGrid.style.transform = 'none';
      productsGrid.innerHTML = filtered.map(p => `
        <div class="product-card visible" data-id="${p.id}">
          <div class="product-card-image">
            <img src="${p.img}" alt="${p.title}" loading="lazy" decoding="async" width="600" height="400" />
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
    }"""

if js_old in js:
    js = js.replace(js_old, js_new)

with open("/Users/riyasudeen/Documents/clien web/xerox/src/main.js", "w") as f:
    f.write(js)

print("Applied opacity fix across all files successfully")
