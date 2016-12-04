class BinarySearch(the_list):
  __init__(a,b):
    length = len(the_list)
    minimum = 0
    maximum = len(the_list) - 1
    return length

def search(index):
    while minimun < maximum:
        median = (minimum + maximum)//2
        if index == the_list[median]:
        x = {index}
        return x
      elif index < the_list[median]:
        for index in range(minimum:median):
          index -= b
          x = {count, index}
          return x
      elif index > the_list[median]:
        for index in range(median:maximum):
          index += b
          x = {count, index}
          return x
      else:
        return index, 'not found'
