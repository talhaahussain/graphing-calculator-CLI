args <- commandArgs(trailingOnly=TRUE)

if (length(args) != 2) {
    stop("ERROR - Incorrect number of arguments")
}

x = as.numeric(as.list(strsplit(gsub('^.|.$', '', args[1]), ", "))[[1]])
y = as.numeric(as.list(strsplit(gsub('^.|.$', '', args[2]), ", "))[[1]])

plot(x, y, type="l", col="red", main="Graph", xlab="x", ylab="y")
