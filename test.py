from pyocd.core.plugin import load_plugin_classes_of_type
from pyocd.target.pack.cmsis_pack import CmsisPack

PACKS = {}

load_plugin_classes_of_type("pyocd.pack", PACKS, CmsisPack)

print("Available targets: ")

for key, pack in PACKS.items():
    instance: CmsisPack = pack()

    for device in instance.devices:
        print(f"    {device.part_number}")