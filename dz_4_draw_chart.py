import turtle
import argparse

if __name__ == "__main__":
	default_color = ['red', 'green', 'orange', 'yellow', 'blue', 'black', 'gray']
	
	def generate_dict_item_count(list_of_items):
		dict = {item: list_of_items.count(item) for item in set(list_of_items)} 
		return dict
	
	default_items=[	'py', 'cpp', 'php', 'php', 'cpp',
					'cpp', 'cpp', 'py', 'php', 'py',
					'py', 'js', 'html', 'cpp', 'js']
	parser = argparse.ArgumentParser(description='Draw chart by import items.')
	parser.add_argument('-t', '--type', default=0, type=int,
						help='type of chart: 0 - pie or 1 - bar, default = 0')
	parser.add_argument('-i', '--items', default=default_items, type=str,
						nargs='*', help=f'items of chart parameters, default = {default_items}')
	type_of_chart = parser.parse_args().type
	items_of_chart = generate_dict_item_count(parser.parse_args().items)
	
	first_pen = turtle.Turtle()
	first_pen.ht()
	first_pen.speed(10)
	index_of_color = 0
	chart_radius = 75
	chart_bar_length = 400
	
	if not type_of_chart:
		for language,value in items_of_chart.items():
			first_pen.begin_fill()
			first_pen.color(default_color[index_of_color])
			index_of_color += 1
			angle = value/sum(items_of_chart.values())*360
			first_pen.circle(chart_radius,angle/2)
			first_pen.up()
			first_pen.rt(90)
			first_pen.fd(chart_radius*0.4)
			first_pen.down()
			first_pen.write(f'{language}')
			first_pen.up()
			first_pen.bk(chart_radius*0.4)		
			first_pen.rt(-90)
			first_pen.down()
			first_pen.circle(chart_radius,angle/2)
			first_pen.lt(90)
			first_pen.fd(chart_radius)
			first_pen.end_fill()
			first_pen.bk(chart_radius)
			first_pen.lt(-90)
	else:
		first_pen.up()
		first_pen.bk(chart_bar_length*0.2*len(items_of_chart)/2)	
		first_pen.down()
		for language,value in items_of_chart.items():
			first_pen.begin_fill()
			first_pen.color(default_color[index_of_color])
			index_of_color += 1
			first_pen.lt(90)
			first_pen.fd(chart_bar_length*value/sum(items_of_chart.values()))
			first_pen.lt(-90)
			first_pen.fd(chart_bar_length*0.1)
			first_pen.up()
			first_pen.lt(90)
			first_pen.fd(chart_bar_length*0.1)
			first_pen.down()
			first_pen.write(f'{language}')
			first_pen.up()
			first_pen.bk(chart_bar_length*0.1)		
			first_pen.lt(-90)
			first_pen.down()	
			first_pen.fd(chart_bar_length*0.1)
			first_pen.lt(-90)
			first_pen.fd(chart_bar_length*value/sum(items_of_chart.values()))
			first_pen.end_fill()
			first_pen.lt(90)
	input()