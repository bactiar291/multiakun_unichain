# Selamat datang di repositori Bactiar291! 🎉
# utamakan "git pull" sebelum menjalankan
## Tentang Proyek Ini
Proyek ini dibuat oleh Bactiar291 untuk tujuan memudahkan pengguna yang menggunakan Unichain. Proyek ini bertujuan untuk memudahkan pengguna dalam melaksanakan transaksi secara otomatis.
![Gambar](https://raw.githubusercontent.com/bactiar291/multiakun_unichain/main/mult.png)

Jika Anda meng-clone atau fork repositori ini, pastikan untuk membaca instruksi di bawah ini untuk memulai.

### Tracking Trx Di explorer Cek 👇
[https://sepolia.uniscan.xyz/](https://sepolia.uniscan.xyz/)

## Cara Menggunakan

1. Clone repositori ini ke mesin lokal Anda:
   ```bash
   git clone https://github.com/bactiar291/multiakun_unichain.git
Masuk ke folder yang telah di-clone:
```bash
cd multiakun_unichain
```
Untuk meng-install dependencies secara manual (jika diperlukan):
```bash
pip install -r requirements.txt
```
Jangan Lupa Untuk Mengganti accounts.json:
```bash
nano accounts.json
```
Isi Alamat Address Dan Private Key Seperti Ini:
```bash
[
    {
        "address": "0xYourAddress1",
        "private_key": "YourPrivateKey1"
    },
    {
        "address": "0xYourAddress2",
        "private_key": "YourPrivateKey2"
    }
]
```
Untuk menjalankan proyek:

```bash
python3 multiakun_unichain.py
```
Khusus Penggunaan di TERMUX
Jika kalian mengalami kegagalan dengan cara di atas, bisa mengikuti cara di bawah ini:

Masuk ke mode proot distro Ubuntu:

```bash
Salin kode
pkg install proot
pkg install openssh
pkg install git
curl -L -o proot_5.1.107-52_aarch64.deb https://github.com/SukunDev/termux-proot/raw/main/proot_5.1.107-52_aarch64.deb
dpkg -i proot_5.1.107-52_aarch64.deb
pkg install -y proot-distro
proot-distro install ubuntu
proot-distro login ubuntu
```
Masuk ke mode venv:

```bash
Salin kode
apt update && apt upgrade
apt install python3-pip
pip install --upgrade pip==24.2
apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate
pip install --upgrade pip setuptools
```
(Jika ada pilihan zona pilih angka 5 yaitu Asia dan 35 untuk waktu area Jakarta, selanjutnya klik y, enter, dan seterusnya)

Setelah semua terpasang, langsung clone repositori GitHub di atas:

Jalankan proyek dengan mengikuti instruksi yang ada di setiap file atau dokumentasi yang tersedia.

Kontribusi sangat dihargai! Jika Anda memiliki ide, saran, atau menemukan bug, jangan ragu untuk membuat issue atau pull request.

Lisensi
Proyek ini menggunakan lisensi [MIT]. Silakan baca file LICENSE untuk informasi lebih lanjut.

Dibuat oleh Bactiar291
Terima kasih telah berkunjung ke repositori saya! 🚀
