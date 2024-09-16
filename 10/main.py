
def overlapping(a,b):
    for item1 in a:
        for item2 in b:
            if item1 == item2:
                return True
    return False

x = overlapping(['a','b'], ['c','d'])
if x == True:
    print("True! They overlap!")
else:
    print("False! They don't overlap")



