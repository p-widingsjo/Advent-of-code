def input(filename): 
  with open(filename, 'r') as f: #Get data
    data = [elf.splitlines() for elf in f.read().split('\n\n')]
  data = [[int(meal) for meal in elf] for elf in data] #Put each elf in to a list
  return data

def part_one(data): #Sorts and takes highest number'
  print([sum(elf) for elf in data])
  return max([sum(elf) for elf in data])

def part_two(data): #Sorts, takes three highest and adds together
  return sum(sorted([sum(elf) for elf in data], reverse=True)[:3])

def main():
  filename = "input_d01.txt"
  data = input(filename)
  print(f'Part one answer: {part_one(data)}')
  print(f'Part two answer: {part_two(data)}')

if __name__ == "__main__":
    main()