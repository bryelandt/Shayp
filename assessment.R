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
fridays_pulses <- pulses[which(wday(CET) == 6)]
fridays_list <- unique(floor_date(fridays, unit = "day"))

# first visualization ----

onedaytime <- CET[which(floor_date(CET, unit = "day") == fridays_list[1])]
onedaypulses <- pulses[which(floor_date(CET, unit = "day") == fridays_list[1])]

plot(onedaytime,onedaypulses,'h')
title(fridays_list[1])
# sélection vdd 1-2am ----

fridays_night <- fridays[which(hour(fridays) >= 1 & hour(fridays) < 2)]
fridays_night_pulses <- fridays_pulses[which(hour(fridays) >= 1 & hour(fridays) < 2)]

plot(fridays_night,fridays_night_pulses,'h')

onedaytime <- fridays_night[which(floor_date(fridays_night, unit = "day") == fridays_list[10])]
onedaypulses <- fridays_night_pulses[which(floor_date(fridays_night, unit = "day") == fridays_list[10])]

plot(onedaytime,onedaypulses,'h')
title(fridays_list[1])













