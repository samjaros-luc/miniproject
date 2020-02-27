library(sleuth)
library(dplyr)

# Get the names of the sequences we're working with
seqNames = list.dirs("data", full.names, F, recursive=F)
print(seqNames)
print("results/"+seqNames)

# Show sleuth where kallisto results are stored
results = data.frame("sample"=c("SRR5660030.1","SRR5660033.1","SRR5660044.1","SRR5660045.1"), "condition"=c("2dpi","6dpi","2dpi","6dpi"), "path"=c("results/SRR5660030.1","results/SRR5660033.1","results/SRR5660044.1","results/SRR5660045.1"), stringsAsFactors=F)

# Create sleuth object
so = sleuth_prep(results)

# Perform differential expression analysis
so = sleuth_fit(so, ~condition, "full")
so = sleuth_fit(so, ~1, "reduced")
so = sleuth_lrt(so, "reduced", "full")

# Extract significant results
sleuthResults = sleuth_results(so, "reduced:full", "lrt", show_all=F)
sleuthSignificant = dplyr::filter(sleuthResults, qval <= 0.05) %>% dplyr::arrange(pval)
sleuthLog = dplyr::select(sleuthSignificant, target_id, test_stat, pval, qval)

# Write results to log
write.table(sleuthLog, file="miniProject.log", quote=F, append=T, row.names=F, sep="\t")
