# 📘 MODUL PEMBELAJARAN PENGOLAHAN SINYAL DIGITAL (PSD)
**Materi Terkompilasi — Sinyal, Sistem, dan Proses Digitalisasi (ADC)**

---

## 📑 DAFTAR ISI MODUL
* [BAB 1: Pengantar Sinyal, Sistem, dan Paradigma Pemrosesan](#bab-1-pengantar-sinyal-sistem-dan-paradigma-pemrosesan)
  * [1.1 Definisi Fundamental Sinyal](#11-definisi-fundamental-sinyal)
  * [1.2 Representasi Matematis Sinyal](#12-representasi-matematis-sinyal)
  * [1.3 Tiga Parameter Utama Sinyal](#13-tiga-parameter-utama-sinyal)
  * [1.4 Anatomi Visual Grafik Sinyal](#14-anatomi-visual-grafik-sinyal)
  * [1.5 Komparasi Visual Parameter Sinyal](#15-komparasi-visual-parameter-sinyal)
  * [1.6 Studi Kasus: Sinyal Ucapan (Speech Signal)](#16-studi-kasus-sinyal-ucapan)
  * [1.7 Konsep Dasar Sistem](#17-konsep-dasar-sistem)
  * [1.8 Tiga Bentuk Realisasi Sistem](#18-tiga-bentuk-realisasi-sistem)
  * [1.9 Klasifikasi Karakteristik Operasi Sistem](#19-klasifikasi-karakteristik-operasi-sistem)
  * [1.10 Paradigma Pemrosesan Sinyal: ASP vs DSP](#110-paradigma-pemrosesan-sinyal-asp-vs-dsp)
  * [1.11 Keunggulan Paradigma DSP](#111-keunggulan-paradigma-dsp)
* [BAB 2: Digitalisasi Sinyal (ADC & Proses Sampling)](#bab-2-digitalisasi-sinyal-adc--proses-sampling)
  * [2.1 Rantai Lengkap Konversi Analog ke Digital (ADC)](#21-rantai-lengkap-konversi-analog-ke-digital-adc)
  * [2.2 Tahap 1: Pencuplikan (Sampling) & Pulsa Clock](#22-tahap-1-pencuplikan-sampling--pulsa-clock)
  * [2.3 Tahap 2: Kuantisasi (Quantization) & Perhitungan Step](#23-tahap-2-kuantisasi-quantization--perhitungan-step)
  * [2.4 Tahap 3: Pengkodean (Encoding) ke Kode Biner](#24-tahap-3-pengkodean-encoding-ke-kode-biner)
  * [2.5 Tabel Terpadu Step Kuantisasi vs Kode Encoding Biner 3-Bit (0V - 10V)](#25-tabel-terpadu-step-kuantisasi-vs-kode-encoding-biner-3-bit-0v---10v)
  * [2.6 Studi Kasus End-to-End: Konversi Sinyal Utuh ke Aliran Bit Biner](#26-studi-kasus-end-to-end-konversi-sinyal-utuh-ke-aliran-bit-biner)
  * [2.7 Teorema Sampling Nyquist-Shannon & Aliasing](#27-teorema-sampling-nyquist-shannon--aliasing)

---

# BAB 1: Pengantar Sinyal, Sistem, dan Paradigma Pemrosesan

## 1.1 Definisi Fundamental Sinyal
> **📌 Definisi Sinyal:**  
> **Sinyal** adalah suatu besaran fisik yang nilainya berubah terhadap waktu, ruang, atau satu maupun lebih variabel bebas lainnya. Sinyal berfungsi sebagai media pembawa informasi fisik dari suatu fenomena alam atau sensor ke sistem pengolah data.

```mermaid
graph LR
    Fenomena["Fenomena Fisik<br>(Tekanan Suara, Suhu, Gelombang Otak)"] -->|Transduser / Sensor| Sinyal["Sinyal Fisik x(t)<br><i>Besaran yang Berubah terhadap Variabel Bebas</i>"]
    Sinyal -->|Sistem DSP| Info["Informasi yang Dimengerti Komputer / Manusia"]
    
    style Fenomena fill:#1e293b,stroke:#f59e0b,color:#fff
    style Sinyal fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#fff
    style Info fill:#064e3b,stroke:#10b981,color:#fff
```

---

## 1.2 Representasi Matematis Sinyal
* **Sinyal 1-Dimensi (1D) — $x = f(t)$:** Contoh: sinyal suara ucapan $s(t)$, tegangan listrik sensor $v(t)$, sinyal detak jantung ECG $x(t)$.
* **Sinyal 2-Dimensi (2D) — $I = f(x, y)$:** Contoh: citra digital/foto (intensitas kecerahan pada baris $x$ dan kolom $y$).
* **Sinyal Multi-Dimensi (3D/4D) — $V = f(x, y, t)$:** Contoh: video digital atau citra medis CT-Scan/MRI 3D.

---

## 1.3 Tiga Parameter Utama Sinyal
$$x(t) = A \cdot \sin(2\pi f t + \phi) = A \cdot \sin(\omega t + \phi)$$

| Parameter | Simbol & Satuan | Makna Matematis | Makna Fisik (Contoh Audio) |
| :--- | :--- | :--- | :--- |
| **Amplitudo** | $A$ (Volt, Pascal, dsb.) | Simpangan puncak maksimum gelombang dari titik nol. | **Kekuatan / Volume Suara (*Loudness*)**. |
| **Frekuensi** | $f = \frac{1}{T}$ (Hz) atau $\omega = 2\pi f$ (rad/s) | Jumlah siklus gelombang penuh per 1 detik. | **Tinggi-Rendah Nada (*Pitch*)**. |
| **Fase** | $\phi$ (Radian / Derajat) | Posisi awal gelombang pada saat $t = 0$. | **Pergeseran Waktu / Arah Kedatangan**. |

---

## 1.4 Anatomi Visual Grafik Sinyal
![Anatomi Parameter Sinyal](assets/anatomi_sinyal.png)

---

## 1.5 Komparasi Visual Parameter Sinyal
![Komparasi Visual Frekuensi, Amplitudo, dan Fase](assets/komparasi_sinyal.png)

---

## 1.6 Studi Kasus: Sinyal Ucapan (*Speech Signal*)
* **Informasi Fonem/Tekstual:** Resonansi rongga vokal (*Formant* $F_1, F_2, F_3$).
* **Informasi Pembicara:** Frekuensi dasar pita suara ($F_0$) dan timbre suara.
* **Informasi Emosi & Intonasi:** Modulasi amplitudo dan kontur naik-turunnya frekuensi.

---

## 1.7 Konsep Dasar Sistem
> **📌 Definisi Sistem:**  
> **Sistem** adalah perangkat fisik atau realisasi perangkat lunak yang melakukan suatu operasi matematis atau transformasi pada sinyal masukan $x[n]$ untuk menghasilkan sinyal keluaran $y[n]$ yang diinginkan:
> $$y[n] = \mathcal{T}\{x[n]\}$$

---

## 1.8 Tiga Bentuk Realisasi Sistem
1. **Hardware Murni (Analog):** Rangkaian RLC, Op-Amp, Transistor.
2. **Software Murni (Digital):** Algoritma Python, C++, MATLAB pada CPU/Server.
3. **Hybrid / Embedded Firmware:** Chip DSP (TMS320), FPGA, Mikrokontroler (STM32, ESP32).

---

## 1.9 Klasifikasi Karakteristik Operasi Sistem
* **Linear vs Non-Linear:** Memenuhi prinsip superposisi $\mathcal{T}\{a x_1 + b x_2\} = a \mathcal{T}\{x_1\} + b \mathcal{T}\{x_2\}$.
* **Time-Invariant (TI) vs Time-Variant:** $x[n - n_0] \implies y[n - n_0]$.
* **Kausal vs Non-Kausal:** Output saat ini hanya bergantung pada input saat ini dan masa lalu.
* **Stabilitas BIBO:** Input terbatas selalu menghasilkan output terbatas.

---

## 1.10 Paradigma Pemrosesan Sinyal: ASP vs DSP
![Diagram Paradigma ASP vs DSP](assets/diagram_asp_vs_dsp.png)

---

## 1.11 Keunggulan Paradigma DSP
* **Fleksibilitas:** Ubah fungsi sistem cukup via update baris kode software tanpa solder ulang PCB.
* **Kekebalan Derau:** Representasi biner (0 dan 1) kebal terhadap penurunan tegangan kecil.
* **Presisi Tinggi:** Reprodusibilitas 100% konsisten (32-bit / 64-bit floating point).
* **Penyimpanan Lossless:** Disimpan di flashdisk/cloud selamanya tanpa penurunan kualitas.

---

# BAB 2: Digitalisasi Sinyal (ADC & Proses Sampling)

Untuk dapat diproses oleh komputer digital, sinyal analog dari alam nyata harus melalui proses konversi **Analog-to-Digital (ADC)**.

![Tahapan ADC Sampling dan Kuantisasi](assets/tahapan_adc_sampling_kuantisasi.png)

---

## 2.1 Rantai Lengkap Konversi Analog ke Digital (ADC)

```mermaid
flowchart LR
    Analog["1. Sinyal Analog x(t)<br><i>Kontinu Waktu & Nilai</i>"] --> LPF["Anti-Aliasing Filter<br>(Low-Pass Analog)"]
    LPF --> Sampler["2. Sampling (Clock Ts)<br>x[n] = x(nTs)<br><i>Diskrit Waktu</i>"]
    Sampler --> Quantizer["3. Kuantisasi (2^B Level)<br>xq[n]<br><i>Diskrit Nilai</i>"]
    Quantizer --> Encoder["4. Encoding (Biner)<br>Stream Bit 0 & 1"]
    Encoder --> DSPCore["Digital Signal Processor<br>(CPU / FPGA / DSP)"]

    style Analog fill:#1e293b,stroke:#64748b,color:#fff
    style LPF fill:#78350f,stroke:#f59e0b,color:#fff
    style Sampler fill:#312e81,stroke:#6366f1,color:#fff
    style Quantizer fill:#581c87,stroke:#a855f7,color:#fff
    style Encoder fill:#064e3b,stroke:#10b981,color:#fff
    style DSPCore fill:#0f172a,stroke:#38bdf8,color:#fff
```

---

## 2.2 Tahap 1: Pencuplikan (Sampling) & Pulsa Clock
* **Proses:** Mengubah waktu kontinu $t \to n \cdot T_s$.
* **Pulsa Clock:** Osilator membangkitkan trigger periodik tiap $T_s = \frac{1}{F_s}$. Rangkaian *Sample-and-Hold* menangkap nilai sesaat $x[n] = x(n \cdot T_s)$.
* **Status:** Diskrit dalam waktu, namun amplitudo masih kontinu.

---

## 2.3 Tahap 2: Kuantisasi (Quantization) & Perhitungan Step

* **Proses:** Memetakan dan membulatkan rentang amplitudo kontinu ke dalam sejumlah step diskrit $x_q[n]$.
* **Jumlah Step Level ($L = 2^B$):** Untuk ADC beresolusi $B$-bit, terdapat $2^B$ buah step level diskrit.
* **Lebar Rentang Per Step (*Step Size* $\Delta$):**
  $$\Delta = \frac{V_{\text{maks}} - V_{\text{min}}}{2^B}$$
  Untuk ADC 3-bit dengan rentang tegangan $0\text{ V} - 10\text{ V}$:
  $$\Delta = \frac{10\text{ V} - 0\text{ V}}{8} = 1.25\text{ Volt / step}$$

---

## 2.4 Tahap 3: Pengkodean (Encoding) ke Kode Biner

* **Proses:** Menetapkan deretan angka biner $B$-bit unik untuk setiap rentang step kuantisasi.
* **Format Biner 3-Bit:** Menghasilkan 8 kombinasi biner mulai dari `000` hingga `111`.

---

## 2.5 Tabel Terpadu Step Kuantisasi vs Kode Encoding Biner 3-Bit (0V - 10V)

![Karakteristik Kuantisasi 3-Bit 0-10V](assets/kuantisasi_3bit_0_10v.png)

| Step Kuantisasi | Rentang Tegangan Analog Input ($V_{\text{in}}$) | Kode Biner Encoding ($3$-bit) | Nilai Representasi Ideal ($V_q$) |
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

## 2.6 Studi Kasus End-to-End: Konversi Sinyal Utuh ke Aliran Bit Biner

Berikut adalah contoh komprehensif konversi sinyal analog riil dari awal gelombang utuh hingga menjadi aliran biner digital:

### A. Skenario Sinyal & Spesifikasi ADC:
1. **Persamaan Gelombang Sinyal Analog Asli:**
   $$x(t) = 5 + 4 \cdot \sin(2\pi \cdot 1 \cdot t) \quad \text{Volt}$$
   * Tegangan terendah (Lembah): $V_{\text{min}} = 5 - 4 = 1.00\text{ Volt}$.
   * Tegangan tertinggi (Puncak): $V_{\text{maks}} = 5 + 4 = 9.00\text{ Volt}$.
   * Frekuensi sinyal: $f = 1\text{ Hz}$ (Periode $T = 1\text{ detik}$).
2. **Spesifikasi ADC:**
   * Resolusi: $B = 3\text{ bit}$ ($L = 8\text{ step}$, Step Size $\Delta = 1.25\text{ V}$).
   * Frekuensi Sampling Clock: $F_s = 8\text{ Hz}$ $\implies$ Interval Pencuplikan $T_s = \frac{1}{8} = 0.125\text{ detik}$.
   * Diambil $8$ titik sampel ($n = 0, 1, 2, 3, 4, 5, 6, 7$) selama 1 siklus penuh ($t = 0$ s.d. $1\text{ detik}$).

---

### B. Grafik Visual Pelacakan Sampel Demi Sampel:

![Studi Kasus Konversi Lengkap](assets/studi_kasus_konversi_lengkap.png)

---

### C. Perhitungan Rinci Titik demi Titik (Per Detak Clock $n$):

1. **Sampel $n=0$ ($t = 0.000\text{ s}$):**
   * $V_{\text{in}} = 5 + 4\sin(0) = \mathbf{5.00\text{ V}}$
   * Masuk Rentang: Step 5 ($5.00\text{ V} - 6.25\text{ V}$) $\implies$ **Biner: `100`**
   * Error: $e = |5.00 - 5.625| = 0.625\text{ V}$

2. **Sampel $n=1$ ($t = 0.125\text{ s}$):**
   * $V_{\text{in}} = 5 + 4\sin(\pi/4) = 5 + 4(0.7071) = \mathbf{7.83\text{ V}}$
   * Masuk Rentang: Step 7 ($7.50\text{ V} - 8.75\text{ V}$) $\implies$ **Biner: `110`**
   * Error: $e = |7.83 - 8.125| = 0.295\text{ V}$

3. **Sampel $n=2$ ($t = 0.250\text{ s}$ — Puncak Gelombang):**
   * $V_{\text{in}} = 5 + 4\sin(\pi/2) = 5 + 4(1) = \mathbf{9.00\text{ V}}$
   * Masuk Rentang: Step 8 ($8.75\text{ V} - 10.00\text{ V}$) $\implies$ **Biner: `111`**
   * Error: $e = |9.00 - 9.375| = 0.375\text{ V}$

4. **Sampel $n=3$ ($t = 0.375\text{ s}$):**
   * $V_{\text{in}} = 5 + 4\sin(3\pi/4) = 5 + 4(0.7071) = \mathbf{7.83\text{ V}}$
   * Masuk Rentang: Step 7 ($7.50\text{ V} - 8.75\text{ V}$) $\implies$ **Biner: `110`**
   * Error: $e = |7.83 - 8.125| = 0.295\text{ V}$

5. **Sampel $n=4$ ($t = 0.500\text{ s}$):**
   * $V_{\text{in}} = 5 + 4\sin(\pi) = \mathbf{5.00\text{ V}}$
   * Masuk Rentang: Step 5 ($5.00\text{ V} - 6.25\text{ V}$) $\implies$ **Biner: `100`**
   * Error: $e = |5.00 - 5.625| = 0.625\text{ V}$

6. **Sampel $n=5$ ($t = 0.625\text{ s}$):**
   * $V_{\text{in}} = 5 + 4\sin(5\pi/4) = 5 - 4(0.7071) = \mathbf{2.17\text{ V}}$
   * Masuk Rentang: Step 2 ($1.25\text{ V} - 2.50\text{ V}$) $\implies$ **Biner: `001`**
   * Error: $e = |2.17 - 1.875| = 0.295\text{ V}$

7. **Sampel $n=6$ ($t = 0.750\text{ s}$ — Lembah Gelombang):**
   * $V_{\text{in}} = 5 + 4\sin(3\pi/2) = 5 - 4(1) = \mathbf{1.00\text{ V}}$
   * Masuk Rentang: Step 1 ($0.00\text{ V} - 1.25\text{ V}$) $\implies$ **Biner: `000`**
   * Error: $e = |1.00 - 0.625| = 0.375\text{ V}$

8. **Sampel $n=7$ ($t = 0.875\text{ s}$):**
   * $V_{\text{in}} = 5 + 4\sin(7\pi/4) = 5 - 4(0.7071) = \mathbf{2.17\text{ V}}$
   * Masuk Rentang: Step 2 ($1.25\text{ V} - 2.50\text{ V}$) $\implies$ **Biner: `001`**
   * Error: $e = |2.17 - 1.875| = 0.295\text{ V}$

---

### D. Tabel Rekapitulasi Konversi 8 Titik Sampel:

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

---

### E. Aliran Bit Digital Akhir (*Digital Bitstream Output*):

Seluruh deretan biner dikirimkan secara sekuensial ke prosesor DSP:

$$\mathbf{\text{Bitstream}} = \underbrace{\mathbf{100}}_{n=0} \ \underbrace{\mathbf{110}}_{n=1} \ \underbrace{\mathbf{111}}_{n=2} \ \underbrace{\mathbf{110}}_{n=3} \ \underbrace{\mathbf{100}}_{n=4} \ \underbrace{\mathbf{001}}_{n=5} \ \underbrace{\mathbf{000}}_{n=6} \ \underbrace{\mathbf{001}}_{n=7}$$

---

## 2.7 Teorema Sampling Nyquist-Shannon & Aliasing
$$F_s \geq 2 \cdot f_{\text{max}}$$
* **Frekuensi Nyquist:** $f_N = \frac{F_s}{2}$.
* Jika $F_s < 2 f_{\text{max}}$, terjadi fenomena **Aliasing** (frekuensi tinggi menyamar menjadi frekuensi rendah palsu).
* Filter analog **Anti-Aliasing LPF** wajib dipasang sebelum ADC.
