import random, math

def R(x, y):
	r = math.sqrt(x * x + y * y)
	return r

def Theta(x, y):
	if not y == 0:
		return math.atan(x / y)
	else:
		return math.pi

def Gamma(x, y):
	if not x == 0:
		return math.atan(y / x)
	else:
		return math.pi

def Omega():
	return random.choice([0, math.pi])

def Alpha():
	return random.choice([-1, 1])

def Beta():
	return random.random()
