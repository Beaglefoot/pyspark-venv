from contextlib import contextmanager
import os
import sys


def get_python_version(venv_path: str) -> str:
    version = ""

    with open(os.path.join(venv_path, "pyvenv.cfg")) as cfg:
        for line in cfg.readlines():
            if line.startswith("version_info"):
                version_full = line.split(" = ")[1]
                version = ".".join(version_full.split(".")[0:2])

    return version


@contextmanager
def venv(venv_path: str):
    old_sys_prefix = sys.prefix
    old_sys_path = sys.path.copy()
    old_environ = os.environ.copy()

    try:
        sys.prefix = venv_path
        venv_python_version = get_python_version(venv_path)

        sys.path.insert(
            1,
            os.path.join(
                sys.prefix, "lib", "python" + venv_python_version, "site-packages"
            ),
        )

        sys.path.insert(
            1,
            os.path.join(
                sys.prefix, "lib64", "python" + venv_python_version, "site-packages"
            ),
        )

        os.environ["VIRTUAL_ENV"] = venv_path

        if os.environ.get("PATH"):
            os.environ["PATH"] = ":".join(
                (os.path.join(venv_path, "bin"), os.environ["PATH"])
            )
        else:
            os.environ["PATH"] = os.path.join(venv_path, "bin")

        yield

    finally:
        sys.prefix = old_sys_prefix
        sys.path = old_sys_path
        os.environ = old_environ
