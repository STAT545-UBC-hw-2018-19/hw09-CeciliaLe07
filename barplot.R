words <- readLines("words.txt")
first_letter <- substring(words, 1, 1)
barplot_dat <- table(toupper(first_letter))
write.table(barplot_dat, "barplot_dat.tsv",
            sep = "\t", row.names = FALSE, quote = FALSE)

png(filename="barplot.png",width = 420, height = 420)
par(las=3)
barplot(barplot_dat,col=heat.colors(length(barplot_dat)+1),border="white")
dev.off()
