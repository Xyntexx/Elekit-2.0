import sys

from JLC2KiCad_lib.JLC2KiCadLib import JLC2KiCadLib

# This is the list of the parts that you want to add to the library
component_list = [
    "C2765186",  # USB Type-C Connector
    "C2934560",  # ESP32-C3-WROOM-02-N4
    "C318884",  # NO Push Button
    "C964833",  # 2032 Coin Cell Battery Holder
    "C5947",  # 74HC595D 8-Bit Shift Register

]

argumets = "-dir ./ -schematic_lib 0_JLCPCB_Symbols -footprint_lib 0_JLCPCB_Footprints" \
    .split(" ")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.argv = ["JLC2KiCadLib", *component_list, *argumets]
    JLC2KiCadLib.main()
