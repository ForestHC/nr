# nr

## Getting started
### Install python
- Author recommendation: [RTX](https://github.com/jdxcode/rtx)
- Or you can use any of theses.
  - [asdf](https://github.com/asdf-vm/asdf)
  - [pyenv](https://github.com/pyenv/pyenv)
### Install poetry
```shell
curl -sSL https://install.python-poetry.org | python3 -
```
### Install deps & run
```shell
poetry install
poetry shell
uvicorn nr.main:app
```
