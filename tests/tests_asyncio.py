import sys

if sys.version_info[:2] > (3, 6):
    from .py37_asyncio import *  # NOQA
else:
    import pytest
    try:
        pytest.skip("async not supported", allow_module_level=True)
    except TypeError:
        pass
