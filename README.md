fractals
========
A small python project demonstrating various fractal algorithms.

### JSON Format for an 'Image' histogram

	{
		"height":int,
		"width":int,
		"max_freq":int,
		"min_freq":int,
		"image": {
			[ // Row (x)
				[ // Column (y)
					{
						"color": {
							"r":int,
							"g":int,
							"b":int
						},
						"frequency":int
					},
					...
				],
				...
			]
		}
	}
