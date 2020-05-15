# coding: utf-8
"""
Treelite: a model compiler for decision tree ensembles
"""
import os

from .core import DMatrix
from .frontend import Model, ModelBuilder
from .annotator import Annotator
from .contrib import create_shared, generate_makefile

VERSION_FILE = os.path.join(os.path.dirname(__file__), 'VERSION')
with open(VERSION_FILE, 'r') as _f:
    __version__ = _f.read().strip()

__all__ = ['DMatrix', 'Model', 'ModelBuilder', 'Annotator', 'create_shared', 'generate_makefile',
           'gallery']