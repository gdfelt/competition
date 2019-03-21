"""
Project Euler Problem 13
========================

Work out the first ten digits of the sum of the following one-hundred
50-digit numbers.


           {{ large_sums.dat }}


"""

def process_line(s):
      return int(s[:12])

def main():
      sum_val = 0
      with open('resources/large_sums.dat') as file:
            for line in file:
                  sum_val += process_line(line)

      print(str(sum_val)[:10])

if __name__ == "__main__":
      main()
