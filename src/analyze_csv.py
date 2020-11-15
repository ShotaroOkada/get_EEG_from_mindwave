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

    # プロット
    left = np.arange(int(N/2))
    height = F_abs[0:int(N/2)] / np.max(F_abs)
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude")
    plt.bar(left, height)
    plt.show()


def main():
    eeg_data = read_csv('data/new.csv')
    analyze_EEG_data(eeg_data)


if __name__ == '__main__':
    main()
