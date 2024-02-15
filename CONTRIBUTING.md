# Contributing

<!-- TOC -->
* [Contributing](#contributing)
  * [Create and use a virtual environment](#create-and-use-a-virtual-environment)
  * [Install the project](#install-the-project)
  * [Code quality](#code-quality)
    * [Check code quality](#check-code-quality)
    * [Reformat the code](#reformat-the-code)
    * [Clean temporary files](#clean-temporary-files)
<!-- TOC -->

## Create and use a virtual environment

```sh
python3 -m venv .venv
source .venv/bin/activate
```

## Install the project

```sh
pip install --editable ".[dev]"
```

## Code quality

### Check code quality

```sh
tox
```

### Reformat the code

```sh
tox -m format
```

### Clean temporary files

```sh
tox -m clean
```
