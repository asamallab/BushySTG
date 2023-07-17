### Sampling_type_information
- This folder contains tsv files of the form <model_name>_samp_type_info.tsv. It provides the information regarding the number
  of inputs at each node and depending upon that and the type of ensemble what would be the sampling method for a node ('exact' or 'approx').
### model_statistics
- This folder contains tsv files of the form <model_name>_model_stats.tsv. It contains the number of plausible functions at each node that
  satisfy the fixed point constraints for each of the four classes of BFs (EFs, EUFs, RoFs, NCFs). For EUFs, RoFs, NCFs the sign-conforming conditions from the network strucutre were imposed. The nodes where the exact number of functions from some class
  could not be computed have been kept blank. The tsv files also provide the total number of plausible models for each ensemble and whether
  models have been sampled or taken exhaustively for the analyses.
### model_all_info
- This folder contains tsv files of the form <model_name>_all_details.tsv. The tsv file contains all the information present in
  <model_name>_model_stats.tsv along with the name of the nodes and their in-degrees.
