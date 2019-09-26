library("jsonlite")
f1 <- fromJSON('http://ergast.com/api/f1/1957/results.json')
f1
str(f1)

dr <- f1$MRData$RaceTable$Races$Results[[1]]$Driver
colnames(dr)
dr[1:5, c('givenName', 'familyName', 'dateOfBirth', 'nationality')]
pwd