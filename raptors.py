from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
import csv

input_file = 'raps.csv'
dict_types = {'age': 2, 'g': 3, 'gs': 4, 'mp': 5, 'fg': 6, 'fga': 7, 'fg%': 8, '3p': 9, '3pa': 10, '3p%': 11, 'ft': 12, 'fta': 13, 'ft%': 14, 'orb': 15, 'drb': 16, 'trb': 17, 'ast': 18, 'stl': 19, 'blk': 20, 'tov': 21, 'pf': 22, 'pts': 23}
user_input = raw_input('category to graph: ')
#print user_input
#print dict_types.keys()
n_store = []
v_store = []

if (user_input in dict_types):
	with open(input_file, 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	        v_store.append (row[dict_types[user_input]])
	        n_store.append (row[1]) #always append the name
	
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

