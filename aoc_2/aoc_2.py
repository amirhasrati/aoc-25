from typing import  List

def main():
  # Create a list of id ranges
  id_ranges: List[str] = open("id_ranges.txt").read().split(',')
  # List for invalid ids
  invalids: List[int] = []

  for range in id_ranges:
    # Split into start and end ranges
    split_range = range.split('-')
    range_start = int(split_range[0])
    range_end = int(split_range[1])

    invalids.extend(get_invalids(range_start, range_end)) 

  sum_invalids = sum(invalids)
  print(sum_invalids)

def get_invalids(range_start: int, range_end: int):
  invalids: List[int] = [] 
  for id in range(range_start, range_end + 1):
    num_digits = len(str(id))
    if num_digits % 2 == 0: # if the number of digits is odd then it must be valid
      part_1 = str(id)[:int(num_digits / 2)]
      part_2 = str(id)[int(num_digits / 2):]
      if part_1 == part_2:
        invalids.append(id)
  
  return invalids


if __name__ == "__main__":
  main()