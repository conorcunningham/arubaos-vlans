vlans = """
1       DEFAULT_VLAN                     | Port-based No    No   
2       OCEAN                            | Port-based No    No   
3       BIRDS                            | Port-based No    No   
4       FLOWERS                          | Port-based No    No    
"""

# put your tagged vlans here - string or int
tagged = ["trk105", 19, "trk100"]
# and your untagged vlans here - string or int
untagged = ["1", "7", 11, 12, "trk111"]

for vlan in vlans.split("\n"):
    tagged = [str(x) for x in tagged]
    untagged = [str(x) for x in untagged]

    if len(vlan) == 0 or vlan == "":
        continue

    print(f"vlan {vlan.split()[0]}")

    if len(tagged) > 0:
        print("tagged " + ",".join(tagged))
    if len(untagged) > 0:
        print("untagged " + ",".join(untagged))
