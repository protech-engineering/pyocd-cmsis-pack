# Demo for creating wheel packages from CMSIS Packs

A python package that automatically encapsulates a cmsis pack, with additional automation to do it for many packs at once.

## How it works

First we download the desired packs into the `src/pack` folder, using the CPM, by setting the index and data folder to that path.

The setup.py script receives via the `CMSIS_PACK` env variable the pack path (something like: `Keil/STM32F0xx_DFP/2.1.1.pack`) that we want to convert into a python package.

From the path it extracts the 3 pack parameters: vendor, pack name and version. From these three it dynamically defines all the wheel package properties (package name, package version, etc.).

It then exposes a pyocd plugin entry `pyocd.pack` that refers to the only source file `plugin.py`. This plugin uses the module name and metadata to find out the cmsis pack and its 3 parameters, and in the load function returns a `CmsisPack` class preconfigured with the pack path, ready to be consumed by PyOCD.

The most important thing is that this source structure is totally independent (does not need to be changed) from the pack file itself, you only add pack files, set the `CMSIS_PACK` env variable build, and the package is ready for uploading.

## Automation

An additional `make.py` script is provided.

This script will do the following:
* [x] Configure and refresh CPM cache in `src/pack` folder
* [x] Determine which packs need to be rebuilt (e.g. because of a new version appearing in the index). At the moment this is a stub. In the future it will check the PyPI and compare the version of the current packages, with the version of cmsis packs present in the index in order to determine which ones to build.
* [x] Download the selected cmsis packs
* [ ] Strip the cmsis packs (TBD)
* [x] Build the package
* [ ] Test the package?
* [ ] Upload the package to PyPI (TBD)

## Building

* Install runtime dependencies:

    ```
    $ pip install build wheel cmsis-pack-manager
    ```

* Run `make.py`
    ```
    $ python make.py
    ```

## Testing

* Install the test dependencies:
    ```
    $ pip install pyocd
    ```

* Install the built packages

    ```
    $ pip install dist/*.whl
    ```

* Run the test script

    ```
    $ python test.py
    ```

    It should list all the acquired new targets (using the pyocd plugin interface).