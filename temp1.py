def extract_initials(input_list):
  """THIS FUNCTION TAKES LIST OF NAMES AND RETURNS INITIALS
  FOR EMAPLE 
  INPUT_LIST = ["Chethan", "Chethan Bekal","Chethan Yeshwanth Bekal"]
  output_list= ["C", "CB", "CYB"]
  """
  return("".join([part[0].upper() for part in input_list.split()]) for name in input_list]

extract_initials(["Chethan", "Chethan Bekal","Chethan Yeshwanth Bekal"])