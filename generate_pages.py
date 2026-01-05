import pandas as pd
import os
import shutil

# Konfigurasi
base_url = "https://invoicemaker.guidify.app"
csv_file = "database_pseo.csv"
template_file = "template.html"
output_dir = "public/layanan"

# Reset: Hapus folder public jika ada agar bersih, lalu buat baru
if os.path.exists('public'):
    shutil.rmtree('public')

# Membuat folder public/layanan secara otomatis
os.makedirs(output_dir, exist_ok=True)

# Baca Data & Template
df = pd.read_csv(csv_file)
with open(template_file, 'r', encoding='utf-8') as f:
    template_content = f.read()

sitemap_urls = []

print("🚀 Memulai proses generate...")

for index, row in df.iterrows():
    # PERBAIKAN: Mengubah "/" menjadi "-" agar tidak dianggap folder oleh macOS
    prof_slug = str(row['prof_slug']).replace("/", "-")
    city_slug = str(row['city_slug'])
    
    slug = f"{prof_slug}-{city_slug}"
    url = f"{base_url}/layanan/{slug}"
    sitemap_urls.append(url)
    
    # Hanya generate 200 file fisik pertama
    if index < 200:
        content = template_content
        content = content.replace("{{city}}", str(row['city']))
        content = content.replace("{{profession}}", str(row['profession']))
        content = content.replace("{{pain_point}}", str(row['pain_point']))
        content = content.replace("{{business_loss}}", str(row['business_loss']))
        
        file_path = os.path.join(output_dir, f"{slug}.html")
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(content)

# Membuat Sitemap
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for loc in sitemap_urls:
    sitemap_content += f'  <url><loc>{loc}</loc><priority>0.8</priority></url>\n'
sitemap_content += '</urlset>'

with open("public/sitemap.xml", "w", encoding='utf-8') as f:
    f.write(sitemap_content)

# Salin index.html utama ke public
if os.path.exists('index.html'):
    shutil.copy('index.html', 'public/index.html')

print(f"✅ Selesai! Cek folder 'public/layanan' di VS Code Anda.")