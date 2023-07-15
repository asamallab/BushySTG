### NCF_perms
-  each file in this folder contains a list of NCFs for a given number of inputs, the signs of which are activatory
### RoF_perms
-  each file in this folder contains a list of RoFs for a given number of inputs, the signs of which are activatory
### UF_perms
-  each file in this folder contains a list of UFs for a given number of inputs, the signs of which are activatory
### RoF_catalog
This folder contains 10 files labeled RoF_cat_XX.tsv, where X takes values 0 to 9. 'XX' refers to the number of input variables (*k*) of the RoF. Each file contains the representative RoFs and their properties such as:
- decimal_rep: integer encoding of the RoF
- bias: Hamming weight of the RoF
- avg_sensitivity: average sensitivity
- CF: whether the RoF is canalyzing
- NCF: whether the RoF is nested canalyzing
- cana_depth: canalyzing depth of the RoF
- expressions: the Boolean expression of the RoF
- isomorphisms: all permutations and negations of the inputs of the RoF
