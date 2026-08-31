"""
Demo Visualisasi Sinyal & Pemrosesan Sinyal Digital (PSD)
Mengilustrasikan:
1. Perbedaan Amplitudo (Besar vs Kecil)
2. Perbedaan Frekuensi (Tinggi vs Rendah)
3. Perbedaan Fase (Pergeseran Waktu)
4. Analisis Spektrum Frekuensi menggunakan FFT
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    # 1. Parameter Sampling
    Fs = 1000.0          # Frekuensi Sampling (1 kHz)
    duration = 1.0       # Durasi 1 Detik
    t = np.linspace(0.0, duration, int(Fs * duration), endpoint=False)

    # 2. Sintesis Berbagai Variasi Sinyal
    # A. Dasar (f = 5 Hz, A = 1.0, phi = 0)
    sig_base = 1.0 * np.sin(2 * np.pi * 5 * t)
    
    # B. Amplitudo Lebih Besar (A = 2.5)
    sig_high_amp = 2.5 * np.sin(2 * np.pi * 5 * t)
    
    # C. Frekuensi Lebih Tinggi (f = 20 Hz)
    sig_high_freq = 1.0 * np.sin(2 * np.pi * 20 * t)
    
    # D. Bergeser Fase (phi = pi/2 atau 90 derajat)
    sig_phase_shift = 1.0 * np.sin(2 * np.pi * 5 * t + (np.pi / 2))

    # 3. Plot Visualisasi
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Visualisasi Karakteristik Parameter Sinyal (PSD)", fontsize=14, fontweight='bold')

    # Subplot 1: Efek Amplitudo
    axes[0, 0].plot(t[:200], sig_base[:200], label='Amplitudo A = 1.0', color='blue')
    axes[0, 0].plot(t[:200], sig_high_amp[:200], label='Amplitudo A = 2.5', color='red', linestyle='--')
    axes[0, 0].set_title("1. Pengaruh Amplitudo (Tinggi Gelombang / Volume)")
    axes[0, 0].set_xlabel("Waktu (detik)")
    axes[0, 0].set_ylabel("Amplitudo")
    axes[0, 0].legend()
    axes[0, 0].grid(True)

    # Subplot 2: Efek Frekuensi
    axes[0, 1].plot(t[:200], sig_base[:200], label='Frekuensi f = 5 Hz (Renggang)', color='blue')
    axes[0, 1].plot(t[:200], sig_high_freq[:200], label='Frekuensi f = 20 Hz (Rapat)', color='green')
    axes[0, 1].set_title("2. Pengaruh Frekuensi (Kerapatan Gelombang / Nada)")
    axes[0, 1].set_xlabel("Waktu (detik)")
    axes[0, 1].set_ylabel("Amplitudo")
    axes[0, 1].legend()
    axes[0, 1].grid(True)

    # Subplot 3: Efek Fase
    axes[1, 0].plot(t[:200], sig_base[:200], label='Fase $\phi = 0^\circ$', color='blue')
    axes[1, 0].plot(t[:200], sig_phase_shift[:200], label='Fase $\phi = 90^\circ$ (Maju 90°)', color='purple', linestyle='-.')
    axes[1, 0].set_title("3. Pengaruh Fase (Pergeseran Titik Awal)")
    axes[1, 0].set_xlabel("Waktu (detik)")
    axes[1, 0].set_ylabel("Amplitudo")
    axes[1, 0].legend()
    axes[1, 0].grid(True)

    # Subplot 4: Spektrum FFT dari Sinyal Campuran
    composite_signal = sig_base + 0.5 * sig_high_freq
    fft_vals = np.abs(np.fft.rfft(composite_signal)) / len(t)
    fft_freqs = np.fft.rfftfreq(len(t), 1.0 / Fs)

    axes[1, 1].plot(fft_freqs[:50], fft_vals[:50], color='darkorange', marker='o', markersize=3)
    axes[1, 1].set_title("4. Spektrum FFT (Deteksi Frekuensi 5 Hz & 20 Hz)")
    axes[1, 1].set_xlabel("Frekuensi (Hz)")
    axes[1, 1].set_ylabel("Magnitudo")
    axes[1, 1].grid(True)

    plt.tight_layout()
    plt.savefig("/home/abuyyy/PSD/visualisasi_sinyal.png", dpi=150)
    print("Grafik disimpan ke /home/abuyyy/PSD/visualisasi_sinyal.png")

if __name__ == '__main__':
    main()
