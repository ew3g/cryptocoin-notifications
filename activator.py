import psutil
import sys
from subprocess import Popen

for process in psutil.process_iter():
    if process.name() == 'python.exe':
        if 'run.py' in process.cmdline():
            sys.exit('run.py already running.\n')

if sys.platform == 'win32':
    python_venv_path = 'venv/Scripts/python'
else:
    python_venv_path = 'venv/bin/activate'

print('run.py not running, starting...')

Popen([python_venv_path, 'run.py'])
