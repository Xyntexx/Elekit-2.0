import sys

from JLC2KiCad_lib.JLC2KiCadLib import JLC2KiCadLib

# This is the list of the parts that you want to add to the library
component_list = [

    "C13453",  # Straight USB Mini-B Connector




]

argumets = "-dir ./ -schematic_lib 0_JLCPCB_Symbols -footprint_lib 0_JLCPCB_Footprints --skip_existing" \
    .split(" ")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.argv = ["JLC2KiCadLib", *component_list
        , *argumets]
    JLC2KiCadLib.main()
