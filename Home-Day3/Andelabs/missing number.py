# Program that comapares two lists and returns the missing index
def find_missing(lista,listb):
  # Statement that checks whether the lists are empty 
  if lista == [] and listb == []:
    return 0
  # Statement that checks whether the lists are equal to each other
  if len(lista) == len(listb):
    return 0
  # Staement that checks whether list a is greater
  if len(lista) > len(listb):
  # If true returns the missing numbers 
    pos = [item for item in lista if item not in listb]
    print pos
  # Staement that checks whether list b is greater
  if len(lista) < len(listb):
  # If true returns the missing numbers
    pos = [item for item in listb if item not in lista]
    print pos
