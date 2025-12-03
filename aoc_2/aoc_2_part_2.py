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
  for val in range(range_start, range_end + 1):
    num_digits = len(str(val))
    if num_digits <= 1:
      continue

    num_partitions = 2
    found = False
    while(num_partitions <= num_digits):

      if(num_digits % num_partitions == 0): # the partition could only work if it splits the id evenly
          partition_start = 0
          partition_len = num_digits // num_partitions
          for i in range(num_partitions):
            if(i == 0): # on the first partition, just store the value
              first_partition_val = str(val)[partition_start:partition_start + partition_len]
              partition_start += partition_len
            elif(i == num_partitions - 1): # last partition
              curr_partition_val = str(val)[partition_start:partition_start + partition_len]
              if(first_partition_val != '' and first_partition_val == curr_partition_val):
                invalids.append(val)
                found = True
                break
            else: # intermediary partitions: break if current partition is not the same as the previous
                curr_partition_val = str(val)[partition_start:partition_start + partition_len]
                partition_start += partition_len
                if(first_partition_val != curr_partition_val):
                  break
      if found:
        break
      num_partitions += 1  

  return invalids


if __name__ == "__main__":
  main()