import pytest

import pyqueuesimu


@pytest.mark.parametrize("module_name", pyqueuesimu.__all__)
def test_imports(module_name: str) -> None:
    """It exposes the pyqueuesimu modules."""
    assert hasattr(pyqueuesimu, module_name)
