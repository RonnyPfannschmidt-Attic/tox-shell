# content of setup.py
from setuptools import setup

if __name__ == "__main__":
    setup(
        name='tox-shell',
        description='starts your shell in tox environments',
        license="MIT license",
        version='0.1',
        package_dir={'': 'src'},
        packages=['tox_shell'],
        entry_points={'console_scripts': ['tox-shell = tox_shell.session:main']},
        install_requires=['tox>=2.0'],
        setup_requires=['setuptools_scm'],
        use_scm_version=True,
    )