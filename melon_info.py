"""
melon_info.py - Prints out all the melons in our inventory

"""

from melons import melon_master

def print_melon(melon_master):
    keys = sorted(melon_master)
    for key in keys:
        if melon_master[key]['seedless']:
            print "%s are %s and cost $%0.2f." % (key, "seedless", melon_master[key]['price'])
        else:
            print "%s are %s and cost $%0.2f." % (key, "not seedless", melon_master[key]['price'])

if __name__ == "__main__":
    print_melon(melon_master)
