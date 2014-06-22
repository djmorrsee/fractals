var id, d, canvas, ctx
var function_set = [Half, Add, Double, Reverse, Root, Quadratic]
function GetFunction() {
	var f = function_set[parseInt(Math.random() * function_set.length)]
	return f
}

$(document).ready(function () {
	canvas = document.getElementById('main-canvas');
	if (canvas.getContext){
	  ctx = canvas.getContext('2d');

		id = ctx.createImageData(1,1)
		d = id.data
		d[3] = 255 // Alpha

		// drawing code here

		RunFractal(255, ctx)
		//PutRGBToPixel(255, 0, 0, 100, 100)
	} else {
	  // canvas-unsupported code here
		console.log("Error Loading Canvas Context")
	}
});




function PixelValueToRGB(val, max) {
	var rgbval = (val / max) * 255;
	return rgbval
}

function RunFractal(count, context) {
	var w = canvas.width
	var h = canvas.height
	var color = [0, 0, 0]

	var x = parseInt(Math.random() * w)
	var y = parseInt(Math.random() * h)

	var points = []
	var table = []
	while(count--) {
		f = GetFunction()
		points = $.map(f(x, y), function (val, i) {
			TrimVal(val)
		})

		x = points[0]
		y = points[1]

	}

}

function TrimVal(v) {
	v = parseInt(v) || 0

	if (v > canvas.width || v < 0) {
		// Random New Point
		v = parseInt(Math.random() * canvas.width)
	}

	return v
}

function PutRGBToPixel(color, x, y) {
	d[0] = color[0]
	d[1] = color[1]
	d[2] = color[2]
	ctx.putImageData(id, x, y)
}

function Linear(x, y) {
	return [x, y]
}

function Sinusoidal(x, y) {
	return [Math.sin(x), Math.sin(y)]
}

function Quadratic(x, y) {
	return [x * x, y * y]
}

function Half(x, y) {
	return [x / 2, y / 2]
}

function Double(x, y) {
	return [x * 2, y * 2]
}

function Reverse(x, y) {
	return [y, x]
}

function XOR(x, y) {
	return [x ^ y, x * y ^ x]
}

function Root(x, y) {
	return [Math.sqrt(x), Math.sqrt(y)]
}

function Swirl(x, y) {
	var r = Math.pi
	return [x * Math.sin(r * r) - y * Math.cos(r * r), x * Math.cos(r * r) - y * Math.sin(r * r)]
}

function Add(x, y) {
	return [x + y, y + x]
}

function Add2(x, y) {
	return [x + getRandomInt(1, canvas.width), y + getRandomInt(1, canvas.height)]
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
