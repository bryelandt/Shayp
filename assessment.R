setwd('~/Documents/Projects/Shayp/')

library("lubridate")
library("magrittr")
find_water_softener <- dget('find_water_softener.R') # algo de détection
water_softener_counter <- dget('water_softener_counter.R') # algo de détection modifié

Data <- read.csv('export_20190301_3A9B9D.csv')

# pulse = 10l
# time UTC
 
UTC <- Data$timestamp
pulses <- Data$pulses
 
UTC <- ymd_hm(UTC) # convert strings to dates

CET <- with_tz(UTC, "CET")

fridays <- CET[which(wday(CET) == 6)]
fridays_pulses <- pulses[which(wday(CET) == 6)]
fridays_list <- unique(floor_date(fridays, unit = "day"))

# first visualization ----

onedaytime <- CET[which(floor_date(CET, unit = "day") == fridays_list[1])]
onedaypulses <- pulses[which(floor_date(CET, unit = "day") == fridays_list[1])]

plot(onedaytime,onedaypulses,'h',main = fridays_list[1], xlab = NA, ylab = 'Pulses') 

day_selected <- ymd("2019-03-25")
day_2 <- ymd("2019-03-31")
time_selected <- CET[which(floor_date(CET, unit = "day") >= day_selected 
                           & floor_date(CET, unit = "day") < day_2)]
pulses_selected <- pulses[which(floor_date(CET, unit = "day") >= day_selected 
                                & floor_date(CET, unit = "day") < day_2)]

plot(time_selected,pulses_selected,'h',main = "25/03 - 31/03/2019", xlab = NA, ylab = 'Pulses')

# sélection vdd 1-2am ----

fridays_night <- fridays[which(hour(fridays) >= 1 & hour(fridays) < 5)]
fridays_night_pulses <- fridays_pulses[which(hour(fridays) >= 1 & hour(fridays) < 5)]

plot(fridays_night,fridays_night_pulses,'h',main = "Fridays night", xlab = NA, ylab = 'Pulses')

water_softener_on <- vector(length = length(fridays_list))

for (i in (1:length(fridays_list))) { 
  
  onedaytime <- fridays_night[which(floor_date(fridays_night, unit = "day") == fridays_list[i])]
  onedaypulses <- fridays_night_pulses[which(floor_date(fridays_night, unit = "day") == fridays_list[i])]
  
  # count occurences ----
  water_softener_on[i] <- find_water_softener(onedaypulses) # check if the water softener is used
  
  
  plot(onedaytime,onedaypulses,'h',main = fridays_list[i], xlab = NA, ylab = 'Pulses')
  mtext(paste('water softener on?',water_softener_on[i]),side = 3)
}

cat('Number of occurences: ',sum(water_softener_on))

# detection with all the data ----

water_softener <- water_softener_counter(CET,pulses)

