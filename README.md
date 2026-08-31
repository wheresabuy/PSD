# 📘 BUKU AJAR & MODUL LENGKAP PENGOLAHAN SINYAL DIGITAL (PSD)
*Panduan Komprehensif: Dari Konsep Dasar, Sinyal Multi-Dimensi, Sinyal Multikanal, Sinyal Waktu Diskrit, Sistem, hingga Proses Digitalisasi (ADC)*

---

## 📑 DAFTAR ISI
1. [BAB 1: Memahami Fondasi Sinyal, Sistem, dan Paradigma Pemrosesan](#bab-1-memahami-fondasi-sinyal-sistem-dan-paradigma-pemrosesan)
   - [1.1 Apa Sebenarnya Sinyal Itu? (Konsep Awam & Filosofi)](#11-apa-sebenarnya-sinyal-itu-konsep-awam--filosofi)
   - [1.2 Sinyal Multi-Dimensi (M-Dimensi): 1D, 2D, 3D, hingga 4D](#12-sinyal-multi-dimensi-m-dimensi-1d-2d-3d-hingga-4d)
   - [1.3 Sinyal Kanal Tunggal vs Sinyal Multikanal (Multi-Channel Signals)](#13-sinyal-kanal-tunggal-vs-sinyal-multikanal-multi-channel-signals)
   - [1.4 Sinyal Waktu Diskrit (Discrete-Time Signals / DTS)](#14-sinyal-waktu-diskrit-discrete-time-signals--dts)
   - [1.5 Tiga Pilar Anatomi Gelombang: Amplitudo, Frekuensi, dan Fase](#15-tiga-pilar-anatomi-gelombang-amplitudo-frekuensi-dan-fase)
   - [1.6 Anatomi Visual Grafik Sinyal](#16-anatomi-visual-grafik-sinyal)
   - [1.7 Komparasi Visual Parameter Sinyal](#17-komparasi-visual-parameter-sinyal)
   - [1.8 Studi Kasus Nyata: Mengapa Suara Manusia Adalah Sinyal?](#18-studi-kasus-nyata-mengapa-suara-manusia-adalah-sinyal)
   - [1.9 Apa Itu Sistem? (Analogi Mesin Pemroses)](#19-apa-itu-sistem-analogi-mesin-pemroses)
   - [1.10 Tiga Wujud Realisasi Sistem Pengolah Sinyal](#110-tiga-wujud-realisasi-sistem-pengolah-sinyal)
   - [1.11 Klasifikasi Sifat & Karakteristik Operasi Sistem](#111-klasifikasi-sifat--karakteristik-operasi-sistem)
   - [1.12 Dua Paradigma Besar: Pemrosesan Analog (ASP) vs Pemrosesan Digital (DSP)](#112-dua-paradigma-besar-pemrosesan-analog-asp-vs-pemrosesan-digital-dsp)
   - [1.13 Mengapa Dunia Beralih ke DSP? (Kelebihan & Batasan)](#113-mengapa-dunia-beralih-ke-dsp-kelebihan--batasan)
2. [BAB 2: Proses Digitalisasi Sinyal (Analog-to-Digital Converter / ADC)](#bab-2-proses-digitalisasi-sinyal-analog-to-digital-converter--adc)
   - [2.1 Mengapa Sinyal Analog Harus Diubah ke Digital?](#21-mengapa-sinyal-analog-harus-diubah-ke-digital)
   - [2.2 Rantai 4 Tahap Lengkap Konversi ADC](#22-rantai-4-tahap-lengkap-konversi-adc)
   - [2.3 Tahap 1: Pencuplikan (Sampling) & Peran Detak Clock](#23-tahap-1-pencuplikan-sampling--peran-detak-clock)
   - [2.4 Teorema Nyquist-Shannon & Bahaya Fenomena Aliasing](#24-teorema-nyquist-shannon--bahaya-fenomena-aliasing)
   - [2.5 Mengapa Wajib Ada Filter Anti-Aliasing Sebelum Sampling?](#25-mengapa-wajib-ada-filter-anti-aliasing-sebelum-sampling)
   - [2.6 Tahap 2: Kuantisasi (Quantization) — Seni Membulatkan Nilai](#26-tahap-2-kuantisasi-quantization--seni-membulatkan-nilai)
   - [2.7 Tahap 3: Pengkodean (Encoding) ke Deretan Bit Biner Digital](#27-tahap-3-pengkodean-encoding-ke-deretan-bit-biner-digital)
   - [2.8 Studi Kasus End-to-End: Konversi Sinyal Sinus Utuh x(t) ke Aliran Biner](#28-studi-kasus-end-to-end-konversi-sinyal-sinus-utuh-xt-ke-aliran-biner)

---

# BAB 1: Memahami Fondasi Sinyal, Sistem, dan Paradigma Pemrosesan

## 1.1 Apa Sebenarnya Sinyal Itu? (Konsep Awam & Filosofi)

Bayangkan Anda sedang berbicara dengan teman di seberang ruangan. Pita suara Anda bergetar, menggetarkan partikel udara di sekitarnya, merambat sebagai gelombang tekanan udara, dan akhirnya menggetarkan gendang telinga teman Anda. 

Secara ilmiah, getaran tekanan udara yang merambat dari mulut ke telinga itulah yang disebut **Sinyal**.

> **📌 Definisi Formal Sinyal:**  
> **Sinyal** adalah besaran fisik yang nilainya berubah (*bervariasi*) terhadap satu atau lebih variabel bebas (seperti waktu, ruang/posisi, suhu, atau kedalaman). Sinyal bertindak sebagai **kendaraan pembawa pesan (*carrier of information*)** mengenai perilaku suatu fenomena alam.

```mermaid
graph LR
    Fenomena["1. Fenomena Fisik Asli<br>(Suara, Panas Suhu, Gempa Bumi, Gelombang Otak)"] -->|Sensor / Transduser| Sinyal["2. Sinyal x(t)<br><i>Besaran Fisik yang Berubah terhadap Waktu</i>"]
    Sinyal -->|Sistem DSP| Hasil["3. Informasi Berguna<br>(Teks Suara, Angka Suhu, Peringatan Gempa)"]

    style Fenomena fill:#1e293b,stroke:#f59e0b,color:#fff
    style Sinyal fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#fff
    style Hasil fill:#064e3b,stroke:#10b981,color:#fff
```

---

## 1.2 Sinyal Multi-Dimensi (M-Dimensi): 1D, 2D, 3D, hingga 4D

Berapa banyak variabel yang menentukan nilai suatu sinyal? Inilah konsep dari **Dimensi Sinyal ($M$-Dimensi)**.

> **📌 Definisi Sinyal $M$-Dimensi:**  
> Suatu sinyal disebut **$M$-Dimensi ($M$-D)** apabila nilai amplitudonya merupakan fungsi matematis dari **$M$ buah variabel bebas (*independent variables*)**:
> $$s = f(v_1, v_2, v_3, \dots, v_M)$$

![Spektrum Sinyal Multi-Dimensi](assets/sinyal_multidimensi.png)

### Klasifikasi Dimensi Sinyal:
1. **Sinyal 1D — $f(t)$:** 1 variabel waktu $t$ (Suara ucapan mono, sinyal ECG jantung).
2. **Sinyal 2D — Citra Intensitas $I = f(x, y)$:** 2 koordinat spasial bidang $(x, y)$ (Foto grayscale, X-Ray).
3. **Sinyal 3D — $V = f(x, y, t)$ atau $f(x, y, z)$:** Rangkaian frame video hitam-putih terhadap waktu $t$, atau citra medis volume 3D (*Voxel*) seperti MRI / CT-Scan.
4. **Sinyal 4D & Multi-Spektral — $C = f(x, y, t, \lambda)$:** Video berwarna (RGB) atau video 3D jantung berdetak $f(x, y, z, t)$.

---

## 1.3 Sinyal Kanal Tunggal vs Sinyal Multikanal (Multi-Channel Signals)

Dalam dunia nyata, kita sering kali tidak hanya menggunakan 1 buah sensor, melainkan **sekumpulan sensor sekaligus** yang bekerja bersamaan:

![Konsep Sinyal Multikanal](assets/sinyal_multikanal.png)

1. **Representasi Vektor Kolom pada Setiap Saat $t$:**
   $$\mathbf{x}(t) = \begin{bmatrix} x_1(t) \\ x_2(t) \\ x_3(t) \\ \vdots \\ x_M(t) \end{bmatrix} \in \mathbb{R}^{M \times 1}$$

2. **Representasi Matriks Spasio-Temporal ($N$ Sampel):**
   $$\mathbf{X} = \begin{bmatrix} 
   x_1[0] & x_1[1] & \dots & x_1[N-1] \\ 
   x_2[0] & x_2[1] & \dots & x_2[N-1] \\ 
   x_3[0] & x_3[1] & \dots & x_3[N-1] \\ 
   \vdots & \vdots & \ddots & \vdots \\ 
   x_M[0] & x_M[1] & \dots & x_M[N-1] 
   \end{bmatrix}_{M \times N}$$

3. **Keunggulan Analisis:** Membuka operasi **Aljabar Linier** (Beamforming arah dengar mikrofon, ICA *Blind Source Separation*, dan PCA).

---

## 1.4 Sinyal Waktu Diskrit (Discrete-Time Signals / DTS)

Berbeda dengan sinyal analog kontinu $x(t)$ yang nilainya selalu mengalir tanpa jeda pada setiap titik waktu riil $t \in \mathbb{R}$, **Sinyal Waktu Diskrit** hanya terdefinisi pada **titik-titik waktu tertentu saja**.

![Fondasi Sinyal Waktu Diskrit](assets/sinyal_waktu_diskrit.png)

### A. Definisi Fundamental Sinyal Waktu Diskrit:
> **📌 Definisi Sinyal Waktu Diskrit:**  
> Sinyal Waktu Diskrit didefinisikan **hanya pada indeks waktu diskrit berupa bilangan bulat (*integer*)** $n \in \mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$. Sinyal ini dinyatakan sebagai **deret bilangan (*sequence*)** riil atau kompleks $x[n]$ atau $x(n)$.
> 
> *Catatan Kritis:* Pada waktu di antara dua indeks bulat (seperti $n = 1.5$ atau $n = 2.8$), sinyal waktu diskrit **tidak terdefinisi (*undefined*)**, bukan bernilai nol.

---

### B. Dua Asal-Usul Pembentukan Sinyal Waktu Diskrit:

```mermaid
flowchart TD
    DTS["Asal Pembentukan Sinyal Waktu Diskrit x[n]"]

    DTS --> S1["1. Hasil Pencuplikan (Sampling) Sinyal Analog Fisik<br>x[n] = x(n·Ts)<br><i>Contoh: Suara mikrofon yang dicuplik chip ADC tiap interval Ts</i>"]
    DTS --> S2["2. Sinyal Diskrit Alami / Murni (Non-Fisik)<br><i>Contoh: Data statistik harga saham per hari, jumlah pengunjung toko per jam</i>"]

    style DTS fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#fff
    style S1 fill:#0f172a,stroke:#38bdf8,color:#fff
    style S2 fill:#78350f,stroke:#f59e0b,color:#fff
```

1. **Hasil Pencuplikan (*Sampling*) Sinyal Analog:**
   Sinyal kontinu $x(t)$ dipotret pada selang waktu seragam $T_s = \frac{1}{F_s}$:
   $$x[n] = x(t)\Big|_{t = n T_s} = x(n \cdot T_s)$$
2. **Sinyal Diskrit Murni (*Inherently Discrete-Time Signals*):**
   Sinyal yang secara alamiah memang lahir dalam bentuk deret data terpisah (tidak ada bentuk analognya). Contoh: Data penutupan harga saham per hari ($n = \text{hari}$), jumlah pasien rumah sakit per minggu ($n = \text{minggu}$).

---

### C. Empat Cara Representasi Matematis Sinyal Diskrit:

1. **Notasi Deret Himpunan (*Sequence Set Notation*):**  
   Menuliskan deretan angka di dalam kurung kurawal. Simbol panah bawah/atas ($\uparrow$) menandakan posisi indeks acuan $n = 0$:
   $$x[n] = \{ \dots, 0.5, \ \underset{\uparrow}{2.0}, \ 3.5, \ 1.0, \ -1.5, \ \dots \}$$
   *(Artinya: $x[-1]=0.5$, $x[0]=2.0$, $x[1]=3.5$, $x[2]=1.0$, $x[3]=-1.5$)*.

2. **Rumus Matematis Fungsional Analitik:**  
   Menyatakan nilai sinyal sebagai formula aljabar:
   $$x[n] = \begin{cases} (0.8)^n, & n \geq 0 \\ 0, & n < 0 \end{cases}$$

3. **Representasi Tabel Nilai ($n$ vs $x[n]$):**  
   | $n$ | $\dots$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $\dots$ |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | **$x[n]$** | $\dots$ | $0$ | $0$ | $2.0$ | $1.6$ | $1.28$ | $1.02$ | $\dots$ |

4. **Representasi Grafis (*Stem Plot / Lollipop Plot*):**  
   Menampilkan sinyal sebagai batang-batang tegak vertikal dengan lingkaran di ujung puncaknya yang menunjuk ke koordinat $(n, x[n])$.

---

### D. Sinyal Diskrit Elementer (Sinyal Dasar Pembangun DSP):

```mermaid
graph LR
    Elem["Sinyal Diskrit Dasar (Elementer)"]
    Elem --> D["1. Unit Impulse delta[n]<br>Bernilai 1 HANYA di n=0, lainnya 0"]
    Elem --> U["2. Unit Step u[n]<br>Bernilai 1 untuk semua n >= 0, lainnya 0"]
    Elem --> R["3. Unit Ramp r[n]<br>Bernilai n untuk n >= 0 (Tanjakan Linier)"]
    Elem --> E["4. Eksponensial a^n<br>Meluruh jika |a| < 1, Meledak jika |a| > 1"]

    style Elem fill:#312e81,stroke:#6366f1,color:#fff
    style D fill:#831843,stroke:#ec4899,color:#fff
    style U fill:#064e3b,stroke:#10b981,color:#fff
    style R fill:#78350f,stroke:#f59e0b,color:#fff
    style E fill:#0f172a,stroke:#38bdf8,color:#fff
```

1. **Unit Impulse / Delta Dirac Diskrit ($\delta[n]$):**
   $$\delta[n] = \begin{cases} 1, & n = 0 \\ 0, & n \neq 0 \end{cases}$$
   *Peran:* Sinyal paling fundamental dalam DSP! Respon sistem terhadap sinyal ini disebut **Impulse Response $h[n]$**, yang mencerminkan DNA/karakteristik lengkap suatu sistem linier.

2. **Unit Step ($u[n]$):**
   $$u[n] = \begin{cases} 1, & n \geq 0 \\ 0, & n < 0 \end{cases}$$
   *Hubungan dengan $\delta[n]$:* $u[n] = \sum_{k=-\infty}^{n} \delta[k]$ atau $\delta[n] = u[n] - u[n-1]$.

3. **Sinyal Eksponensial Diskrit ($x[n] = a^n$):**
   * Jika $|a| < 1$ (misal $a = 0.7$): Sinyal meluruh turun (*decaying*) menuju nol seiring bertambahnya $n$.
   * Jika $|a| > 1$ (misal $a = 1.5$): Sinyal meledak membesar (*growing*) menuju tak hingga.
   * Jika $a < 0$ (misal $a = -0.8$): Sinyal berganti-ganti tanda positif dan negatif (*berosilasi*).

---

### E. Operasi Dasar pada Sinyal Waktu Diskrit:

1. **Pergeseran Waktu (*Time Shifting*):**  
   * $y[n] = x[n - k]$ : Sinyal **ditunda (*delayed*)** ke kanan sejauh $k$ satuan sampel.
   * $y[n] = x[n + k]$ : Sinyal **dimajukan (*advanced*)** ke kiri sejauh $k$ satuan sampel.
2. **Pembalikan Waktu (*Time Reversal / Folding*):**  
   * $y[n] = x[-n]$ : Membalik urutan sinyal secara horizontal terhadap sumbu $n = 0$.
3. **Penskalaan Amplitudo (*Amplitude Scaling*):**  
   * $y[n] = c \cdot x[n]$ : Mengalikan setiap nilai cuplikan dengan faktor penguatan $c$.

---

## 1.5 Tiga Pilar Anatomi Gelombang: Amplitudo, Frekuensi, dan Fase

Persamaan matematis gelombang sinus dinyatakan sebagai:

$$x(t) = A \cdot \sin(2\pi f t + \phi) = A \cdot \sin(\omega t + \phi)$$

```mermaid
graph TD
    subgraph Tiga Pilar Parameter Sinyal
        P1["1. AMPLITUDO (A)<br><i>Simpangan Tertinggi</i><br><b>Analogi: Volume Suara / Kekuatan Ombak</b>"]
        P2["2. FREKUENSI (f)<br><i>Kerapatan / Jumlah Getaran per Detik</i><br><b>Analogi: Tinggi Nada Melengking vs Suara Bass</b>"]
        P3["3. FASE (phi)<br><i>Titik Awal Mulai Gelombang</i><br><b>Analogi: Selisih Waktu Start Lari Dua Orang</b>"]
    end
    
    style P1 fill:#78350f,stroke:#f59e0b,color:#fff
    style P2 fill:#0f172a,stroke:#38bdf8,color:#fff
    style P3 fill:#312e81,stroke:#a855f7,color:#fff
```

---

## 1.6 Anatomi Visual Grafik Sinyal

![Anatomi Parameter Sinyal](assets/anatomi_sinyal.png)

---

## 1.7 Komparasi Visual Parameter Sinyal

![Komparasi Visual Parameter Sinyal](assets/komparasi_sinyal.png)

---

## 1.8 Studi Kasus Nyata: Mengapa Suara Manusia Adalah Sinyal?

```mermaid
flowchart LR
    PitaSuara["1. Paru-paru & Pita Suara<br><i>Sumber Getaran Tekanan</i>"] --> Udara["2. Partikel Udara<br><i>Sinyal Akustik p(t)</i>"]
    Udara --> Mic["3. Diafragma Mikrofon<br><i>Transduser Listrik v(t)</i>"]
    Mic --> DSP["4. Modul DSP<br><i>Ekstraksi Karakteristik</i>"]
    DSP --> Output["5. Aplikasi Cerdas<br>• Siri / Google Assistant<br>• Speech-to-Text<br>• Noise Suppression"]

    style PitaSuara fill:#312e81,stroke:#6366f1,color:#fff
    style Udara fill:#1e293b,stroke:#f59e0b,color:#fff
    style Mic fill:#0f172a,stroke:#38bdf8,color:#fff
    style DSP fill:#581c87,stroke:#a855f7,color:#fff
    style Output fill:#064e3b,stroke:#10b981,color:#fff
```

---

## 1.9 Apa Itu Sistem? (Analogi Mesin Pemroses)

> **📌 Definisi Sistem:**  
> **Sistem** adalah perangkat fisik (elektronika) atau algoritma perangkat lunak yang menerima sinyal masukan $x[n]$, melakukan operasi matematis terhadapnya, lalu mengeluarkan sinyal baru $y[n]$ yang telah dimodifikasi:
> $$y[n] = \mathcal{T}\{x[n]\}$$

---

## 1.10 Tiga Wujud Realisasi Sistem Pengolah Sinyal

1. **Hardware Murni (Analog):** Rangkaian RLC, Op-Amp, Transistor.
2. **Software Murni (Digital):** Algoritma Python, C++, MATLAB di PC/Server.
3. **Hybrid / Embedded Firmware:** Chip DSP (TMS320), FPGA, Mikrokontroler (STM32, ESP32).

---

## 1.11 Klasifikasi Sifat & Karakteristik Operasi Sistem

* **Linear:** Mematuhi prinsip superposisi $\mathcal{T}\{a x_1 + b x_2\} = a \mathcal{T}\{x_1\} + b \mathcal{T}\{x_2\}$.
* **Time-Invariant (TI):** Sifat sistem tidak berubah seiring waktu ($x[n - n_0] \implies y[n - n_0]$).
* **Kausal:** Output saat ini hanya bergantung pada input saat ini dan masa lalu.
* **Stabilitas BIBO:** Input terbatas menjamin output selalu terbatas.

---

## 1.12 Dua Paradigma Besar: Pemrosesan Analog (ASP) vs Pemrosesan Digital (DSP)

![Diagram Paradigma ASP vs DSP](assets/diagram_asp_vs_dsp.png)

---

## 1.13 Mengapa Dunia Beralih ke DSP? (Kelebihan & Batasan)

| Aspek | Pemrosesan Analog (ASP) | Pemrosesan Digital (DSP) |
| :--- | :--- | :--- |
| **Fleksibilitas** | ❌ Kaku. Ubah fitur harus ganti komponen solder fisik. | ✅ **Sangat Fleksibel**. Cukup update baris kode program (*software update*). |
| **Kekebalan Derau (*Noise*)** | ❌ Rentan. Gangguan kabel langsung merusak sinyal. | ✅ **Sangat Kebal**. Data berupa biner (0 & 1). |
| **Akurasi & Presisi** | ❌ Rendah. Bergantung toleransi fisik pabrik dan suhu. | ✅ **Eksak & 100% Konsisten** (32-bit / 64-bit). |
| **Penyimpanan Data** | ❌ Sulit. Pita kaset aus setiap diputar. | ✅ **Abadi Tanpa Rusak (*Lossless*)**. |
| **Kompleksitas Algoritma** | ❌ Hanya operasi sederhana. | ✅ **Bisa Sangat Rumit** (ANC, Kompresi MP4, AI Speech Recognition). |

---

# BAB 2: Proses Digitalisasi Sinyal (Analog-to-Digital Converter / ADC)

## 2.1 Mengapa Sinyal Analog Harus Diubah ke Digital?

Komputer hanya mengerti bilangan biner ($0$ dan $1$). Oleh karena itu, kita memerlukan jembatan penerjemah yang disebut **Analog-to-Digital Converter (ADC)**.

![Tahapan Lengkap ADC](assets/tahapan_adc_sampling_kuantisasi.png)

---

## 2.2 Rantai 4 Tahap Lengkap Konversi ADC

```mermaid
flowchart LR
    Analog["Sinyal Analog x(t)<br><i>Kontinu Waktu & Nilai</i>"] --> LPF["0. Anti-Aliasing Filter<br>(Low-Pass Analog)"]
    LPF --> Sampler["1. Sampling (Clock Ts)<br>x[n] = x(nTs)<br><i>Diskrit Waktu</i>"]
    Sampler --> Quantizer["2. Kuantisasi (2^B Step)<br>xq[n]<br><i>Diskrit Nilai</i>"]
    Quantizer --> Encoder["3. Encoding (Biner)<br>Stream Bit 0 & 1"]
    Encoder --> DSPCore["Digital Signal Processor<br>(CPU / FPGA / DSP)"]

    style Analog fill:#1e293b,stroke:#64748b,color:#fff
    style LPF fill:#78350f,stroke:#f59e0b,color:#fff
    style Sampler fill:#312e81,stroke:#6366f1,color:#fff
    style Quantizer fill:#581c87,stroke:#a855f7,color:#fff
    style Encoder fill:#064e3b,stroke:#10b981,color:#fff
    style DSPCore fill:#0f172a,stroke:#38bdf8,color:#fff
```

---

## 2.3 Tahap 1: Pencuplikan (Sampling) & Peran Detak Clock

* Generator clock osilator membangkitkan trigger periodik tiap $T_s = \frac{1}{F_s}$. Rangkaian *Sample-and-Hold* menangkap nilai tegangan sesaat $x[n] = x(n \cdot T_s)$.
* **Status:** Diskrit dalam waktu, namun amplitudo masih berupa bilangan riil kontinu.

---

## 2.4 Teorema Nyquist-Shannon & Bahaya Fenomena Aliasing

> **🛡️ Teorema Sampling Nyquist:**  
> $$F_s \geq 2 \cdot f_{\text{maks}}$$
* Jika $F_s < 2 f_{\text{maks}}$, terjadi fenomena **Aliasing** (frekuensi tinggi menyamar menjadi frekuensi rendah palsu).

---

## 2.5 Mengapa Wajib Ada Filter Anti-Aliasing Sebelum Sampling?

Filter analog Low-Pass Filter (LPF) dipasang tepat sebelum ADC untuk memangkas frekuensi liar $f > F_s/2$ agar tidak merusak data.

---

## 2.6 Tahap 2: Kuantisasi (Quantization) — Seni Membulatkan Nilai

* **Jumlah Step ($L$):** $L = 2^B$.
* **Lebar Rentang Per Step (*Step Size* $\Delta$):**
  $$\Delta = \frac{V_{\text{maks}} - V_{\text{min}}}{2^B}$$
* **Quantization Error ($e$):** $e = x_q[n] - x[n]$, di mana $|e| \leq \frac{\Delta}{2}$.

---

## 2.7 Tahap 3: Pengkodean (Encoding) ke Deretan Bit Biner Digital

![Karakteristik Kuantisasi 3-Bit 0-10V](assets/kuantisasi_3bit_0_10v.png)

### Tabel Pemetaan Step Kuantisasi vs Biner 3-Bit ($0\text{V} - 10\text{V}$):
$$\Delta = \frac{10\text{ V} - 0\text{ V}}{8} = 1.25\text{ Volt / step}$$

| Step Kuantisasi | Rentang Tegangan Analog Input ($V_{\text{in}}$) | Kode Biner Encoding ($3$-bit) | Nilai Tengah Representasi ($V_q$) |
| :---: | :---: | :---: | :---: |
| **Step 1** | $0.00\text{ V} \leq V_{\text{in}} < 1.25\text{ V}$ | **`000`** | $0.625\text{ V}$ |
| **Step 2** | $1.25\text{ V} \leq V_{\text{in}} < 2.50\text{ V}$ | **`001`** | $1.875\text{ V}$ |
| **Step 3** | $2.50\text{ V} \leq V_{\text{in}} < 3.75\text{ V}$ | **`010`** | $3.125\text{ V}$ |
| **Step 4** | $3.75\text{ V} \leq V_{\text{in}} < 5.00\text{ V}$ | **`011`** | $4.375\text{ V}$ |
| **Step 5** | $5.00\text{ V} \leq V_{\text{in}} < 6.25\text{ V}$ | **`100`** | $5.625\text{ V}$ |
| **Step 6** | $6.25\text{ V} \leq V_{\text{in}} < 7.50\text{ V}$ | **`101`** | $6.875\text{ V}$ |
| **Step 7** | $7.50\text{ V} \leq V_{\text{in}} < 8.75\text{ V}$ | **`110`** | $8.125\text{ V}$ |
| **Step 8** | $8.75\text{ V} \leq V_{\text{in}} \leq 10.00\text{ V}$| **`111`** | $9.375\text{ V}$ |

---

## 2.8 Studi Kasus End-to-End: Konversi Sinyal Sinus Utuh x(t) ke Aliran Biner

* **Sinyal Masukan:** $x(t) = 5 + 4 \cdot \sin(2\pi \cdot 1 \cdot t)\text{ Volt}$
* **Spesifikasi ADC:** $3\text{-bit}$, rentang $0-10\text{ V}$, Clock $F_s = 8\text{ Hz}$ ($T_s = 0.125\text{ detik}$, $8$ titik sampel $n = 0 \dots 7$).

![Studi Kasus Konversi Lengkap](assets/studi_kasus_konversi_lengkap.png)

### Tabel Rekapitulasi Lengkap 8 Titik Sampel:

| Sampel ($n$) | Waktu ($t$) | Tegangan Analog $V_{\text{in}}$ | Step Kuantisasi | Nilai Level $V_q$ | Output Biner | Quantization Error ($e$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$n = 0$** | $0.000\text{ s}$ | $5.00\text{ V}$ | **Step 5** | $5.625\text{ V}$ | **`100`** | $+0.625\text{ V}$ |
| **$n = 1$** | $0.125\text{ s}$ | $7.83\text{ V}$ | **Step 7** | $8.125\text{ V}$ | **`110`** | $+0.295\text{ V}$ |
| **$n = 2$** | $0.250\text{ s}$ | $9.00\text{ V}$ (Peak) | **Step 8** | $9.375\text{ V}$ | **`111`** | $+0.375\text{ V}$ |
| **$n = 3$** | $0.375\text{ s}$ | $7.83\text{ V}$ | **Step 7** | $8.125\text{ V}$ | **`110`** | $+0.295\text{ V}$ |
| **$n = 4$** | $0.500\text{ s}$ | $5.00\text{ V}$ | **Step 5** | $5.625\text{ V}$ | **`100`** | $+0.625\text{ V}$ |
| **$n = 5$** | $0.625\text{ s}$ | $2.17\text{ V}$ | **Step 2** | $1.875\text{ V}$ | **`001`** | $-0.295\text{ V}$ |
| **$n = 6$** | $0.750\text{ s}$ | $1.00\text{ V}$ (Trough) | **Step 1** | $0.625\text{ V}$ | **`000`** | $-0.375\text{ V}$ |
| **$n = 7$** | $0.875\text{ s}$ | $2.17\text{ V}$ | **Step 2** | $1.875\text{ V}$ | **`001`** | $-0.295\text{ V}$ |

### Aliran Bit Digital Akhir (*Bitstream*):

$$\mathbf{\text{Aliran Bit (Bitstream)}} = \underbrace{\mathbf{100}}_{n=0} \ \underbrace{\mathbf{110}}_{n=1} \ \underbrace{\mathbf{111}}_{n=2} \ \underbrace{\mathbf{110}}_{n=3} \ \underbrace{\mathbf{100}}_{n=4} \ \underbrace{\mathbf{001}}_{n=5} \ \underbrace{\mathbf{000}}_{n=6} \ \underbrace{\mathbf{001}}_{n=7}$$
