### unique_perm_k
- There are 8 folders (for k = {1,2,...,8}) . Each of the folders contains four files with names \<ensemble\>_unique_perm.tsv. These files
  provide the number of non-equivalent pemutations ('No_of_unique_perms' in the file) for all or sampled BFs depending on the values of k
  and the type of functions.
### bio_2650_unique_perm_dataframe.tsv
- This dataset contains the number of non-equivalent(unique) permutations of the functions compiled from discrete models in published literature. We have sub-selected the functions with less or equal to 8-inputs from the [biological dataset](https://github.com/asamallab/MCBF/blob/main/biological_dataset/Reference_biological_dataset.tsv) for the comparison.
- It also contains the number of inputs to the function, total number of possible permutations and the fraction of non-equivalent
permutations over total number of possible permutations.
### avg_unique_perm.pdf
- the plot of average fraction of non-equivalent permutation with the number of inputs for the four classes of functions (EF, EUF, RoF and NCF) and for the functions provided in 'bio_2650_unique_perm_dataframe.tsv'. See the 'Bushiness_python_codes_for_plots.ipynb' file in the 'codes' folder for the code to generate this file.

## CITATION
P. Sil#, A. Subbaroyan#, Saumitra Kulkarni, O. C. Martin* and A. Samal*. Biologically meaningful regulatory logic enhances the convergence rate in Boolean networks and bushiness of their state transition graph.
