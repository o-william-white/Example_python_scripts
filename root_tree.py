
import sys
from ete3 import Tree

# run as
# root_tree.py input_tree output_tree outgroup1,outgroup2,etc

# input agruments
input_tree  = sys.argv[1]
output_tree = sys.argv[2]
outgroups   = sys.argv[3]

# read input tree
tree = Tree(open(input_tree, "r").read().rstrip("\n"))

# print info
print("Input tree:")
print(tree)
print()
print("Rooting on:")
print(outgroups)
print()

# split outgroups
outgroups = outgroups.split(",")

# find ancestor
ancestor = tree.get_common_ancestor(outgroups)

# check if ancestor is already the current root
# if not, root on ancestor
if tree == ancestor:
    print("MRCA of outgroups is the current root node")
else:
    print("Setting root")
    tree.set_outgroup(ancestor)
    print("Rooted tree:")
    print(tree)

# write outfile
print()
print("Writing output")
outfile = open(output_tree, "w")
outfile.write(tree.write())
outfile.close()


