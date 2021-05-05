from pathlib import PosixPath
import os
from shutil import copyfile


def installZsh(args):
    ohmyzshDir = PosixPath("~/.oh-my-zsh").expanduser()
    if not ohmyzshDir.exists():
        os.system("sh -c \"$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\"")


def installZshSyntaxHighlighting(args):
    zshHighlightDir = PosixPath("~/.zsh-syntax-highlighting").expanduser()
    if not zshHighlightDir.exists():
        os.system("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh-syntax-highlighting")


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

        print("Insalling OhMyZsh")
        installZsh(args=args)
        print("Installing Zsh Syntax Highlighting")
        installZshSyntaxHighlighting(args=args)
        print("Overwriting vimrc")
        copyfile(PosixPath("./shared/vimrc"), PosixPath("~/.vimrc").expanduser())
        print("Overwriting input")
        copyfile(PosixPath("./shared/inputrc"), PosixPath("~/.inputrc").expanduser())
        print("Overwriting tmux")
        copyfile(PosixPath("./shared/tmux.conf"), PosixPath("~/.tmux.conf").expanduser())
        print("Overwriting gitignore")
        copyfile(PosixPath("./shared/gitignore"), PosixPath("~/.gitignore").expanduser())

def installNeoVim(args):
    print("Checking for Vim directory")
    vimDir = PosixPath("~/.config/nvim/").expanduser()
    if not vimDir.exists():
        print("Neovim config dir not found, need to install...")
    else:
        copyfile(PosixPath("./shared/init.vim"), PosixPath("~/.config/nvim/init.vim").expanduser())
        copyfile(PosixPath("./shared/plug.vim"), PosixPath("~/.config/nvim/autoload/plug.vim").expanduser())
        os.system("python3 -m pip install --user --upgrade pynvim")
        print("Additional Notes:")
        print("================")
        print("Install universal-ctags...")
        print("https://github.com/universal-ctags/ctags")
        print("Install the coc-json and coc-tsserver in nvim:")
        print(":CocInstall coc-json coc-tsserver")


def copySnippets(args):
    print("Checking for the snippets configuration directory")
    vimDir = PosixPath("~/.config/nvim/").expanduser()
    if not vimDir.exists():
        print("Neovim config dir not found, need to install...")
        return
    snippetsDir = PosixPath("~/.config/nvim/UltiSnips").expanduser()
    if not snippetsDir.exists():
        print("Directory not created, creating...")
        snippetsDir.mkdir(parents=True, exist_ok=True)
    copyfile(PosixPath("./snippets/html.snippets"), PosixPath("~/.config/nvim/UltiSnips/html.snippets").expanduser())
    copyfile(PosixPath("./snippets/typescript.snippets"), PosixPath("~/.config/nvim/UltiSnips/typescript.snippets").expanduser())
    copyfile(PosixPath("./snippets/scss.snippets"), PosixPath("~/.config/nvim/UltiSnips/scss.snippets").expanduser())


def main(args):
    print("Running Shared Environment setup...")

    print("Executing OhMyZsh install...")
    installZsh(args=args)

    print("Executing VIM Install Process...")
    installVim(args=args)

    print("Executing Neovim Install Process...")
    installNeoVim(args=args)

    print("Copying Snippets...")
    copySnippets(args=args)
