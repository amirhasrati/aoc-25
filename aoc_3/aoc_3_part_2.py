# batteries labeled with joltage rating (1-9)
# each line of input is a bank
# turn on exactly two batteries in each bank
# maximize the joltage: if bank = 61115 --> pick 6 and 5 (forms 65 as bank joltage)
# cannot rearrange numbers
# give total joltage output (as the sum of each banks joltage)
from typing import List
import time

def run_program():
  main()



def main():
  joltage_ratings: List[str] = open("joltage_ratings.txt").read().splitlines()
  optimized_joltage_outputs: List[int] = []

  for bank_joltage_rating in joltage_ratings:
    optimized_joltage_outputs.append(max_bank_joltage(bank_joltage_rating, 12))
    
  total_joltage = sum(optimized_joltage_outputs)
  print(total_joltage)

def max_bank_joltage(bank_joltage_rating: str, num_batteries: int) -> int:
  start = 0
  end = len(bank_joltage_rating) - (num_batteries - 1)
  joltage_out = "" # we build this string, battery by battery
  
  while(num_batteries > 0):
    biggest_seen = "0"
    for i in range(start, end):
      if(bank_joltage_rating[i] > biggest_seen):
        biggest_seen = bank_joltage_rating[i]
        start = i + 1
  
    joltage_out += biggest_seen
    end += 1
    num_batteries -= 1

  return int(joltage_out)

if __name__ == "__main__":
  times = []

  for _ in range(50):
    start = time.perf_counter()
    run_program()
    end = time.perf_counter()
    times.append((end - start) * 1000)  # convert to ms

  print(f"Average time: {sum(times)/len(times):.3f} ms")
  print(f"Fastest: {min(times):.3f} ms")
  print(f"Slowest: {max(times):.3f} ms")