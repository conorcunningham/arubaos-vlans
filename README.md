# arubaos-vlans
Assign vlans to port on Arubaos switches

Very simply script with no promises. Used to assign vlans to ports. Designed to assign all VLANs to some ports, a surpisingly common thing to have to do on ArubaOS switches.

**Requires Python 3.6 or greator (f-strings)**

### VLANs
On your Aruba switch, display all VLANs
```
sh vlans

1       DEFAULT_VLAN                     | Port-based No    No   
2       OCEAN                            | Port-based No    No   
3       BIRDS                            | Port-based No    No   
4       FLOWERS                          | Port-based No    No    
```

Copy all the VLANs and assign the string to the variable `vlans`

```python
vlans = """
1       DEFAULT_VLAN                     | Port-based No    No   
2       OCEAN                            | Port-based No    No   
3       BIRDS                            | Port-based No    No   
4       FLOWERS                          | Port-based No    No    
"""
```

Define which ports on which you want the vlans tagged and untagged

```python
# put your tagged vlans here - string or int
tagged = ["trk105", 19, "trk100"]
# and your untagged vlans here - string or int
untagged = ["1", "7", 11, 12, "trk111"]
```
Now your good to go. Run the script 

`python3 aruba_vlans.py`

and you'll get ouput like this, ready to be pasted into your switch.
```
vlan 1
tagged trk105,19,trk100
untagged 1,7,11,12,trk111
vlan 2
tagged trk105,19,trk100
untagged 1,7,11,12,trk111
vlan 3
tagged trk105,19,trk100
untagged 1,7,11,12,trk111
vlan 4
tagged trk105,19,trk100
untagged 1,7,11,12,trk111
```
