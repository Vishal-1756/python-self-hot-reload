import subprocess
import time
import os
import sys

WATCH_EXTENSIONS = (".py",)
WATCH_PATHS = ["."]
CHECK_INTERVAL = 1  # seconds


def run_script():
    return subprocess.Popen(
        [sys.executable, "-m", "xyz"],
        stdin=sys.stdin,
        stdout=sys.stdout,
        stderr=sys.stderr
    )


def scan_files():
    mtimes = {}
    for path in WATCH_PATHS:
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(WATCH_EXTENSIONS):
                    full_path = os.path.join(root, file)
                    try:
                        mtimes[full_path] = os.path.getmtime(full_path)
                    except FileNotFoundError:
                        continue
    return mtimes


def restart_process(proc):
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
    return run_script()


def main():
    print("Auto-reload started...")
    mtimes = scan_files()
    proc = run_script()

    try:
        while True:
            time.sleep(CHECK_INTERVAL)
            new_mtimes = scan_files()
            if new_mtimes != mtimes:
                print("Change detected. Restarting...")
                proc = restart_process(proc)
                mtimes = new_mtimes
    except KeyboardInterrupt:
        print("Interrupted. Exiting...")
        restart_process(proc)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        restart_process(proc)


if __name__ == "__main__":
    main()
