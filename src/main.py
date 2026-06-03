# 𝓜𝓲𝓷𝓲𝓙𝓸𝔂𝓼𝓮 - 𝕧𝟘.𝟙.𝟘 (MiniJoyse v0.1.0)
# THIS IS EXPECTED TO BE RUNNED BY THE RUN SCRIPT!!!
# A mini programming language by Jay

MINIJOYSE_VERSION = "0.1.0"

import sys, time, subprocess, shlex
from pathlib import Path
from rich import print as rich_print
from rich.text import Text
from lexer import Lexer
from parser import Parser

# Functions
def warn(*args):
	"""Prints a warn"""
	msg = Text(" ".join(map(str, args)), style="yellow")
	rich_print(msg)

# Environmentals and Parser
def _envfunc_print(*args) -> None:
	"""Prints a message"""
	print(f"[MiniJoyse]:", *args)
def _envfunc_raw_print(*args) -> None:
	"""Prints a message rawly"""
	print(*args)
def _envfunc_warn(*args) -> None:
	"""Prints a warn"""
	warn("[MiniJoyse - Warning]:", *args)

KEYWORDS = {
	"set", # Set variable | set var "string" ; print var
	";", # New line | print "a" ; print "b"
}

standard_env = {
	"constants": {

	},
	"funcs": {
		"print": _envfunc_print,
		"raw_print": _envfunc_raw_print,
		"warn": _envfunc_warn
	}
}



class MiniJoyse:
	def __init__(self, env: dict=None, debug: bool=False) -> None:
		self.env = env or standard_env.copy()
		self.DEBUG = debug
	
	def set_env(self, new_env: dict) -> None:
		"""Sets a new environment for the class"""
		if not new_env: return
		self.env = new_env

	def get_env(self) -> dict:
		"""Gets the environment from the class"""
		return self.env

	def run(self, program: str) -> None:
		print(f"\nPROGRAM:\n{program}")
		lexer = Lexer(program)
		tokens = lexer.process()
		print(f"\nTOKENS:\n{tokens}")
		parser = Parser(tokens)
		instructions = parser.process()


# Main
MiniJoyse = MiniJoyse()
MiniJoyse.run("print hello")