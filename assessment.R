setwd('~/Documents/Projects/Shayp/')

library("lubridate")
library("magrittr")

Data <- read.csv('export_20190301_3A9B9D.csv')

# pulse = 10l
# time UTC
 
# convert UTC time to CET time
# trouver les vdd
# compter les occurences de water softener
# proposer autres solutions de comptage
 
UTC <- Data$timestamp
pulses <- Data$pulses
 
UTC <- ymd_hm(UTC) # convert strings to dates

CET <- UTC + dhours(1)

fridays <- CET[which(wday(CET) == 6)]
fridays_list <- unique(floor_date(fridays, unit = "day"))

onedaytime <- CET[which(floor_date(CET, unit = "day") == fridays_list[1])]
onedaypulses <- pulses[which(floor_date(CET, unit = "day") == fridays_list[1])]

plot(onedaytime,onedaypulses,'h')
title(fridays_list[1])
