# 📘 BUKU AJAR VISUAL KOMPREHENSIF PENGOLAHAN SINYAL DIGITAL (PSD)
*Panduan Analitis & Visual Tingkat Lanjut: Dari Fisika Sensor \& Transduksi, Formulasi Rantai ASP vs DSP, Konversi Digitalisasi ADC, Teori Kuantisasi \& Kinerja SQNR, Aljabar Sinyal Multikanal-Multidimensi, hingga Analisis Frekuensi Diskrit Tingkat Lanjut*

---

# BAB 1: Fondasi Pemrosesan Sinyal & Analisis Gelombang

## 📑 DAFTAR ISI BAB 1

- [1.1 Paradigma Pemrosesan Sinyal — Dari Dunia Fisik Analog (ASP) ke Era Digital (DSP)](#11-paradigma-pemrosesan-sinyal--dari-dunia-fisik-analog-asp-ke-era-digital-dsp)
  - [1.1.1 Dari Fenomena Fisik Menjadi Sinyal Listrik (Peran Sensor & Transduser)](#111-dari-fenomena-fisik-menjadi-sinyal-listrik-peran-sensor--transduser)
  - [1.1.2 Paradigma Pemrosesan: Rantai ASP (Analog) vs Rantai DSP (Digital)](#112-paradigma-pemrosesan-rantai-asp-analog-vs-rantai-dsp-digital)
  - [1.1.3 Tiga Pilar Anatomi Gelombang: Amplitudo, Frekuensi, dan Fase](#113-tiga-pilar-anatomi-gelombang-amplitudo-frekuensi-dan-fase)
  - [1.1.4 Sistem Pengolah Sinyal & 4 Klasifikasi Karakteristik Operasinya](#114-sistem-pengolah-sinyal--4-klasifikasi-karakteristik-operasinya)
- [1.2 Proses Digitalisasi Sinyal (Analog-to-Digital Converter / ADC)](#12-proses-digitalisasi-sinyal-analog-to-digital-converter--adc)
  - [1.2.1 Rantai 4 Tahap Lengkap Digitalisasi ADC](#121-rantai-4-tahap-lengkap-digitalisasi-adc)
  - [1.2.2 Pencuplikan (Sampling Clock), Teorema Nyquist, dan Bencana Aliasing](#122-pencuplikan-sampling-clock-teorema-nyquist-dan-bencana-aliasing)
  - [1.2.3 Kuantisasi & Pengkodean Biner 3-Bit (Rentang 0 s.d. 10 Volt)](#123-kuantisasi--pengkodean-biner-3-bit-rentang-0-sd-10-volt)
  - [1.2.4 Studi Kasus End-to-End: Konversi Sinyal Sinus Utuh x(t) ke Aliran Bit Biner](#124-studi-kasus-end-to-end-konversi-sinyal-sinus-utuh-xt-ke-aliran-bit-biner)
- [1.3 Klasifikasi Lanjutan Sinyal Modern](#13-klasifikasi-lanjutan-sinyal-modern)
  - [1.3.1 Sinyal Multikanal (Multi-Channel Signals) & Representasi Vektor-Matriks](#131-sinyal-multikanal-multi-channel-signals--representasi-vektor-matriks)
  - [1.3.2 Sinyal Multi-Dimensi (Multi-Dimensional Signals / M-D): 1D, 2D, 3D, hingga 4D](#132-sinyal-multi-dimensi-multi-dimensional-signals--m-d-1d-2d-3d-hingga-4d)
  - [1.3.3 Sinyal Waktu Diskrit (Discrete-Time Signals / DTS) & Sinyal Elementer](#133-sinyal-waktu-diskrit-discrete-time-signals--dts--sinyal-elementer)
- [1.4 Klasifikasi Ruang Nilai & Kepastian Sinyal](#14-klasifikasi-ruang-nilai--kepastian-sinyal)
  - [1.4.1 Definisi Hakiki Sinyal Digital: Diskrit Waktu & Diskrit Amplitudo (4 Ruang Sinyal)](#141-definisi-hakiki-sinyal-digital-diskrit-waktu--diskrit-amplitudo-4-ruang-sinyal)
  - [1.4.2 Sinyal Deterministik vs Sinyal Acak (Random / Stokastik)](#142-sinyal-deterministik-vs-sinyal-acak-random--stokastik)
- [1.5 Analisis Frekuensi & Gelombang Sinusoidal (Kontinu vs Diskrit)](#15-analisis-frekuensi--gelombang-sinusoidal-kontinu-vs-diskrit)
  - [1.5.1 Perbandingan Domain Frekuensi: Sinyal Waktu Kontinu vs Sinyal Waktu Diskrit](#151-perbandingan-domain-frekuensi-sinyal-waktu-kontinu-vs-sinyal-waktu-diskrit)
  - [1.5.2 Sinyal Sinusoidal Waktu-Kontinu (1/2): Sifat Keunikan Frekuensi Fisik & Laju Tak Terbatas](#152-sinyal-sinusoidal-waktu-kontinu-12-sifat-keunikan-frekuensi-fisik--laju-tak-terbatas)
  - [1.5.3 Sinyal Sinusoidal Waktu-Kontinu (2/2): Periodisitas Universal untuk Setiap Frekuensi F](#153-sinyal-sinusoidal-waktu-kontinu-22-periodisitas-universal-untuk-setiap-frekuensi-f)
  - [1.5.4 Sinyal Sinusoidal Waktu-Diskrit (1/3): Syarat Wajib Periodisitas Bilangan Rasional f = k/N](#154-sinyal-sinusoidal-waktu-diskrit-13-syarat-wajib-periodisitas-bilangan-rasional-f--kn)
  - [1.5.5 Sinyal Sinusoidal Waktu-Diskrit (2/3): Fenomena Frekuensi Identik Kelipatan 2π](#155-sinyal-sinusoidal-waktu-diskrit-23-fenomena-frekuensi-identik-kelipatan-2π)
  - [1.5.6 Sinyal Sinusoidal Waktu-Diskrit (3/3): Laju Osilasi Tertinggi pada ω = π (f = 1/2)](#156-sinyal-sinusoidal-waktu-diskrit-33-laju-osilasi-tertinggi-pada-ω--π-f--12)
- [1.6 Studi Kasus & Contoh Perhitungan Komprehensif Terpadu (Sintesis Subbab 1.1 - 1.5)](#16-studi-kasus--contoh-perhitungan-komprehensif-terpadu-sintesis-subbab-11---15)
- [1.7 Glosarium Ringkas Istilah Kunci Persinyalan](#17-glosarium-ringkas-istilah-kunci-persinyalan)

---

## 1.1 Paradigma Pemrosesan Sinyal — Dari Dunia Fisik Analog (ASP) ke Era Digital (DSP)

### 1.1.1 Dari Fenomena Fisik Menjadi Sinyal Listrik (Peran Sensor & Transduser)

Dunia fisis beroperasi berdasarkan besaran-besaran alamiah non-listrik yang bersifat kontinu terhadap ruang dan waktu. Untuk menjembatani dunia analog fisis dengan sistem komputasi terotomatisasi, diperlukan perangkat **transduser** (elemen pengubah bentuk energi) dan **sensor** (elemen pendeteksi kuantitas fisik spesifik).

Secara analitis, fungsi transduksi dari suatu sensor riil memetakan besaran fisis masukan $P(t)$ menjadi sinyal tegangan keluaran $v(t)$ melalui hubungan pemodelan matematis:
$$v(t) = \mathcal{S} \cdot P(t) + \beta \cdot P^2(t) + \eta(t)$$

di mana $\mathcal{S} = \left.\frac{\partial v}{\partial P}\right|_{P_0}$ merupakan koefisien sensitivitas nominal (*sensitivity factor*), $\beta$ merepresentasikan deviasi non-linieritas orde-2, dan $\eta(t)$ adalah derau termal aditif acak (*Johnson-Nyquist noise*) dengan kerapatan spektral daya:
$$\overline{v_n^2} = 4 k_B T R \Delta f \quad [\text{V}^2]$$
dengan $k_B = 1.380649 \times 10^{-23}\text{ J/K}$ (konstanta Boltzmann), $T$ suhu mutlak Kelvin, $R$ resistansi ekuivalen Thévenin sensor, dan $\Delta f$ lebar pita frekuensi pengukuran (*bandwidth*).

![Fenomena Fisik Menjadi Sinyal Listrik](assets/fenomena_fisik_ke_sinyal.png)

#### 🔍 Dekomposisi Fisik & Analisis Matematis Tiga Kelas Sinyal:

1. **Panel 1 (Gelombang Akustik / Suara — Biru Muda):**  
   Pita suara manusia menghasilkan gelombang longitudinal tekanan udara $p(x,t)$ yang merambat memenuhi persamaan gelombang Helmholtz 1-D:
   $$\frac{\partial^2 p(x,t)}{\partial x^2} - \frac{1}{c_s^2}\frac{\partial^2 p(x,t)}{\partial t^2} = 0 \quad (c_s \approx 343\text{ m/s})$$
   Diafragma mikrofon kapasitif mengubah gradien tekanan diferensial $\Delta p(t)$ menjadi perpindahan kapasitansi $\Delta C(t)$, menghasilkan fluktuasi tegangan $v(t) = \frac{Q_0}{C_0^2}\Delta C(t)$ berskala milivolt (mV) dengan spektrum vokal $50\text{ Hz} \le f \le 4\text{ kHz}$.

2. **Panel 2 (Dinamika Termal / Suhu — Oranye):**  
   Perpindahan panas pada medium sensor termokopel diatur oleh persamaan difusi Fourier $\frac{\partial T}{\partial t} = \alpha \nabla^2 T$. Respon transien kenaikan temperatur dari $25^\circ\text{C}$ menuju $65^\circ\text{C}$ dimodelkan oleh respon sistem orde-1:
   $$T(t) = T_{\text{akhir}} + (T_{\text{awal}} - T_{\text{akhir}})e^{-t/\tau_{\text{th}}} + w_{\text{thermal}}(t)$$
   di mana $\tau_{\text{th}} = R_{\text{th}} C_{\text{th}}$ adalah konstanta waktu termal. Tegangan Seebeck yang dihasilkan $v(t) = \alpha_S (T_{\text{hot}} - T_{\text{cold}})$ memperlihatkan riak derau gerigi mikro akibat fluktuasi termal acak.

3. **Panel 3 (Percepatan Seismik Kerak Bumi — Magenta):**  
   Gelombang elastisitas sesar tektonik mematuhi persamaan elastodinamika Navier-Cauchy:
   $$\rho \frac{\partial^2 \mathbf{u}}{\partial t^2} = (\lambda + \mu)\nabla(\nabla \cdot \mathbf{u}) + \mu \nabla^2 \mathbf{u}$$
   Massa seismometer menghasilkan gaya inersia $F(t) = -m \ddot{x}_g(t)$ yang ditransduksikan menjadi lonjakan akselerasi tajam hingga $+3.8\text{ m/s}^2$ pada saat $t = 3.0\text{ s}$ dan meluruh secara sinusoidal teredam (*damped harmonic oscillation*):
   $$a(t) = A_0 e^{-\zeta \omega_n (t - t_0)} \sin\left(\omega_n \sqrt{1 - \zeta^2}(t - t_0)\right) u(t - t_0)$$

---

### 1.1.2 Paradigma Pemrosesan: Rantai ASP (Analog) vs Rantai DSP (Digital)

![Diagram Paradigma ASP vs DSP](assets/diagram_asp_vs_dsp.png)

#### 🔍 Formulasi Matematis Sistem ASP vs DSP:

* **Arsitektur Rantai Analog Signal Processing (ASP):**  
  Sistem ASP direalisasikan oleh interkoneksi fisik komponen pasif ($R, L, C$) dan aktif (*Operational Amplifier*). Dinamika sistem kontinu dimodelkan secara rigid oleh Persamaan Diferensial Linier Koefisien Konstan (LCCDE):
  $$\sum_{k=0}^N a_k \frac{d^k y(t)}{dt^k} = \sum_{m=0}^M b_m \frac{d^m x(t)}{dt^m} \quad \xrightarrow{\mathcal{L}} \quad H(s) = \frac{Y(s)}{X(s)} = \frac{\sum_{m=0}^M b_m s^m}{\sum_{k=0}^N a_k s^k}$$
  *Kelemahan Kritis ASP:* Sensitivitas tinggi terhadap toleransi komponen $\frac{\Delta H(s)}{H(s)} \approx \sum_i S_{p_i}^H \frac{\Delta p_i}{p_i}$, drift termal resistansi $\Delta R(T) = R_0(1 + \alpha \Delta T)$, degradasi penuaan elektrolit kapasitor, rentan terhadap induksi dengung jala-jala $50/60\text{ Hz}$, serta ketidakmungkinan merancang filter dengan fase linear murni.

* **Arsitektur Rantai Digital Signal Processing (DSP):**  
  Sistem DSP memetakan cuplikan terkuantisasi melalui algoritma komputasi pada arsitektur prosesor (CPU, ALU, FPGA, DSP Chip). Dinamikanya diatur oleh Persamaan Beda Linier Koefisien Konstan (LCCDDE):
  $$\sum_{k=0}^N a_k y[n-k] = \sum_{m=0}^M b_m x[n-m] \quad \xrightarrow{\mathcal{Z}} \quad H(z) = \frac{Y(z)}{X(z)} = \frac{\sum_{m=0}^M b_m z^{-m}}{\sum_{k=0}^N a_k z^{-k}}$$
  *Keunggulan Superior DSP:*
  1. **Akurasi & Reproduktibilitas 100%:** Bebas dari drift suhu lingkungan dan toleransi nilai fisik komponen.
  2. **Fleksibilitas Reconfigurability:** Respons filter dapat diubah secara instan secara adaptif (*Adaptive LMS Filtering*) melalui perangkat lunak tanpa modifikasi sirkuit.
  3. **Fase Linear Sempurna:** Mampu merealisasikan filter FIR simetris dengan penundaan grup konstan ($\tau_g = -\frac{d\theta(\omega)}{d\omega} = \text{konstan}$), mustahil dicapai pada ASP.

---

### 1.1.3 Tiga Pilar Anatomi Gelombang: Amplitudo, Frekuensi, dan Fase

Persamaan matematis gelombang sinusoidal waktu-kontinu dinyatakan dalam domain riil dan domain kompleks Euler:
$$x(t) = A \sin(2\pi f t + \phi) = A \sin(\Omega t + \phi) \equiv \operatorname{Re}\left\{ A e^{j(\Omega t + \phi)} \right\} = \frac{A}{2j} e^{j(\Omega t + \phi)} - \frac{A}{2j} e^{-j(\Omega t + \phi)}$$

![Anatomi Parameter Sinyal](assets/anatomi_sinyal.png)

![Komparasi Visual Parameter Sinyal](assets/komparasi_sinyal.png)

#### 🔍 Karakterisasi Energi & Parameter Gelombang:

1. **Amplitudo ($A$) & Daya Sinyal ($P_{\text{avg}}$):**  
   Menentukan besaran simpangan puncak dari titik keseimbangan. Nilai kuadrat rata-rata (*Root-Mean-Square* / RMS) dan daya rata-rata untuk gelombang sinus beban $1\ \Omega$ adalah:
   $$V_{\text{rms}} = \sqrt{\frac{1}{T}\int_0^T x^2(t) dt} = \frac{A}{\sqrt{2}}, \qquad P_{\text{avg}} = V_{\text{rms}}^2 = \frac{A^2}{2}$$

2. **Frekuensi Siklik ($f$), Sudut ($\Omega$), dan Periode ($T$):**  
   $f$ mengukur laju osilasi per satuan waktu (Hertz $\equiv \text{s}^{-1}$), $\Omega = 2\pi f$ adalah kecepatan sudut ($\text{rad/s}$), dan periode fundamental $T = \frac{1}{f} = \frac{2\pi}{\Omega}$. Pada Gambar Komparasi Panel 1, peningkatan frekuensi dari $1\text{ Hz}$ ke $3\text{ Hz}$ melipatgandakan kerapatan energi spektral pada sumbu frekuensi.

3. **Fase Awal ($\phi$) & Pergeseran Waktu ($\Delta t$):**  
   Pergeseran fase $\phi$ setara secara eksak dengan translasi waktu $\Delta t = -\frac{\phi}{\Omega} = -\frac{\phi}{2\pi f}$. Jika $\phi = +90^\circ = +\frac{\pi}{2}\text{ rad}$ (Gambar Komparasi Panel 3), gelombang bertransformasi menjadi fungsi cosinus:
   $$x(t) = A \sin\left(\Omega t + \frac{\pi}{2}\right) = A \cos(\Omega t)$$
   yang mengindikasikan komponen kuadratur ($Q$-channel) mendahului (*leading*) komponen in-phase ($I$-channel) sebesar $\Delta t = -T/4$.

---

### 1.1.4 Sistem Pengolah Sinyal & 4 Klasifikasi Karakteristik Operasinya

Suatu sistem waktu-diskrit didefinisikan sebagai transformasi matematis atau operator $\mathcal{T}\{\cdot\}$ yang memetakan sinyal masukan $x[n]$ menjadi sinyal keluaran $y[n] = \mathcal{T}\{x[n]\}$.

![Klasifikasi Sistem](assets/klasifikasi_sistem.png)

#### 🔍 Uji Matematis Rigor Empat Sifat Karakteristik Sistem:

1. **Linearitas (Superposisi & Homogenitas):**  
   Sistem linier wajib memenuhi prinsip superposisi simultan:
   $$\mathcal{T}\left\{ \alpha x_1[n] + \beta x_2[n] \right\} = \alpha \mathcal{T}\{x_1[n]\} + \beta \mathcal{T}\{x_2[n]\} = \alpha y_1[n] + \beta y_2[n], \quad \forall \alpha, \beta \in \mathbb{C}$$
   *Analisis Visual (Panel 1):* Sistem $y[n] = 1.5 x[n]$ membentuk garis linier proporsional sempurna. Sebaliknya, sistem kubik $y[n] = 0.5 x^3[n]$ bersifat non-linier; jika dimasukkan input harmonisa tunggal $x[n] = \cos(\omega_0 n)$, keluarannya menghasilkan distorsi harmonisa ganjil $\cos^3(\omega_0 n) = \frac{3}{4}\cos(\omega_0 n) + \frac{1}{4}\cos(3\omega_0 n)$, memunculkan komponen frekuensi baru $3\omega_0$ yang merusak integritas sinyal asli.

2. **Kekekalan Waktu (Time-Invariance / TI):**  
   Operator sistem komutatif terhadap operator pergeseran waktu $\mathcal{S}_{n_0}\{x[n]\} = x[n - n_0]$:
   $$\mathcal{T}\left\{ \mathcal{S}_{n_0}\{x[n]\} \right\} = \mathcal{S}_{n_0}\left\{ \mathcal{T}\{x[n]\} \right\} \iff \mathcal{T}\{x[n - n_0]\} = y[n - n_0]$$
   *Analisis Visual (Panel 2):* Input yang ditunda sejauh $n_0 = 4$ detik menghasilkan kurva hijau yang identik secara morfologi dengan kurva oranye tanpa distorsi bentuk.

3. **Kausalitas (Causality):**  
   Keluaran sistem pada setiap indeks $n = n_0$ hanya bergantung pada nilai masukan saat ini dan masa lalu ($x[n]$ untuk $n \leq n_0$). Syarat perlu dan cukup untuk sistem Linier Time-Invariant (LTI) kausal adalah respon impulsnya harus nol untuk indeks waktu negatif:
   $$h[n] = 0, \quad \forall n < 0$$
   *Analisis Visual (Panel 3):* Respon ungu ($h[n] \neq 0$ hanya saat $n \geq 0$) bersifat kausal (*realizable* di dunia nyata). Respon pink aktif saat $n < 0$, mengindikasikan sistem non-kausal yang memerlukan pengetahuan input masa depan.

4. **Stabilitas BIBO (Bounded-Input Bounded-Output):**  
   Sistem stabil BIBO menjamin bahwa untuk setiap masukan terbatas $|x[n]| \leq M_x < \infty, \forall n$, keluarannya terikat terbatas $|y[n]| \leq M_y < \infty, \forall n$. Syarat perlu dan cukup untuk sistem LTI stabil BIBO adalah respon impulsnya **terjumlahkan secara mutlak** (*absolutely summable*):
   $$S_h = \sum_{k=-\infty}^{\infty} |h[k]| < \infty$$
   *Analisis Visual (Panel 4):* Untuk sistem orde-1 dengan respon impuls $h[n] = a^n u[n]$:
   $$S_h = \sum_{n=0}^{\infty} |a|^n = \frac{1}{1 - |a|} \quad \text{konvergen jika dan hanya jika } |a| < 1$$
   Kurva hijau ($a = 0.75 < 1$) menghasilkan $S_h = \frac{1}{1 - 0.75} = 4 < \infty$ (Stabil). Kurva merah ($a = 1.35 > 1$) menghasilkan deret divergen $S_h \to \infty$, memicu osilasi tak hingga yang merusak rangkaian (*Unstable*).

---

## 1.2 Proses Digitalisasi Sinyal (Analog-to-Digital Converter / ADC)

### 1.2.1 Rantai 4 Tahap Lengkap Digitalisasi ADC

![Tahapan Lengkap ADC](assets/tahapan_adc_sampling_kuantisasi.png)

#### 🔍 Formulasi Matematis 4 Blok Digitalisasi ADC:

1. **Anti-Aliasing Filter (AAF) & Sinyal Asli $x_a(t)$:**  
   Sinyal input analog kontinu $x_a(t) \in \mathbb{R}$ dilewatkan ke filter lolos-rendah (*low-pass filter*) analog dengan frekuensi cut-off $f_c \leq F_s / 2$ untuk memangkas komponen frekuensi tinggi di atas batas Nyquist.

2. **Pencuplikan Ideal (Ideal Impulse Train Sampling):**  
   Sinyal dikalikan dengan deretan pulsa Dirac periodik (*Dirac Comb*) $p(t) = \sum_{n=-\infty}^\infty \delta(t - n T_s)$:
   $$x_s(t) = x_a(t) \cdot p(t) = \sum_{n=-\infty}^\infty x_a(n T_s) \delta(t - n T_s)$$
   Domain waktu menghasilkan deret diskrit $x[n] \equiv x_a(n T_s)$, di mana waktu kini terdiskritisasi menjadi bilangan bulat $n \in \mathbb{Z}$, namun nilai amplitudo $x[n] \in \mathbb{R}$ masih berkesinambungan kontinu (*infinite precision*).

3. **Kuantisasi Amplitudo Non-Linier ($\mathcal{Q}\{\cdot\}$):**  
   Pemetaan fungsi tangga non-linier $\mathcal{Q}: \mathbb{R} \to \{V_1, V_2, \dots, V_L\}$ membulatkan nilai amplitudo riil $x[n]$ ke level representasi terdekat:
   $$x_q[n] = \mathcal{Q}\{x[n]\} = x[n] + e_q[n]$$
   di mana $e_q[n] = x_q[n] - x[n]$ adalah galat kuantisasi (*quantization error*). Sinyal kini diskrit dalam waktu dan diskrit dalam nilai amplitudo.

4. **Pengkodean Biner (Binary Word Encoding $\mathcal{E}\{\cdot\}$):**  
   Setiap level indeks $k \in \{0, 1, \dots, 2^B - 1\}$ dipetakan menjadi vektor biner $B$-bit:
   $$\mathbf{b}[n] = \mathcal{E}\{x_q[n]\} = [b_{B-1}, b_{B-2}, \dots, b_1, b_0]^T, \quad b_i \in \{0, 1\}$$
   menghasilkan aliran bit serial (*bitstream*) berkecepatan data $R = B \cdot F_s\ \text{bps}$.

---

### 1.2.2 Pencuplikan (Sampling Clock), Teorema Nyquist, dan Bencana Aliasing

Transformasi Fourier dari sinyal tercuplik $x_s(t)$ diturunkan melalui sifat konvolusi domain frekuensi:
$$X_s(F) = \mathcal{F}\left\{ x_a(t) \cdot \sum_{n=-\infty}^\infty \delta(t - n T_s) \right\} = F_s \sum_{k=-\infty}^\infty X_a(F - k F_s)$$

![Sampling Nyquist dan Aliasing](assets/sampling_nyquist_aliasing.png)

#### 🔍 Derivasi Perilaku Tiga Kondisi Sampling:

* **Kondisi A — Over-Sampling ($F_s = 40\text{ Hz} \gg 2 f_{\max} = 10\text{ Hz}$):**  
  Replika spektral $X_a(F - k F_s)$ terpisah sejauh interval $40\text{ Hz}$ dengan pita transisi pelindung (*guard band*) selebar $\Delta F = F_s - 2 f_{\max} = 30\text{ Hz}$. Rekonstruksi gelombang melalui filter rekonstruksi ideal menghasilkan sinyal asli sempurna 100% tanpa distorsi.

* **Kondisi B — Batas Kritis Nyquist ($F_s = 10\text{ Hz} = 2 f_{\max}$):**  
  Ujung-ujung spektrum replika tepat bersinggungan pada frekuensi lipat $f_{\text{fold}} = F_s / 2 = 5\text{ Hz}$. Rekonstruksi masih dimungkinkan secara teoritis menggunakan filter *brick-wall* ideal tanpa guard band.

* **Kondisi C — Bencana Under-Sampling & Aliasing ($F_s = 6\text{ Hz} < 2 f_{\max}$):**  
  Spektrum replika mengalami tumpang tindih (*spectral overlapping*). Komponen frekuensi asli $F = +5\text{ Hz}$ terlipat masuk ke pita dasar $|F| \le F_s/2 = 3\text{ Hz}$ menghasilkan frekuensi semu alias:
  $$f_{\text{alias}} = |F - 1 \cdot F_s| = |5\text{ Hz} - 6\text{ Hz}| = 1\text{ Hz}$$
  Komputer merekonstruksi gelombang hantu palsu berwarna merah pada frekuensi $1\text{ Hz}$ yang sama sekali tidak ada di dunia nyata!

> **🛡️ Teorema Sampling Nyquist-Shannon & Rekonstruksi Whittaker-Shannon:**
> Jika sinyal kontinu $x_a(t)$ berpita terbatas pada rentang $-f_{\max} \le F \le f_{\max}$, maka $x_a(t)$ dapat dipulihkan secara eksak tanpa cacat dari sampel diskritnya $x[n] = x_a(n T_s)$ jika dan hanya jika $F_s \geq 2 f_{\max}$, dengan rumus rekonstruksi interpolasi sinus kardinal (Sinc):
> $$x_a(t) = \sum_{n=-\infty}^{\infty} x[n] \operatorname{sinc}\left( \frac{t - n T_s}{T_s} \right) = \sum_{n=-\infty}^{\infty} x[n] \frac{\sin\left(\pi (t - n T_s)/T_s\right)}{\pi (t - n T_s)/T_s}$$

---

### 1.2.3 Kuantisasi & Pengkodean Biner 3-Bit (Rentang 0 s.d. 10 Volt)

Kuantisasi seragam (*uniform quantization*) membagi rentang tegangan penuh $V_{\text{range}} = V_{\text{maks}} - V_{\text{min}}$ menjadi $L = 2^B$ sub-interval dengan lebar step $\Delta$:
$$\Delta = \frac{V_{\text{maks}} - V_{\text{min}}}{2^B} = \frac{10.0\text{ V} - 0.0\text{ V}}{2^3} = \frac{10.0\text{ V}}{8} = 1.25\text{ Volt / step}$$

![Karakteristik Kuantisasi 3-Bit 0-10V](assets/kuantisasi_3bit_0_10v.png)

#### 🔍 Pemodelan Derau Kuantisasi & Derivasi Formal Rasio SQNR:

Asumsikan galat kuantisasi $e_q[n] = x_q[n] - x[n]$ berdistribusi seragam kontinu pada interval $[-\Delta/2, +\Delta/2]$ dengan fungsi densitas probabilitas $f_E(e) = 1/\Delta$. Nilai rata-rata dan daya derau (variansi $\sigma_e^2$) dihitung sebagai:
$$\mu_e = \mathbb{E}[e] = 0, \qquad P_e = \sigma_e^2 = \mathbb{E}[e^2] = \int_{-\Delta/2}^{+\Delta/2} e^2 \cdot \frac{1}{\Delta} de = \left[ \frac{e^3}{3\Delta} \right]_{-\Delta/2}^{+\Delta/2} = \frac{\Delta^2}{12}$$

Untuk sinyal input sinusoidal penuh yang mengisi seluruh rentang dinamis ADC $V_{\text{pp}} = 2^B \Delta$, amplitudonya $A = \frac{2^B \Delta}{2} = 2^{B-1}\Delta$. Daya rata-rata sinyal adalah:
$$P_s = \frac{A^2}{2} = \frac{(2^{B-1}\Delta)^2}{2} = \frac{2^{2B-2}\Delta^2}{2} = \frac{2^{2B}\Delta^2}{8}$$

Rasio Daya Sinyal terhadap Derau Kuantisasi (*Signal-to-Quantization-Noise Ratio* / SQNR) dalam skala desibel (dB):
$$\text{SQNR} = 10 \log_{10}\left( \frac{P_s}{P_e} \right) = 10 \log_{10}\left( \frac{\frac{2^{2B}\Delta^2}{8}}{\frac{\Delta^2}{12}} \right) = 10 \log_{10}\left( \frac{12}{8} \cdot 2^{2B} \right) = 10 \log_{10}(1.5) + 20 B \log_{10}(2)$$

$$\mathbf{\text{SQNR} \approx 6.02 \cdot B + 1.76 \quad [\text{dB}]}$$

*Aturan Praktis (Rule of Thumb):* Setiap penambahan $1\text{ bit}$ resolusi ADC meningkatkan kualitas sinyal sebesar $\approx 6.02\text{ dB}$ (mereduksi daya derau kuantisasi hingga $1/4$ atau $\approx 75\%$).

#### Tabel Pemetaan Partisi & Nilai Tengah Kuantisasi 3-Bit ($0 - 10\text{ V}, \Delta = 1.25\text{ V}$):

| Step Kuantisasi | Rentang Partisi Masukan ($V_{\text{in}}$) | Kode Biner | Level Representasi ($V_q$) | Error Maks ($\pm \Delta/2$) |
| :---: | :---: | :---: | :---: | :---: |
| **Step 1** | $0.00\text{ V} \leq V_{\text{in}} < 1.25\text{ V}$ | `000` | $0.625\text{ V}$ | $\pm 0.625\text{ V}$ |
| **Step 2** | $1.25\text{ V} \leq V_{\text{in}} < 2.50\text{ V}$ | `001` | $1.875\text{ V}$ | $\pm 0.625\text{ V}$ |
| **Step 3** | $2.50\text{ V} \leq V_{\text{in}} < 3.75\text{ V}$ | `010` | $3.125\text{ V}$ | $\pm 0.625\text{ V}$ |
| **Step 4** | $3.75\text{ V} \leq V_{\text{in}} < 5.00\text{ V}$ | `011` | $4.375\text{ V}$ | $\pm 0.625\text{ V}$ |
| **Step 5** | $5.00\text{ V} \leq V_{\text{in}} < 6.25\text{ V}$ | `100` | $5.625\text{ V}$ | $\pm 0.625\text{ V}$ |
| **Step 6** | $6.25\text{ V} \leq V_{\text{in}} < 7.50\text{ V}$ | `101` | $6.875\text{ V}$ | $\pm 0.625\text{ V}$ |
| **Step 7** | $7.50\text{ V} \leq V_{\text{in}} < 8.75\text{ V}$ | `110` | $8.125\text{ V}$ | $\pm 0.625\text{ V}$ |
| **Step 8** | $8.75\text{ V} \leq V_{\text{in}} \leq 10.00\text{ V}$| `111` | $9.375\text{ V}$ | $\pm 0.625\text{ V}$ |

---

### 1.2.4 Studi Kasus End-to-End: Konversi Sinyal Sinus Utuh x(t) ke Aliran Bit Biner

* Sinyal Input: $x(t) = 5.0 + 4.0 \sin(2\pi \cdot 1.0 \cdot t)\text{ Volt}$, disampling dengan laju $F_s = 8\text{ Hz}$ ($T_s = 0.125\text{ s}$) pada sistem ADC 3-bit ($0 - 10\text{ V}, \Delta = 1.25\text{ V}$).

![Studi Kasus Konversi Lengkap](assets/studi_kasus_konversi_lengkap.png)

#### 🔍 Tabel Kalkulasi Numerik Eksak 8 Titik Sampel ($n=0 \dots 7$):

| Indeks $n$ | Waktu $t_n$ | Tegangan Eksak $x(t_n)$ | Step \& Level $V_q$ | Galat $e_q[n]$ | Kode Biner |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $n = 0$ | $0.000\text{ s}$ | $5.000\text{ V}$ | Step 5 ($5.625\text{ V}$) | $+0.625\text{ V}$ | `100` |
| $n = 1$ | $0.125\text{ s}$ | $5 + 4\sin(\pi/4) = 7.828\text{ V}$ | Step 7 ($8.125\text{ V}$) | $+0.297\text{ V}$ | `110` |
| $n = 2$ | $0.250\text{ s}$ | $5 + 4\sin(\pi/2) = 9.000\text{ V}$ | Step 8 ($9.375\text{ V}$) | $+0.375\text{ V}$ | `111` |
| $n = 3$ | $0.375\text{ s}$ | $5 + 4\sin(3\pi/4) = 7.828\text{ V}$ | Step 7 ($8.125\text{ V}$) | $+0.297\text{ V}$ | `110` |
| $n = 4$ | $0.500\text{ s}$ | $5 + 4\sin(\pi) = 5.000\text{ V}$ | Step 5 ($5.625\text{ V}$) | $+0.625\text{ V}$ | `100` |
| $n = 5$ | $0.625\text{ s}$ | $5 + 4\sin(5\pi/4) = 2.172\text{ V}$ | Step 2 ($1.875\text{ V}$) | $-0.297\text{ V}$ | `001` |
| $n = 6$ | $0.750\text{ s}$ | $5 + 4\sin(3\pi/2) = 1.000\text{ V}$ | Step 1 ($0.625\text{ V}$) | $-0.375\text{ V}$ | `000` |
| $n = 7$ | $0.875\text{ s}$ | $5 + 4\sin(7\pi/4) = 2.172\text{ V}$ | Step 2 ($1.875\text{ V}$) | $-0.297\text{ V}$ | `001` |

**Evaluasi Rata-rata Galat Kuadrat (Mean Squared Error / MSE):**
$$\text{MSE} = \frac{1}{8}\sum_{n=0}^7 (e_q[n])^2 = \frac{2(0.625)^2 + 4(0.297)^2 + 2(0.375)^2}{8} \approx \mathbf{0.1769\ \text{V}^2}$$

$$\mathbf{\text{Aliran Bit Output (Bitstream)}} = \mathbf{\underbrace{100}_{n=0} \ \underbrace{110}_{n=1} \ \underbrace{111}_{n=2} \ \underbrace{110}_{n=3} \ \underbrace{100}_{n=4} \ \underbrace{001}_{n=5} \ \underbrace{000}_{n=6} \ \underbrace{001}_{n=7}} \quad (24\text{ bit per siklus})$$

---

## 1.3 Klasifikasi Lanjutan Sinyal Modern

### 1.3.1 Sinyal Multikanal (Multi-Channel Signals) & Representasi Vektor-Matriks

![Konsep Sinyal Multikanal](assets/sinyal_multikanal.png)

#### 🔍 Formulasi Aljabar Linear Sinyal Multikanal:

* **Vektor Kolom Cuplikan Spasial pada Detak Waktu $n$:**
  $$\mathbf{x}[n] = \begin{bmatrix} x_1[n] \\ x_2[n] \\ \vdots \\ x_M[n] \end{bmatrix} \in \mathbb{R}^{M \times 1}, \quad \text{untuk } n = 0, 1, \dots, N-1$$

* **Matriks Spasio-Temporal $\mathbf{X}_{M \times N}$:**
  $$\mathbf{X} = \begin{bmatrix} \mathbf{x}[0] & \mathbf{x}[1] & \cdots & \mathbf{x}[N-1] \end{bmatrix} = \begin{bmatrix} 
  x_1[0] & x_1[1] & \cdots & x_1[N-1] \\
  x_2[0] & x_2[1] & \cdots & x_2[N-1] \\
  \vdots & \vdots & \ddots & \vdots \\
  x_M[0] & x_M[1] & \cdots & x_M[N-1]
  \end{bmatrix} \in \mathbb{R}^{M \times N}$$

* **Matriks Korelasi Spasial ($\mathbf{R}_{xx}$) & Pemisahan Sumber Sinyal:**  
  Struktur kovariansi antar-sensor dihitung melalui:
  $$\mathbf{R}_{xx} = \frac{1}{N} \mathbf{X} \mathbf{X}^T \in \mathbb{R}^{M \times M}$$
  Melalui Dekomposisi Nilai Singular (SVD) $\mathbf{X} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$, vektor basis ortogonal $\mathbf{U}$ memisahkan sumber interferensi artefak gerak dari sinyal biomedis murni (*Principal Component Analysis* / PCA).

---

### 1.3.2 Sinyal Multi-Dimensi (Multi-Dimensional Signals / M-D): 1D, 2D, 3D, hingga 4D

![Spektrum Sinyal Multi-Dimensi](assets/sinyal_multidimensi.png)

#### 🔍 Klasifikasi Matematis & Ruang Domain Sinyal M-D:

1. **Sinyal 1-Dimensi ($s: \mathbb{R} \to \mathbb{R}$):** Fungsi bergantung pada variabel tunggal (waktu $t$). Contoh: rekaman ucapan fonetik $s = f(t)$.
2. **Sinyal 2-Dimensi ($I: \mathbb{R}^2 \to \mathbb{R}$):** Fungsi intensitas luminansi terdefinisi pada koordinat kartesius bidang spasial $(x,y)$. Transformasi Fourier 2-D sinyal kontinu dinyatakan:
   $$F(u, v) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} I(x, y) e^{-j 2\pi (ux + vy)} dx dy$$
3. **Sinyal 3-Dimensi ($V: \mathbb{R}^3 \to \mathbb{R}$):** Memiliki 3 variabel bebas, seperti koordinat spasial-temporal video monokrom $V = f(x, y, t)$ atau volume tomografi 3-D medan magnetik MRI $V = f(x, y, z)$.
4. **Sinyal 4-Dimensi ($C: \mathbb{R}^4 \to \mathbb{R}$):** Menggabungkan ruang $(x,y)$, waktu $(t)$, dan dimensi spektral panjang gelombang fotometrik $(\lambda)$ pada citra satelit hyperspectral atau video RGB berwarna bioskop $C(x, y, t, \lambda_c)$ di mana $\lambda_c \in \{\text{Red}, \text{Green}, \text{Blue}\}$.

---

### 1.3.3 Sinyal Waktu Diskrit (Discrete-Time Signals / DTS) & Sinyal Elementer

![Fondasi Sinyal Waktu Diskrit](assets/sinyal_waktu_diskrit.png)

#### 🔍 Dekomposisi Sinyal & Sifat Tiga Sinyal Elementer:

1. **Sinyal Impuls Satuan / Kronecker Delta ($\delta[n]$):**
   $$\delta[n] = \begin{cases} 1, & n = 0 \\ 0, & n \neq 0 \end{cases}$$
   *Sifat Penyaringan (Sifting Property):* Sembarang sinyal diskrit $x[n]$ dapat didekomposisi menjadi kombinasi linier tak terhingga dari impuls-impuls tergeser dan terbobot:
   $$\mathbf{x[n] = \sum_{k=-\infty}^{\infty} x[k] \delta[n - k]}$$

2. **Sinyal Undak Satuan (Unit Step $u[n]$):**
   $$u[n] = \begin{cases} 1, & n \ge 0 \\ 0, & n < 0 \end{cases} \equiv \sum_{k=-\infty}^n \delta[k]$$
   Hubungan diferensial diskrit (selisih maju): $\delta[n] = u[n] - u[n-1]$.

3. **Sinyal Eksponensial Diskrit Riil & Kompleks ($x[n] = a^n u[n]$):**  
   Untuk $a \in \mathbb{R}$: jika $|a| < 1$ kurva meluruh asimtotik (Panel 3 kurva ungu $0.7^n$); jika $a < 0$ tanda nilai berosilasi bolak-balik $\operatorname{sgn}(x[n]) = (-1)^n$. Jika $a = e^{\sigma_0 + j\omega_0} \in \mathbb{C}$, sinyal menghasilkan osilasi sinusoidal teredam/tumbuh $x[n] = e^{\sigma_0 n} \cos(\omega_0 n) u[n]$.

---

## 1.4 Klasifikasi Ruang Nilai & Kepastian Sinyal

### 1.4.1 Definisi Hakiki Sinyal Digital: Diskrit Waktu & Diskrit Amplitudo (4 Ruang Sinyal)

> **🎯 Definisi Baku Sinyal Digital dalam Ruang Metrik Diskrit:**
> **Sinyal Digital** adalah sinyal yang berada dalam himpunan pemetaan metrik diskrit ganda:
> $$x_d: \mathbb{Z} \to \mathbb{D}_L, \quad \text{di mana } \mathbb{D}_L = \{V_1, V_2, \dots, V_L\} \subset \mathbb{R}, \quad L = 2^B < \infty$$
> yang berarti sinyal telah mengalami diskritisasi variabel waktu independen ($n \in \mathbb{Z}$) dan sekaligus diskritisasi himpunan nilai dependen ($x_q[n]$) ke dalam kuantisasi berhingga.

![Klasifikasi 4 Ruang Sinyal](assets/sinyal_digital_4_kuadran.png)

#### 🔍 Dekomposisi 4 Kuadran Ruang Keadaan Sinyal:

1. **Kuadran 1 (Waktu Kontinu, Nilai Kontinu — Sinyal Analog Asli):** $x(t) \in \mathbb{R}, \forall t \in \mathbb{R}$. Contoh: tegangan langsung pada elektroda sensor bio-potensial EKG.
2. **Kuadran 2 (Waktu Diskrit, Nilai Kontinu — Sinyal Sampled-Data):** $x[n] \in \mathbb{R}, \forall n \in \mathbb{Z}$. Tegangan tersimpan pada kapasitor rangkaian *Sample-and-Hold* sebelum masuk ke komparator ADC.
3. **Kuadran 3 (Waktu Kontinu, Nilai Diskrit — Sinyal Terkuantisasi Analog):** $x_q(t) \in \mathbb{D}_L, \forall t \in \mathbb{R}$. Contoh: keluaran sistem transmisi pulsa modulasi *Pulse-Code* analog terkuantisasi sebelum clocking.
4. **Kuadran 4 (Waktu Diskrit, Nilai Diskrit — SINYAL DIGITAL MURNI):** $x_q[n] \in \mathbb{D}_L, \forall n \in \mathbb{Z}$. Inilah satu-satunya format sinyal yang dapat dimanipulasi oleh memori RAM, register biner, dan arsitektur aritmatika ALU prosesor digital!

---

### 1.4.2 Sinyal Deterministik vs Sinyal Acak (Random / Stokastik)

![Sinyal Deterministik vs Sinyal Acak](assets/sinyal_deterministik_vs_acak.png)

#### 🔍 Analisis Stokastik: Fungsi Korelasi & Teorema Wiener-Khinchin:

* **Sinyal Deterministik (Panel 1 — Biru Muda):**  
  Sinyal yang setiap nilai masa lalunya, saat ini, dan masa depannya dapat ditentukan **secara pasti 100% tanpa ambiguitas** melalui hubungan analitik eksplisit, misalnya kombinasi deret Fourier:
  $$x(t) = 2.5 \sin(6\pi t) + 1.2 \cos(12\pi t)$$
  Nilai $x(0.5\text{ s}) = 2.5 \sin(3\pi) + 1.2 \cos(6\pi) = 0 + 1.2(1) = 1.200\text{ V}$ dapat dihitung secara analitis presisi.

* **Sinyal Acak / Stokastik (Panel 2 — Merah):**  
  Sinyal yang masa depannya tidak dapat diprediksi secara eksak dan hanya dapat dimodelkan sebagai proses acak (*stochastic process*) $X(t, \zeta)$ melalui parameter statistik ensemble:
  1. **Nilai Ekspektasi / Mean ($\mu_x(t)$):** $\mu_x(t) = \mathbb{E}[X(t)] = \int_{-\infty}^{\infty} x f_X(x; t) dx$.
  2. **Fungsi Autokorelasi ($R_{xx}(t_1, t_2)$):** $R_{xx}(t_1, t_2) = \mathbb{E}[X(t_1) X^*(t_2)]$.
  3. **Stasioneritas Lebar (Wide-Sense Stationary / WSS):** Jika $\mu_x(t) = \mu_x$ (konstan) dan $R_{xx}(t_1, t_2) = R_{xx}(\tau)$ di mana $\tau = t_1 - t_2$.

  **Teorema Wiener-Khinchin:** Kerapatan spektral daya (*Power Spectral Density* / PSD) dari sinyal acak WSS adalah Transformasi Fourier dari fungsi autokorelasinya:
  $$S_{xx}(F) = \mathcal{F}\left\{ R_{xx}(\tau) \right\} = \int_{-\infty}^{\infty} R_{xx}(\tau) e^{-j 2\pi F \tau} d\tau$$
  Untuk derau putih murni (*Additive White Gaussian Noise* / AWGN), autokorelasinya berupa impuls $R_{ww}(\tau) = \sigma^2 \delta(\tau)$, menghasilkan spektrum frekuensi yang datar rata di semua frekuensi: $S_{ww}(F) = \sigma^2\ [\text{W/Hz}]$.

---

## 1.5 Analisis Frekuensi & Gelombang Sinusoidal (Kontinu vs Diskrit)

### 1.5.1 Perbandingan Domain Frekuensi: Sinyal Waktu Kontinu vs Sinyal Waktu Diskrit

Pemetaan frekuensi dari domain kontinu ($F,\Omega$) ke domain diskrit ($f,\omega$) terjadi melalui hubungan parameter interval sampling $T_s = 1/F_s$:
$$\omega = \Omega T_s = \frac{\Omega}{F_s} = \frac{2\pi F}{F_s} = 2\pi f \quad [\text{rad/sampel}], \qquad f = \frac{F}{F_s} \quad [\text{siklus/sampel}]$$

![Perbandingan Domain Frekuensi](assets/frekuensi_kontinu_vs_diskrit.png)

#### 🔍 Tabel Perbandingan Komprehensif Domain Frekuensi:

| Karakteristik Parameter | Domain Waktu-Kontinu (Analog) | Domain Waktu-Diskrit (Digital) |
| :--- | :--- | :--- |
| **Frekuensi Siklik** | $F$ ($\text{Hertz} = \text{siklus/detik}$) | $f = F / F_s$ ($\text{siklus/sampel}$) |
| **Frekuensi Sudut** | $\Omega = 2\pi F$ ($\text{rad/detik}$) | $\omega = \Omega T_s = 2\pi f$ ($\text{rad/sampel}$) |
| **Rentang Nilai Unik** | $-\infty < \Omega < +\infty$ (Tak terbatas) | $\mathbf{-\pi \leq \omega \leq +\pi}$ atau $\mathbf{-\frac{1}{2} \leq f \leq +\frac{1}{2}}$ |
| **Periodisitas Spektrum** | Bersifat Aperiodik pada sumbu $\Omega$ | **Periodik mutlak dengan periode $2\pi$** ($\omega \equiv \omega + 2\pi k$) |
| **Laju Osilasi Tertinggi** | $\Omega \to \infty$ (Meningkat tanpa batas) | **Tercapai tepat di $\omega = \pm \pi$ ($f = \pm 1/2$)** |
| **Representasi Transformasi** | Fourier: $X(j\Omega) = \int x(t)e^{-j\Omega t}dt$ | DTFT: $X(e^{j\omega}) = \sum x[n] e^{-j\omega n}$ |

---

### 1.5.2 Sinyal Sinusoidal Waktu-Kontinu (1/2): Sifat Keunikan Frekuensi Fisik & Laju Tak Terbatas

Persamaan gelombang sinusoidal waktu-kontinu: $x_a(t) = A \cos(\Omega t + \theta) = A \cos(2\pi F t + \theta)$.

![Sinus Kontinu Karakteristik 1](assets/sinus_kontinu_karakteristik_1.png)

#### 🔍 Pembuktian Keunikan & Laju Tak Terbatas:

1. **Keunikan Frekuensi Fisik (Ortogonalitas Continuous Basis):**  
   Dua sinyal sinusoidal kontinu dengan frekuensi berbeda $F_1 \neq F_2$ selalu independen secara ortogonal pada interval pengamatan kelipatan persekutuan $T_0$:
   $$\frac{1}{T_0}\int_0^{T_0} \cos(2\pi F_1 t) \cos(2\pi F_2 t) dt = \frac{1}{2} \delta_{F_1, F_2}$$
   Tidak ada dua frekuensi kontinu berbeda yang dapat menghasilkan profil fisik gelombang yang sama.

2. **Laju Osilasi Bertambah Monotonik Menuju Tak Hingga:**  
   Turunan pertama sinyal terhadap waktu merepresentasikan laju perubahan tegangan:
   $$\left| \frac{d x_a(t)}{dt} \right|_{\max} = | -A \cdot 2\pi F \sin(2\pi F t + \theta) |_{\max} = 2\pi A F$$
   Ketika $F \to \infty$, laju kemiringan tegangan $\frac{dx_a}{dt} \to \infty$ bertambah tanpa ada batas maksimum.

---

### 1.5.3 Sinyal Sinusoidal Waktu-Kontinu (2/2): Periodisitas Universal untuk Setiap Frekuensi F

![Sinus Kontinu Periodisitas 2](assets/sinus_kontinu_periodisitas_2.png)

#### 🔍 Pembuktian Matematis Periodisitas Universal Sinyal Kontinu:

Suatu sinyal $x_a(t)$ dikatakan periodik jika terdapat konstanta waktu $T_p > 0$ sedemikian rupa sehingga $x_a(t + T_p) = x_a(t), \forall t \in \mathbb{R}$. Untuk sembarang frekuensi $F > 0$:
$$x_a(t + T_p) = A \cos\left(2\pi F \left(t + \frac{1}{F}\right) + \theta\right) = A \cos(2\pi F t + 2\pi + \theta) = A \cos(2\pi F t + \theta) = x_a(t)$$

Karena kesamaan ini berlaku identik untuk semua $F \in \mathbb{R}^+$, maka **semua sinyal sinusoidal kontinu di alam semesta dijamin 100% selalu periodik**.

---

### 1.5.4 Sinyal Sinusoidal Waktu-Diskrit (1/3): Syarat Wajib Periodisitas Bilangan Rasional f = k/N

Persamaan umum sinusoidal diskrit: $x[n] = A \cos(\omega n + \theta) = A \cos(2\pi f n + \theta)$.

> **⚠️ Fakta Krusial: Sinyal Sinus Diskrit TIDAK SELALU Periodik!**
> Agar sinyal diskrit $x[n]$ periodik dengan periode fundamental integer $N \in \mathbb{Z}^+$ ($x[n + N] = x[n]$), maka frekuensi sikliknya $f$ wajib berupa **Bilangan Rasional**:
> $$\cos(2\pi f (n + N) + \theta) = \cos(2\pi f n + 2\pi f N + \theta) \equiv \cos(2\pi f n + 2\pi k + \theta)$$
> $$\implies 2\pi f N = 2\pi k \implies \mathbf{f = \frac{k}{N} \in \mathbb{Q}, \quad k, N \in \mathbb{Z}^+}$$
> Periode fundamental integer terkecil sampel $N$ dihitung melalui:
> $$N = \frac{k}{f} = \frac{2\pi k}{\omega}, \quad \text{di mana } k \text{ adalah integer terkecil pembuat } N \in \mathbb{Z}^+$$

![Sinus Diskrit Periodisitas 1](assets/sinus_diskrit_periodisitas_1.png)

#### 🔍 Pembuktian Analitik Panel A vs Panel B:

* **Panel A ($x_1[n] = \cos(\frac{\pi}{4} n)$):** $\omega = \frac{\pi}{4} \implies f = \frac{\omega}{2\pi} = \frac{\pi/4}{2\pi} = \frac{1}{8}$. Karena $\frac{1}{8} \in \mathbb{Q}$ (bilangan rasional), sinyal **Periodik** dengan periode $N = \frac{1}{1/8} = 8\text{ sampel}$. Pola sampel berulang identik setiap 8 ketukan.
* **Panel B ($x_2[n] = \cos(1 \cdot n)$):** $\omega = 1\text{ rad/sampel} \implies f = \frac{1}{2\pi}$. Karena $\pi$ adalah bilangan transendental irasional, maka $f \notin \mathbb{Q}$. Tidak ada bilangan bulat $N$ dan $k$ yang memenuhi $N = 2\pi k$. Akibatnya, sinyal $x_2[n]$ **100% Aperiodik / Non-Periodik**; titik-titik sampelnya tidak akan pernah berulang sama persis di sepanjang garis waktu sampai kapan pun!

---

### 1.5.5 Sinyal Sinusoidal Waktu-Diskrit (2/3): Fenomena Frekuensi Identik Kelipatan 2π

![Sinus Diskrit Identik 2pi](assets/sinus_diskrit_identik_2pi_2.png)

#### 🔍 Teorema Kesamaan Frekuensi Diskrit Modulo $2\pi$:

Untuk sembarang bilangan bulat $k \in \mathbb{Z}$:
$$\cos((\omega + 2\pi k)n + \theta) = \cos(\omega n + 2\pi k n + \theta) = \cos(\omega n + \theta + 2\pi(kn)) = \cos(\omega n + \theta)$$

*Konsekuensi Fundamental DSP:* Frekuensi diskrit yang terpisah sejauh kelipatan integer $2\pi$ bukan sekadar menghasilkan gelombang mirip, melainkan **benar-benar identik pada seluruh titik sampel $n$**. Oleh sebab itu, seluruh rentang analisis frekuensi digital dunia hanya dibatasi pada **Interval Fundamental**:
$$-\pi \leq \omega \leq +\pi \quad \iff \quad -\frac{1}{2} \leq f \leq +\frac{1}{2}$$

---

### 1.5.6 Sinyal Sinusoidal Waktu-Diskrit (3/3): Laju Osilasi Tertinggi pada ω = π (f = 1/2)

![Sinus Diskrit Osilasi Maksimum](assets/sinus_diskrit_osilasi_maksimum_3.png)

#### 🔍 Dekomposisi Laju Osilasi Sinyal Diskrit pada 4 Titik Spektrum:

1. **Titik 1 — Frekuensi Nol / DC ($\omega = 0, f = 0$):**  
   $x[n] = \cos(0 \cdot n) = +1.0, \forall n$. Sinyal berupa garis horizontal konstan tanpa perubahan dinamis.

2. **Titik 2 — Frekuensi Menengah ($\omega = \pi/4, f = 1/8$):**  
   Sinyal berosilasi harmonik mulus dengan periode fundamental $N = 8$ sampel per siklus gelombang.

3. **Titik 3 — LAJU OSILASI TERTINGGI MAKSIMUM DI DUNIA DIGITAL ($\omega = \pi, f = 1/2$):**  
   $$x[n] = \cos(\pi n) = (-1)^n = \{+1, -1, +1, -1, +1, -1, \dots\}$$
   Perhatikan titik-titik sampel merah: Sinyal melompat ekstrem dari nilai puncak tertinggi $+1$ ke lembah terendah $-1$ **di setiap 1 perpindahan sampel ($n \to n+1$)**. Ini adalah laju fluktuasi tercepat yang secara matematis dan fisis mungkin terjadi pada sistem waktu-diskrit.

4. **Titik 4 — Frekuensi Tinggi Melampaui $\pi$ ($\omega = 7\pi/4 \equiv -\pi/4$):**  
   Ketika frekuensi sudut dinaikkan melampaui $\pi$ menuju $2\pi$, laju osilasi **JUSTRU MELAMBAT KEMBALI**:
   $$\cos\left(\frac{7\pi}{4} n\right) = \cos\left(\left(2\pi - \frac{\pi}{4}\right)n\right) = \cos\left(-\frac{\pi}{4} n\right) = \cos\left(\frac{\pi}{4} n\right)$$
   Gelombang ini persis identik dengan sinyal frekuensi rendah $\omega = \pi/4$. Fenomena ini membuktikan bahwa batas kecepatan osilasi digital mutlak terkunci di $\omega = \pi$.

---

## 1.6 Studi Kasus & Contoh Perhitungan Komprehensif Terpadu (Sintesis Subbab 1.1 - 1.5)

### 🏥 Grand Problem: Desain Sistem Telemetri Biomedis Multikanal Cerdas (*Bio-DSP System*)

Sebuah sistem instrumentasi biomedis dirancang untuk memonitor sinyal bio-elektrik jantung pasien. Sistem ini mengintegrasikan rantai fisik sensorik, struktur data multikanal, penapisan filter LTI, digitalisasi ADC kuantisasi resolusi tinggi, serta analisis harmonisa frekuensi diskrit.

#### 1. Spesifikasi Sistem:
1. **Rantai Fisik & Sensorik (Subbab 1.1):** Tiga elektroda sensor bio-potensial $Ag/AgCl$ ($M = 3$ kanal) merekam sinyal elektrofisiologis kontinu pasien yang terkontaminasi oleh interferensi derau jala-jala listrik $50\text{ Hz}$ dan osilasi pernapasan respirasi lambat $0.2\text{ Hz}$:
   $$x_1(t) = 3.0 \cos(2\pi \cdot 10 t) + 1.2 \cos(2\pi \cdot 50 t) + 0.8 \sin(2\pi \cdot 0.2 t) \quad [\text{V}]$$
   $$x_2(t) = 2.5 \cos(2\pi \cdot 10 t - \pi/6) + 1.2 \cos(2\pi \cdot 50 t) + 0.4 \sin(2\pi \cdot 0.2 t) \quad [\text{V}]$$
   $$x_3(t) = 1.8 \cos(2\pi \cdot 10 t + \pi/4) + 1.2 \cos(2\pi \cdot 50 t) - 0.5 \sin(2\pi \cdot 0.2 t) \quad [\text{V}]$$

2. **Struktur Data Multikanal (Subbab 1.3):** Sinyal multikanal diorganisasikan ke dalam matriks spasio-temporal $\mathbf{X}(t) \in \mathbb{R}^{3 \times N}$. Dilakukan operasi pembobotan spasial diferensial untuk membatalkan komponen *common-mode noise* $50\text{ Hz}$ dengan vektor bobot $\mathbf{w} = [1, -1, 0]^T$:
   $$s_a(t) = \mathbf{w}^T \mathbf{x}(t) = x_1(t) - x_2(t)$$

3. **Spesifikasi ADC & Digitalisasi (Subbab 1.2 & 1.4):**
   - Frekuensi Sampling Sistem: $F_s = 200\text{ Hz}$ ($T_s = 5\text{ ms} = 0.005\text{ s}$).
   - Terdapat komponen derau interferensi frekuensi tinggi liar tak terfilter pada $f_{\text{noise}} = 230\text{ Hz}$ dengan persamaan $v_{\text{noise}}(t) = 0.5 \cos(2\pi \cdot 230 t)$.
   - Konverter ADC Uniform 4-Bit ($B = 4\text{ bit} \implies L = 16\text{ level}$), dengan rentang tegangan dinamis $V_{\text{min}} = -4.0\text{ V}$ hingga $V_{\text{maks}} = +4.0\text{ V}$ ($V_{\text{range}} = 8.0\text{ V}$).

4. **Filter Digital Pemroses LTI (Subbab 1.1 & 1.3):** Sinyal tercuplik $s[n]$ dilewatkan ke sebuah filter rata-rata bergerak 3-titik (*3-Point Moving Average Filter*):
   $$y[n] = \frac{1}{3}s[n] + \frac{1}{3}s[n-1] + \frac{1}{3}s[n-2]$$

---

#### 2. Penyelesaian Komputasi Analitis Langkah-demi-Langkah:

##### 🔹 Langkah 1: Reduksi Multikanal & Analisis Parameter Gelombang (Subbab 1.1 & 1.3)
Hitung sinyal hasil kombinasi spasial $s_a(t) = x_1(t) - x_2(t)$:
$$s_a(t) = \left[ 3.0 \cos(20\pi t) + 1.2 \cos(100\pi t) + 0.8 \sin(0.4\pi t) \right] - \left[ 2.5 \cos(20\pi t - \pi/6) + 1.2 \cos(100\pi t) + 0.4 \sin(0.4\pi t) \right]$$
$$= \underbrace{\left[ 3.0 \cos(20\pi t) - 2.5 \cos(20\pi t - \pi/6) \right]}_{\text{Komponen Jantung 10 Hz}} + \underbrace{[1.2 - 1.2]\cos(100\pi t)}_{\mathbf{0\text{ (Derau 50 Hz Lenyap!)}}} + \underbrace{0.4 \sin(0.4\pi t)}_{\text{Respirasi 0.2 Hz}}$$

Gunakan identitas trigonometri fasor untuk menyederhanakan komponen $10\text{ Hz}$:
$$2.5 \cos(20\pi t - \pi/6) = 2.5 \left[ \frac{\sqrt{3}}{2} \cos(20\pi t) + \frac{1}{2} \sin(20\pi t) \right] \approx 2.165 \cos(20\pi t) + 1.250 \sin(20\pi t)$$
$$s_{10\text{Hz}}(t) = (3.0 - 2.165)\cos(20\pi t) - 1.250 \sin(20\pi t) = 0.835 \cos(20\pi t) - 1.250 \sin(20\pi t)$$

Amplitudo resultan $A_R$ dan sudut fase $\phi_R$:
$$A_R = \sqrt{(0.835)^2 + (-1.250)^2} = \sqrt{0.6972 + 1.5625} = \sqrt{2.2597} \approx \mathbf{1.503\text{ Volt}}$$
$$\phi_R = \operatorname{atan2}(-1.250, 0.835) \approx -56.27^\circ \approx -0.982\text{ rad}$$

Persamaan analitis bersih sinyal kontinu yang masuk ke ADC (termasuk derau liar $230\text{ Hz}$):
$$s_{\text{total}}(t) = 1.503 \cos(2\pi \cdot 10 t - 0.982) + 0.4 \sin(2\pi \cdot 0.2 t) + 0.5 \cos(2\pi \cdot 230 t)$$

---

##### 🔹 Langkah 2: Evaluasi Nyquist, Identifikasi Aliasing, dan Pemetaan Frekuensi Diskrit (Subbab 1.2 & 1.5)
1. **Frekuensi Nyquist:** $f_{\text{fold}} = \frac{F_s}{2} = \frac{200\text{ Hz}}{2} = \mathbf{100\text{ Hz}}$.
2. **Evaluasi Komponen $F_1 = 10\text{ Hz}$ dan $F_2 = 0.2\text{ Hz}$:**  
   Karena $F_1, F_2 < 100\text{ Hz}$, disampling aman bebas aliasing:
   $$\omega_1 = \frac{2\pi \cdot 10}{200} = \mathbf{\frac{\pi}{10}\ \text{rad/sampel}}, \qquad f_1 = \frac{10}{200} = \mathbf{\frac{1}{20}\ \text{siklus/sampel}}$$
   $$\omega_2 = \frac{2\pi \cdot 0.2}{200} = \mathbf{\frac{\pi}{500}\ \text{rad/sampel}}, \qquad f_2 = \frac{0.2}{200} = \mathbf{\frac{1}{1000}\ \text{siklus/sampel}}$$
3. **Evaluasi Aliasing Komponen Liar $F_3 = 230\text{ Hz}$:**  
   Karena $F_3 = 230\text{ Hz} > 100\text{ Hz}$, terjadi aliasing ke frekuensi semu:
   $$f_{\text{alias}} = |230\text{ Hz} - 200\text{ Hz}| = \mathbf{30\text{ Hz}} \implies \omega_{\text{alias}} = \frac{2\pi \cdot 30}{200} = \mathbf{\frac{3\pi}{10}\ \text{rad/sampel}}$$
4. **Uji Periodisitas Diskrit (Subbab 1.5.4):**
   - $f_1 = 1/20 \in \mathbb{Q} \implies$ **Periodik** dengan periode fundamental $N_1 = 20\text{ sampel}$.
   - $f_2 = 1/1000 \in \mathbb{Q} \implies$ **Periodik** dengan periode fundamental $N_2 = 1000\text{ sampel}$.
   - $f_{\text{alias}} = 3/20 \in \mathbb{Q} \implies$ **Periodik** dengan periode fundamental $N_3 = \frac{20}{\gcd(3,20)} = 20\text{ sampel}$.
   - **Periode Fundamental Total:** $N_{\text{total}} = \operatorname{KPK}(20, 1000, 20) = \mathbf{1000\text{ sampel}}$ ($5.0\text{ detik}$).

---

##### 🔹 Langkah 3: Perhitungan Kuantisasi ADC 4-Bit \& Kinerja Derau SQNR (Subbab 1.2 & 1.4)
1. **Lebar Step Kuantisasi ADC 4-Bit:**
   $$\Delta = \frac{+4.0\text{ V} - (-4.0\text{ V})}{16} = \frac{8.0\text{ V}}{16} = \mathbf{0.50\text{ Volt / step}}$$
2. **Daya Derau Kuantisasi Teoritis:**
   $$P_e = \sigma_e^2 = \frac{\Delta^2}{12} = \frac{(0.50)^2}{12} = \mathbf{0.020833\ \text{V}^2}$$
3. **SQNR Maksimum Teoritis (Skala Penuh $A = 4.0\text{ V}$):**
   $$\text{SQNR}_{\text{teoritis}} = 6.02(4) + 1.76 = \mathbf{25.84\text{ dB}}$$

**Pelacakan 4 Sampel Pertama ($n=0, 1, 2, 3$):**
- **Sampel $n=0$ ($t = 0.000\text{ s}$):**  
  $s[0] = 1.503(0.5552) + 0 + 0.5(1) = \mathbf{+1.3345\text{ V}} \implies$ **Step 11** (`1010`), $V_q = \mathbf{+1.250\text{ V}}$, $e_q[0] = \mathbf{-0.0845\text{ V}}$.
- **Sampel $n=1$ ($t = 0.005\text{ s}$):**  
  $s[1] = 1.503(0.7856) + 0.0025 + 0.2939 = \mathbf{+1.4772\text{ V}} \implies$ **Step 11** (`1010`), $V_q = \mathbf{+1.250\text{ V}}$, $e_q[1] = \mathbf{-0.2272\text{ V}}$.
- **Sampel $n=2$ ($t = 0.010\text{ s}$):**  
  $s[2] = 1.503(0.9377) + 0.0050 - 0.1545 = \mathbf{+1.2599\text{ V}} \implies$ **Step 11** (`1010`), $V_q = \mathbf{+1.250\text{ V}}$, $e_q[2] = \mathbf{-0.0099\text{ V}}$.
- **Sampel $n=3$ ($t = 0.015\text{ s}$):**  
  $s[3] = 1.503(0.9992) + 0.0075 - 0.4755 = \mathbf{+1.0338\text{ V}} \implies$ **Step 11** (`1010`), $V_q = \mathbf{+1.250\text{ V}}$, $e_q[3] = \mathbf{+0.2162\text{ V}}$.

$$\mathbf{\text{Frame Bitstream Serial [4 Sampel]}} = \mathbf{\underbrace{1010}_{n=0} \ \underbrace{1010}_{n=1} \ \underbrace{1010}_{n=2} \ \underbrace{1010}_{n=3}} \quad (16\text{ bit})$$

---

##### 🔹 Langkah 4: Pemrosesan Filter LTI \& Uji Karakteristik Sistem (Subbab 1.1 & 1.3)
Sinyal terkuantisasi $s_q[n]$ diproses oleh filter rata-rata bergerak 3-titik:
$$y[n] = \frac{1}{3} s_q[n] + \frac{1}{3} s_q[n-1] + \frac{1}{3} s_q[n-2]$$

1. **Uji 4 Karakteristik Sistem Filter:**
   - **Linearitas:** $\mathcal{T}\{a x_1 + b x_2\} = a y_1 + b y_2 \implies$ **Terbukti Linier!**
   - **Time-Invariance:** $\mathcal{T}\{s_q[n-n_0]\} = y[n-n_0] \implies$ **Terbukti Time-Invariant!**
   - **Kausalitas:** $h[n] = \frac{1}{3}\delta[n] + \frac{1}{3}\delta[n-1] + \frac{1}{3}\delta[n-2] = 0$ untuk seluruh $n < 0 \implies$ **Terbukti Kausal!**
   - **Stabilitas BIBO:** $S_h = \sum |h[n]| = 1/3 + 1/3 + 1/3 = \mathbf{1.0 < \infty} \implies$ **Terbukti Stabil BIBO!**

2. **Respon Frekuensi Filter terhadap Sinyal Jantung vs Derau Alias 30 Hz:**
   $$H(e^{j\omega}) = \frac{1}{3} e^{-j\omega} (1 + 2\cos\omega)$$
   - Pada sinyal jantung $\omega_1 = \frac{\pi}{10} = 18^\circ$: $|H(e^{j\pi/10})| = \frac{1}{3}|1 + 2(0.9511)| \approx \mathbf{0.9674\ (-0.29\text{ dB})} \implies$ **Lolos Utuh!**
   - Pada derau liar alias $\omega_{\text{alias}} = \frac{3\pi}{10} = 54^\circ$: $|H(e^{j3\pi/10})| = \frac{1}{3}|1 + 2(0.5878)| \approx \mathbf{0.7252\ (-2.79\text{ dB})} \implies$ **Tereduksi!**

3. **Keluaran Filter $y[2]$:**
   $$y[2] = \frac{1}{3}(1.250) + \frac{1}{3}(1.250) + \frac{1}{3}(1.250) = \mathbf{1.250\text{ Volt}}$$

---

## 1.7 Glosarium Ringkas Istilah Kunci Persinyalan

### 🏷️ 1. Konsep Dasar & Paradigma
| Istilah | Definisi & Konsep Kunci |
| :--- | :--- |
| **Sinyal (*Signal*)** | Besaran fisik pembawa informasi yang nilainya berubah sebagai fungsi dari satu atau lebih variabel bebas (tegangan, tekanan akustik, suhu). |
| **Sistem (*System*)** | Entitas fisik atau algoritma komputasi yang memetakan sinyal masukan (*excitation*) menjadi sinyal keluaran (*response*). |
| **ASP (*Analog Signal Processing*)** | Pemrosesan sinyal kontinu langsung menggunakan komponen perangkat keras fisik ($R, L, C, \text{Op-Amp}$) diatur oleh persamaan diferensial LCCDE. |
| **DSP (*Digital Signal Processing*)** | Pemrosesan sinyal diskrit numerik menggunakan algoritma aljabar pada prosesor digital diatur oleh persamaan beda LCCDDE. |
| **Sensor / Transduser** | Perangkat konversi energi yang mengubah fenomena fisis non-listrik menjadi fluktuasi sinyal tegangan/arus listrik proporsional. |

### 🏷️ 2. Anatomi & Parameter Gelombang
| Istilah | Definisi & Konsep Kunci |
| :--- | :--- |
| **Amplitudo ($A$)** | Simpangan puncak ekstrem gelombang dari titik nol, menentukan daya rata-rata $P = A^2/2$ dan tegangan efektif $V_{\text{rms}} = A/\sqrt{2}$. |
| **Frekuensi ($f, F$)** | Jumlah osilasi siklus gelombang lengkap dalam 1 detik ($\text{Hertz} = \text{s}^{-1}$). |
| **Periode ($T$)** | Interval waktu minimum yang diperlukan untuk menyelesaikan 1 siklus osilasi periodik penuh ($T = 1/f$). |
| **Frekuensi Sudut ($\Omega, \omega$)** | Laju kecepatan rotasi fase gelombang ($\Omega = 2\pi F\text{ rad/s}$ untuk kontinu; $\omega = 2\pi f\text{ rad/sampel}$ untuk diskrit). |
| **Fase Awal ($\phi, \theta$)** | Posisi sudut mula gelombang pada $t = 0$, setara dengan pergeseran translasi waktu $\Delta t = -\phi/\Omega$. |

### 🏷️ 3. Proses Digitalisasi & ADC
| Istilah | Definisi & Konsep Kunci |
| :--- | :--- |
| **ADC (*A/D Converter*)** | Subsistem pengubah sinyal kontinu analog menjadi kata-kata biner digital melalui rantai sampling, kuantisasi, dan encoding. |
| **Pencuplikan (*Sampling*)** | Proses modulasi sinyal kontinu dengan deretan pulsa Dirac pada interval waktu berkala $T_s = 1/F_s$. |
| **Teorema Nyquist** | Syarat batas absolut bebas aliasing: frekuensi sampling wajib memenuhi $F_s \ge 2 f_{\max}$. |
| **Aliasing** | Distorsi lipatan spektral di mana frekuensi di atas $F_s/2$ menyamar menjadi frekuensi rendah palsu $f_{\text{alias}} = |F - k F_s|$. |
| **Kuantisasi (*Quantization*)** | Pembulatan non-linier amplitudo kontinu ke $L = 2^B$ level diskrit terdekat dengan lebar step $\Delta = V_{\text{range}}/2^B$. |
| **SQNR** | Rasio Daya Sinyal terhadap Derau Kuantisasi berdaya $\sigma_e^2 = \Delta^2/12$, bernilai $\text{SQNR} \approx 6.02 B + 1.76\text{ dB}$. |

### 🏷️ 4. Klasifikasi Sinyal & Karakteristik Sistem
| Istilah | Definisi & Konsep Kunci |
| :--- | :--- |
| **Sinyal Digital Murni** | Sinyal pada Kuadran-4 yang berada dalam domain waktu-diskrit ($n \in \mathbb{Z}$) dan bernilai amplitudo diskrit biner ($x_q \in \mathbb{D}_L$). |
| **Sinyal Multikanal** | Matriks data spasio-temporal $\mathbf{X} \in \mathbb{R}^{M \times N}$ yang dihimpun dari array $M$ sensor serentak. |
| **Sinyal Multi-Dimensi** | Sinyal yang dipetakan oleh $M$ variabel bebas independen (1D audio, 2D citra, 3D video/MRI, 4D hyperspectral). |
| **Deterministik vs Stokastik** | Sinyal terprediksi 100\% via formula matematis eksak vs sinyal acak berderau yang dimodelkan via autokorelasi $R_{xx}(\tau)$ dan PSD. |
| **Linearitas** | Kepatuhan sistem terhadap prinsip superposisi: $\mathcal{T}\{\alpha x_1 + \beta x_2\} = \alpha y_1 + \beta y_2$. |
| **Time-Invariance** | Kekekalan sifat sistem terhadap pergeseran waktu: $\mathcal{T}\{x[n-n_0]\} = y[n-n_0]$. |
| **Kausalitas** | Sistem yang responnya tidak mendahului input ($h[n] = 0, \forall n < 0$). |
| **Stabilitas BIBO** | Jaminan keluaran terbatas untuk masukan terbatas, dicapai jika dan hanya jika $\sum |h[n]| < \infty$. |

---
*Dokumen ini disusun sebagai Modul Pembelajaran Visual Komprehensif Pengolahan Sinyal Digital (PSD) berstandar industri dan akademis.*
