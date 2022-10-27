"""Declarative Typed Argument Parsing with Pydantic Models.

This is the `pydantic-argparse` package, which contains the classes, methods
and functions required for declarative and typed argument parsing with
`pydantic` models.

The public interface exposed by this package is the declarative and typed
`ArgumentParser` class, as well as the package "dunder" metadata.
"""

# Local
from .argparse import ArgumentParser

try:
    from .__metadata__ import __title__, __description__, __version__, __author__, __license__
    _metadata_exports = (
        "__title__",
        "__description__",
        "__version__",
        "__author__",
        "__license__",
    )
except ModuleNotFoundError:
    _metadata_exports = ()


# Public Re-Exports
__all__ = ("ArgumentParser",) + _metadata_exports
