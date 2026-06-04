# 𝓜𝓲𝓷𝓲𝓙𝓸𝔂𝓼𝓮 - 𝕧𝟘.𝟙.𝟙 (MiniJoyse v0.1.1)
# THIS IS EXPECTED TO BE RUNNED BY THE RUN SCRIPT!!!
# A mini programming language by Jay

MINIJOYSE_VERSION = "0.1.1"

import sys, time, subprocess, shlex
from pathlib import Path
from rich import print as rich_print
from rich.text import Text
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

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
def _envfunc_quit() -> None:
	"""Quits the program"""
	_envfunc_print("Bye!")
	sys.exit()
def _envfunc_exit() -> None:
	"""Quits the program"""
	_envfunc_print("Bye!")
	sys.exit()

KEYWORDS = {
	"set", # Set variable | set var "string" ; print var
}

standard_env = {
	"print": _envfunc_print,
	"raw_print": _envfunc_raw_print,
	"warn": _envfunc_warn,
	"quit": _envfunc_quit,
	"exit": _envfunc_exit
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
		# print(f"\nPROGRAM:\n{program}")
		lexer = Lexer(program)
		tokens = lexer.process()
		# print(f"\nTOKENS:\n{tokens}")
		parser = Parser(tokens)
		nodes = parser.process()
		# print(f"\nNODES:\n{nodes}\n\n")
		interpreter = Interpreter(nodes, self.env, KEYWORDS)
		result = interpreter.run()



MiniJoyse = MiniJoyse()

print(sys.argv)

cmd = sys.argv[0]
args = sys.argv[1:]

if not args:
	print(f"𝓜𝓲𝓷𝓲𝓙𝓸𝔂𝓼𝓮 - v{MINIJOYSE_VERSION}\nMiniJoyse is a line-based DSL language by Jay\nCommands:\n    version - Shows the MiniJoyse version.\n    update - NOT USABLE!\n\nType 'quit' or 'exit' to quit the loop.")

	while True:
		line = input(">>> ")
		MiniJoyse.run(line)
elif args[0] == "version":
	print(f"𝓜𝓲𝓷𝓲𝓙𝓸𝔂𝓼𝓮 - v{MINIJOYSE_VERSION} (MiniJoyse)")
elif args[0] == "update":
	installer = Path(__file__).resolve().parent.parent / "scripts" / "installer.sh"
	subprocess.run(["bash", installer])
elif args[0]:
	file = Path(args[0])
	
	if not file.exists():
		warn(f"File not found: {args[0]}")
		sys.exit(1)
	
	program = file.read_text()
	MiniJoyse.run(program)