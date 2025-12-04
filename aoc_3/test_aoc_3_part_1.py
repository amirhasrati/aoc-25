from aoc_3_part_1 import max_bank_joltage

def test_biggest_at_start():
  ratings = "987654321111111"
  max = max_bank_joltage(ratings)

  assert max == 98

def test_in_between():
  ratings = "811111111111119"
  max = max_bank_joltage(ratings)

  assert max == 89

def test_at_end():
  ratings = "234234234234278"
  max = max_bank_joltage(ratings)

  assert max == 78

def test_in_middle():
  ratings = "818181911112111"
  max = max_bank_joltage(ratings)

  assert max == 92