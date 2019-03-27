# (a) Make a frequency distribution and histogram for the monthly off-campus rent paid by
# 30 students. (b) Repeat the exercise, using a different number of bins. Which is preferred? Why?

obs <- c(730, 730, 730, 930, 700, 570, 690, 1030, 740, 620, 720, 670, 560, 740, 650, 660, 850, 930, 600, 620, 760, 690, 710, 500, 730, 800, 820, 840, 720, 700)

table(obs)
prop.table(obs)
prop.table(table(obs))

data.frame(table(obs))
data.frame(prop.table(table(obs)))

hist(obs)
hist(obs, breaks = seq(500, 1050, 50))
