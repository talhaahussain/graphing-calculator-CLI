args = commandArgs(trailingOnly=TRUE)

if (length(args) == 0) {
    stop("ERROR - Please supply arguments.")
}

print(args)
