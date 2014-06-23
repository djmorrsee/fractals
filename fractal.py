import bin.flame.variations
from bin.flame.colors import colors as clrs

import random
from pprint import pprint
width = 100
height = 100

class data_point:
	def __init__(self):
		# Number of Times Hit
		self.frequency = 0

		# Color in (255, 255, 255) RGB Format
		self.color = (0, 0, 0)

	def Data(self):
		return { "frequency":self.frequency, "color": {"r":self.color[0], "g":self.color[1], "b":self.color[2]} }

	def __repr__(self):
		return str(self.__dict__)


class histogram:
	def __init__(self, w, h):
		self.hist = []
		self.width = w
		self.height = h

		for i in range(0, self.width):
			self.hist.append([])
			for j in range(0, self.height):
				self.hist[i].append(data_point())

	def Plot(self, x_bit, y_bit, c):
		x = int(((x_bit + 1) / 2) * self.width) % self.width
		y = int(((y_bit + 1) / 2) * self.width) % self.width

		self.hist[x][y].frequency += 1
		old_color = self.hist[x][y].color
		new_color = ((old_color[0] + c[0]) / 2, (old_color[1] + c[1]) / 2, (old_color[2] + c[2]) / 2)
		self.hist[x][y].color = new_color

	def Data(self):
		d = {
			"width":self.width,
			"height":self.height
		}
		rows = []
		max_f = 0
		min_f = 10000
		for i in range(0, self.width):
			row = []
			for j in range(0, self.height):
				point = self.hist[i][j]

				if point.frequency > max_f:
					max_f = point.frequency
				if point.frequency < min_f:
					min_f = point.frequency

				row.append(point.Data())
			rows.append(row)
		d.update({"image":rows})
		d.update({"min_freq":min_f})
		d.update({"max_freq":max_f})

		return d

	def WriteToFile(self, file_path):
		file = open(file_path, 'w+')
		from json import dump
		dump(self.Data(), file)
		file.close()

	def __repr__(self):
		return str(self.Data())


## Returns an array of functions defined in the variations.py script
def GetVariations():
	func_names = dir(bin.flame.variations)[:-6]
	return [bin.flame.variations.__dict__.get(a) for a in func_names]


def PopulateHistogram(i, funcs, hist):
	(x, y) = (random.random() * 2 - 1, random.random() * 2 - 1)
	c = random.random()
	for j in range(0, i):

		k = random.choice(range(0, len(funcs)))
		f = funcs[k]

		x, y = f(x,y)
		c = clrs[k]

		hist.Plot(x, y, c)


def Main():
	fs = GetVariations()
	hist = histogram(width, height)
	PopulateHistogram(100000, fs, hist)
	# SaveHistogram(hist)
	hist.WriteToFile('hist.json')


if __name__ == '__main__':
	Main()
