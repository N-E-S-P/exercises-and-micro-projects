# The table shows raw scores on a state civil service exam taken by 24 applicants for positions in
# law enforcement. Construct a frequency distribution and histogram, using nice (round) bin limits.

obs <- c(83, 93, 74, 98, 85, 82, 79, 78, 82, 68, 67, 82, 78, 83, 70, 99, 18, 96, 93, 62, 64, 93, 27, 58)

table(obs)
prop.table(obs)
prop.table(table(obs))

data.frame(table(obs))
data.frame(prop.table(table(obs)))

hist(obs)           
hist(obs, main = "Histogram of scores", xlab = "Scores", ylab = "N. of applicants", breaks = seq(0, 100, 10))
