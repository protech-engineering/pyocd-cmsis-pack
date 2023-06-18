import os

from setuptools import setup
from pathlib import Path

CMSIS_PACK_ENV = "CMSIS_PACK"
CMSIS_PACK_PATH = os.environ.get(CMSIS_PACK_ENV, None)

if not CMSIS_PACK_PATH:
    raise Exception()

CMSIS_PACK = Path(CMSIS_PACK_PATH)

# Extract 3 pack parameters (vendor, pack and version)
PATH = CMSIS_PACK.absolute()
VENDOR = CMSIS_PACK.parents[1].name
PACK = CMSIS_PACK.parents[0].name
VERSION = CMSIS_PACK.stem

# CMSIS Pack name (formatted a bit)
PN = f"{VENDOR}.{PACK}"
# python package name
PKG = f"pyocd_cmsis_pack.{PN}"

setup(
    name=PKG,
    version=VERSION,
    install_requires=[],
    packages=[PKG],
    package_dir={
        PKG: "src",
    },
    # Include the pack file
    package_data={
        PKG: [f"pack/{VENDOR}/{PACK}/{VERSION}.pack"],
    },
    # Add a PyOCD plugin entry point
    entry_points={
        "pyocd.pack": [f"{PN} = {PKG}.plugin:PackPlugin"],
    },
)
