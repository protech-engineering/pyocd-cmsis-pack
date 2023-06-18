import importlib_metadata
from pathlib import Path

from pyocd.core.plugin import Plugin
from pyocd.target.pack.cmsis_pack import CmsisPack


class PackPlugin(Plugin):
    def __init__(self) -> None:
        # Module is pyocd_cmsis_pack.[vendor].[pack].plugin
        module = __name__.split(".")
        # Distribution name is pyocd_cmsis_pack.[vendor].[pack]
        distribution_name = ".".join(__name__.split(".")[:-1])

        self._vendor = module[1]
        self._pack = module[2]
        self._version = importlib_metadata.version(distribution_name)
        self._path = (
            Path(__file__).parent
            / "pack"
            / self._vendor
            / self._pack
            / f"{self._version}.pack"
        )

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
        return f"{self._vendor}.{self._pack}"

    @property
    def description(self):
        return f"{self._vendor} {self._pack} CMSIS Pack"

    @property
    def version(self):
        return self._version
