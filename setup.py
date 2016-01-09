# content of setup.py
from setuptools import setup

if __name__ == "__main__":
    setup(
        name='tox-shell',
        description='starts your shell in tox environments',
        license="MIT license",
        version='0.1',
        py_modules=['tox_shell'],
        entry_points={'tox': ['shell = tox_shell']},
        install_requires=['tox>=2.0'],
        setup_requires=['setuptools_scm'],
        use_scm_version=True,
    )