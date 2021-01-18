def leap_year(year):
  """Is a give year a leap year???"""
  if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
      return True
    elif year % 100 == 0:
      return False

    return True
    
  return False
