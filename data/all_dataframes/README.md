### bio_basinprops_main_models.tsv
- contains all data ($G$-density, $\langle d_{in} \rangle_{non-GoE}$, $\mathcal{T}_{GoE}$, $\overline{Z} _{max}$, $\overline{Z} _{min}$, $\overline{Z} _{ave}$, $\overline{Z} _{mid}$ and $\overline{s}$) of the models provided by the modelers for 4 GRNs. The GRNs are a. RSCN-GRN ('buylla'), b. EMT-GRN ('sullivan'), c. NCD-GRN ('cortical') and d. EHD-GRN ('cardiac').
### bio_basinprops_SI_models.tsv
- contains all data ($G$-density, $\langle d_{in} \rangle_{non-GoE}$, $\mathcal{T}_{GoE}$, $\overline{Z} _{max}$, $\overline{Z} _{min}$, $\overline{Z} _{ave}$, $\overline{Z} _{mid}$ and $\overline{s}$) of the models provided by the modelers for 6 GRNs. The GRNs are a. MD-GRN 
 ('myeloid'), b. THC-GRN ('t_cell'), c. EGFR-GRN ('drug'), d. EMT-Senescence-GRN ('emt_senescent'), e. FOS-GRN ('corrales') and f. GSD-GRN ('gonadal').
### \<model_name\>_buylla_basin_props_plot_df.tsv
- tsv file with this nomenclature contains all data ($G$-density, $\langle d_{in} \rangle_{non-GoE}$, $\mathcal{T}_{GoE}$, $\overline{Z} _{max}$, $\overline{Z} _{min}$, $\overline{Z} _{ave}$, $\overline{Z} _{mid}$ and $\overline{s}$) of all the sampled or exhaustively considered models for all four ensembles of some GRN (indicated by model name).
- For an example the data for RSCN-GRN has been provided as a zip file ('buylla_basin_props_plot_df.tsv.zip'). Extracting this the required tsv file for the GRN, RSCN-GRN ('buylla_basin_props_plot_df.tsv') can be obtained. Similar tsv file can be generated for remaining 9 GRNs using the codes given in this repository except cardiac and t_cell for which certain input nodes are required to be kept fixed.

## CITATION
P. Sil#, A. Subbaroyan#, Saumitra Kulkarni, O. C. Martin* and A. Samal*. Biologically meaningful regulatory logic enhances the convergence rate in Boolean networks and bushiness of their state transition graph.
