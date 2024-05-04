def main():
  dollars = dollars_to_float(input("How much was the meal? "))
  percent = percent_to_float(input("What percentage would you like to tip? "))
  tip = dollars * percent
  print(f"Leave ${tip:.2f}") 


def dollars_to_float(d):
  """Converts a string with a dollar sign to a float.

  Args:
      d: A string representing a dollar amount (e.g., "$50.00").

  Returns:
      A float representing the dollar amount without the dollar sign.
  """
  return float(d[1:])


def percent_to_float(p):
  """Converts a string with a percentage sign to a float between 0 and 1.

  Args:
      p: A string representing a percentage (e.g., "15%").

  Returns:
      A float representing the percentage as a value between 0 and 1.
  """
  return float(p[:-1]) / 100

main()
