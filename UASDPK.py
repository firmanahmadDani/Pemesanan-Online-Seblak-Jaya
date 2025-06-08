import json

# ======================= KELAS ITEM DASAR ==========================
class Item:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def total_harga(self, jumlah):
        return self.harga * jumlah

# =================== KELAS TURUNAN MIE DAN SEBLAK ==================
class MieJebew(Item):
    pass

class Seblak(Item):
    pass

# ============== ITEM DETAIL KELAS (LEVEL, KATEGORI, PEMBELI) =======
class ItemDetail:
    def __init__(self, item, jumlah, kategori, pembeli_ke):
        self.item = item
        self.jumlah = jumlah
        self.kategori = kategori
        self.pembeli_ke = pembeli_ke

    def subtotal(self):
        return self.item.total_harga(self.jumlah)

# =================== KELAS TRANSAKSI DAN STRUK =====================
class Transaksi:
    def __init__(self, nama_penjual):
        self.nama_penjual = nama_penjual
        self.items = []
        self.total = 0
        self.detail_pembeli = {}

    def tambah_item(self, detail):
        self.items.append(detail)
        self.total += detail.subtotal()

    def set_detail_pembeli(self, pembeli_ke, nama, kuah=None, rasa=None, level_mie=None, level_seblak=None):
        self.detail_pembeli[pembeli_ke] = {
            "nama": nama,
            "kuah": kuah,
            "rasa": rasa,
            "level_mie": level_mie,
            "level_seblak": level_seblak
        }

    def cetak_struk(self, metode_bayar, uang_dibayar):
        lebar = 85
        garis = "+" + "-" * lebar + "+"

        print("\n" + garis)
        print(f"|{'STRUK PEMBELIAN':^{lebar}}|")
        print(f"|{'Warung Seblak Jaya - SMKN 1 Probolinggo':^{lebar}}|")
        print(garis)
        print(f"| {'Penjual':<12}: {self.nama_penjual:<{lebar - 15}}|")
        print(garis)
        print(f"| {'No':<3} {'Pembeli':<15} {'Nama Item':<30} {'Jumlah':>9} {'Subtotal (Rp)':>22} |")
        print(garis)

        for i, detail in enumerate(self.items, 1):
            nama_pembeli = self.detail_pembeli[detail.pembeli_ke]['nama']
            # Limit to 15 chars if too long, and pad to 15
            nama_pembeli_display = f"{nama_pembeli[:15]:<15}"
            # Limit to 30 chars if too long, and pad to 30
            nama_item_display = f"{detail.item.nama[:30]:<30}"
            subtotal_formatted = f"{detail.subtotal():,}"
            print(f"| {i:<3} {nama_pembeli_display} {nama_item_display} {detail.jumlah:>9} {subtotal_formatted:>22} |")

        print(garis)

        for no, detail in self.detail_pembeli.items():
            # Calculate remaining space for header. The total length of the line should be 'lebar' characters between '|' and '|'
            header_content = f"Pembeli {no} ({detail['nama']})"
            # Calculate spaces needed: total width - (length of content + 2 for initial ' ' + 1 for final ' ')
            remaining_space_header = lebar - len(header_content) - 2 
            print(f"| {header_content}{' ' * remaining_space_header} |")
            
            # Check if there are any specific details for this buyer
            has_details = False
            for label, key in [("Level Mie Jebew", "level_mie"), ("Level Seblak", "level_seblak"),
                               ("Kuah Seblak", "kuah"), ("Rasa Seblak", "rasa")]:
                if detail[key]:
                    has_details = True
                    value = str(detail[key])
                    # Calculate remaining space for detail lines.
                    # The total length of the line should be 'lebar' characters between '|' and '|'
                    # Content starts with '   ' (3 spaces), then label, then ': ', then value.
                    # So, length to account for: 3 (indent) + len(label) + 2 (': ') + len(value)
                    
                    # Pad label to a fixed width (e.g., 15) for consistent alignment
                    label_padded = f"{label:<15}"
                    content_length = len(f"   {label_padded}: {value}") 
                    remaining_space_detail = lebar - content_length -     -0 # -1 for the final ' ' before '|'
                    print(f"|   {label_padded}: {value}{' ' * remaining_space_detail}|")
            
            # Add an empty line if there were details for this buyer to separate from next buyer/total
            if has_details and no != len(self.detail_pembeli):
                print(f"|{' ' * lebar}|")
        
        print(garis)
        print(f"| {'Total Pembelian':<60} Rp{self.total:>20,} |")
        print(f"| {'Bayar (' + metode_bayar.upper() + ')':<60} Rp{uang_dibayar:>20,} |")
        print(f"| {'Kembalian':<60} Rp{(uang_dibayar - self.total):>20,} |")
        print(garis)
        print(f"|{'Terima kasih! Jaga kebersihan & K3LH!':^{lebar}}|")
        print(garis)

    def simpan_ke_json(self, nama_file='transaksi.json'):
        data = {
            "penjual": self.nama_penjual,
            "total": self.total,
            "pembeli": [],
            "items": []
        }

        for no, detail in self.detail_pembeli.items():
            data["pembeli"].append({
                "nomor": no,
                "nama": detail["nama"],
                "kuah": detail["kuah"],
                "rasa": detail["rasa"],
                "level_mie": detail["level_mie"],
                "level_seblak": detail["level_seblak"]
            })

        for detail in self.items:
            data["items"].append({
                "pembeli_ke": detail.pembeli_ke,
                "nama_pembeli": self.detail_pembeli[detail.pembeli_ke]["nama"],
                "nama_item": detail.item.nama,
                "kategori": detail.kategori,
                "jumlah": detail.jumlah,
                "subtotal": detail.subtotal()
            })

        with open(nama_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"\n📁 Data transaksi berhasil disimpan ke file '{nama_file}'.")

