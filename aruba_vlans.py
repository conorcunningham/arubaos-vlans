# Below is the program's configuration

# paste your VLAN output in betweek the """
VLANS = """
1       DEFAULT_VLAN                     | Port-based No    No
2       OCEAN                            | Port-based No    No
3       BIRDS                            | Port-based No    No
4       FLOWERS                          | Port-based No    No
"""

# put your tagged vlans here - string or int
TAGGED = ["trk105", 19, "trk100"]
# and your untagged vlans here - string or int
UNTAGGED = ["1", "7", 11, 12, "trk111"]

# this is the filename to which the vlan config
# will be output
OUTPUT_FILE = "vlans.txt"

# Do you want to also print the config
# if yes, set this to True
# if you do not want to print to cli,
# set this to False
PRINT_TO_CLI = True


def main():
    """
    Open the define file for writing
    And process the vlans from the switch
    :return: None
    """

    with open(OUTPUT_FILE, "w") as file:
        process_vlans(file)


def process_vlans(handler):
    """
    Parse the vlan config and output switch config
    which is required to assign the various ports
    to the desired vlans

    :param handler: The writing file handler
    :return: None
    """

    for vlan in VLANS.split("\n"):
        tagged = [str(x) for x in TAGGED]
        untagged = [str(x) for x in UNTAGGED]

        if len(vlan) == 0 or vlan == "":
            continue

        # this outputs the root vlan config line
        # e.g., vlan 20
        output(f"vlan {vlan.split()[0]}", handler)

        # here we ouput the interfaces which will
        # access/tag the vlan
        if len(tagged) > 0:
            output("  tagged " + ",".join(tagged), handler)
        if len(untagged) > 0:
            output("  untagged " + ",".join(untagged), handler)


def output(text, handler, printf=PRINT_TO_CLI):
    """
    Helper method which
    """
    handler.write(text + "\n")
    if printf:
        print(text)


if __name__ == "__main__":
    main()
