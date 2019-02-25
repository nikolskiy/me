"""
Document and automate most commonly performed tasks.

List all commands:
inv --list

Shell tab completion:
http://docs.pyinvoke.org/en/latest/cli.html#shell-tab-completion
"""
from invoke import Collection
from tools import make

ns = Collection(
    make.build, make.clean, make.run, make.update, make.html,
)