# =================== MENU YANG TERSEDIA =============================
def tampilkan_menu(menu):
    for i, item in enumerate(menu):
        print(f"{i+1}. {item.nama} - Rp{item.harga:,}")

# =================== PROGRAM UTAMA =================================
def main():
    print("Selamat datang di Warung Seblak Jaya - SMKN 1 Probolinggo")
    print("Jaga K3LH: Kebersihan, Keselamatan, Keamanan, dan Lingkungan Hidup")

    nama_penjual = input("Masukkan nama penjual: ")
    transaksi = Transaksi(nama_penjual)

    mie_menu = [
        MieJebew("Mie Jebew Original", 10000),
        MieJebew("Toping Pentol", 1000),
        MieJebew("Toping Sosis", 2000),
        MieJebew("Toping Telur", 2000),
        MieJebew("Toping Dumpling", 2000)
    ]

    seblak_menu = [
        Seblak("Sosis", 2000),
        Seblak("Pentol", 1000),
        Seblak("Cikuwa", 2000),
        Seblak("Dumpling", 2000),
        Seblak("Krupuk", 1000),
        Seblak("Mie Eko", 1000),
        Seblak("Jamur Enoki", 2000),
        Seblak("Sayur (sepuasnya)", 2000)
    ]

    while True:
        try:
            jumlah_pembeli = int(input("Berapa jumlah pembeli? (1-5): "))
            if 1 <= jumlah_pembeli <= 5:
                break
            else:
                print("Masukkan angka antara 1 sampai 5.")
        except ValueError:
            print("Input harus berupa angka!")

    for i in range(1, jumlah_pembeli + 1):
        print(f"\n--- Pembeli {i} ---")
        nama_pembeli = input(f"Masukkan nama pembeli ke-{i}: ")
        kuah, rasa, level_mie, level_seblak = None, None, None, None

        while True:
            print("\nPilih kategori:")
            print("1. Mie Jebew")
            print("2. Seblak")
            print("3. Selesai Memilih untuk Pembeli Ini")
            kategori = input("Pilih (1/2/3): ").strip()

            if kategori == "1":
                # Check if "Mie Jebew Original" has been added for the current buyer
                has_original_mie = any(isinstance(item_detail.item, MieJebew) and "Original" in item_detail.item.nama and item_detail.pembeli_ke == i for item_detail in transaksi.items)
                if not has_original_mie:
                    original_mie = next((item for item in mie_menu if "Original" in item.nama), None)
                    if original_mie:
                        transaksi.tambah_item(ItemDetail(original_mie, 1, "Mie Jebew", i))

                while True:
                    print("\n--- Menu Mie Jebew ---")
                    # Display toppings starting from index 1 (excluding Mie Jebew Original)
                    for idx, item in enumerate(mie_menu[1:]):
                        print(f"{idx+1}. {item.nama} - Rp{item.harga:,}")
                    
                    try:
                        idx_input = input("Pilih topping Mie Jebew (0 untuk selesai): ")
                        if idx_input == "0":
                            break
                        
                        # Adjust index to match the full mie_menu list (mie_menu[0] is Original)
                        selected_idx = int(idx_input) 

                        if not (0 < selected_idx < len(mie_menu)): # Ensure index is valid for toppings
                            print("Pilihan tidak valid.")
                            continue
                        
                        jumlah = int(input("Jumlah: "))
                        if jumlah <= 0:
                            print("Jumlah harus lebih dari 0.")
                            continue
                        
                        transaksi.tambah_item(ItemDetail(mie_menu[selected_idx], jumlah, "Mie Jebew", i))
                    except ValueError:
                        print("Input tidak valid. Masukkan angka.")
                level_mie = input("Level pedas Mie Jebew (1-5): ")

            elif kategori == "2":
                if not kuah:
                    kuah = input("Jenis kuah Seblak (Berkuah/Nyemek): ").strip().capitalize()
                    rasa = input("Rasa Seblak (Asin/Manis/Gurih Manis): ").strip().capitalize()
                while True:
                    print("\n--- Menu Seblak ---")
                    tampilkan_menu(seblak_menu)
                    try:
                        idx = int(input("Pilih topping Seblak (0 untuk selesai): ")) - 1
                        if idx == -1:
                            break
                        if not (0 <= idx < len(seblak_menu)):
                            print("Pilihan tidak valid.")
                            continue
                        jumlah = int(input("Jumlah: "))
                        if jumlah <= 0:
                            print("Jumlah harus lebih dari 0.")
                            continue
                        transaksi.tambah_item(ItemDetail(seblak_menu[idx], jumlah, "Seblak", i))
                    except ValueError:
                        print("Input tidak valid. Masukkan angka.")
                level_seblak = input("Level pedas Seblak (1-5): ")

            elif kategori == "3":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

        transaksi.set_detail_pembeli(i, nama_pembeli, kuah, rasa, level_mie, level_seblak)

    print(f"\nTotal semua pembelian: Rp{transaksi.total:,}")

    while True:
        metode_bayar = input("Pilih metode pembayaran (Cash/QRIS): ").strip().lower()
        if metode_bayar in ['cash', 'qris']:
            break
        else:
            print("Metode tidak valid. Silakan pilih 'Cash' atau 'QRIS'.")

    while True:
        try:
            uang_dibayar = int(input("Masukkan nominal uang dibayar: "))
            if uang_dibayar >= transaksi.total:
                break
            else:
                print("Uang tidak cukup! Silakan masukkan nominal yang lebih besar atau sama dengan total pembelian.")
        except ValueError:
            print("Masukkan angka yang valid untuk nominal uang dibayar.")

    transaksi.cetak_struk(metode_bayar, uang_dibayar)
    transaksi.simpan_ke_json()

    tampilkan = input("Ingin lihat isi file JSON? (y/n): ").strip().lower()
    if tampilkan == 'y':
        try:
            with open('transaksi.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                print("\n📄 Isi File JSON:")
                print(json.dumps(data, indent=4, ensure_ascii=False))
        except FileNotFoundError:
            print("File 'transaksi.json' tidak ditemukan.")
        except json.JSONDecodeError:
            print("Error saat membaca file JSON. Pastikan formatnya benar.")


# =================== JALANKAN PROGRAM ===============================
if __name__ == "__main__":
    main()