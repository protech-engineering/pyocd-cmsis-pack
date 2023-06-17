from setuptools import setup
from pathlib import Path

packs = Path("src/pack").rglob("*.pack")

for pack in packs:
    PATH = pack.absolute()
    VENDOR = pack.parents[1].name
    PACK = pack.parents[0].name
    VERSION = pack.stem
    break

PN = f"{VENDOR.lower()}_{PACK.lower()}"
PKG = f"cmsis_pack_{PN}"

setup(
    name=PKG,
    version=VERSION,
    install_requires=[],
    packages=[PKG],
    package_dir={
        PKG: "src",
    },
    package_data={
        PKG: [f"pack/{VENDOR}/{PACK}/{VERSION}.pack"],
    },
    entry_points={
        "pyocd.pack": [f"{PN} = {PKG}.plugin:PackPlugin"],
    },
)
