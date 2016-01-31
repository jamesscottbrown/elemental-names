library(ggplot2)
library(scales)

boys <- read.table("boy-names-elemental-counted", sep=" ", col.names=c('count', 'name'))
girls <- read.table("girl-names-elemental-counted", sep=" ", col.names=c('count', 'name'))

boys$sex = 'Male'
girls$sex = 'Female'

boys$freq = 1 / 1219
girls$freq = 1 / 4275

names <- rbind(boys, girls)


q <- ggplot(names, aes(x=count, fill=sex, weight=freq))

q + geom_histogram(position='dodge') +
labs(x = "Number of ways name can be spelt using chemical symbols", y = "Percentage of names", title="") +
scale_y_continuous(labels=percent, breaks=(1:14)*0.01)

ggsave("elemental-names.pdf")
ggsave("elemental-names.png")