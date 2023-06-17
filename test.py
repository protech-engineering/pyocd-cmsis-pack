from pyocd.core.plugin import load_plugin_classes_of_type
from pyocd.target.pack.cmsis_pack import CmsisPack

PACKS = {}

load_plugin_classes_of_type("pyocd.pack", PACKS, CmsisPack)

for pack in PACKS.keys():
    print(pack)