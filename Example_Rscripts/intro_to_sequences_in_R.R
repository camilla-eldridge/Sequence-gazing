library(ape)
library(pegas)
library(phangorn)

alignment<-read.dna("example.fasta", format = "fasta")
metadata<-read.csv("example_metadata.csv", header = TRUE)

group1_ids <- subset(metadata, Group == "1")

model_test<-modelTest(phyDat(alignment), G=TRUE, I=TRUE, model="all")
best_fit_model <- as.pml(model_test)

dist_matrix <- dist.dna(alignment, model = "F81", as.matrix = TRUE)
NJ_tree<-nj(dist_matrix)
plot(NJ_tree)

extracted_sequences <- alignment[rownames(alignment) %in% group1_ids$Accession,]
write.dna(extracted_sequences, file = "group1.fasta", format = "fasta", colsep = "", colw = 60, nbcol=1)
