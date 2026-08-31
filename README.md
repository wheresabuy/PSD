# 📘 BUKU AJAR VISUAL KOMPREHENSIF PENGOLAHAN SINYAL DIGITAL (PSD)
*Panduan Analitis & Visual Tingkat Lanjut Dilengkapi Asal-Usul & Penurunan Matematis Rumus (A-to-Z): Dari Fisika Sensor \& Transduksi, Formulasi Rantai ASP vs DSP, Konversi Digitalisasi ADC, Teori Kuantisasi \& Kinerja SQNR, Aljabar Sinyal Multikanal-Multidimensi, hingga Analisis Frekuensi Diskrit Tingkat Lanjut*

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

---

#### 🔬 [Penurunan Matematis A-to-Z] Asal-Usul Pemodelan Fungsi Transduksi Sensor via Deret Taylor
Bagaimana persamaan kurva respon sensor $v(t) = \mathcal{S} \cdot P(t) + \beta \cdot P^2(t) + \eta(t)$ terbentuk?
1. **Fondasi Dasar:** Hubungan antara besaran fisik masukan $P$ dan tegangan keluaran $v$ secara umum diatur oleh fungsi respon sembarang yang kontinu $v = f(P)$.
2. **Ekspansi Deret Taylor di Sekitar Titik Operasi Nominal $P_0$:**
   $$f(P) = f(P_0) + \left.\frac{df}{dP}\right|_{P_0}(P - P_0) + \frac{1}{2!}\left.\frac{d^2f}{dP^2}\right|_{P_0}(P - P_0)^2 + \frac{1}{3!}\left.\frac{d^3f}{dP^3}\right|_{P_0}(P - P_0)^3 + \dots$$
3. **Pemisahan Komponen Orde:**
   * $f(P_0) = V_0$ adalah tegangan offset DC (dikalibrasi ke nol pada sistem seimbang).
   * Koefisien linearitas $\mathcal{S} = \left.\frac{df}{dP}\right|_{P_0}$ didefinisikan sebagai **Sensitivitas Nominal Sensor** (Volt/Satuan Fisis).
   * Koefisien kuadratik $\beta = \frac{1}{2}\left.\frac{d^2f}{dP^2}\right|_{P_0}$ merepresentasikan **Deviasi Non-Linearitas Orde-2**.
4. **Asal-Usul Derau Termal Aditif ($\eta(t)$):** Elektron bebas di dalam atom konduktor bergetar secara acak akibat energi kinetik termal $k_B T$. Berdasarkan **Teorema Fluktuasi-Disipasi Nyquist (1928)**, kerapatan daya derau tegangan pada resistor $R$ diturunkan dari mekanika statistik Boltzmann:
   $$\mathbf{\overline{v_n^2} = 4 k_B T R \Delta f \quad [\text{Volt}^2]}$$
   di mana $k_B = 1.380649 \times 10^{-23}\text{ J/K}$ (konstanta Boltzmann), $T$ temperatur mutlak Kelvin, $R$ resistansi Thévenin sensor, dan $\Delta f$ bandwidth frekuensi pengukuran.

---

![Fenomena Fisik Menjadi Sinyal Listrik](assets/fenomena_fisik_ke_sinyal.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Asal-Usul Fisika Tiga Kelas Sinyal:

1. **Panel 1: Gelombang Suara (Persamaan Helmholtz 1-D):**
   * *Hukum II Newton untuk elemen fluida udara:* Gaya tekan diferensial sebanding dengan percepatan massa udara: $-\frac{\partial p}{\partial x} = \rho_0 \frac{\partial u}{\partial t}$ ($p$ tekanan akustik, $u$ kecepatan partikel, $\rho_0$ densitas udara).
   * *Hukum Konservasi Massa Fluida (Kontinuitas):* Laju kompresi volume sebanding dengan laju perubahan tekanan: $-\frac{\partial u}{\partial x} = \frac{1}{B}\frac{\partial p}{\partial t}$ ($B$ bulk modulus elastisitas udara).
   * *Eliminasi Kecepatan Partikel $u$:* Turunkan persamaan pertama terhadap $x$ ($\frac{\partial^2 p}{\partial x^2} = -\rho_0 \frac{\partial^2 u}{\partial x \partial t}$) dan persamaan kedua terhadap $t$ ($\frac{\partial^2 u}{\partial t \partial x} = -\frac{1}{B}\frac{\partial^2 p}{\partial t^2}$), lalu substitusikan suku turunan parsial silang:
     $$\mathbf{\frac{\partial^2 p(x,t)}{\partial x^2} - \frac{1}{c_s^2}\frac{\partial^2 p(x,t)}{\partial t^2} = 0 \quad \text{di mana laju rambat suara } c_s = \sqrt{\frac{B}{\rho_0}} \approx 343\text{ m/s}}}$$

2. **Panel 2: Respon Termal Orde-1 Sensor Suhu:**
   * *Hukum I Termodinamika (Kekekalan Energi):* Kalor yang diserap oleh massa sensor $m$ sama dengan perpindahan panas konveksi Newton:
     $$m c_p \frac{dT(t)}{dt} = h A \left( T_{\text{lingkungan}} - T(t) \right)$$
   * Definisikan konstanta waktu termal $\tau_{\text{th}} = \frac{m c_p}{h A} = R_{\text{th}} C_{\text{th}}$. Persamaan diferensial menjadi:
     $$\tau_{\text{th}}\frac{dT(t)}{dt} + T(t) = T_{\text{akhir}}$$
   * Menggunakan metode faktor integrasi $e^{t/\tau_{\text{th}}}$ dengan syarat awal $T(0) = T_{\text{awal}}$, solusi eksak adalah kurva eksponensial:
     $$\mathbf{T(t) = T_{\text{akhir}} + (T_{\text{awal}} - T_{\text{akhir}})e^{-t/\tau_{\text{th}}} + w_{\text{thermal}}(t)}$$

