import os

from build import ProjectBuilder
from cmsis_pack_manager import Cache, CmsisPackRef
from pathlib import Path


CMSIS_PACK_ENV = "CMSIS_PACK"


def get_package_name_from_pack(pack: CmsisPackRef):
    return f"pyocd_cmsis_pack.{pack.vendor}.{pack.pack}"


def get_packs_to_build(cache: Cache) -> list[CmsisPackRef]:
    # TODO: Replace with check against PyPI
    all_packs: list[CmsisPackRef] = cache.packs_for_devices(cache.index.values())
    packs_to_build: list[CmsisPackRef] = []

    for pack in all_packs:
        if get_package_name_from_pack(pack) in [
            "pyocd_cmsis_pack.Keil.STM32F1xx_DFP",
            "pyocd_cmsis_pack.Keil.STM32F0xx_DFP",
        ]:
            packs_to_build.append(pack)

    return packs_to_build


if __name__ == "__main__":
    srcdir = Path(__file__).parent
    outdir = srcdir / "dist"

    index = os.path.join(os.path.dirname(__file__), "src/pack")
    cache = Cache(False, False, json_path=index, data_path=index)

    cache.cache_descriptors()
    packs = get_packs_to_build(cache)
    cache.download_pack_list(packs)

    for pack in packs:
        os.environ[CMSIS_PACK_ENV] = pack.get_pack_name()

        builder = ProjectBuilder(srcdir)

        builder.build("sdist", outdir, {})
        builder.build("wheel", outdir, {})
