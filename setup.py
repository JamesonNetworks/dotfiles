#!/usr/bin/env python3 

from sys import platform, argv

print('Starting environment initialization script...')

print('Platform is ' + platform)

if platform == "linux" or platform == "linux2":
	from linux.setup import main
	main(args=argv)
if platform == "darwin":
	from macos.setup import main
	main(args=argv)

