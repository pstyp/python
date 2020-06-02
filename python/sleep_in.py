def sleep_in(weekday, vacation):
    if weekday==False and vacation==False:
        return True
    elif weekday==True and vacation==False:
        return False
    elif weekday==False and vacation==True:
        return True
    if weekday==False and vacation==False:
        return True
    elif weekday==True and vacation==False:
        return False
    elif weekday==True and vacation==True:
        return True


#def sleep_in(weekday, vacation):
 # if not weekday or vacation:
 #   return True
  # else:
  #  return False
  # This can be shortened to: return(not weekday or vacation)
