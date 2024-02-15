# Contributing

<!-- TOC -->
* [Contributing](#contributing)
  * [Create and use a virtual environment](#create-and-use-a-virtual-environment)
    * [Unix-based systems](#unix-based-systems)
    * [Windows](#windows)
  * [Install the project](#install-the-project)
  * [Code quality](#code-quality)
    * [Check code quality](#check-code-quality)
    * [Reformat the code](#reformat-the-code)
    * [Clean temporary files](#clean-temporary-files)
<!-- TOC -->

## Create and use a virtual environment

### Unix-based systems

```sh
# Move to the project's root
cd project_location
# Create a virtual environment to not pollute your system
python3 -m venv .venv
# Use your newly-created virtual environment
source .venv/bin/activate
```

### Windows

```shell
# Move to the project's root
cd project_location
# Create a virtual environment to not pollute your system
python -m venv .venv
# Use your newly-created virtual environment
.venv/Scripts/activate
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
