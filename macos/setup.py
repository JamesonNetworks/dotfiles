import pathlib
import os


def installVim(args):
	print("Checking for Vim directory")
	vimDir = pathlib.Path("~/.vim")
	if !vimDir.exists():
		print("Vim not found, need to install...")
	else:
		print("Vim exists, continuing with process")
		print("Checking for Vundle")
		vundleDir = pathlib.Path("~/.vim/bundle/Vundle.vim")
		if !vundleDir.exists():
			print("Vundle not found, cloning...")
			os.system('git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim')
		
			


def main(args):
	print("Running MacOS Environment setup...")

	print("Executing VIM Install Process...")
	installVim(args=args)
