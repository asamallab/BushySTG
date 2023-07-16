## Folder names (<model_name>) and their associated abbreviated form used in the manuscript
- buylla: RSCN-GRN
- sullivan: EMT-GRN
- cortical: NCD-GRN
- cardiac: EHD-GRN
- myeloid: MD-GRN
- t_cell: THC-GRN
- drug: EGFR-GRN
- emt_senescent: EMT-Senescence-GRN
- corrales: FOS-GRN
- gonadal: GSD-GRN
## Files and subfolders in the 10 folders
- edges_<model_name>.tsv: contains the edgelist of the network along with the signs of the edges (activatory: 'a' or inhibitory: 'i')
- attractors_<model_name>.tsv: contains the biological fixed point attractors that we impose as a constraint at each node.
- Exhaustive_models: This subfolder contains all plausible models that satisfy the fixed point constraint for some ensemble ('EF', 'scEUF', 'scRoF', 'scNCF') as .pkl file format whenever the cardianlity of all plausible models is less than $10^6$.
- 1e5_sampled_models: The folders 'gonadal' and 'corrales' contain this subfolder. This subfolder has 4 .pkl file containing $10^5$ sampled models of 4 ensembles respectively those satisfy the fixed point constraints.
- 1e6_sampled_models: This subfolders consists of $10^6$ sampled models as .pkl format when the number of plausible models satisfying the fixed point constraint for some ensemble is more than $10^6$ (except for 'gonadal' and 'corrales').
### Other subfolders in 'buylla' folder
- EF_bnet_models: contains the first $20$ models of sampled EF ensemble of RSCN-GRN ('buylla') in BoolNet (.bnet) file format.
- results: contains 'basin_props_data/EF/EF_basin_props_example.tsv'. The tsv file contains the values of G-density, average in-degree of non-GoE states and the average transient lengths of GoE states for the $20$ (.bnet) models of 'EF_bnet_models' subfolder.
