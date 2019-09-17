# (a) Make a frequency distribution and histogram (using appropriate bins) for these 28 observations
# on the amount spent for dinner for four in downtown Chicago on Friday night. (b) Repeat
# the exercise, using a different number of bins. Which is preferred? Why?

obs <- c(95, 103, 109, 170, 114, 113, 107, 124, 105, 80, 104, 84, 176, 115, 69, 95, 134, 108, 61, 160, 128, 68, 95, 61, 150, 52, 87, 136)

table(obs)
prop.table(obs)
prop.table(table(obs))

data.frame(table(obs))
data.frame(prop.table(table(obs)))

hist(obs, breaks = seq(50, 200, 25))

hist(obs, breaks = seq(50, 200, 50))