3. **Panel 3: Osilasi Seismometer Teredam Kerak Bumi:**
   * *Hukum II Newton pada sistem massa-pegas-peredam inersia:*
     $$m \ddot{x}(t) + c \dot{x}(t) + k x(t) = -m \ddot{x}_g(t)$$
   * Bagi dengan massa $m$, substitusikan $\omega_n = \sqrt{k/m}$ (frekuensi natural) dan rasio redaman $\zeta = \frac{c}{2\sqrt{km}}$:
     $$\ddot{x}(t) + 2\zeta\omega_n \dot{x}(t) + \omega_n^2 x(t) = -\ddot{x}_g(t)$$
   * Untuk kondisi teredam kurang (*underdamped* $\zeta < 1$), akar persamaan karakteristik kuadrat adalah bilangan kompleks $s_{1,2} = -\zeta\omega_n \pm j\omega_n\sqrt{1-\zeta^2}$, menghasilkan respon transien sinusoidal teredam:
     $$\mathbf{a(t) = A_0 e^{-\zeta \omega_n (t - t_0)} \sin\left(\omega_n \sqrt{1 - \zeta^2}(t - t_0)\right) u(t - t_0)}$$

---

### 1.1.2 Paradigma Pemrosesan: Rantai ASP (Analog) vs Rantai DSP (Digital)

