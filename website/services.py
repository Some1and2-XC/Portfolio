#!/usr/bin/env python3

def RunKyros(args: dict, BonusSet = {}):
	# Function for generating a fractal from args

	from . import ROOTDIR

	from Kyros import fractal, color
	import os

	def DelFFiles():
		# Function for deleting All Files with the `F --` prefix
		from glob import glob
		import os
		for directory in glob("F --*/"):
			os.chdir(directory)
			for file in glob("*"):
				os.remove(file)
			os.chdir("..")
			os.rmdir(directory)
		return True

	os.chdir(f"{ROOTDIR}\\static\\Session")
	DelFFiles()

	if "BoxRange" not in args:
		args["BoxRange"] = ((4, 4), (-2, -2))

	f = fractal()

	c = color(
		RateOfColorChange = float(args["RateOfColorChange"]),
		MaxI = int(args["MaxI"]),
		ColorStyle = args["ColorStyle"],
		ShadowStyle = args["ShadowStyle"]
	)

	c.ModulusValue = 3

	settings = {
		"count": 0,
		"ci": float(args["ci"]),
		"cj": float(args["cj"]),
		"MaxI": int(args["MaxI"]),
		"IsJulia": bool(int(args["IsJulia"])),
		"SizeX": int(args["SizeX"]),
		"BoxRange": args["BoxRange"],
		"GenType": "{} {}".format(args["GenType1"], args["GenType2"])
	}

	f.SetAll(settings = settings, clr = c)

	if BonusSet:
		BonusSet["x"] = BonusSet["x"] * f.SizeX / 100
		BonusSet["y"] = BonusSet["y"] * int((f.BoxRange[0][1] / f.BoxRange[0][0]) * f.SizeX) / 100 # SizeY Isn't set so it is required that this is used

	f.eval(**BonusSet)

	os.chdir("../..")

	return "/".join(f"Session\\{f.FileName} - #{f.count-1}.png".split("\\")), f.BoxRange
