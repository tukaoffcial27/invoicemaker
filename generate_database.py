import json
import csv
import random
import os

def generate_database():
    if not os.path.exists('cities.json'):
        print("❌ Error: File cities.json TIDAK DITEMUKAN!")
        return

    with open('cities.json', 'r', encoding='utf-8') as f:
        cities_data = json.load(f)

    professions = [
        # KREATIF
        {"name": "Fotografer Pernikahan", "cat": "kreatif", "pain": "sulit melacak pelunasan sisa pembayaran setelah acara", "loss": "arus kas tersendat dan tabungan bisnis sering terpakai untuk operasional"},
        {"name": "Videografer Freelance", "cat": "kreatif", "pain": "klien meminta revisi tanpa batas karena tidak ada kontrak jelas", "loss": "waktu produktif habis untuk pekerjaan tidak berbayar"},
        {"name": "Makeup Artist (MUA)", "cat": "kreatif", "pain": "invoice manual sering hilang atau terselip di chat WhatsApp", "loss": "kehilangan kepercayaan dari klien kelas atas"},
        {"name": "Desainer Grafis", "cat": "kreatif", "pain": "klien menunda pembayaran termin kedua hingga berbulan-bulan", "loss": "sulit membayar biaya langganan software desain tepat waktu"},
        {"name": "Content Creator", "cat": "kreatif", "pain": "bingung menghitung rate card dan PPh21 dalam satu nota", "loss": "potensi penghasilan berkurang karena salah perhitungan pajak"},
        {"name": "Social Media Manager", "cat": "kreatif", "pain": "sulit membuktikan laporan kerja bulanan yang sudah terbayar", "loss": "terjadi tumpang tindih penagihan yang membingungkan klien"},
        {"name": "Editor Video", "cat": "kreatif", "pain": "proses render terhambat karena stres memikirkan tagihan belum cair", "loss": "deadline proyek berantakan dan reputasi profesional menurun"},
        {"name": "Animator 3D", "cat": "kreatif", "pain": "biaya lisensi asset sering tidak tercover di invoice awal", "loss": "keuntungan bersih menipis karena pengeluaran tak terduga"},
        {"name": "Copywriter", "cat": "kreatif", "pain": "klien korporat meminta format invoice khusus yang rumit", "loss": "pembayaran tertunda berminggu-minggu karena kesalahan format"},
        {"name": "Web Developer", "cat": "kreatif", "pain": "biaya maintenance server sering lupa ditagihkan ke klien", "loss": "harus menanggung biaya hosting dari kantong pribadi"},
        {"name": "Illustrator", "cat": "kreatif", "pain": "sulit melacak lisensi karya karena invoice tidak mencantumkan hak cipta", "loss": "karya digunakan komersial tanpa royalti yang sah"},
        {"name": "Voice Over Artist", "cat": "kreatif", "pain": "sulit menagih biaya tambahan untuk durasi penggunaan suara", "loss": "kehilangan pendapatan pasif dari hak siar"},
        {"name": "UI/UX Designer", "cat": "kreatif", "pain": "dokumentasi pembayaran startup sering tidak terorganisir", "loss": "sulit melakukan audit keuangan pribadi di akhir tahun"},
        {"name": "Wedding Organizer", "cat": "kreatif", "pain": "rekap tagihan banyak vendor dalam satu proyek sering selisih", "loss": "risiko salah bayar vendor yang merugikan margin profit"},
        {"name": "Music Producer", "cat": "kreatif", "pain": "pembagian royalti antar musisi tidak tercatat di sistem", "loss": "potensi konflik hukum dengan rekan kerja di masa depan"},
        {"name": "Architectural Photographer", "cat": "kreatif", "pain": "biaya transportasi dan akomodasi sulit direimburse", "loss": "pengeluaran pribadi membengkak untuk urusan klien"},
        {"name": "Blogger", "cat": "kreatif", "pain": "pembayaran agency sering melewati jatuh tempo 30 hari", "loss": "perputaran uang untuk operasional website terganggu"},
        {"name": "Podcast Producer", "cat": "kreatif", "pain": "biaya sewa studio fluktuatif sulit dicatat manual", "loss": "pembukuan bulanan selalu selisih dan tidak akurat"},
        {"name": "Fashion Stylist", "cat": "kreatif", "pain": "sulit menagih ganti rugi jika properti baju rusak oleh klien", "loss": "harus menanggung biaya perbaikan pakaian yang mahal"},
        {"name": "Drone Pilot", "cat": "kreatif", "pain": "risiko kerusakan alat tinggi tidak tercatat di biaya jasa", "loss": "tabungan habis untuk perbaikan alat tanpa cadangan biaya"},
        
        # KONSTRUKSI
        {"name": "Kontraktor Bangunan", "cat": "konstruksi", "pain": "penagihan termin proyek sering terlewat dari jadwal", "loss": "dana operasional beli material tahap berikutnya macet"},
        {"name": "Interior Designer", "cat": "konstruksi", "pain": "bingung merinci biaya pembelian barang titipan belanja klien", "loss": "sering terjadi selisih harga yang ditanggung sendiri"},
        {"name": "Tukang Listrik", "cat": "konstruksi", "pain": "sulit memberikan bukti pembayaran formal untuk klaim kantor", "loss": "klien perusahaan besar enggan memakai jasa kembali"},
        {"name": "Ahli Plumbing", "cat": "konstruksi", "pain": "biaya material kecil sering lupa dimasukkan ke nota", "loss": "akumulasi kerugian material merusak profit bulanan"},
        {"name": "Jasa Pasang Kanopi", "cat": "konstruksi", "pain": "sulit mengelola uang muka (DP) dari banyak pelanggan", "loss": "kehabisan modal di tengah jalan sebelum proyek selesai"},
        {"name": "Arsitek Mandiri", "cat": "konstruksi", "pain": "revisi desain terus bertambah tanpa charge tambahan", "loss": "waktu pengerjaan molor tidak sebanding dengan honor"},
        {"name": "Pembersih Kaca Gedung", "cat": "konstruksi", "pain": "risiko kerja tinggi namun asuransi tidak terinci di invoice", "loss": "perusahaan sulit klaim jika terjadi kecelakaan kerja"},
        {"name": "Jasa Cat Rumah", "cat": "konstruksi", "pain": "estimasi kebutuhan cat meleset dari invoice awal", "loss": "keuntungan habis untuk menutupi kekurangan material"},
        {"name": "Mandor Borongan", "cat": "konstruksi", "pain": "sulit membagi gaji karena catatan kas bon berantakan", "loss": "kepercayaan anak buah menurun dan proyek terbengkalai"},
        {"name": "Tukang Kayu Custom", "cat": "konstruksi", "pain": "pengerjaan furniture lama membuat invoice terlupakan", "loss": "klien lupa bayar pelunasan karena barang sudah dikirim"},
        {"name": "Jasa Pasang CCTV", "cat": "konstruksi", "pain": "sulit menagih biaya kunjungan servis kerusakan kecil", "loss": "biaya bensin lebih besar dari pendapatan servis"},
        {"name": "Ahli Taman", "cat": "konstruksi", "pain": "biaya perawatan tanaman setelah tanam tidak tertagih", "loss": "tanaman mati di lokasi klien menjadi beban kontraktor"},
        {"name": "Jasa Pasang Wallpaper", "cat": "konstruksi", "pain": "sisa bahan banyak tidak tercatat sebagai inventaris", "loss": "modal mati di stok barang sisa yang tidak terpakai"},
        {"name": "Spesialis Atap Bocor", "cat": "konstruksi", "pain": "garansi pekerjaan disalahgunakan klien tanpa bukti nota", "loss": "harus perbaikan gratis meski masa garansi habis"},
        {"name": "Jasa Sumur Bor", "cat": "konstruksi", "pain": "kedalaman sumur meleset dari estimasi awal di invoice", "loss": "biaya tenaga kerja membengkak tanpa tambahan pendapatan"},
        {"name": "Tukang Pasang Keramik", "cat": "konstruksi", "pain": "pecahnya keramik saat pemasangan tidak terhitung di biaya", "loss": "margin keuntungan habis untuk ganti keramik rusak"},
        {"name": "Jasa Bongkar Bangunan", "cat": "konstruksi", "pain": "biaya pembuangan puing ditolak klien di akhir proyek", "loss": "harus membayar biaya pembuangan sendiri ke pihak ketiga"},
        {"name": "Ahli Konstruksi Baja", "cat": "konstruksi", "pain": "kenaikan harga besi mendadak sebelum invoice cair", "loss": "proyek rugi karena harga beli lebih tinggi dari nota"},
        {"name": "Jasa Pasang Parquet", "cat": "konstruksi", "pain": "kelembaban ruangan merusak kayu tidak tercatat risikonya", "loss": "klien menuntut ganti rugi penuh atas kerusakan alamiah"},
        {"name": "Kontraktor Kolam Renang", "cat": "konstruksi", "pain": "biaya chemical awal sering dianggap gratis oleh pemilik", "loss": "pengeluaran rutin operasional menggerus keuntungan"},

        # JASA
        {"name": "Tutor Privat", "cat": "jasa", "pain": "rekap jam mengajar bulanan tidak akurat di mata wali murid", "loss": "pendapatan berkurang karena sesi dianggap belum masuk"},
        {"name": "Konsultan Pajak", "cat": "jasa", "pain": "menghabiskan waktu berjam-jam membuat format nota", "loss": "fokus analisis data klien menjadi terpecah"},
        {"name": "Pengacara Freelance", "cat": "jasa", "pain": "biaya operasional sidang sulit ditagihkan rinci", "loss": "honor pokok habis menutupi biaya perjalanan dinas"},
        {"name": "Penterjemah", "cat": "jasa", "pain": "perhitungan biaya per kata diperdebatkan klien", "loss": "waktu habis negosiasi ulang tagihan yang selesai"},
        {"name": "Personal Trainer", "cat": "jasa", "pain": "klien membatalkan sesi mendadak tanpa penalti", "loss": "kehilangan potensi pendapatan dari slot waktu kosong"},
        {"name": "Konsultan Bisnis", "cat": "jasa", "pain": "sulit melacak jam konsultasi via telepon atau VC", "loss": "banyak ilmu diberikan gratis tanpa kompensasi"},
        {"name": "Psikolog", "cat": "jasa", "pain": "administrasi tagihan berbelit mengganggu fokus empati", "loss": "kualitas layanan menurun karena beban kerja admin"},
        {"name": "Notaris", "cat": "jasa", "pain": "rekap biaya PNBP banyak membingungkan asisten", "loss": "risiko teguran instansi jika terjadi selisih bayar"},
        {"name": "Agen Properti", "cat": "jasa", "pain": "biaya iklan tidak kembali jika rumah belum laku", "loss": "modal iklan amblas tanpa kepastian komisi"},
        {"name": "Akuntan Publik", "cat": "jasa", "pain": "pengarsipan bukti bayar klien berantakan di kantor", "loss": "sulit melakukan audit internal performa bisnis"},
        {"name": "Digital Marketer", "cat": "jasa", "pain": "sulit memisahkan tagihan jasa dengan biaya iklan", "loss": "terkena pajak lebih besar karena omzet terlihat tinggi"},
        {"name": "Event Organizer", "cat": "jasa", "pain": "uang muka klien habis untuk operasional awal", "loss": "kesulitan melunasi vendor di akhir acara"},
        {"name": "Data Analyst", "cat": "jasa", "pain": "biaya komputasi cloud lupa dibebankan ke klien", "loss": "keuntungan bersih terpotong biaya server mahal"},
        {"name": "Freelancer", "cat": "jasa", "pain": "tidak memiliki slip gaji atau invoice untuk kredit", "loss": "sulit mendapatkan akses perbankan atau KPR"},
        {"name": "Guru Musik", "cat": "jasa", "pain": "biaya sewa instrumen tidak masuk nota bulanan", "loss": "aset instrumen rusak tanpa dana cadangan servis"},
        {"name": "Instruktur Yoga", "cat": "jasa", "pain": "jumlah peserta kelas tidak sesuai laporan keuangan", "loss": "potensi kebocoran pendapatan kelas"},
        {"name": "Jasa Pengetikan", "cat": "jasa", "pain": "biaya tinta dan kertas dianggap remeh pelanggan", "loss": "pendapatan bersih hanya cukup beli perlengkapan lagi"},
        {"name": "Editor Naskah", "cat": "jasa", "pain": "waktu membaca lama tidak dihargai profesional", "loss": "lelah mental tanpa kompensasi finansial layak"},
        {"name": "Life Coach", "cat": "jasa", "pain": "klien menunggak bayar karena hubungan terlalu dekat", "loss": "profesionalisme rusak oleh rasa sungkan menagih"},
        {"name": "Tour Guide", "cat": "jasa", "pain": "biaya tips dan makan tidak tercatat penghasilan", "loss": "perhitungan pajak tahunan menjadi tidak akurat"},

        # KULINER & RETAIL
        {"name": "Catering Harian", "cat": "kuliner", "pain": "rekap pesanan bulanan selisih dengan dapur", "loss": "salah kirim menu berujung komplain pedas"},
        {"name": "Pemilik Laundry", "cat": "retail", "pain": "nota kertas sering basah atau hilang di baju", "loss": "kekeliruan pengambilan baju merusak nama baik"},
        {"name": "Bengkel Motor", "cat": "retail", "pain": "stok sparepart keluar tidak tercatat di nota", "loss": "modal habis untuk stok tapi uang tidak kembali"},
        {"name": "Pet Shop", "cat": "retail", "pain": "biaya titip hewan tidak dibayar penuh saat jemput", "loss": "menanggung biaya makan tanpa bayaran pemilik"},
        {"name": "Toko Online", "cat": "retail", "pain": "sulit buat invoice profesional untuk instansi", "loss": "kehilangan peluang pesanan besar atau bulk order"},
        {"name": "Warung Kopi", "cat": "kuliner", "pain": "pengeluaran bahan baku harian tidak terkontrol", "loss": "bisnis ramai tapi pemilik tidak pegang uang"},
        {"name": "Jasa Sewa Mobil", "cat": "umum", "pain": "biaya denda telat sulit ditagih ke penyewa", "loss": "kerugian waktu sewa untuk pelanggan berikutnya"},
        {"name": "Barbershop", "cat": "umum", "pain": "sulit melacak performa kapster per kepala", "loss": "pembagian komisi tidak adil memicu konflik"},
        {"name": "Florist", "cat": "retail", "pain": "biaya kirim berubah sesuai jarak lokasi", "loss": "ongkos kirim nomok karena salah estimasi awal"},
        {"name": "Jasa Titip", "cat": "umum", "pain": "perubahan kurs saat belanja tidak tercatat nota", "loss": "keuntungan habis karena selisih kurs merugikan"},
        {"name": "Sewa Alat Camping", "cat": "umum", "pain": "kerusakan alat saat mendaki tidak diganti penyewa", "loss": "aset bisnis habis rusak tanpa biaya perbaikan"},
        {"name": "Studio Foto", "cat": "kreatif", "pain": "biaya overtime studio sering lupa dimasukkan", "loss": "listrik membengkak tanpa tambahan pendapatan"},
        {"name": "Jasa Cuci Sepatu", "cat": "umum", "pain": "sulit lacak status pengerjaan dari nota manual", "loss": "sepatu lama tidak diambil memenuhi rak"},
        {"name": "Bakery Rumahan", "cat": "kuliner", "pain": "biaya packaging cantik lupa masuk harga jual", "loss": "terlihat premium tapi margin sangat tipis"},
        {"name": "Frozen Food", "cat": "kuliner", "pain": "biaya listrik freezer mahal tidak terhitung harga", "loss": "bisnis rugi karena beban operasional listrik"},
        {"name": "Service AC", "cat": "umum", "pain": "sulit tagih biaya freon yang habis saat pengerjaan", "loss": "bolak-balik toko material tanpa biaya bensin"},
        {"name": "Toko Bangunan", "cat": "retail", "pain": "utang mandor menumpuk sulit dilacak tanpa sistem", "loss": "macetnya arus kas membuat toko terancam tutup"},
        {"name": "Jasa Setrika", "cat": "umum", "pain": "pelanggan komplain baju kurang licin tanpa bukti", "loss": "reputasi menurun akibat subjektivitas komplain"},
        {"name": "Cleaning Service", "cat": "umum", "pain": "biaya pembersih kimia khusus tidak tercatat invoice", "loss": "modal habis untuk obat pembersih mahal"},
        {"name": "Desain Undangan", "cat": "kreatif", "pain": "revisi teks berkali-kali menyita waktu kerja", "loss": "pendapatan per jam menjadi sangat rendah"},
        {"name": "Rental Playstation", "cat": "umum", "pain": "billing waktu dimanipulasi oknum penjaga", "loss": "kebocoran pendapatan harian sulit dideteksi"},
        {"name": "Toko Aksesoris HP", "cat": "retail", "pain": "garansi barang diklaim tanpa nota fisik", "loss": "harus ganti barang yang bukan dibeli dari toko"},
        {"name": "Custom Mahar", "cat": "kreatif", "pain": "harga bingkai naik mendadak tidak tercover", "loss": "bisnis merugi karena kenaikan bahan baku"},
        {"name": "Catering Diet", "cat": "kuliner", "pain": "permintaan menu custom harian memusingkan admin", "loss": "operasional dapur kacau karena admin buruk"},
        {"name": "Toko Helm", "cat": "retail", "pain": "stok gudang tidak sesuai nota penjualan", "loss": "risiko kehilangan barang akibat kelalaian"},
        {"name": "Jasa Jahit", "cat": "umum", "pain": "klien tidak ambil baju selesai berbulan-bulan", "loss": "modal kain dan tenaga tertahan di barang"},
        {"name": "Percetakan Spanduk", "cat": "retail", "pain": "biaya setting desain diminta gratis pelanggan", "loss": "waktu desainer terbuang tanpa nilai finansial"},
        {"name": "Basmi Hama", "cat": "umum", "pain": "garansi hama tidak kembali sulit dibuktikan", "loss": "harus kunjungan ulang gratis yang merugikan"},
        {"name": "Toko Sepeda", "cat": "retail", "pain": "biaya servis ringan lupa ditagih saat beli unit", "loss": "beban kerja mekanik tinggi tanpa pemasukan"},
        {"name": "Apotek Rakyat", "cat": "retail", "pain": "obat expired tidak terdeteksi karena nota berantakan", "loss": "kerugian finansial akibat barang dibuang"},
        {"name": "Pindahan Rumah", "cat": "umum", "pain": "barang lecet di jalan tidak tercover nota", "loss": "tuntutan ganti rugi klien melebihi biaya jasa"},
        {"name": "Toko Alat Tulis", "cat": "retail", "pain": "pembelian eceran instansi sulit nota gabungan", "loss": "pelanggan instansi pindah ke toko lain"},
        {"name": "Service Laptop", "cat": "umum", "pain": "biaya cek tidak dibayar jika tidak jadi servis", "loss": "waktu dan keahlian teknisi terbuang sia-sia"},
        {"name": "Toko Pancing", "cat": "retail", "pain": "sulit kelola retur pelanggan ke distributor", "loss": "modal tertahan di barang rusak tidak terjual"},
        {"name": "Henna Artist", "cat": "kreatif", "pain": "biaya transportasi ke lokasi sering lupa dihitung", "loss": "honor habis di jalan hanya untuk bensin"},
        {"name": "Toko Oleh-oleh", "cat": "retail", "pain": "sulit buat invoice rombongan bus pariwisata", "loss": "transaksi lama membuat pelanggan tidak nyaman"},
        {"name": "Akupuntur", "cat": "umum", "pain": "rekap kunjungan pasien per bulan manual/lambat", "loss": "pasien lama tidak dipantau untuk sesi lanjut"},
        {"name": "Toko Jam", "cat": "retail", "pain": "biaya ganti baterai dianggap sepele pelanggan", "loss": "margin kecil jika tidak dikelola merusak profit"},
        {"name": "Kalibrasi Alat", "cat": "umum", "pain": "sertifikat kalibrasi hilang karena nota tidak digital", "loss": "klien kesulitan saat ada audit resmi"},
        {"name": "Distributor Telur", "cat": "retail", "pain": "risiko telur pecah kirim tidak terhitung nota", "loss": "keuntungan harian tergerus penyusutan barang"},
    ]

    with open('database_pseo.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['city', 'city_slug', 'profession', 'prof_slug', 'category', 'pain_point', 'business_loss'])
        
        for _ in range(1000):
            c = random.choice(cities_data)
            p = random.choice(professions)
            
            p_slug = p['name'].lower().replace(" ", "-").replace("(", "").replace(")", "")
            
            writer.writerow([
                c['city'], 
                c['slug'], 
                p['name'], 
                p_slug, 
                p['cat'], 
                p['pain'], 
                p['loss'] # Kunci sudah disamakan menjadi 'loss'
            ])

    print("✨ Sukses! database_pseo.csv siap dengan 1000 baris.")

if __name__ == "__main__":
    generate_database()