# Demo for creating wheel packages from CMSIS Packs

## How it works

The setup.py script looks in the `src/pack` folder for a `*.pack` file deployed in the same directory structure of the cmsis-pack-manager cache folder (i.e. `Keil/STM32F0xx_DFP/2.1.1.pack`).

From the path it extracts the 3 pack parameters: vendor, pack name and version. From these three it dynamically defines all the wheel package properties (package name, package version, etc.).

It then exposes a pyocd plugin entry `pyocd.pack` that refers to the only source file `pack.py`. This plugin finds the `*.pack` file and discovers the 3 pack parameters (in the same way as the setup.py) and in the load function returns a `CmsisPack` class preconfigured with the pack path, ready to be consumed by PyOCD.

The most important thing is that this source structure is totally independent (does not need to be changed) from the pack file itself, you only add a pack file, build, and the package is ready for uploading.

## Building

* Install runtime dependencies:

    ```
    $ pip install build cmsis-pack-manager
    ```

* List the available packs:

    ```
    $ python download.py --list
    ```

    And pick the name of the desired pack.

* Download the desired pack:

    ```
    $ python download.py -p Keil.STM32F0xx_DFP.2.1.1
    ```

* Build the package:

    ```
    $ python -m build
    ```

    The output `*.whl` package is in the dist folder.

## Testing

* Install the built package

    ```
    $ pip install dist/cmsis_pack_keil_stm32f0xx_dfp-2.1.1-py3-none-any.whl
    ```

* Run the test script

    ```
    $ python test.py
    ```

    It should list all the cmsis packs installed via pip (using the pyocd plugin interface).