#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy as np
import matplotlib.pyplot as plt


def read_csv(csvfile_path):
    # timestamp = 0
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
    fc = 60  # カットオフ周波数
    freq = np.linspace(0, 1.0/dt, N)  # 周波数軸

    f = eeg_data

    # 高速フーリエ変換
    F = np.fft.fft(f)

    # 正規化 + 交流成分2倍
    F = F/(N/2)
    F[0] = F[0]/2

    # 配列Fをコピー
    F2 = F.copy()

    # ローパスフィル処理（カットオフ周波数を超える帯域の周波数信号を0にする）
    F2[(freq > fc)] = 0

    # ハイパスフィルタ処理（1Hz未満の周波数信号を削除）
    F2[(freq < 1)] = 0

    # 振幅スペクトルを計算
    Amp = np.abs(F2)

    # グラフ表示
    axes = plt.axes()
    axes.set_xlim([0, 60])
    plt.plot(freq, Amp)
    plt.xlabel('Frequency', fontsize=20)
    plt.ylabel('Amplitude', fontsize=20)
    plt.show()


def main():
    eeg_data = read_csv('data/1016125/1.csv')
    fft_EEG(eeg_data)


if __name__ == '__main__':
    main()
