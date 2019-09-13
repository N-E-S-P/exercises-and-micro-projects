# The table shows the number of days on the market for the 36 recent home sales in the city of
# Sonando Hills. Construct a frequency distribution and histogram, using nice (round) bin limits.

obs <- c(18, 70, 52, 17, 86, 121, 86, 3, 66, 96, 41, 50, 176, 26, 28, 6, 55, 21, 43, 20, 56, 71, 57, 16, 20, 30, 31, 44, 44, 92, 179, 80, 98, 44, 66, 15)

table(obs)
prop.table(table(obs))

data.frame(table(obs))
data.frame(prop.table(table(obs)))

hist(obs, main = "Histogram of number of days for home sales", xlab = "Number of days", breaks = seq(0, 200, 25))
