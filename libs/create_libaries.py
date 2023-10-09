import sys

from JLC2KiCad_lib.JLC2KiCadLib import JLC2KiCadLib

# This is the list of the parts that you want to add to the library

argumets = "-dir ./ -symbol_lib 0_JLCPCB_Symbols -footprint_lib 0_JLCPCB_Footprints" \
    .split(" ")  # --skip_existing

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Ask user which parts to add to the library
    print("Which parts do you want to add to the library?")
    print("Enter the part number and press enter. When you are done, press enter again.")
    component_list = []
    while True:
        part = input("JLCPCB part number: ")
        part = part.strip()  # remove whitespace
        if part == "":
            break
            # check if part already in list
        if part in component_list:
            print("Part already in list. Please try again.")
            continue
        # check if part is valid JLCPCB part number format (C13453)
        if part[0] == "C" and part[1:].isdigit():
            component_list.append(part)
        else:
            print("Invalid part number format. Please try again.")

    # Check if user entered any parts
    if len(component_list) == 0:
        print("No parts entered. Exiting...")
        sys.exit()
    sys.argv = ["JLC2KiCadLib", *component_list, *argumets]
    JLC2KiCadLib.main()
