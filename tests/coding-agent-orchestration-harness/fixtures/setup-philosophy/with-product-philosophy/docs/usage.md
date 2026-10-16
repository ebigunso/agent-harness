# Usage

Run `python tally.py README.md` from the project directory; it prints `21`.
Quick check: `python -c "import subprocess, sys; assert subprocess.check_output([sys.executable, 'tally.py', 'README.md'], text=True).strip() == '21'"`.
Tally reads UTF-8 files and never changes them; unreadable input produces an error and no count.
