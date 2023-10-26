from math import *
from struct import pack
import wave
import os
import matplotlib.pyplot as plt

ACTUAL_DIR = os.path.dirname(os.path.abspath(__file__))

RATES = [44110, 22050]


PENTATONIC = {
    "Do": 261.63,
    "Re": 293.66,
    "Mi": 329.63,
    "Fa": 349.23,
    "Sol": 392.00,
    "La": 440.00,
    "Si": 493.88,
}


def getPeriod(rate, freq):
    return int(rate / freq)


def getUnitsWaves(seconds, rate, period):
    return int(seconds * rate/period)


def fourier(x, period: int):
    return 8000 * sin(2 * pi * x / period)


def createWave(rate, freq, time):
    period = getPeriod(rate, freq)
    unitsWaves = getUnitsWaves(time, rate, period)
    x = range(period)
    y = period*[0]
    for i in x:
        y[i] = fourier(i, period)

    y = unitsWaves * y
    x = range(unitsWaves * period)
    return x, y


def intiWav(rate, channels, filename):
    wavFile = wave.open(ACTUAL_DIR + "/" + filename, "w")
    wavFile.setnchannels(channels)
    wavFile.setsampwidth(2)
    wavFile.setframerate(rate)
    wavFile.setcomptype('NONE', 'Not Compressed')
    return wavFile

# ACT 1
def act1():
    wav = intiWav(RATES[0], 1, "test.wav")
    BinStr = b''
    for i in PENTATONIC:
        x, y = createWave(rate=RATES[0], freq=PENTATONIC[i], time=1)
        for i in range(len(y)):
            BinStr = BinStr + pack('h', round(y[i]))
    wav.writeframesraw(BinStr)
    wav.close()

act1()

# ACT 2
def act2():
    wav = intiWav(RATES[1], 2, "test2.wav")
    BinStr = b''
    for i in PENTATONIC:
        x, y = createWave(rate=RATES[1], freq=PENTATONIC[i], time=1)
        for i in range(len(y)):
            BinStr = BinStr + pack('h', round(y[i]))  # to left
            BinStr = BinStr + pack('h', round(y[i]))  # to right

    wav.writeframesraw(BinStr)
    wav.close()


act2()


# ACT 3

def act3():
    RATE = RATES[0]
    wav = intiWav(RATE, 2, "test3.wav")
    def y(i):
        return 8000 * sin(2 * pi * 500/RATE * i) + 8000 * sin(2*pi*250/RATE*i)
    BinStr = b''
    for x in range(RATE * 3):
        BinStr = BinStr + pack('h', round(y(x)))  # to left
        BinStr = BinStr + pack('h', round(y(x)))  # to right

    wav.writeframesraw(BinStr)
    wav.close()

act3()


# plt.plot(*createWave(rate=RATES[0], freq=PENTATONIC["Do"], time=0.5))
# plt.show()
