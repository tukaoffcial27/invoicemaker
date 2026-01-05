from flask import Flask, render_template_string, send_from_directory
import pandas as pd
import os

app = Flask(__name__)

# Load data & template
df = pd.read_csv('database_pseo.csv')
with open('template.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# --- TAMBAHKAN INI: Rute untuk Halaman Utama ---
@app.route('/')
def home():
    if os.path.exists('index.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    return "File index.html tidak ditemukan", 404

# --- Rute untuk 1000 Halaman pSEO ---
@app.route('/layanan/<slug>')
def serve_dynamic_page(slug):
    match = None
    for _, row in df.iterrows():
        current_prof_slug = str(row['prof_slug']).replace("/", "-")
        current_slug = f"{current_prof_slug}-{row['city_slug']}"
        
        if current_slug == slug:
            match = row
            break
    
    if match is not None:
        content = template_content.replace("{{city}}", str(match['city']))
        content = content.replace("{{profession}}", str(match['profession']))
        content = content.replace("{{pain_point}}", str(match['pain_point']))
        content = content.replace("{{business_loss}}", str(match['business_loss']))
        return render_template_string(content)
    
    return "Halaman tidak ditemukan", 404