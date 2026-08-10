from subprocess import run
import pathlib
import os
import sys


def create_norec_env(current_path, python_executable=sys.executable):
    venv_dir = pathlib.Path(current_path) / "NOREC4DNA" / "venv"
    run([python_executable, "-m", "venv", str(venv_dir)], check=True)


def install_norec_packages(current_path):
    venv_dir = pathlib.Path(current_path) / "NOREC4DNA" / "venv"

    if os.name == "nt":
        pip = venv_dir / "Scripts" / "pip.exe"
    else:
        pip = venv_dir / "bin" / "pip"

    run([str(pip), "install", "wheel"], check=True)

    run(
        [
            str(pip),
            "install",
            "-r",
            str(pathlib.Path(current_path) / "NOREC_requirements.txt"),
        ],
        check=True,
    )


def compile_dna_aeon(current_path):
    run(["cmake", "-S", str(current_path), "-B", str(current_path / "build")], check=True)
    run(["cmake", "--build", str(current_path / "build"), "--config", "Release"], check=True)


if __name__ == "__main__":
    cpath = pathlib.Path(__file__).parent.resolve()

    print("Setting up NOREC4DNA virtual environment.")
    create_norec_env(cpath)

    print("Installing packages required for NOREC4DNA.")
    install_norec_packages(cpath)

    print("Compiling DNA-Aeon.")
    compile_dna_aeon(cpath)

    print("Installation finished!")
