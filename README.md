# Example_python_scripts
Example python scripts for working with bioinformatic data

Print read lengths from a sequence file
```
# requires SeqIO
# python read_lengths.py input_file format
python read_lengths.py example.fasta fasta
```

Root a tree on a single sample or most recent ancestor of multiple samples
```
# requires ete3
# python root_tree.py input_tree output_tree outgroup1,outgroup2,etc
python root_tree.py example_trees/example_tree_1.newick example_trees/example_tree_1_rooted.newick sampleA
python root_tree.py example_trees/example_tree_1.newick example_trees/example_tree_1_rooted.newick sampleA,sampleD
```


Root multiple trees on a single sample or most recent ancestor of multiple samples
```
# requires ete3
# python root_multiple_trees.py input_file output_file outgroup1,outgroup2,etc
python root_multiple_trees.py example_trees example_trees_rooted sampleF
python root_multiple_trees.py example_trees example_trees_rooted sampleF,sampleC
```
