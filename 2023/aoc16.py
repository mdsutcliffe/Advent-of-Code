file = open("input/input16_test.txt", "r")
x = file.read().split("\n")
file.close()

mirror_dict = {
  ("/",  "N"):  [ 0,  1, "E"],
  ("/",  "E"):  [-1,  0, "N"],
  ("/",  "S"):  [ 0, -1, "W"],
  ("/",  "W"):  [ 1,  0, "S"],

  ("\\",  "N"): [ 0, -1, "W"],
  ("\\",  "E"): [ 1,  0, "S"],
  ("\\",  "S"): [ 0,  1, "E"],
  ("\\",  "W"): [-1,  0, "N"]
}

continue_dict = { "E": [0, 1], "W": [0, -1], "S": [1, 0], "N": [-1, 0] }

beam_history = []
def shine(beam):
  while True:
    current_location = beam[-1]
    if current_location in beam_history:
      return beam
    beam_history.append(current_location)
    if current_location[0] >= len(x) or current_location[0] < 0 or \
            current_location[1] >= len(x[0]) or current_location[1] < 0:
      return beam
    elif x[current_location[0]][current_location[1]] == "|" and current_location[2] in "EW":
      beam_history.append(current_location)
      return [beam,
              shine([(current_location[0] - 1, current_location[1], "N")]),
              shine([(current_location[0] + 1, current_location[1], "S")])]
    elif x[current_location[0]][current_location[1]] == "-" and current_location[2] in "NS":
      beam_history.append(current_location)
      return [beam,
              shine([(current_location[0], current_location[1] - 1, "W")]),
              shine([(current_location[0], current_location[1] + 1, "E")])]
    elif x[current_location[0]][current_location[1]] in "/\\":
      beam_history.append(current_location)
      delta = mirror_dict.get((x[current_location[0]][current_location[1]], current_location[2]))
      beam.append((current_location[0] + delta[0],
                   current_location[1] + delta[1],
                   delta[2]))
    else:
      beam_history.append(current_location)
      delta = continue_dict.get(current_location[2])
      beam.append((current_location[0] + delta[0],
                   current_location[1] + delta[1],
                   current_location[2]))

def get_energized(beam_history):
  total = 0
  spot_history = [(i[0], i[1]) for i in beam_history]
  for i in range(len(x)):
    for j, _ in enumerate(x[i]):
      if (i, j) in spot_history:
        total += 1
  return total

def part1():
  beam_history = []
  shine([(0, 0, "E")])
  energized = get_energized(beam_history)
  return energized

print(part1())