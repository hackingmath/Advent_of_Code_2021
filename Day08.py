'''Advent of Code Day 8
Digits with letters'''

loc = "/home/bodhi-math/day08.txt"#C:\\Users\\Owner\\Documents\\AoC2021\\day05.txt"

with open(loc)as f:
    lst = []
    for line in f.readlines():
        numstr = line.split()
        lst.append(numstr)

def input_output():
     input_list = list()
     output_list = list()
     for i,row in enumerate(lst):
          input_list.append([])
          output_list.append([])
          idx = lst[i].index('|')
          for string in lst[i][:idx]:
               input_list[i].append(string)
          for string in lst[i][(idx+1):]:
               output_list[i].append(string)
     return input_list,output_list

def part1():
     total = 0
     for row in output_list:
          for str in row:
               if len(set(str)) in [2,3,4,7]:
                    total += 1
     return total

#print("total",total)
#print(output_list[:5])
#print(lst[:5])

def convert(string):
     output = list()
     output[:0] = string
     return output

def string_in_string(a,b):
     for letter in a:
          if letter not in b:
               return False
     return True

def missing_letter(a,b):
     """Returns letter in a not in b"""
     for letter in a:
          if letter not in b:
               return letter
     return False

def figure_digits(slist):
     letters = 'abcdefg'
     if '|' in slist:
          slist.remove('|')
     digits = dict()
     for s in slist:
          if len(s)==2:
               digits[1] = s
          if len(s) == 3:
               digits[7] = s
          if len(s) == 4:
               digits[4] = s
          if len(s) == 7:
               digits[8] = s
     top = missing_letter(digits[7],digits[1])

     for s in slist:
               
          if len(s) == 6:
               #print(s)
               if string_in_string(digits[4] + top,s):
                    digits[9] = s
                    lower_left = missing_letter(letters,s)
               elif missing_letter(digits[1],s):
                    digits[6] = s
                    upper_right = missing_letter(digits[1],s)
               else:
                    digits[0] = s
     for s in slist:
          if len(s) == 5:
               if string_in_string(digits[1],s):
                    digits[3] = s
               if string_in_string(top+upper_right+lower_left,s):
                    digits[2]=s
     for s in slist:
          if len(s) == 5:
               if s not in [digits[2],digits[3]]:
                    digits[5] = s
          
     return digits

def match_digit(outstr,inputdict):
     """Finds value in inputdict that
     matches jumbled outstr"""
     for v in inputdict:
          #print(v)
          if set(convert(outstr)) == set(convert(inputdict[v])):
               return str(v)

input_list,output_list = input_output()
print("input,output:",input_list[:5],output_list[:5])
def part2():
     total = 0
     for r,row in enumerate(input_list):
          digitstr = ''
          #print("figuring digits",r)
          #print(row)
          d = figure_digits(row)
          print(d)
          '''for n in d:
               print("n:",n)
               conv_n = set(convert(d[n]))'''
          for numstr in output_list[r]:
               print("numstr",numstr)
               digitstr += match_digit(numstr,d)
          total += int(digitstr)
     return total
          
print(part2())
          
     
