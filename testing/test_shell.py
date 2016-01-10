import tox_shell



def test_entrypoint():
    import pkg_resources
    pkg_resources.load_entry_point('tox-shell', 'console_scripts', 'tox-shell')