![Diagram Paradigma ASP vs DSP](assets/diagram_asp_vs_dsp.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Asal-Usul Persamaan Diferensial ASP vs Persamaan Beda DSP:

* **Asal-Usul Rantai ASP (Hukum Sirkuit Kirchhoff KCL/KVL):**  
  Pada rangkaian analog RLC, hubungan arus-tegangan komponen adalah $v_R = iR$, $v_L = L\frac{di}{dt}$, dan $i_C = C\frac{dv_C}{dt}$. Menggabungkan persamaan sirkuit menghasilkan Persamaan Diferensial Linier Koefisien Konstan (LCCDE):
  $$\sum_{k=0}^N a_k \frac{d^k y(t)}{dt^k} = \sum_{m=0}^M b_m \frac{d^m x(t)}{dt^m} \quad \xrightarrow{\mathcal{L}} \quad H(s) = \frac{Y(s)}{X(s)} = \frac{\sum_{m=0}^M b_m s^m}{\sum_{k=0}^N a_k s^k}$$
  *Kelemahan Fisis ASP:* Sangat sensitif terhadap toleransi nilai fisik komponen $\frac{\Delta H}{H} \approx \sum S_{p_i}^H \frac{\Delta p_i}{p_i}$, drift suhu lingkungan $\Delta R(T) = R_0(1 + \alpha \Delta T)$, dan penuaan kapasitor.

* **Asal-Usul Rantai DSP (Aproksimasi Selisih Beda Diskrit):**  
  Pada domain diskrit dengan periode sampling $T_s$, turunan waktu pertama didekati oleh selisih mundur (*backward difference*): $\frac{dy(t)}{dt} \approx \frac{y[n] - y[n-1]}{T_s}$. Menggantikan seluruh turunan kontinu menghasilkan Persamaan Beda Linier Koefisien Konstan (LCCDDE):
  $$\sum_{k=0}^N a_k y[n-k] = \sum_{m=0}^M b_m x[n-m] \quad \xrightarrow{\mathcal{Z}} \quad H(z) = \frac{Y(z)}{X(z)} = \frac{\sum_{m=0}^M b_m z^{-m}}{\sum_{k=0}^N a_k z^{-k}}$$
  *Keunggulan DSP:* Presisi mutlak $100\%$, respons filter dapat diubah secara instan melalui perangkat lunak (*software programmable*), dan memungkinkan realisasi filter FIR linier fase murni.

---

### 1.1.3 Tiga Pilar Anatomi Gelombang: Amplitudo, Frekuensi, dan Fase

Persamaan analitis gelombang sinusoidal dinyatakan:
$$x(t) = A \sin(2\pi f t + \phi) = A \sin(\Omega t + \phi)$$

![Anatomi Parameter Sinyal](assets/anatomi_sinyal.png)

![Komparasi Visual Parameter Sinyal](assets/komparasi_sinyal.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Penurunan Nilai RMS, Daya Sinyal, dan Pergeseran Waktu:

1. **Penurunan Daya Rata-rata $P_{\text{avg}} = A^2/2$ & Tegangan Efektif $V_{\text{rms}} = A/\sqrt{2}$:**
   * Energi disipasi pada beban resistor $1\ \Omega$ selama satu periode $T$ adalah integral kuadrat tegangan sesaat:
     $$P_{\text{avg}} = \frac{1}{T}\int_0^T x^2(t) dt = \frac{1}{T}\int_0^T A^2 \sin^2(\Omega t + \phi) dt$$
   * Gunakan identitas trigonometri sudut ganda $\sin^2\theta = \frac{1 - \cos(2\theta)}{2}$:
     $$P_{\text{avg}} = \frac{A^2}{2T} \left[ \int_0^T 1\ dt - \int_0^T \cos(2\Omega t + 2\phi) dt \right]$$
   * Karena integral dari fungsi kosinus periodik selama satu periode penuh adalah nol ($\int_0^T \cos(2\Omega t + 2\phi) dt = 0$), persamaan menyusut menjadi:
     $$\mathbf{P_{\text{avg}} = \frac{A^2}{2T} [T - 0] = \frac{A^2}{2} \implies V_{\text{rms}} = \sqrt{P_{\text{avg}}} = \frac{A}{\sqrt{2}} \approx 0.7071 A}$$

2. **Penurunan Hubungan Fase ($\phi$) terhadap Pergeseran Waktu ($\Delta t$):**
   * Faktorkan kecepatan sudut $\Omega$ dari dalam argumen sinus:
     $$x(t) = A \sin(\Omega t + \phi) = A \sin\left( \Omega \left( t + \frac{\phi}{\Omega} \right) \right) = A \sin(\Omega(t - \Delta t))$$
   * Dengan menyamakan kedua bentuk persamaan:
     $$\mathbf{\Delta t = -\frac{\phi}{\Omega} = -\frac{\phi}{2\pi f}}$$
     Jika $\phi = +\pi/2$ ($+90^\circ$), gelombang bergeser ke kiri sebesar $\Delta t = -T/4$, mengubah fungsi sinus menjadi kosinus $A\cos(\Omega t)$ (fase kuadratur).

---

### 1.1.4 Sistem Pengolah Sinyal & 4 Klasifikasi Karakteristik Operasinya

![Klasifikasi Sistem](assets/klasifikasi_sistem.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Penurunan \& Uji Karakteristik Sistem:

1. **Uji Prinsip Superposisi Linearitas:**
   * Sistem linier wajib mematuhi $\mathcal{T}\{\alpha x_1 + \beta x_2\} = \alpha \mathcal{T}\{x_1\} + \beta \mathcal{T}\{x_2\}$.
   * *Mengapa sistem kubik $y[n] = 0.5 x^3[n]$ non-linier?* Masukkan $x[n] = \alpha x_1[n]$:
     $$y[n] = 0.5 (\alpha x_1[n])^3 = \alpha^3 (0.5 x_1^3[n]) = \alpha^3 y_1[n] \neq \alpha y_1[n]$$
     Munculnya faktor pangkat $\alpha^3$ merusak prinsip homogenitas. Jika diberi masukan $\cos(\omega_0 n)$, ekspansi kubik $\cos^3\theta = \frac{3\cos\theta + \cos(3\theta)}{4}$ memunculkan komponen frekuensi baru $3\omega_0$ (distorsi harmonisa non-linier).

2. **Penurunan Syarat Keterjumlahan Mutlak Stabilitas BIBO:**
   * Misalkan masukan dibatasi terhingga $|x[n]| \le M_x < \infty$. Output sistem LTI diatur oleh konvolusi $y[n] = \sum_{k=-\infty}^\infty h[k] x[n-k]$.
   * Ambil nilai mutlak $|y[n]|$ dan terapkan pertidaksamaan segitiga (*triangle inequality*):
     $$|y[n]| = \left| \sum_{k=-\infty}^{\infty} h[k] x[n-k] \right| \le \sum_{k=-\infty}^{\infty} |h[k] x[n-k]| = \sum_{k=-\infty}^{\infty} |h[k]| \cdot |x[n-k]|$$
   * Karena $|x[n-k]| \le M_x$, keluarkan konstanta $M_x$:
     $$|y[n]| \le M_x \sum_{k=-\infty}^{\infty} |h[k]|$$
   * Agar $|y[n]| \le M_y < \infty$ untuk sembarang nilai $M_x < \infty$, syarat perlu dan cukup mutlak adalah deret respon impuls harus konvergen:
     $$\mathbf{S_h = \sum_{k=-\infty}^{\infty} |h[k]| < \infty \quad (\text{Absolutely Summable})}$$

---

## 1.2 Proses Digitalisasi Sinyal (Analog-to-Digital Converter / ADC)

### 1.2.1 Rantai 4 Tahap Lengkap Digitalisasi ADC

![Tahapan Lengkap ADC](assets/tahapan_adc_sampling_kuantisasi.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Asal-Usul Modulasi Kereta Impuls Dirac:
Bagaimana spektrum frekuensi $X_s(F) = F_s \sum X_a(F - k F_s)$ terbentuk saat sinyal dicuplik?
1. **Model Kereta Impuls Dirac (*Dirac Comb*):** $p(t) = \sum_{n=-\infty}^\infty \delta(t - n T_s)$.
2. **Perkalian Domain Waktu:** Sinyal tercuplik adalah $x_s(t) = x_a(t) \cdot p(t) = \sum_{n=-\infty}^\infty x_a(n T_s) \delta(t - n T_s)$.
3. **Ekspansi Deret Fourier Kompleks dari Kereta Dirac:** Karena $p(t)$ periodik dengan periode $T_s$, koefisien Fourier $c_k$ dihitung:
   $$c_k = \frac{1}{T_s}\int_{-T_s/2}^{T_s/2} \delta(t) e^{-j 2\pi k F_s t} dt = \frac{1}{T_s} = F_s \implies p(t) = F_s \sum_{k=-\infty}^{\infty} e^{j 2\pi k F_s t}$$
4. **Transformasi Fourier dari Sinyal Tercuplik:**
   $$X_s(F) = \mathcal{F}\left\{ x_a(t) \cdot F_s \sum_{k=-\infty}^\infty e^{j 2\pi k F_s t} \right\} = F_s \sum_{k=-\infty}^\infty \mathcal{F}\left\{ x_a(t) e^{j 2\pi k F_s t} \right\}$$
   Menggunakan teorema translasi modulasi frekuensi $\mathcal{F}\{x_a(t) e^{j 2\pi F_0 t}\} = X_a(F - F_0)$:
   $$\mathbf{X_s(F) = F_s \sum_{k=-\infty}^{\infty} X_a(F - k F_s)}$$

---

### 1.2.2 Pencuplikan (Sampling Clock), Teorema Nyquist, dan Bencana Aliasing

![Sampling Nyquist dan Aliasing](assets/sampling_nyquist_aliasing.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Penurunan Rumus Lipatan Aliasing \& Rekonstruksi Whittaker-Shannon:

1. **Asal-Usul Rumus Frekuensi Alias $f_{\text{alias}} = |F - k F_s|$:**
   * Spektrum $X_s(F)$ memuat pergeseran spektrum $X_a(F - k F_s)$.
   * Filter rekonstruksi hanya membuka jendela frekuensi pada pita dasar $|F| \le F_s/2$.
   * Jika komponen frekuensi asli $F > F_s/2$, salinan spektrum pada indeks $k$ masuk ke jendela pita dasar. Karena spektrum sinyal riil bersifat simetri genap $|X(F)| = |X(-F)|$, frekuensi positif semu yang teramati adalah jarak mutlak terdekat ke kelipatan sampling:
     $$\mathbf{f_{\text{alias}} = |F - k F_s|, \quad \text{di mana } k = \operatorname{round}(F / F_s)}$$

2. **Penurunan Rumus Rekonstruksi Sinc Whittaker-Shannon:**
   * Untuk memulihkan $X_a(F)$ dari $X_s(F)$, kalikan $X_s(F)$ dengan filter lolos-rendah ideal $H_r(F) = T_s \cdot \operatorname{rect}\left(\frac{F}{F_s}\right)$ yang bernilai $T_s$ pada $|F| \le F_s/2$ dan $0$ di luar itu.
   * Transformasi Fourier balik dari fungsi kotak $H_r(F)$ adalah fungsi sinus kardinal:
     $$h_r(t) = \int_{-F_s/2}^{F_s/2} T_s e^{j 2\pi F t} dF = T_s \left[ \frac{e^{j 2\pi F t}}{j 2\pi t} \right]_{-F_s/2}^{F_s/2} = T_s \frac{\sin(\pi F_s t)}{\pi t} = \operatorname{sinc}\left(\frac{t}{T_s}\right)$$
   * Di domain waktu, perkalian spektral menjadi konvolusi deretan impuls:
     $$\mathbf{x_a(t) = x_s(t) * h_r(t) = \sum_{n=-\infty}^{\infty} x[n] \operatorname{sinc}\left(\frac{t - n T_s}{T_s}\right)}$$

---

### 1.2.3 Kuantisasi & Pengkodean Biner 3-Bit (Rentang 0 s.d. 10 Volt)

![Karakteristik Kuantisasi 3-Bit 0-10V](assets/kuantisasi_3bit_0_10v.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Penurunan Eksak Daya Derau Kuantisasi $\sigma_e^2 = \Delta^2/12$ dan Formula SQNR:

1. **Penurunan Integral Variansi Galat Derau Kuantisasi:**
   * Galat kuantisasi $e = x_q - x$ berdistribusi acak seragam kontinu pada interval $[-\Delta/2, +\Delta/2]$ dengan fungsi densitas probabilitas konstan $f_E(e) = \frac{1}{\Delta}$.
   * Daya derau kuantisasi adalah nilai ekspektasi kuadrat galat:
     $$P_e = \sigma_e^2 = \mathbb{E}[e^2] = \int_{-\Delta/2}^{+\Delta/2} e^2 f_E(e) de = \int_{-\Delta/2}^{+\Delta/2} e^2 \frac{1}{\Delta} de = \frac{1}{\Delta} \left[ \frac{e^3}{3} \right]_{-\Delta/2}^{+\Delta/2}$$
     $$= \frac{1}{\Delta} \left[ \frac{(\Delta/2)^3}{3} - \frac{(-\Delta/2)^3}{3} \right] = \frac{1}{\Delta} \left[ \frac{\Delta^3/8}{3} + \frac{\Delta^3/8}{3} \right] = \frac{1}{\Delta} \left[ \frac{2\Delta^3}{24} \right] = \mathbf{\frac{\Delta^2}{12}}$$

2. **Penurunan Rumus Baku SQNR $\approx 6.02 B + 1.76\text{ dB}$:**
   * Rentang skala penuh ADC adalah $V_{\text{range}} = 2^B \Delta$.
   * Sinyal sinus penuh memiliki tegangan $V_{\text{pp}} = 2^B \Delta \implies A = 2^{B-1}\Delta$.
   * Daya rata-rata sinyal adalah $P_s = \frac{A^2}{2} = \frac{(2^{B-1}\Delta)^2}{2} = \frac{2^{2B-2}\Delta^2}{2} = \frac{2^{2B}\Delta^2}{8}$.
   * Rasio daya sinyal terhadap derau (SQNR linier):
     $$\frac{P_s}{P_e} = \frac{\frac{2^{2B}\Delta^2}{8}}{\frac{\Delta^2}{12}} = \frac{12}{8} \cdot 2^{2B} = 1.5 \cdot 2^{2B}$$
   * Konversi ke skala logaritmik Desibel (dB):
     $$\text{SQNR}_{\text{dB}} = 10 \log_{10}(1.5 \cdot 2^{2B}) = 10 \log_{10}(1.5) + 20 B \log_{10}(2) = 1.7609 + 20 B (0.30103)$$
     $$\mathbf{\text{SQNR} \approx 6.02 \cdot B + 1.76 \quad [\text{dB}]}$$

---

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

---

#### 🔬 [Penurunan Matematis A-to-Z] Asal-Usul Matriks Kovariansi Spasial Multikanal:
Bagaimana persamaan matriks kovariansi spasial $\mathbf{R}_{xx} = \frac{1}{N} \mathbf{X} \mathbf{X}^T$ diturunkan dari konsep statistik dasar?
1. **Definisi Statistik Kovariansi Antar-Dua Sensor:** Kovariansi spasial antara kanal ke-$i$ ($x_i[n]$) dan kanal ke-$j$ ($x_j[n]$) dengan rata-rata nol adalah:
   $$R_{ij} = \frac{1}{N}\sum_{n=0}^{N-1} x_i[n] x_j[n]$$
2. **Bentuk Perkalian Titik Vektor Baris:** Ambil baris ke-$i$ matriks $\mathbf{X}$, yaitu $\mathbf{x}_i^T = [x_i[0], x_i[1], \dots, x_i[N-1]]$, dan baris ke-$j$, yaitu $\mathbf{x}_j^T$. Perkalian titik $\mathbf{x}_i^T \mathbf{x}_j$ adalah $\sum_{n=0}^{N-1} x_i[n] x_j[n]$.
3. **Sintesis Seluruh Matriks:** Dalam aljabar linier, menghitung perkalian titik untuk seluruh pasangan $i,j \in \{1, \dots, M\}$ setara secara eksak dengan mengalikan matriks data $\mathbf{X} \in \mathbb{R}^{M \times N}$ dengan transposisinya $\mathbf{X}^T \in \mathbb{R}^{N \times M}$:
   $$\mathbf{R}_{xx} = \frac{1}{N} \mathbf{X} \mathbf{X}^T \in \mathbb{R}^{M \times M}$$

---

### 1.3.2 Sinyal Multi-Dimensi (Multi-Dimensional Signals / M-D): 1D, 2D, 3D, hingga 4D

![Spektrum Sinyal Multi-Dimensi](assets/sinyal_multidimensi.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Asal-Usul Transformasi Fourier 2-Dimensi Citra:
1. **Ekstensi Basis Kompleks 1-D ke 2-D:** Gelombang planar 2-D yang merambat dengan frekuensi spasial horizontal $u$ dan vertikal $v$ dinyatakan oleh perkalian dua basis ortogonal:
   $$\phi_{u,v}(x,y) = e^{j 2\pi u x} \cdot e^{j 2\pi v y} = e^{j 2\pi (ux + vy)}$$
2. **Proyeksi Sinyal Citra $I(x,y)$ ke Basis Planar:**
   $$\mathbf{F(u, v) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} I(x, y) e^{-j 2\pi (ux + vy)} dx dy}$$
   Komponen $(u,v)$ mengekstrak orientasi sudut kontur, tekstur, dan gradien intensitas cahaya pada bidang 2-D.

---

### 1.3.3 Sinyal Waktu Diskrit (Discrete-Time Signals / DTS) & Sinyal Elementer

![Fondasi Sinyal Waktu Diskrit](assets/sinyal_waktu_diskrit.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Pembuktian Sifat Penyaringan (*Sifting Property*) Sinyal Diskrit:
Mengapa sembarang sinyal diskrit $x[n]$ selalu dapat dituliskan sebagai $x[n] = \sum_{k=-\infty}^\infty x[k]\delta[n-k]$?
1. Berdasarkan definisi impuls Kronecker:
   $$\delta[n - k] = \begin{cases} 1, & \text{saat } k = n \\ 0, & \text{saat } k \neq n \end{cases}$$
2. Evaluasi suku-suku deret penjumlahan:
   $$\sum_{k=-\infty}^{\infty} x[k]\delta[n-k] = \dots + x[n-1]\underbrace{\delta[1]}_{0} + x[n]\underbrace{\delta[0]}_{1} + x[n+1]\underbrace{\delta[-1]}_{0} + \dots = x[n] \cdot 1 = \mathbf{x[n]}$$
   Setiap sampel $x[k]$ dipandang sebagai impuls berskala yang "ditembakkan" pada posisi indeks waktu $k$. Inilah dasar lahirnya konsep **Konvolusi Linier**!

---

## 1.4 Klasifikasi Ruang Nilai & Kepastian Sinyal

### 1.4.1 Definisi Hakiki Sinyal Digital: Diskrit Waktu & Diskrit Amplitudo (4 Ruang Sinyal)

> **🎯 Definisi Baku Sinyal Digital dalam Ruang Metrik Diskrit:**
> **Sinyal Digital** adalah sinyal yang berada dalam himpunan pemetaan metrik diskrit ganda:
> $$x_d: \mathbb{Z} \to \mathbb{D}_L, \quad \text{di mana } \mathbb{D}_L = \{V_1, V_2, \dots, V_L\} \subset \mathbb{R}, \quad L = 2^B < \infty$$

![Klasifikasi 4 Ruang Sinyal](assets/sinyal_digital_4_kuadran.png)

---

### 1.4.2 Sinyal Deterministik vs Sinyal Acak (Random / Stokastik)

![Sinyal Deterministik vs Sinyal Acak](assets/sinyal_deterministik_vs_acak.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Penurunan Teorema Wiener-Khinchin (Dari Autokorelasi ke Kerapatan Spektral Daya PSD):
Mengapa Transformasi Fourier dari Autokorelasi $R_{xx}[k]$ menghasilkan Kerapatan Daya Spektral $S_{xx}(\omega)$?
1. **Definisi Transformasi Fourier Sampel Berhingga $N$:** $X_N(\omega) = \sum_{n=0}^{N-1} x[n] e^{-j\omega n}$.
2. **Perhitungan Daya Spektral Rata-rata:**
   $$S_{xx}(\omega) = \lim_{N \to \infty} \frac{1}{N} \mathbb{E}\left[ |X_N(\omega)|^2 \right] = \lim_{N \to \infty} \frac{1}{N} \mathbb{E}\left[ \left( \sum_{n=0}^{N-1} x[n] e^{-j\omega n} \right) \left( \sum_{m=0}^{N-1} x[m] e^{j\omega m} \right) \right]$$
3. **Gabungkan Penjumlahan Ganda:**
   $$S_{xx}(\omega) = \lim_{N \to \infty} \frac{1}{N} \sum_{n=0}^{N-1} \sum_{m=0}^{N-1} \mathbb{E}[x[n]x[m]] e^{-j\omega(n-m)}$$
4. **Substitusi Variabel Selisih Waktu $k = n - m$:** Untuk proses stasioner lebar (WSS), $\mathbb{E}[x[n]x[m]] = R_{xx}[n-m] = R_{xx}[k]$. Penjumlahan ganda menyusut menjadi Transformasi Fourier Diskrit:
   $$\mathbf{S_{xx}(\omega) = \sum_{k=-\infty}^{\infty} R_{xx}[k] e^{-j\omega k}}$$

---

## 1.5 Analisis Frekuensi & Gelombang Sinusoidal (Kontinu vs Diskrit)

### 1.5.1 Perbandingan Domain Frekuensi: Sinyal Waktu Kontinu vs Sinyal Waktu Diskrit

![Perbandingan Domain Frekuensi](assets/frekuensi_kontinu_vs_diskrit.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Asal-Usul Periodisitas Spektrum DTFT $X(e^{j(\omega + 2\pi)}) = X(e^{j\omega})$:
Mengapa spektrum frekuensi diskrit dijamin 100% periodik dengan periode $2\pi$?
1. Berdasarkan definisi Transformasi Fourier Waktu Diskrit (DTFT): $X(e^{j\omega}) = \sum_{n=-\infty}^\infty x[n] e^{-j\omega n}$.
2. Evaluasi nilai DTFT pada frekuensi tergeser $\omega + 2\pi k$:
   $$X(e^{j(\omega + 2\pi k)}) = \sum_{n=-\infty}^\infty x[n] e^{-j(\omega + 2\pi k)n} = \sum_{n=-\infty}^\infty x[n] e^{-j\omega n} \cdot e^{-j 2\pi k n}$$
3. Berdasarkan rumus identitas Euler: $e^{-j 2\pi k n} = \cos(2\pi kn) - j \sin(2\pi kn)$. Karena $k \in \mathbb{Z}$ dan $n \in \mathbb{Z}$, hasil kali $kn$ selalu bilangan bulat, sehingga $\cos(2\pi kn) = 1$ dan $\sin(2\pi kn) = 0 \implies e^{-j 2\pi k n} = 1$.
4. Maka:
   $$\mathbf{X(e^{j(\omega + 2\pi k)}) = \sum_{n=-\infty}^\infty x[n] e^{-j\omega n} \cdot 1 = X(e^{j\omega})} \quad \forall k \in \mathbb{Z}$$

---

### 1.5.2 Sinyal Sinusoidal Waktu-Kontinu (1/2): Sifat Keunikan Frekuensi Fisik & Laju Tak Terbatas

![Sinus Kontinu Karakteristik 1](assets/sinus_kontinu_karakteristik_1.png)

---

### 1.5.3 Sinyal Sinusoidal Waktu-Kontinu (2/2): Periodisitas Universal untuk Setiap Frekuensi F

![Sinus Kontinu Periodisitas 2](assets/sinus_kontinu_periodisitas_2.png)

---

### 1.5.4 Sinyal Sinusoidal Waktu-Diskrit (1/3): Syarat Wajib Periodisitas Bilangan Rasional f = k/N

![Sinus Diskrit Periodisitas 1](assets/sinus_diskrit_periodisitas_1.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Penurunan Syarat Mutlak Bilangan Rasional $f = k/N \in \mathbb{Q}$:
Mengapa sinyal sinusoidal diskrit $x[n] = \cos(2\pi f n)$ tidak selalu periodik?
1. **Syarat Definisi Periodik:** Harus ada bilangan bulat positif $N \in \mathbb{Z}^+$ sedemikian rupa sehingga $x[n + N] = x[n]$ untuk semua $n$.
2. Substitusikan ke dalam fungsi cosinus:
   $$\cos(2\pi f (n + N)) = \cos(2\pi f n + 2\pi f N) = \cos(2\pi f n)$$
3. Fungsi cosinus berulang nilainya jika dan hanya jika pergeseran sudutnya merupakan kelipatan bilangan bulat dari satu putaran lingkaran $2\pi k$ ($k \in \mathbb{Z}^+$):
   $$2\pi f N = 2\pi k \implies f N = k \implies \mathbf{f = \frac{k}{N}}$$
4. Karena $k \in \mathbb{Z}^+$ dan $N \in \mathbb{Z}^+$, rasio $k/N$ adalah **Bilangan Rasional ($\mathbb{Q}$)**. Jika frekuensi $f$ memuat bilangan irasional (seperti $\pi$ atau $\sqrt{2}$), persamaan ini mustahil dipenuhi oleh sembarang bilangan bulat $N$, sehingga sinyal dijamin **Aperiodik**.

---

### 1.5.5 Sinyal Sinusoidal Waktu-Diskrit (2/3): Fenomena Frekuensi Identik Kelipatan 2π

![Sinus Diskrit Identik 2pi](assets/sinus_diskrit_identik_2pi_2.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Penurunan Rumus Identitas Modulo $2\pi$ Trigonometri:
Buktikan $\cos((\omega + 2\pi k)n + \theta) = \cos(\omega n + \theta)$:
1. Gunakan rumus trigonometri penjumlahan sudut $\cos(A + B) = \cos A \cos B - \sin A \sin B$, dengan $A = \omega n + \theta$ dan $B = 2\pi k n$:
   $$\cos((\omega n + \theta) + 2\pi k n) = \cos(\omega n + \theta)\cos(2\pi kn) - \sin(\omega n + \theta)\sin(2\pi kn)$$
2. Karena $k \in \mathbb{Z}$ dan $n \in \mathbb{Z}$, maka $kn$ adalah bilangan bulat, menghasilkan $\cos(2\pi kn) = 1$ dan $\sin(2\pi kn) = 0$.
3. Maka terbukti secara mutlak:
   $$\mathbf{\cos((\omega + 2\pi k)n + \theta) = \cos(\omega n + \theta) \cdot 1 - \sin(\omega n + \theta) \cdot 0 = \cos(\omega n + \theta)}$$

---

### 1.5.6 Sinyal Sinusoidal Waktu-Diskrit (3/3): Laju Osilasi Tertinggi pada ω = π (f = 1/2)

![Sinus Diskrit Osilasi Maksimum](assets/sinus_diskrit_osilasi_maksimum_3.png)

---

#### 🔬 [Penurunan Matematis A-to-Z] Penurunan Aljabar Lompatan Ekstrem $(-1)^n$ pada $\omega = \pi$:
1. Substitusikan $\omega = \pi$ ke dalam persamaan Euler:
   $$x[n] = e^{j\pi n} = (e^{j\pi})^n = (\cos\pi + j\sin\pi)^n = (-1 + j0)^n = \mathbf{(-1)^n}$$
2. Untuk deret indeks $n = 0, 1, 2, 3, 4, \dots$:
   $$x[0] = +1, \quad x[1] = -1, \quad x[2] = +1, \quad x[3] = -1, \dots$$
   Sinyal berubah tanda di setiap 1 perpindahan sampel ($\Delta n = 1$). Tidak ada sinyal diskrit lain yang dapat berfluktuasi lebih cepat dari pergantian tanda setiap 1 sampel ini!

---

## 1.6 Studi Kasus & Contoh Perhitungan Komprehensif Terpadu (Sintesis Subbab 1.1 - 1.5)

### 🏥 Grand Problem: Desain Sistem Telemetri Biomedis Multikanal Cerdas (*Bio-DSP System*)

Sebuah sistem instrumentasi biomedis dirancang untuk memonitor sinyal bio-elektrik jantung pasien. Sistem ini mengintegrasikan rantai fisik sensorik, struktur data multikanal, penapisan filter LTI, digitalisasi ADC kuantisasi resolusi tinggi, serta analisis harmonisa frekuensi diskrit.

#### 1. Spesifikasi Sistem:
1. **Rantai Fisik & Sensorik (Subbab 1.1):** Tiga elektroda sensor bio-potensial $Ag/AgCl$ ($M = 3$ kanal) merekam sinyal elektrofisiologis kontinu pasien:
   $$x_1(t) = 3.0 \cos(2\pi \cdot 10 t) + 1.2 \cos(2\pi \cdot 50 t) + 0.8 \sin(2\pi \cdot 0.2 t) \quad [\text{V}]$$
   $$x_2(t) = 2.5 \cos(2\pi \cdot 10 t - \pi/6) + 1.2 \cos(2\pi \cdot 50 t) + 0.4 \sin(2\pi \cdot 0.2 t) \quad [\text{V}]$$
   $$x_3(t) = 1.8 \cos(2\pi \cdot 10 t + \pi/4) + 1.2 \cos(2\pi \cdot 50 t) - 0.5 \sin(2\pi \cdot 0.2 t) \quad [\text{V}]$$

2. **Struktur Data Multikanal (Subbab 1.3):** Pembobotan spasial diferensial untuk membatalkan komponen *common-mode noise* $50\text{ Hz}$ dengan vektor bobot $\mathbf{w} = [1, -1, 0]^T$:
   $$s_a(t) = \mathbf{w}^T \mathbf{x}(t) = x_1(t) - x_2(t)$$

3. **Spesifikasi ADC & Digitalisasi (Subbab 1.2 & 1.4):**
   - Frekuensi Sampling Sistem: $F_s = 200\text{ Hz}$ ($T_s = 5\text{ ms} = 0.005\text{ s}$).
   - Terdapat komponen derau interferensi frekuensi tinggi liar tak terfilter pada $f_{\text{noise}} = 230\text{ Hz}$ dengan persamaan $v_{\text{noise}}(t) = 0.5 \cos(2\pi \cdot 230 t)$.
   - Konverter ADC Uniform 4-Bit ($B = 4\text{ bit} \implies L = 16\text{ level}$), rentang dinamis $V_{\text{min}} = -4.0\text{ V}$ hingga $V_{\text{maks}} = +4.0\text{ V}$ ($V_{\text{range}} = 8.0\text{ V}$).

4. **Filter Digital Pemroses LTI (Subbab 1.1 & 1.3):** Sinyal tercuplik $s[n]$ dilewatkan ke sebuah filter rata-rata bergerak 3-titik (*3-Point Moving Average Filter*):
   $$y[n] = \frac{1}{3}s[n] + \frac{1}{3}s[n-1] + \frac{1}{3}s[n-2]$$

---

#### 2. Penyelesaian Komputasi Analitis Langkah-demi-Langkah:

##### 🔹 Langkah 1: Reduksi Multikanal & Analisis Parameter Gelombang (Subbab 1.1 & 1.3)
Hitung sinyal hasil kombinasi spasial $s_a(t) = x_1(t) - x_2(t)$:
$$s_a(t) = \underbrace{\left[ 3.0 \cos(20\pi t) - 2.5 \cos(20\pi t - \pi/6) \right]}_{\text{Komponen Jantung 10 Hz}} + \underbrace{[1.2 - 1.2]\cos(100\pi t)}_{\mathbf{0\text{ (Derau 50 Hz Lenyap!)}}} + \underbrace{0.4 \sin(0.4\pi t)}_{\text{Respirasi 0.2 Hz}}$$

Gunakan identitas trigonometri fasor untuk menyederhanakan komponen $10\text{ Hz}$:
$$2.5 \cos(20\pi t - \pi/6) = 2.5 \left[ \frac{\sqrt{3}}{2} \cos(20\pi t) + \frac{1}{2} \sin(20\pi t) \right] \approx 2.165 \cos(20\pi t) + 1.250 \sin(20\pi t)$$
$$s_{10\text{Hz}}(t) = (3.0 - 2.165)\cos(20\pi t) - 1.250 \sin(20\pi t) = 0.835 \cos(20\pi t) - 1.250 \sin(20\pi t)$$

Amplitudo resultan $A_R$ dan sudut fase $\phi_R$:
$$A_R = \sqrt{(0.835)^2 + (-1.250)^2} = \sqrt{0.6972 + 1.5625} \approx \mathbf{1.503\text{ Volt}}$$
$$\phi_R = \operatorname{atan2}(-1.250, 0.835) \approx -56.27^\circ \approx -0.982\text{ rad}$$

Persamaan analitis bersih sinyal kontinu yang masuk ke ADC (termasuk derau liar $230\text{ Hz}$):
$$s_{\text{total}}(t) = 1.503 \cos(2\pi \cdot 10 t - 0.982) + 0.4 \sin(2\pi \cdot 0.2 t) + 0.5 \cos(2\pi \cdot 230 t)$$

---

##### 🔹 Langkah 2: Evaluasi Nyquist, Identifikasi Aliasing, dan Pemetaan Frekuensi Diskrit (Subbab 1.2 & 1.5)
1. **Frekuensi Nyquist:** $f_{\text{fold}} = \frac{F_s}{2} = \frac{200\text{ Hz}}{2} = \mathbf{100\text{ Hz}}$.
2. **Evaluasi Komponen $F_1 = 10\text{ Hz}$ dan $F_2 = 0.2\text{ Hz}$:** Bebas aliasing:
   $$\omega_1 = \frac{2\pi \cdot 10}{200} = \mathbf{\frac{\pi}{10}\ \text{rad/sampel}}, \qquad f_1 = \frac{10}{200} = \mathbf{\frac{1}{20}\ \text{siklus/sampel}}$$
   $$\omega_2 = \frac{2\pi \cdot 0.2}{200} = \mathbf{\frac{\pi}{500}\ \text{rad/sampel}}, \qquad f_2 = \frac{0.2}{200} = \mathbf{\frac{1}{1000}\ \text{siklus/sampel}}$$
3. **Evaluasi Aliasing Komponen Liar $F_3 = 230\text{ Hz}$:**  
   Karena $F_3 = 230\text{ Hz} > 100\text{ Hz}$, terjadi aliasing ke frekuensi semu:
   $$f_{\text{alias}} = |230\text{ Hz} - 200\text{ Hz}| = \mathbf{30\text{ Hz}} \implies \omega_{\text{alias}} = \frac{2\pi \cdot 30}{200} = \mathbf{\frac{3\pi}{10}\ \text{rad/sampel}}$$
4. **Uji Periodisitas Diskrit (Subbab 1.5.4):**
   - $f_1 = 1/20 \in \mathbb{Q} \implies$ **Periodik** ($N_1 = 20\text{ sampel}$).
   - $f_2 = 1/1000 \in \mathbb{Q} \implies$ **Periodik** ($N_2 = 1000\text{ sampel}$).
   - $f_{\text{alias}} = 3/20 \in \mathbb{Q} \implies$ **Periodik** ($N_3 = 20\text{ sampel}$).
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
- **Sampel $n=0$ ($t = 0.000\text{ s}$):** $s[0] = \mathbf{+1.3345\text{ V}} \implies$ **Step 11** (`1010`), $V_q = \mathbf{+1.250\text{ V}}$, $e_q[0] = \mathbf{-0.0845\text{ V}}$.
- **Sampel $n=1$ ($t = 0.005\text{ s}$):** $s[1] = \mathbf{+1.4772\text{ V}} \implies$ **Step 11** (`1010`), $V_q = \mathbf{+1.250\text{ V}}$, $e_q[1] = \mathbf{-0.2272\text{ V}}$.
- **Sampel $n=2$ ($t = 0.010\text{ s}$):** $s[2] = \mathbf{+1.2599\text{ V}} \implies$ **Step 11** (`1010`), $V_q = \mathbf{+1.250\text{ V}}$, $e_q[2] = \mathbf{-0.0099\text{ V}}$.
- **Sampel $n=3$ ($t = 0.015\text{ s}$):** $s[3] = \mathbf{+1.0338\text{ V}} \implies$ **Step 11** (`1010`), $V_q = \mathbf{+1.250\text{ V}}$, $e_q[3] = \mathbf{+0.2162\text{ V}}$.

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
