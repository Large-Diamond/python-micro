# micro-py

[![Python CI](https://github.com/Akagi201/micro-py/actions/workflows/ci.yml/badge.svg)](https://github.com/Akagi201/micro-py/actions/workflows/ci.yml) [![Super Linter](https://github.com/Akagi201/micro-py/actions/workflows/super_linter.yml/badge.svg)](https://github.com/Akagi201/micro-py/actions/workflows/super_linter.yml)

## Features

- [x] argparse - command line arguments
- [x] [pdm](https://github.com/pdm-project/pdm) - package manager(国人项目，很棒，哎可惜老外们不支持)
- [x] [poetry](https://github.com/python-poetry/poetry) - package manager
- [ ] [attrs](https://github.com/python-attrs/attrs) - class decorators
- [x] [black](https://github.com/psf/black) - code formatter
- [x] [ruff](https://github.com/charliermarsh/ruff) - code linter
- [ ] [pytest](https://github.com/pytest-dev/pytest) - testing framework
- [ ] [loguru](https://github.com/Delgan/loguru) - simple and structured logging
- [ ] [requests](https://github.com/psf/requests) - python client
- [ ] [pipx](https://github.com/pypa/pipx) - install and run python applications in isolated environments
- [ ] [mypy](https://mypy.readthedocs.io/en/stable/) - static type checker
- [ ] [httpx](https://www.python-httpx.org/) - next generation http client

## Libs

- loguru - simple and structured logging

## Tools

- <https://github.com/mamba-org/mamba> - faster alternative to conda
- miniconda - not support macOS m1
- miniforge(conda-forge) - support macOS m1
- sage

## src layout vs flat layout

- <https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/>


## Sage

```sh
mamba create -n sage sage python=X        # either
conda create -n sage sage python=X
conda activate sage
sage
```

## pipx

```sh
pip install pipx
pipx ensurepath
```

## poetry

```sh
pipx install poetry
```

vscode configs

use in-project virtualenv

```sh
poetry config virtualenvs.in-project true
```

remove global virtualenvs

```sh
poetry env list
poetry env remove <current environment>
poetry config virtualenvs.in-project true
poetry install
```

vscode python extension select the in-project interpreter

```sh
cmd + shift + p
>Python: Select Interpreter
```
