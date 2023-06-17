from pathlib import Path

from pyocd.core.plugin import Plugin
from pyocd.target.pack.cmsis_pack import CmsisPack


class PackPlugin(Plugin):
    def __init__(self) -> None:
        # Find the pack file
        packs = Path(__file__).parent.rglob("*.pack")

        # Extract the 3 pack parameters (vendor, pack, version)
        for pack in packs:
            self._path = pack.absolute()
            self._vendor = pack.parents[1].name
            self._pack = pack.parents[0].name
            self._version = pack.stem
            break

        super().__init__()

    def load(self):
        path = self._path

        # Create class where pack path is already defined
        class FixedCmsisPack(CmsisPack):
            def __init__(self) -> None:
                super().__init__(path)

        return FixedCmsisPack

    @property
    def name(self):
        return f"{self._vendor.lower()}_{self._pack.lower()}"

    @property
    def description(self):
        return f"{self._vendor} {self._pack} CMSIS Pack"

    @property
    def version(self):
        return self._version
