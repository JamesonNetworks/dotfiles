from pathlib import PosixPath
import os
from shutil import copyfile

def installZsh(args):
    print("Would check for zsh and ohmyzsh")


def printInstruction(msg):
    print("---")
    print(msg)
    print("---")


def installVim(args):
    print("Checking for Vim directory")
    vimDir = PosixPath("~/.vim").expanduser()
    if not vimDir.exists():
        print("Vim not found, need to install...")
    else:
        print("Vim exists, continuing with process")
        print("Checking for Vundle")
        vundleDir = PosixPath("~/.vim/bundle/Vundle.vim").expanduser()
        if not vundleDir.exists():
            print("Vundle not found, cloning...")
            os.system('git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim')
        else:
            print("Vundle Found! Continuing with install...")
        print("Overwriting vimrc")
        copyfile(PosixPath("./shared/vimrc"), PosixPath("~/.vimrc").expanduser())
        print("Overwriting input")
        copyfile(PosixPath("./shared/vimrc"), PosixPath("~/.inputrc").expanduser())
        print("Overwriting tmux")
        copyfile(PosixPath("./shared/tmux.conf"), PosixPath("~/.tmux.conf").expanduser())



def main(args):
    print("Running Shared Environment setup...")

    print("Executing OhMyZsh install...")
    installZsh(args=args)

    print("Executing VIM Install Process...")
    installVim(args=args)
