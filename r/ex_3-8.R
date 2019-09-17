# Make a frequency distribution and histogram for the 2007 annual compensation of
# 40 randomly chosen CEOs (millions of dollars).

obs <- c(5.33, 18.3, 24.55, 9.08, 12.22, 5.52, 2.01, 3.81, 192.92, 17.83, 23.77, 8.7, 11.15, 4.87, 1.72, 3.72, 66.08, 15.41, 22.59, 6.75, 9.97, 4.83, 1.29, 3.72, 28.09, 12.32, 19.55, 5.55, 9.19, 3.83, 0.79, 2.79, 34.91, 13.95, 20.77, 6.47, 9.63, 4.47, 1.01, 3.07)

table(obs)
prop.table(table(obs))

data.frame(table(obs))
data.frame(prop.table(table(obs)))

hist(obs, breaks = seq(0, 200, 10), ylim = c(0, 25))
hist(obs, breaks = seq(0, 200, 25), ylim = c(0, 40))
