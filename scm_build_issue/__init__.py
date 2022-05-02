try:
    import importlib.metadata as metadata
except ModuleNotFoundError:
    import importlib_metadata as metadata

try:
    __version__ = metadata.version("scm_build_issue")
except metadata.PackageNotFoundError:
    pass
