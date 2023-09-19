from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die(10)

results = []

for roll_num in range(50_000):
    results.append(die_1.roll() + die_2.roll())

# print(results)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequencies.append(results.count(value))

# print(frequencies)

# visualize the results
x_values = list(range(2, max_result + 1 ))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}

my_layout = Layout(title='Results of rolling one two D6 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')