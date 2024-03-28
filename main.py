# Built-in imports
import math

GRADE = {}
for i in range(101):
  if i >= 70:
    GRADE[i] = "A"
  elif i >= 60:
    GRADE[i] = "B"
  elif i >= 55:
    GRADE[i] = "C"
  elif i >= 50:
    GRADE[i] = "D"
  elif i >= 45:
    GRADE[i] = "E"
  elif i >= 40:
    GRADE[i] = "S"
  else:
    GRADE[i] = "U"

def read_testscores(filename):
  lst = []
  with open(filename, "r") as f:
    for lines in f:
      dictionary = {}
      data = f.readline().strip().split(",")
      dictionary["class"] = data[0]
      dictionary["name"] = data[1]
      dictionary["overall"] = math.ceil(int(data[2])/2 + int(data[3]) / 40 * 30 + int(data[4]) / 80 * 35 + int(data[5]) / 30 * 20)
      dictionary["grade"] = GRADE[dictionary["overall"]]
      lst.append(dictionary)
  return lst

def analyze_grades(studentdata):
  output = {}
  for dictionary in studentdata:
    val = list(dictionary.values())
    if val[0] not in output.keys(): #new class
      output[val[0]] = {val[3] : 1}
    else: 
      if val[3] in output[val[0]].keys(): #alphabet grade already recorded
        output[val[0]][val[3]] += 1
      else: #new alphabet grade
        output[val[0]][val[3]] = 1
  return output
