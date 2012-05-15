from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
import csv

input_file = 'raps.csv'
n_store = []
v_store = []

with open(input_file, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        v_store.append (row[8])
        n_store.append (row[1])

values = v_store[1:len(v_store)]

#cast each of the items in array to type int
values = [float(x) for x in values]

#get max value
def getMaxValue(array_values = []):
	max_value = array_values[0]
	for i in array_values:
		if (i > max_value):
			max_value = i

#create a bar graph
d = Drawing(2000, 1000)

chart = VerticalBarChart()
chart.width = 1600
chart.height = 800
chart.x = 110
chart.y = 90
chart.data = [values]
chart.groupSpacing = 10
chart.categoryAxis.labels.angle = 45
chart.valueAxis.labels.fontSize = 18
chart.valueAxis.valueMin = 0
chart.valueAxis.valueMax = getMaxValue(values)
chart.categoryAxis.labels.fontSize = 24
chart.categoryAxis.categoryNames = n_store[1:len(n_store)]
chart.valueAxis.valueMin = 0

d.add(chart)
d.save(fnRoot='test', formats=['png', 'pdf'])

