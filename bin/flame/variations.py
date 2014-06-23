import variables

def Linear(x, y):
	return (x, y)

def Sinusoidal(x, y):
	from math import sin
	return (sin(x), sin(y))

def Spherical(x, y):
	r = variables.R(x, y)
	mult = 1.0 / (r * r)
	return (mult * x, mult * y)

def Swirl(x, y):
	from math import sin, cos
	r = variables.R(x, y)
	return (x * sin(r * r) - y * cos(r * r), x * cos(r * r) - y * cos(r * r))

def Horseshoe(x, y):
	r = variables.R(x, y)
	mult = (1.0 / r)
	return (mult * (x - y) * (x + y), mult * 2 * x * y)

def Polar(x, y):
	from math import pi

	theta = variables.Theta(x, y)
	r = variables.R(x, y)
	return (theta / pi, r - 1)

#
# def Handkerchief(x, y):
# 	pass
#
# def Heart(x, y):
# 	pass
#
# def Disc(x, y):
# 	pass
#
# def Spiral(x, y):
# 	pass
#
# def Hyperbolic(x, y):
# 	pass
#
# def Diamond(x, y):
# 	pass
#
# def Ex(x, y):
# 	pass
#
# def Julia(x, y):
# 	pass
#
# def Bent(x, y):
# 	pass
#
# def Waves(x, y):
# 	pass
#
# def Fisheye(x, y):
# 	pass
#
# def Popcorn(x, y):
# 	pass
#
# def Exponential(x, y):
# 	pass
#
# def Power(x, y):
# 	pass
#
# def Cosine(x, y):
# 	pass
#
# def Rings(x, y):
# 	pass
#
# def Fan(x, y):
# 	pass
#
# def Blob(x, y):
# 	pass
#
# def PDJ(x, y):
# 	pass
#
# def Fan2(x, y):
# 	pass
#
# def Rings(x, y):
# 	pass
#
# def Eyefish(x, y):
# 	pass
#
# def Bubble(x, y):
# 	pass
#
# def Cylinder(x, y):
# 	pass
#
# def Perspective(x, y):
# 	pass
#
# def Noise(x, y):
# 	pass
#
# def JuliaN(x, y):
# 	pass
#
# def Blur(x, y):
# 	pass
#
# def Gaussian(x, y):
# 	pass
#
# def RadialBlur(x, y):
# 	pass
#
# def Pie(x, y):
# 	pass
#
# def Ngon(x, y):
# 	pass
#
# def Curl(x, y):
# 	pass
#
# def Rectangles(x, y):
# 	pass
#
# def Arch(x, y):
# 	pass
#
# def Tangent(x, y):
# 	pass
#
# def Square(x, y):
# 	pass
#
# def Rays(x, y):
# 	pass
#
# def Blade(x, y):
# 	pass
#
# def Secant(x, y):
# 	pass
#
# def Twintrain(x, y):
# 	pass
#
# def Cross(x, y):
# 	pass
