# Example_python_scripts
Example python scripts for working with bioinfomratic data

Print read lengths from a sequence file
```
# requires SeqIO
python read_lengths.py example.fasta fasta
```

Root a single tree
```
# requires ete3
python root_tree.py example_trees/example_tree_1.newick example_trees/example_tree_1_rooted.newick sampleA,sampleD
```
