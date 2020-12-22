#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy as np
import matplotlib.pyplot as plt


def read_csv(csvfile_path):
    timestamp = 0
    row_wave_value = 1
    eeg_data = []
    with open(csvfile_path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            eeg_data.append(float(row[row_wave_value]))
    return eeg_data


def analyze_EEG_data(eeg_data):
    N = len(eeg_data)

    # 窓関数
    hw = np.hamming(N)  # ハミング窓
    windowData = hw * eeg_data

    # フーリエ変換
    F = np.fft.fft(windowData)
    F_abs = np.abs(F)

    print(len(F_abs))

    # プロット
    left = np.arange(int(N/2))
    height = F_abs[0:int(N/2)] / np.max(F_abs)
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude")
    plt.bar(left, height)
    plt.show()


def fft_EEG(eeg_data):
    # データのパラメータ
    N = len(eeg_data)  # サンプル数
    dt = float(1)/512  # サンプリング間隔
    t = np.arange(0, N*dt, dt)  # 時間軸
    freq = np.linspace(0, 1.0/dt, N)  # 周波数軸

    # 信号を生成（周波数10の正弦波+周波数20の正弦波+ランダムノイズ）
    f = eeg_data

    # 高速フーリエ変換
    F = np.fft.fft(f)

    # 振幅スペクトルを計算
    Amp = np.abs(F)

    # グラフ表示
    plt.figure()
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 17
    plt.subplot(121)
    plt.plot(t, f)
    plt.xlabel("Time", fontsize=20)
    plt.ylabel("Signal", fontsize=20)
    plt.grid()
    leg = plt.legend(loc=1, fontsize=25)
    leg.get_frame().set_alpha(1)
    plt.subplot(122)
    plt.plot(freq, Amp)
    plt.xlabel('Frequency', fontsize=20)
    plt.ylabel('Amplitude', fontsize=20)
    plt.grid()
    leg = plt.legend(loc=1, fontsize=25)
    leg.get_frame().set_alpha(1)
    plt.show()


def main():
    eeg_data = read_csv('data/test5.csv')
    fft_EEG(eeg_data)


if __name__ == '__main__':
    main()
