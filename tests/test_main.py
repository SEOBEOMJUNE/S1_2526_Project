# tests/test_main.py
import subprocess
import sys

def test_main_executes():
    result = subprocess.run([sys.executable, "main.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello from venv!" in result.stdout
