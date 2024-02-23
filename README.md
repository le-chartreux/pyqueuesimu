# pyqueuesimu

Simulation of queues.

Project made by Nathan ROUSSEAU and Swan FRERE as part of TELECOM Nancy's course "Performance evaluation". 

The subject is available [here](docs/subject.pdf).

## Table of Contents

<!-- TOC -->
* [pyqueuesimu](#pyqueuesimu)
  * [Table of Contents](#table-of-contents)
  * [Usage](#usage)
    * [Unix-based systems](#unix-based-systems)
    * [Windows](#windows)
<!-- TOC -->

## Usage

To use pyqueuesimu, run the commands specified according your operating system: [Unix-based](#unix-based-systems) or [Windows](#windows).

### Unix-based systems

```shell
# Move to the project's root
cd project_location
# Create a virtual environment to not pollute your system
python3 -m venv .venv
# Use your newly-created virtual environment
source .venv/bin/activate
# Install the project
pip install .
# Run pyqueuesimu with the parameters you want
pyqueuesimu cli 8 12 --observation-duration 10
pyqueuesimu gui 100 2 --observation-duration 60
# The list of parameters is available with the following command
pyqueuesimu --help
```

### Windows

```shell
# Move to the project's root
cd project_location
# Create a virtual environment to not pollute your system
python -m venv .venv
# Use your newly-created virtual environment
.venv/Scripts/activate
# Install the project
pip install .
# Run pyqueuesimu with the parameters you want
pyqueuesimu cli 8 12 --observation-duration 10
pyqueuesimu gui 100 2 --observation-duration 60
# The list of parameters is available with the following command
pyqueuesimu --help
```
