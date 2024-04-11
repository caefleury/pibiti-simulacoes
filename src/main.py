
from scripts import n1_crack, n2_crack, n1_edge_crack, replicate_cell, strains
import subprocess
import sys


def run_commands(commands):
    try:
        # Run each command in the virtual environment
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
    print()
    print("Linting and reformatting code...")
    run_commands(commands)

    print()
    print("============================== Generating Structures ==============================\n")
    replications = [17, 19]  # [x,y]
    n1_crack.run(replications[0], replications[1], 'x')
    n1_crack.run(replications[0], replications[1], 'y')
    n1_edge_crack.run(replications[0], replications[1])
    n2_crack.run(replications[0], replications[1], 'y')
    replicate_cell.run()
    print()
    print(
        "\033[1;32m" +
        "============================== Structures Generated ===========================" +
        "\033[0m")

    print("============================== Generating LAMPPS Simulations ==============================\n")
    strains.run()
    print(
        "\033[1;32m" +
        "============================== Simulations Generated ===========================" +
        "\033[0m")
