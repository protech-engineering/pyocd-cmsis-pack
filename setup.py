from setuptools import setup
from pathlib import Path

# Find the pack file
packs = Path("src/pack").rglob("*.pack")

# Extract 3 pack parameters (vendor, pack and version)
for pack in packs:
    PATH = pack.absolute()
    VENDOR = pack.parents[1].name
    PACK = pack.parents[0].name
    VERSION = pack.stem
    break

# CMSIS Pack name (formatted a bit)
PN = f"{VENDOR.lower()}_{PACK.lower()}"
# python package name
PKG = f"cmsis_pack_{PN}"

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
