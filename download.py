import os
import argparse

from cmsis_pack_manager import Cache, CmsisPackRef

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--pack")
parser.add_argument("-l", "--list", action="store_true")

args = parser.parse_args()

index = os.path.join(os.path.dirname(__file__), "src/pack")
cache = Cache(False, False, json_path=index, data_path=index)

# cache.cache_clean()
cache.cache_descriptors()

packs: CmsisPackRef = cache.packs_for_devices(cache.index.values())  # type: ignore

if args.list:  # type: ignore
    print("Available packs for download:")

    for pack in packs:
        print(pack)
elif args.pack:
    for pack in packs:
        if str(pack) == args.pack:
            print(f"Downloading pack: {pack}")
            cache.download_pack_list([pack])

            print("To create the *.whl package (in the dist folder) run:")
            print(" $ python -m build")
            break
else:
    print("Must specify --list or --pack")
