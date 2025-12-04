# batteries labeled with joltage rating (1-9)
# each line of input is a bank
# turn on exactly two batteries in each bank
# maximize the joltage: if bank = 61115 --> pick 6 and 5 (forms 65 as bank joltage)
# cannot rearrange numbers
# give total joltage output (as the sum of each banks joltage)
from typing import List

def main():
  joltage_ratings: List[str] = open("joltage_ratings.txt").read().splitlines()
  optimized_joltage_outputs: List[int] = []

  for bank_joltage_rating in joltage_ratings:
    optimized_joltage_outputs.append(max_bank_joltage(bank_joltage_rating))
    
  total_joltage = sum(optimized_joltage_outputs)
  print(total_joltage)

def max_bank_joltage(bank_joltage_rating: str) -> int:
  # scan to find the largest joltage for the first battery
  joltage_1: str = bank_joltage_rating[0]
  battery_1_pos: int = 0
  for i in range(1, len(bank_joltage_rating) - 1): # minus 1 because we cant have the first battery be the last battery in the bank
    if bank_joltage_rating[i] > joltage_1:
      joltage_1 = bank_joltage_rating[i]
      battery_1_pos = i

  # scan to find the largest joltage to the right of the first battery
  joltage_2: str = bank_joltage_rating[battery_1_pos + 1]
  for i in range(battery_1_pos + 2, len(bank_joltage_rating)):
    if bank_joltage_rating[i] > joltage_2:
      joltage_2 = bank_joltage_rating[i]

  return int(joltage_1 + joltage_2)


if __name__ == "__main__":
  main()