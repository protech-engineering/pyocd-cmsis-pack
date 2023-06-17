from collections import namedtuple
from pathlib import Path

from pyocd.core.plugin import Plugin
from pyocd.target.pack.cmsis_pack import CmsisPack

Pack = namedtuple("Pack", ["vendor", "pack", "version"])


class PackPlugin(Plugin):
    def __init__(self) -> None:
        packs = Path(__file__).parent.rglob("*.pack")

        for pack in packs:
            self._path = pack.absolute()
            self._vendor = pack.parents[1].name
            self._pack = pack.parents[0].name
            self._version = pack.stem
            break

        super().__init__()

    def load(self):
        path = self._path

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
