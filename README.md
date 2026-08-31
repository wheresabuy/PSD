# 📘 BUKU AJAR VISUAL PENGOLAHAN SINYAL DIGITAL (PSD)
*Panduan Komprehensif Berbasis Visual: Dari Paradigma ASP vs DSP, Konversi Digitalisasi ADC, Sinyal Multikanal, Sinyal Multi-Dimensi, hingga Sinyal Waktu Diskrit*

---

## 📑 DAFTAR ISI VISUAL

1. [BAB 1: Paradigma Pemrosesan Sinyal — Dari Dunia Fisik Analog (ASP) ke Era Digital (DSP)](#bab-1-paradigma-pemrosesan-sinyal--dari-dunia-fisik-analog-asp-ke-era-digital-dsp)
   - [1.1 Dari Fenomena Fisik Menjadi Sinyal Listrik (Peran Sensor & Transduser)](#11-dari-fenomena-fisik-menjadi-sinyal-listrik-peran-sensor--transduser)
   - [1.2 Paradigma Pemrosesan: Rantai ASP (Analog) vs Rantai DSP (Digital)](#12-paradigma-pemrosesan-rantai-asp-analog-vs-rantai-dsp-digital)
   - [1.3 Tiga Pilar Anatomi Gelombang: Amplitudo, Frekuensi, dan Fase](#13-tiga-pilar-anatomi-gelombang-amplitudo-frekuensi-dan-fase)
   - [1.4 Sistem Pengolah Sinyal & 4 Klasifikasi Karakteristik Operasinya](#14-sistem-pengolah-sinyal--4-klasifikasi-karakteristik-operasinya)
2. [BAB 2: Proses Digitalisasi Sinyal (Analog-to-Digital Converter / ADC)](#bab-2-proses-digitalisasi-sinyal-analog-to-digital-converter--adc)
   - [2.1 Rantai 4 Tahap Lengkap Digitalisasi ADC](#21-rantai-4-tahap-lengkap-digitalisasi-adc)
   - [2.2 Pencuplikan (Sampling Clock), Teorema Nyquist, dan Bencana Aliasing](#22-pencuplikan-sampling-clock-teorema-nyquist-dan-bencana-aliasing)
   - [2.3 Kuantisasi & Pengkodean Biner 3-Bit (Rentang 0 s.d. 10 Volt)](#23-kuantisasi--pengkodean-biner-3-bit-rentang-0-sd-10-volt)
   - [2.4 Studi Kasus End-to-End: Konversi Sinyal Sinus Utuh x(t) ke Aliran Bit Biner](#24-studi-kasus-end-to-end-konversi-sinyal-sinus-utuh-xt-ke-aliran-bit-biner)
3. [BAB 3: Klasifikasi Lanjutan Sinyal Modern](#bab-3-klasifikasi-lanjutan-sinyal-modern)
   - [3.1 Sinyal Multikanal (Multi-Channel Signals) & Representasi Vektor-Matriks](#31-sinyal-multikanal-multi-channel-signals--representasi-vektor-matriks)
   - [3.2 Sinyal Multi-Dimensi (Multi-Dimensional Signals / M-D): 1D, 2D, 3D, hingga 4D](#32-sinyal-multi-dimensi-multi-dimensional-signals--m-d-1d-2d-3d-hingga-4d)
   - [3.3 Sinyal Waktu Diskrit (Discrete-Time Signals / DTS) & Sinyal Elementer](#33-sinyal-waktu-diskrit-discrete-time-signals--dts--sinyal-elementer)

---

# BAB 1: Paradigma Pemrosesan Sinyal — Dari Dunia Fisik Analog (ASP) ke Era Digital (DSP)

## 1.1 Dari Fenomena Fisik Menjadi Sinyal Listrik (Peran Sensor & Transduser)

![Fenomena Fisik Menjadi Sinyal Listrik](assets/fenomena_fisik_ke_sinyal.png)

### 🔍 Bedah Contoh Berdasarkan Visualisasi di Atas:

* **Panel 1 (Sinyal Akustik / Suara — Biru Muda):**  
  Ketika manusia berbicara, pita suara menggetarkan partikel udara (tekanan Pascal). Diafragma mikrofon menangkap getaran tersebut dan mengubahnya menjadi fluktuasi **tegangan listrik $v(t)$ dalam skala milivolt (mV)**. Pada grafik, terlihat gelombang berosilasi bolak-balik naik turun terhadap waktu dalam rentang $50\text{ ms}$.

* **Panel 2 (Sinyal Termal / Suhu — Oranye):**  
  Ketika suhu ruangan memanas, sensor termokopel atau RTD mengubah energi panas menjadi tegangan listrik yang merayap naik. Pada grafik, suhu naik perlahan dari $25^\circ\text{C}$ menuju $65^\circ\text{C}$ dalam waktu $60\text{ detik}$. Terdapat sedikit gerigi halus (*noise termal*) yang menyertai kenaikan kurva tersebut.

* **Panel 3 (Sinyal Seismik / Gempa Bumi — Pink Magenta):**  
  Kerak bumi yang awalnya tenang tiba-tiba bergeser pada detik ke-$3$. Sensor seismometer / geophone langsung merekam lonjakan akselerasi getaran tanah hingga $+3.8\text{ m/s}^2$ yang kemudian mereda perlahan secara eksponensial.

> **📌 Kesimpulan Intuitif:** Sinyal adalah besaran fisik terukur yang membawa pesan/informasi tentang kondisi fenomena alam di sekitarnya.

---

## 1.2 Paradigma Pemrosesan: Rantai ASP (Analog) vs Rantai DSP (Digital)

![Diagram Paradigma ASP vs DSP](assets/diagram_asp_vs_dsp.png)

### 🔍 Bedah Alur Pemrosesan Berdasarkan Diagram di Atas:

* **Rantai Atas — Analog Signal Processing (ASP):**
  $$\text{Sinyal Analog Asli } x(t) \longrightarrow \mathbf{\text{Rangkaian ASP (Resistor, Kapasitor, Op-Amp)}} \longrightarrow \text{Sinyal Analog Hasil } y(t)$$
  * **Contoh Nyata:** Radio FM jadul atau equalizer mixer analog.
  * **Kelemahan Visual:** Sinyal analog langsung melewati kabel dan komponen solder. Jika suhu ruangan panas atau ada kabel berkarat, suara langsung kemrosok/rusak terkena derau (*noise*).

* **Rantai Bawah — Digital Signal Processing (DSP):**
  $$\text{Sinyal Analog } x(t) \longrightarrow \mathbf{A/D} \longrightarrow \mathbf{\text{DSP Processor (CPU/Algoritma)}} \longrightarrow \mathbf{D/A} \longrightarrow \text{Sinyal Analog } y(t)$$
  * **Contoh Nyata:** Smartphone modern, headphone peredam bising (ANC), dan streaming musik Spotify.
  * **Keunggulan Visual:** Sinyal analog diubah menjadi bit biner ($0$ dan $1$) oleh chip ADC. Di dalam prosesor DSP, manipulasi dilakukan murni melalui baris kode matematika, sehingga **100% kebal derau dan fleksibel tanpa perlu bongkar solder**.

---

## 1.3 Tiga Pilar Anatomi Gelombang: Amplitudo, Frekuensi, dan Fase

Persamaan matematis gelombang sinus murni:
$$x(t) = A \cdot \sin(2\pi f t + \phi)$$

![Anatomi Parameter Sinyal](assets/anatomi_sinyal.png)

![Komparasi Visual Parameter Sinyal](assets/komparasi_sinyal.png)

### 🔍 Bedah Parameter Berdasarkan Gambar Visual:

1. **Amplitudo ($A = 3.0\text{ Volt}$):**  
   * *Lihat Gambar Anatomi:* Diukur dari garis tengah $y=0$ menuju puncak tertinggi (*Peak* di $+3\text{V}$) atau dasar terdalam (*Trough* di $-3\text{V}$).  
   * *Contoh Nyata:* Mengatur volume suara. Semakin besar $A$ (kurva ungu pada Gambar Komparasi), semakin keras bunyi audio yang keluar.

2. **Frekuensi ($f = 2\text{ Hz}$) & Periode ($T = 0.5\text{ detik}$):**  
   * *Lihat Gambar Anatomi:* Periode $T$ adalah durasi horizontal untuk menyelesaikan 1 bukit dan 1 lembah ($0.5\text{ detik}$). Frekuensinya adalah $f = \frac{1}{T} = \frac{1}{0.5} = 2\text{ siklus/detik (Hz)}$.  
   * *Lihat Gambar Komparasi Panel 1:* Gelombang oranye ($3\text{ Hz}$) memiliki getaran 3 kali lebih rapat daripada gelombang biru ($1\text{ Hz}$), menghasilkan nada suara yang lebih melengking tinggi.

3. **Fase ($\phi = 90^\circ$ atau $\pi/2\text{ rad}$):**  
   * *Lihat Gambar Komparasi Panel 3:* Gelombang merah memiliki fase $\phi = 90^\circ$. Saat $t=0$, gelombang merah sudah berada di puncak tertinggi, artinya ia "start berlari lebih awal" mendahului gelombang biru ($\phi = 0^\circ$).

---

## 1.4 Sistem Pengolah Sinyal & 4 Klasifikasi Karakteristik Operasinya

![Klasifikasi Sistem](assets/klasifikasi_sistem.png)

### 🔍 Bedah Karakteristik Sistem Berdasarkan 4 Panel di Atas:

1. **Panel 1 — Linearitas (Linear vs Non-Linear):**  
   * Garis biru adalah sistem linier $y[n] = 1.5 x[n]$ (garis lurus sempurna, memenuhi superposisi).  
   * Garis putus-putus merah adalah sistem non-linier $y[n] = 0.5 x^3[n]$ (kurva melengkung, mendistorsi bentuk sinyal).

2. **Panel 2 — Kekekalan Waktu (Time-Invariant / TI):**  
   * Sinyal oranye dimasukkan pada $n=0$, menghasilkan pola respon tertentu.  
   * Sinyal hijau dimasukkan 4 detik kemudian ($n-4$). Karena sistem bersifat *Time-Invariant*, bentuk keluarannya **persis 100% sama**, hanya bergeser posisinya ke kanan.

3. **Panel 3 — Kausalitas (Kausal vs Non-Kausal):**  
   * Respon impuls ungu hanya muncul pada $n \geq 0$ (Kausal, realistis di dunia nyata).  
   * Respon impuls pink sudah aktif di $n < 0$ (Non-Kausal, tidak realistis karena memerlukan input masa depan).

4. **Panel 4 — Stabilitas BIBO (Stabil vs Meledak):**  
   * Kurva hijau adalah sistem stabil ($y[n] = 0.75^n$): Nilai output meluruh turun mendekati $0$.  
   * Kurva merah putus-putus adalah sistem tidak stabil ($y[n] = 1.35^n$): Nilai output meledak menuju tak hingga ($\infty$) dan merusak perangkat.

---

# BAB 2: Proses Digitalisasi Sinyal (Analog-to-Digital Converter / ADC)

## 2.1 Rantai 4 Tahap Lengkap Digitalisasi ADC

![Tahapan Lengkap ADC](assets/tahapan_adc_sampling_kuantisasi.png)

### 🔍 Bedah Alur Kerja ADC Berdasarkan 4 Panel di Atas:

1. **Panel 1 (Sinyal Analog Asli):** Gelombang mulus yang kontinu dalam waktu ($t$) dan kontinu dalam nilai tegangan ($V$).
2. **Panel 2 (Pencuplikan / Sampling Clock):** Sakelar clock memotret nilai tegangan pada interval teratur $T_s$. Sinyal kini **Diskrit Waktu**, tapi amplitudonya masih bilangan desimal riil tak terbatas.
3. **Panel 3 (Kuantisasi Tegangan):** Nilai desimal dibulatkan ke garis anak tangga horizontal terdekat ($x_q[n]$). Sinyal kini **Diskrit Nilai**.
4. **Panel 4 (Pengkodean Biner):** Setiap nomor anak tangga dikonversikan menjadi deretan angka biner `0` dan `1` yang siap dibaca oleh prosesor komputer.

---

## 2.2 Pencuplikan (Sampling Clock), Teorema Nyquist, dan Bencana Aliasing

![Sampling Nyquist dan Aliasing](assets/sampling_nyquist_aliasing.png)

### 🔍 Bedah Kasus Nyata Berdasarkan 3 Grafik di Atas:
*Kita menguji sinyal sinus dengan frekuensi asli $f = 5\text{ Hz}$ (garis titik-titik abu-abu).*

* **Grafik A — Over-Sampling ($F_s = 40\text{ Hz} \gg 2 \times 5\text{ Hz}$):**  
  Detak jam clock mengambil $40$ titik sampel per detik (titik lingkaran biru). Hasil rekonstruksi garis biru mereproduksi gelombang asli dengan sangat presisi dan bebas cacat.

* **Grafik B — Batas Kritis Nyquist ($F_s = 10\text{ Hz} = 2 \times 5\text{ Hz}$):**  
  Detak clock mengambil tepat $2$ titik per siklus gelombang (titik kotak oranye). Ini adalah batas minimum absolut agar sinyal masih dapat dikenali.

* **Grafik C — Bencana Aliasing ($F_s = 6\text{ Hz} < 2 \times 5\text{ Hz}$):**  
  Clock bekerja terlalu lambat (titik segitiga merah). Akibatnya, komputer salah menghubungkan titik-titik tersebut dan menghasilkan **Gelombang Palsu Merah yang berosilasi sangat lambat ($1\text{ Hz}$)**. Fenomena gelombang hantu palsu inilah yang disebut **Aliasing**.

> **🛡️ Teorema Nyquist:** Syarat mutlak bebas aliasing adalah $F_s \geq 2 \cdot f_{\text{maks}}$.

---

## 2.3 Kuantisasi & Pengkodean Biner 3-Bit (Rentang 0 s.d. 10 Volt)

![Karakteristik Kuantisasi 3-Bit 0-10V](assets/kuantisasi_3bit_0_10v.png)

### 🔍 Bedah Tangga Kuantisasi Berdasarkan Grafik di Atas:

* **Resolusi ADC:** $3\text{-bit} \implies 2^3 = 8\text{ Anak Tangga Level}$.
* **Lebar Rentang Per Step (*Step Size* $\Delta$):**  
  $$\Delta = \frac{V_{\text{maks}} - V_{\text{min}}}{2^B} = \frac{10.0\text{ V} - 0.0\text{ V}}{8} = 1.25\text{ Volt / step}$$

### Tabel Pemetaan Visual Step 1 s.d. Step 8:

| Step Kuantisasi | Rentang Tegangan Masukan ($V_{\text{in}}$) | Kode Biner Encoding | Nilai Tengah Level ($V_q$) |
| :---: | :---: | :---: | :---: |
| **Step 1** | $0.00\text{ V} \leq V_{\text{in}} < 1.25\text{ V}$ | **`000`** | $0.625\text{ V}$ |
| **Step 2** | $1.25\text{ V} \leq V_{\text{in}} < 2.50\text{ V}$ | **`001`** | $1.875\text{ V}$ |
| **Step 3** | $2.50\text{ V} \leq V_{\text{in}} < 3.75\text{ V}$ | **`010`** | $3.125\text{ V}$ |
| **Step 4** | $3.75\text{ V} \leq V_{\text{in}} < 5.00\text{ V}$ | **`011`** | $4.375\text{ V}$ |
| **Step 5** | $5.00\text{ V} \leq V_{\text{in}} < 6.25\text{ V}$ | **`100`** | $5.625\text{ V}$ |
| **Step 6** | $6.25\text{ V} \leq V_{\text{in}} < 7.50\text{ V}$ | **`101`** | $6.875\text{ V}$ |
| **Step 7** | $7.50\text{ V} \leq V_{\text{in}} < 8.75\text{ V}$ | **`110`** | $8.125\text{ V}$ |
| **Step 8** | $8.75\text{ V} \leq V_{\text{in}} \leq 10.00\text{ V}$| **`111`** | $9.375\text{ V}$ |

*Lihat pita hijau pada grafik:* Error kuantisasi maksimal dibatasi $\pm \frac{\Delta}{2} = \pm 0.625\text{ Volt}$.

---

## 2.4 Studi Kasus End-to-End: Konversi Sinyal Sinus Utuh x(t) ke Aliran Bit Biner

* **Rumus Sinyal Input:** $x(t) = 5 + 4 \cdot \sin(2\pi \cdot 1 \cdot t)\text{ Volt}$
* **ADC Clock:** $F_s = 8\text{ Hz}$ ($T_s = 0.125\text{ s}$, total 8 titik cuplikan $n = 0 \dots 7$).

![Studi Kasus Konversi Lengkap](assets/studi_kasus_konversi_lengkap.png)

### 🔍 Pelacakan 8 Titik Cuplikan Berdasarkan Grafik di Atas:

1. **Titik $n = 0$ ($t = 0.000\text{ s}$):** Tegangan $V = 5.00\text{V} \implies$ Masuk **Step 5** $\implies$ Level $5.625\text{V} \implies$ **Biner `100`**.
2. **Titik $n = 1$ ($t = 0.125\text{ s}$):** Tegangan $V = 7.83\text{V} \implies$ Masuk **Step 7** $\implies$ Level $8.125\text{V} \implies$ **Biner `110`**.
3. **Titik $n = 2$ ($t = 0.250\text{ s}$):** Puncak Tertinggi $V = 9.00\text{V} \implies$ Masuk **Step 8** $\implies$ Level $9.375\text{V} \implies$ **Biner `111`**.
4. **Titik $n = 3$ ($t = 0.375\text{ s}$):** Tegangan $V = 7.83\text{V} \implies$ Masuk **Step 7** $\implies$ Level $8.125\text{V} \implies$ **Biner `110`**.
5. **Titik $n = 4$ ($t = 0.500\text{ s}$):** Tegangan $V = 5.00\text{V} \implies$ Masuk **Step 5** $\implies$ Level $5.625\text{V} \implies$ **Biner `100`**.
6. **Titik $n = 5$ ($t = 0.625\text{ s}$):** Tegangan $V = 2.17\text{V} \implies$ Masuk **Step 2** $\implies$ Level $1.875\text{V} \implies$ **Biner `001`**.
7. **Titik $n = 6$ ($t = 0.750\text{ s}$):** Dasar Lembah $V = 1.00\text{V} \implies$ Masuk **Step 1** $\implies$ Level $0.625\text{V} \implies$ **Biner `000`**.
8. **Titik $n = 7$ ($t = 0.875\text{ s}$):** Tegangan $V = 2.17\text{V} \implies$ Masuk **Step 2** $\implies$ Level $1.875\text{V} \implies$ **Biner `001`**.

$$\mathbf{\text{Aliran Bit Output (Bitstream)}} = \underbrace{\mathbf{100}}_{n=0} \ \underbrace{\mathbf{110}}_{n=1} \ \underbrace{\mathbf{111}}_{n=2} \ \underbrace{\mathbf{110}}_{n=3} \ \underbrace{\mathbf{100}}_{n=4} \ \underbrace{\mathbf{001}}_{n=5} \ \underbrace{\mathbf{000}}_{n=6} \ \underbrace{\mathbf{001}}_{n=7}$$

---

# BAB 3: Klasifikasi Lanjutan Sinyal Modern

## 3.1 Sinyal Multikanal (Multi-Channel Signals) & Representasi Vektor-Matriks

![Konsep Sinyal Multikanal](assets/sinyal_multikanal.png)

### 🔍 Bedah Konsep Berdasarkan Visualisasi di Atas:

* **Panel Kiri (4 Gelombang Sensor Simultan):**  
  Menampilkan 4 sensor/elektroda yang merekam secara serentak:
  * **Kanal 1 (Biru):** Sensor Dada $V_1 \implies x_1(t)$
  * **Kanal 2 (Oranye):** Sensor Dada $V_2 \implies x_2(t)$
  * **Kanal 3 (Pink):** Sensor Lengan Kiri $\implies x_3(t)$
  * **Kanal 4 (Hijau):** Sensor Lengan Kanan $\implies x_4(t)$

* **Panel Kanan (Matematika Vektor & Matriks):**
  1. **Vektor Kolom pada Saat $t$:** Pada setiap detak waktu, data yang masuk adalah 1 vektor kolom $\mathbf{x}(t) = [x_1(t), x_2(t), x_3(t), x_4(t)]^T \in \mathbb{R}^{4 \times 1}$.
  2. **Matriks Spasio-Temporal $\mathbf{X}_{M \times N}$:** Jika direkam selama $N$ sampel, seluruh data membentuk matriks di mana **Baris adalah Dimensi Spasial (Sensor 1..4)** dan **Kolom adalah Dimensi Waktu ($n = 0 \dots N-1$)**.
  3. **Aplikasi Nyata:** ECG 12-Lead jantung, EEG 32-kanal otak, audio 7.1 surround sound, dan algoritma *Beamforming* smart speaker.

---

## 3.2 Sinyal Multi-Dimensi (Multi-Dimensional Signals / M-D): 1D, 2D, 3D, hingga 4D

![Spektrum Sinyal Multi-Dimensi](assets/sinyal_multidimensi.png)

### 🔍 Bedah Hierarki Dimensi Berdasarkan 4 Panel di Atas:

1. **Panel 1 — Sinyal 1D ($s = f(t)$):**  
   Hanya memiliki **1 variabel bebas (Waktu $t$)**. Contoh: Sinyal suara ucapan dan detak jantung ECG.

2. **Panel 2 — Sinyal 2D ($I = f(x, y)$):**  
   Memiliki **2 variabel spasial $(x, y)$**. Nilai fungsi merepresentasikan intensitas kecerahan piksel (heatmap kuning terang hingga ungu gelap). Contoh: Foto rontgen X-ray dan citra digital grayscale.

3. **Panel 3 — Sinyal 3D Spasio-Temporal ($V = f(x, y, t)$):**  
   Menampilkan tumpukan 3 lembar frame citra 2D yang berjalan seiring sumbu vertikal waktu $t$ ($t=0.2\text{s}, 0.6\text{s}, 1.0\text{s}$). Contoh: Video rekaman TV hitam-putih dan pemindaian 3D organ tubuh MRI / CT-Scan.

4. **Panel 4 — Sinyal 4D & Multi-Spektral ($C = f(x, y, t, \lambda)$):**  
   Memiliki 4 variabel: Ruang $(x, y)$, Waktu $(t)$, dan Saluran Warna ($\lambda$ / RGB). Contoh: Video digital berwarna di bioskop.

---

## 3.3 Sinyal Waktu Diskrit (Discrete-Time Signals / DTS) & Sinyal Elementer

![Fondasi Sinyal Waktu Diskrit](assets/sinyal_waktu_diskrit.png)

### 🔍 Bedah Sinyal Diskrit Berdasarkan 4 Panel di Atas:

1. **Panel 1 (Hasil Pencuplikan Sampling / Stem Plot):**  
   Sinyal kontinu abu-abu dipotret menjadi batang-batang vertikal biru $x[n] = x(n \cdot T_s)$ dengan indeks integer bulat $n \in \{0, 1, 2, \dots, 12\}$. Di antara dua titik bulat, sinyal **tidak terdefinisi (*undefined*)**.

2. **Panel 2 (Sinyal Diskrit Murni / Non-Fisik):**  
   Batang-batang oranye merepresentasikan fluktuasi harga saham harian per hari ke-$n$. Sinyal ini secara alamiah lahir sebagai angka diskrit tanpa pernah ada gelombang fisiknya.

3. **Panel 3 (Tiga Sinyal Elementer Utama):**  
   * **Unit Impulse $\delta[n]$ (Titik Pink):** Bernilai $1$ hanya di $n=0$. Merupakan "kunci DNA" sistem DSP (*Impulse Response $h[n]$*).  
   * **Unit Step $u[n]$ (Segitiga Hijau):** Bernilai $1$ untuk semua $n \geq 0$ (seperti sakelar On/Off).  
   * **Eksponensial $a^n u[n]$ (Kotak Ungu):** Nilai meluruh turun $0.7^n$ mendekati nol.

4. **Panel 4 (Empat Cara Representasi):**  
   * Notasi Array Himpunan: $x[n] = \{ \dots, 0.5, \underset{\uparrow}{2.0}, 3.5, 1.0, -1.5, \dots \}$
   * Rumus Analitik: $x[n] = 2(0.8)^n u[n] + 3\delta[n-2]$
   * Tabel Nilai $n$ vs $x[n]$
   * Stem Plot Grafis

---
*Dokumen ini disusun sebagai Modul Pembelajaran Visual Pengolahan Sinyal Digital (PSD) berstandar industri dan akademis.*
