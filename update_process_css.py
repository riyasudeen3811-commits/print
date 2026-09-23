import os

with open("/Users/riyasudeen/Documents/clien web/xerox/styles.css") as f:
    css = f.read()

# Replace or add process card styles
old_process_css = """/* ═══ PROCESS STEPS SHOWCASE ═══ */
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

.process-card p { font-size: 0.88rem; color: var(--text-muted); }"""

new_process_css = """/* ═══ PROCESS STEPS SHOWCASE (WITH VISUAL STEP IMAGES) ═══ */
.process-showcase { background: #ffffff; }

.process-steps-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 24px;
}

.process-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
}

.process-card:hover {
  transform: translateY(-6px);
  border-color: var(--primary);
  box-shadow: var(--shadow-md);
}

.process-card-image {
  position: relative;
  width: 100%;
  height: 180px;
  overflow: hidden;
  background: #f1f5f9;
}

.process-card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.process-card:hover .process-card-image img {
  transform: scale(1.08);
}

.step-num-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  background: var(--primary);
  color: #ffffff;
  font-family: 'Outfit', sans-serif;
  font-size: 0.85rem;
  font-weight: 800;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  box-shadow: 0 4px 10px rgba(37,99,235,0.35);
}

.process-card-content {
  padding: 20px;
}

.process-card-content h3 {
  font-size: 1.15rem;
  margin-bottom: 8px;
}

.process-card-content p {
  font-size: 0.88rem;
  color: var(--text-muted);
}"""

if old_process_css in css:
    css = css.replace(old_process_css, new_process_css)
else:
    css += "\n\n" + new_process_css

with open("/Users/riyasudeen/Documents/clien web/xerox/styles.css", "w") as f:
    f.write(css)

print("Updated styles.css with Process Step Images styling")
