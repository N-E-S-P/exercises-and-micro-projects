# (a) Make a stem-and-leaf plot for these 24 observations on the number of customers who
# used a downtown CitiBank ATM during the noon hour on 24 consecutive workdays.
# (b) Make a dot plot of the ATM data.

obs = c(39, 32, 21, 26, 19, 27, 32, 25, 18, 26, 34, 18, 31, 35, 21, 33, 33, 9, 16, 32, 35, 42, 15, 24)

obs

table(obs)
data.frame(table(obs))

sort(obs)

stem(obs)

dotchart(obs, labels = 1:24, cex = .6)

