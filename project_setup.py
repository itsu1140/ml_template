import argparse
from pathlib import Path

from cookiecutter.main import cookiecutter


def cookiecutter_setup(project_name: str, python_version: str) -> None:
    output_dir = Path("..")
    cookiecutter(
        template=".",
        output_dir=output_dir,
        no_input=True,
        extra_context={
            "project_name": project_name,
            "python_version": python_version,
        },
    )
    proj_dir = output_dir / project_name
    (proj_dir / "data").mkdir()

    src_dirs = ["models", "plot", "data", "train", "utils"]
    src = proj_dir / "src"
    for dir_name in src_dirs:
        (src / dir_name).mkdir()
        (src / dir_name / "__init__.py").touch()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_name", required=True)
    parser.add_argument("--python_version")
    args = parser.parse_args()
    cookiecutter_setup(args.project_name, args.python_version)


if __name__ == "__main__":
    main()
