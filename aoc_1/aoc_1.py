import time

def main():
  dial_pos = 50
  num_zeroes = 0

  file = open("input.txt")
  input = file.read()
  lines = input.splitlines()

  for line in lines:
    if(line[0] == "L"): # turn the dial left
      turns_left = int(line[1:])
      if(dial_pos == 0):
        num_zeroes += turns_left // 100
        dial_pos += (100 - turns_left % 100) % 100
      else:
        if(turns_left >= dial_pos):
          num_zeroes += 1
          turns_left -= dial_pos
          dial_pos = 0
          num_zeroes += turns_left // 100
          dial_pos += (100 - turns_left % 100) % 100
        else:
          dial_pos -= turns_left

    else: # turn the dial right
      turns_right = int(line[1:])
      if(dial_pos == 0):
        num_zeroes += turns_right // 100
        dial_pos += turns_right % 100
      else:
        if(turns_right >= 100 - dial_pos):
          num_zeroes += 1
          turns_right -= 100 - dial_pos
          dial_pos = 0
          num_zeroes += turns_right // 100
          dial_pos += turns_right % 100
        else:
          dial_pos += turns_right
  print(num_zeroes)

if __name__ == "__main__":
  start = time.time()
  main()
  end = time.time()
  print(f"Runtime: {end - start:.6f} seconds")