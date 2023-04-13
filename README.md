# micro-py

[![Python CI](https://github.com/Akagi201/micro-py/actions/workflows/ci.yml/badge.svg)](https://github.com/Akagi201/micro-py/actions/workflows/ci.yml) [![Super Linter](https://github.com/Akagi201/micro-py/actions/workflows/super_linter.yml/badge.svg)](https://github.com/Akagi201/micro-py/actions/workflows/super_linter.yml)

## Features

- [x] argparse - command line arguments
- [x] [pdm](https://github.com/pdm-project/pdm) - package manager
- [ ] [attrs](https://github.com/python-attrs/attrs) - class decorators
- [x] [black](https://github.com/psf/black) - code formatter
- [ ] [pytest](https://github.com/pytest-dev/pytest) - testing framework
- [ ] [loguru](https://github.com/Delgan/loguru) - simple and structured logging
- [ ] [requests](https://github.com/psf/requests) - python client

## Tools

- <https://github.com/mamba-org/mamba> - faster alternative to conda
- miniconda - not support macOS m1
- miniforge(conda-forge) - support macOS m1
- sage

## Sage

```sh
mamba create -n sage sage python=X        # either
conda create -n sage sage python=X
conda activate sage
sage
```
