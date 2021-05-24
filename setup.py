from setuptools import setup

setup(
	name = "wocker",
	packages = [ "wocker" ],
	entry_points = { "console_scripts": [
		"wocker=wocker.cli:entry"
	] }
)
