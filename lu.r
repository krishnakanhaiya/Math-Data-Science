library(Matrix)
A <- matrix(c(1, 1, 1, 0, 1, -3, 2, 1, 5), 3, 3, byrow=T)
dim(A) <- c(3, 3)
expand(lu(A))