#!/usr/bin/env python

"""
Setup script for FALCON-formatter
"""

try:
	from setuptools import setup, Extension
except:
	from distutils.core import setup, Extension

setup(name = "FALCON_formatter",
	version = "0.1",
	author = "Greg Zynda",
	author_email="gzynda@tacc.utexas.edu",
	license="BSD-3",
	description="Bioinformatics tools",
	packages = ["FALCON_formatter"],
	scripts = ["bin/FALCON-formatter"])
	#test_suite="tests")
