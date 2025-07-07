# Python Auto-Reload Runner

This is a simple Python script that watches for file changes in your project and automatically restarts the target module (`xzy`) when a change is detected.

## Features

- Watches all `.py` files recursively
- Automatically restarts the Python process on code changes
- Cross-platform support (Windows, macOS, Linux)
- Clean shutdown and restart handling

## Usage

1. Save the script as `dev.py`.

2. Run the script:

```bash
python dev.py
````

This will run the module `xyz` using:

```bash
python -m xyz
```

and restart it whenever any Python file changes in the current directory or subdirectories.

