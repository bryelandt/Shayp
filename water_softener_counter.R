function(time,pulses) {
  
  # This function calculate if a water softener has been used
  # return TRUE if water softener detected (and then stop)
  # return FALSE if no water softener is detected
  
  p <- 1
  res <- data.frame("First peak" = time[1],"Second peak"= time[1])
  
  while (p <= length(pulses)) { # loop that check pulses one to one
    
    first_peak <- 0
    second_peak <- 0
    
    if (pulses[p] >= 2){ # detect first peak
      
      if (pulses[p + 1] < 2){ # if the peak is finished
        
        first_peak <- p

      }
    }
    
    if (first_peak != 0 & first_peak + 10 < length(pulses)) { # detect second peak
      
      i <- 6
      while (i <= 10) { # 36-60 minutes after first peak
        
        if (pulses[first_peak + i] >= 2) { # second peak found
          
          second_peak <- p + i
          i = i+10
          
        }else {
          
          i = i + 1
          
        }
      }
    }
    
    if (second_peak != 0) { # check continuous consumption
      
      no_pulse <- 0 # sometimes not pulse during regeneration
      
      for (j in seq(from = first_peak+1, to = second_peak-1)) {
        
        if (pulses[j] == 0 | pulses[j] > 1) {
          
          no_pulse = no_pulse + 1
          
        }
      }
      if (no_pulse < 3) {
        
        res <- rbind(res,list(time[first_peak],time[second_peak]))
        #print(time[first_peak])
        
      }else{
        
        p = second_peak
        
      }
      
    } # else -> next pulse
    
    p = p + 1
  }
  
  res <- res[-1,]
  return(res)
  
}