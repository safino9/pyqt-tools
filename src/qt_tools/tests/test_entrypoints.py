import os
import pathlib
import subprocess
import sys

import pytest


fspath = getattr(os, 'fspath', str)


def test_designer():
    with pytest.raises(subprocess.TimeoutExpired):
        subprocess.run(
            [
                fspath(
                    pathlib.Path(sys.executable).with_name('designer'),
                ),
            ],
            check=True,
            env={**os.environ, 'QT_DEBUG_PLUGINS': '1'},
            timeout=10,
        )


def test_qmlscene():
    with pytest.raises(subprocess.TimeoutExpired):
        subprocess.run(
            [
                fspath(
                    pathlib.Path(sys.executable).with_name('qmlscene'),
                ),
            ],
            check=True,
            env={**os.environ, 'QT_DEBUG_PLUGINS': '1'},
            timeout=10,
        )