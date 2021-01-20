"""
Sort a list of string in alphabetical order
"""

a_file = open("sample.txt", "r")
mylist = [(line.strip()) for line in a_file].sort()
mylist.sort()
print("\n".join(mylist))
