import subprocess
import sys


def run_commands_in_virtualenv(commands):
    try:
        for command in commands:
            subprocess.run(command, check=True, shell=True)

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        sys.exit(1)


if __name__ == "__main__":
    commands = [
        "autopep8 --in-place --recursive .",
        "pytest"
    ]
    run_commands_in_virtualenv(commands)
