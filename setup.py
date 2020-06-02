#!/usr/bin/env python3 

from sys import platform, argv
from shared.setup import main

print('Starting environment initialization script...')

print('Platform is ' + platform)

if platform == "linux" or platform == "linux2":
	from linux.setup import main as linuxMain
	linuxMain(args=argv)
if platform == "darwin":
    from macos.setup import main as macMain
    macMain(args=argv)

main(args=argv)

