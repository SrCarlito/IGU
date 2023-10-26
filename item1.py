import matplotlib.pyplot as plt
import pandas as pd
import os

ACTUAL_DIR = os.path.dirname(os.path.abspath(__file__))


def openCsv(fileRoute):
    try:
        csvOpened = pd.read_csv(ACTUAL_DIR + fileRoute, sep=',')
        return csvOpened
    except Exception as e:
        print("Error al abrir el archivo:", e)
        return


def initPlots():
    plt.style.use('ggplot')
    fig, ax = plt.subplots(3, 1)
    for a in ax:
        a.grid(True)
        a.set_ylabel('ug/m3')

    return fig, ax


def umbralComparator(value, neightbors):
    for n in neightbors:
        if value < n:
            return False
    return True


def getPeaks(data, umbral):
    columns = ["PM1.0", "PM2.5", "PM10"]
    peaks_x = []
    peaks_y = []

    for column in columns:
        yValTEMP = []
        xVal = []
        
        for x in range(len(data[column])):
            if umbralComparator(data[column][x], data[column][x-umbral:x+umbral]):
                if data[column][x] not in yValTEMP and data[column][x] :
                    yValTEMP.append(data[column][x])
                    xVal.append(x)
        
        yVal = sorted(yValTEMP, reverse=True)[:5]
        xVal = [xVal[yValTEMP.index(y)] for y in yVal]
        
        peaks_y.append(yVal)
        peaks_x.append(xVal)

    return peaks_x, peaks_y


def plottingPeaks(ax_, data_):
    peaks_x, peaks_y = getPeaks(data_, 20)
    for i in range(3):
        ax_[i].plot(peaks_x[i], peaks_y[i], "x")


def plottingData():

    fig, ax = initPlots()

    data = openCsv("./datos.csv")

    ax[0].plot(data.index, data['PM1.0'], color='red', label='PM1.0')
    ax[1].plot(data.index, data['PM2.5'], color='green', label='PM2.5')
    ax[2].plot(data.index, data['PM10'], color='blue', label='PM10')

    plottingPeaks(ax, data)

    ax[0].legend()
    ax[1].legend()
    ax[2].legend()

    plt.show()


def showStats(fileRoute):
    data = openCsv(fileRoute)
    print(data.describe())


if __name__ == "__main__":
    plottingData()
    showStats("./datos.csv")
