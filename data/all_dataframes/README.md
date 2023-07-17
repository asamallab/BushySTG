### bio_basinprops_main_models.tsv
- contains all data ($G$-density, $\langle d_{in} \rangle_{non-GoE}$, $\mathcal{T}_{GoE}$, $\overline{Z} _{max}$, $\overline{Z} _{min}$, $\overline{Z} _{ave}$, $\overline{Z} _{mid}$ and $\overline{s}$) of the models provided by the modelers for 4 GRNs. The GRNs are 1. RSCN-GRN 
 ('buylla'), 2. EMT-GRN ('sullivan'), 3. NCD-GRN ('cortical') and 4. EHD-GRN ('cardiac').
### bio_basinprops_SI_models.tsv
- contains all data ($G$-density, $\langle d_{in} \rangle_{non-GoE}$, $\mathcal{T}_{GoE}$, $\overline{Z} _{max}$, $\overline{Z} _{min}$, $\overline{Z} _{ave}$, $\overline{Z} _{mid}$ and $\overline{s}$) of the models provided by the modelers for 6 GRNs. The GRNs are 1. MD-GRN 
 ('myeloid'), 2. THC-GRN ('t_cell'), 3. EGFR-GRN ('drug'), 4. EMT-Senescence-GRN ('emt_senescent'), 5. FOS-GRN ('corrales') and 6. GSD-GRN ('gonadal').
### \<model_name\>_buylla_basin_props_plot_df.tsv
- tsv file with this nomenclature contains all data ($G$-density, $\langle d_{in} \rangle_{non-GoE}$, $\mathcal{T}_{GoE}$, $\overline{Z} _{max}$, $\overline{Z} _{min}$, $\overline{Z} _{ave}$, $\overline{Z} _{mid}$ and $\overline{s}$) of all the sampled or exhaustively considered models for all four ensembles of some GRN (indicated by model name).
- For an example the data for RSCN-GRN has been provided as a zip file ('buylla_basin_props_plot_df.tsv.zip'). Extracting this the required tsv file for the GRN, RSCN-GRN ('buylla_basin_props_plot_df.tsv') can be obtained. Similar tsv file can be generated for remaining 9 GRNs using the codes given in this repository except cardiac and t_cell for which certain input nodes are required to be kept fixed.
