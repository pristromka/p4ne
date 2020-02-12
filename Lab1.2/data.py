from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

def getvalue(x):
    return x.value

dates = list(map(getvalue, sheet['A'][1:]))

otn_temp = list(map(getvalue, sheet['C'][1:]))

activ = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(dates, otn_temp, label="Относительная температура")
pyplot.plot(dates, activ, label="Активность солнца")
pyplot.xlabel('Годы')
pyplot.ylabel('Температура/Активность солнца')
pyplot.legend(loc='upper left')
pyplot.show()
