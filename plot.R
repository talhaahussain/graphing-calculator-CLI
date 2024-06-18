args <- commandArgs(trailingOnly=TRUE)

if (length(args) != 2) {
    stop("ERROR - Incorrect number of arguments")
}

x = as.numeric(as.list(strsplit(gsub('^.|.$', '', args[1]), ", "))[[1]])

y = as.numeric(as.list(strsplit(gsub('^.|.$', '', args[2]), ", "))[[1]])

print(x)
print(y)
