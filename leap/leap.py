"""exercism leap module."""

def leap_year(year):
  """
  Given a year, report if it is a leap year.

  :param year int - The year to check
  :return bool - Leap year or not.

  On every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400

  For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.
  """

  is_a_leap_year = False
  if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
      is_a_leap_year = True
    elif year % 100 == 0:
      is_a_leap_year = False
    else:
      is_a_leap_year = True

  return is_a_leap_year
