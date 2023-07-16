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
- attractors_<model_name>.tsv: contains the biological fixed point attractors that ecah model recovers.
- Exhaustive_models: This subfolder contains all plausible models for some ensemble ('EF','scEUF','scRoF','scNCF') as .pkl file format whenever the cardianlity of all plausible models is less than $10^6$,<br>
