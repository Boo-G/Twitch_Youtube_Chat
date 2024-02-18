import subprocess
import signal
import os

# Store subprocess PIDs
subprocesses = []

def run_script(script_name):
    process = subprocess.Popen(['python', script_name])
    subprocesses.append(process.pid)

def stop_scripts():
    for pid in subprocesses:
        os.kill(pid, signal.SIGTERM)

def main():
    # Run scripts
    run_script('TwitchChat.py')

    run_script('YoutubeChat.py')

    run_script('UI.py')

    try:
        while True:
            pass
    except KeyboardInterrupt:
        stop_scripts()
        print("Scripts stopped.")

if __name__ == "__main__":
    main()

