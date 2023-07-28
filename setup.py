from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in jscustom/__init__.py
from jscustom import __version__ as version

setup(
	name="jscustom",
	version=version,
	description="custom codes used by justsigns",
	author="manoj",
	author_email="manoj@mith.tech",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
