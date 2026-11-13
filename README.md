# subrunner

**subrunner** is a lightweight, modern Python wrapper around the built-in `subprocess` module designed to execute external CLI utilities with clean syntax and built-in **Rich** terminal logging.

## Features

- **Minimalist API:** One `CommandRunner` class and one `run()` method to keep your automation scripts clean and readable.
- **Real-Time Rich Logging:** Stream `stdout` and `stderr` in real time with styled panels, colored error highlighting, and status indicators (`rich=True`).
- **Structured Results:** Returns an immutable `CommandResult` dataclass containing `returncode`, `stdout`, and `stderr`.

## Requirements

- Python 3.13+
- [Rich](https://github.com/Textualize/rich)

## Instalation

Using `uv`:
```bash
uv add subrunner
```

Using `pip`:
```bash
pip install subrunner
```

## Quick Start
1) Basic usage:
```python
from subrunner import CommandRunner

git = CommandRunner('git')
result = git.run(['status'])

print(f'Exit code: {result.returncode}')
print(result.stdout)
```

2) Logging with rich:
```python
from subrunner import CommandRunner

git = CommandRunner('git')
git.run(['status'], rich=True)
```

3) Working Directory & Timeout:
```python
from subrunner import CommandRunner

yt_dlp = CommandRunner('yt-dlp')
yt_dlp.run(
    ['--version'],
    cwd='./downloads',
    timeout=10.0,
    rich=True,
)
```

## License
MIT