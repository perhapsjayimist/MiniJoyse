#!/usr/bin/env python3
from pathlib import Path
import shutil, subprocess

proj = Path(__file__).resolve().parent.parent
python = proj / "venv" / "bin" / "python3"
main = proj / "src" / "main.py"

subprocess.run([str(python), str(main)])
