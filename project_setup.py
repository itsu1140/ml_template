from dataclasses import dataclass
from pathlib import Path

import yaml
from cookiecutter.main import cookiecutter


@dataclass
class proj_setting:
    output_dir: str
    project_name: str


def main():
    with Path.open("setting.yaml", "r") as f:
        settings = proj_setting(**yaml.safe_load(f))

    output_dir = Path(settings.output_dir)
    cookiecutter(
        template=".",
        output_dir=output_dir,
        no_input=True,
        extra_context={
            "project_name": settings.project_name,
        },
    )
    proj_dir = output_dir / settings.project_name
    (proj_dir / "data").mkdir()
    src = proj_dir / "src"
    for directory in src.iterdir():
        if directory.is_dir():
            (directory / "__init__.py").touch()


if __name__ == "__main__":
    main()
