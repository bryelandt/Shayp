function(pulses) {
  
  p <- 1
  
  while (p <= length(pulses)) { # loop that check pulses one to one
    
    print(p)
    
    first_peak <- 0
    second_peak <- 0
    
    if (pulses[p] >= 2){ # detect first peak
      
      if (pulses[p + 1] < 2){ # if the peak is finished
        
        first_peak <- p
        cat(' first peak detected at: ',p, '\n')
        
      }
    }
    
    if (first_peak != 0 & first_peak + 10 < length(pulses)) { # detect second peak
      
      i <- 6
      while (i <= 10) { # 36-60 minutes after first peak
        
        if (pulses[first_peak + i] >= 2) { # second peak found
          
          second_peak <- p + i
          cat('second peak detected at: ',second_peak,'\n')
          i = i+10
          
        }else {
          
          i = i + 1
          
        }
      }
    }
        
    if (second_peak != 0) { # check continuous consumption
      
      no_pulse <- 0 # sometimes not pulse during regeneration

      for (j in (first_peak : second_peak)) {
        
        if (pulses[j] == 0) {
          
          cat('pulse en ',j,'equals',pulses[j],'\n')
          no_pulse = no_pulse + 1
          
        }
      }
      if (no_pulse < 3) {
        
        return(TRUE)
        
      }else{
        
        p = second_peak
        cat('p set to: ',p)
        
      }
      
    } # else -> next pulse
    
    p = p + 1
  }
  
  return(FALSE)
  
}