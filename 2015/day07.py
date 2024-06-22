file = "./2015/input/input07.txt"

d = dict()
sol = dict()

with open(file, "r") as f:
	for f_i in f:
		x = f_i.split()
		d.update({x[-1]: x[:-2]})

# # part 2 only
# d.update({"b": ["16076"]})

unresolved = list(d.keys())

ind = 0
while len(unresolved) > 0:
	if ind >= len(d):
		ind = 0
	i = list(d.keys())[ind]

	if i not in unresolved:
		ind += 1
		continue

	if len(d.get(i)) == 1 and d.get(i)[0].isnumeric():
		sol.update({i: int(d.get(i)[0])})
		unresolved.remove(i)
		ind += 1
		continue
	
	if len(d.get(i)) == 1 and d.get(i)[0] in sol.keys():
		val = sol.get(d.get(i)[0])
		sol.update({i: val})
		unresolved.remove(i)
		ind += 1
		continue

	if len(d.get(i)) == 1:
		ind += 1
		continue

	if len(d.get(i)) == 2 and d.get(i)[0] == "NOT" and \
	  (d.get(i)[1].isnumeric() or d.get(i)[1] in sol.keys()):
		val = 0xffff - int(sol.get(d.get(i)[1]))
		sol.update({i: val})
		unresolved.remove(i)
		ind += 1
		continue
	
	if d.get(i)[1] == "AND" and \
	  (d.get(i)[0].isnumeric() or d.get(i)[0] in sol.keys()) and \
	  (d.get(i)[2].isnumeric() or d.get(i)[2] in sol.keys()):
		if d.get(i)[0].isnumeric():
			val1 = int(d.get(i)[0])
		else:
			val1 = sol.get(d.get(i)[0])
		
		if d.get(i)[2].isnumeric():
			val2 = int(d.get(i)[2])
		else:
			val2 = sol.get(d.get(i)[2])
		val = val1 & val2
		sol.update({i: val})
		unresolved.remove(i)
		ind += 1
		continue
	
	if d.get(i)[1] == "OR" and \
	  (d.get(i)[0].isnumeric() or d.get(i)[0] in sol.keys()) and \
	  (d.get(i)[2].isnumeric() or d.get(i)[2] in sol.keys()):
		if d.get(i)[0].isnumeric():
			val1 = int(d.get(i)[0])
		else:
			val1 = sol.get(d.get(i)[0])
		
		if d.get(i)[2].isnumeric():
			val2 = int(d.get(i)[2])
		else:
			val2 = sol.get(d.get(i)[2])
		val = val1 | val2
		sol.update({i: val})
		unresolved.remove(i)
		ind += 1
		continue
	
	if d.get(i)[1] == "LSHIFT" and \
	  (d.get(i)[0].isnumeric() or d.get(i)[0] in sol.keys()) and \
	  (d.get(i)[2].isnumeric() or d.get(i)[2] in sol.keys()):
		if d.get(i)[0].isnumeric():
			val1 = int(d.get(i)[0])
		else:
			val1 = sol.get(d.get(i)[0])
		
		if d.get(i)[2].isnumeric():
			val2 = int(d.get(i)[2])
		else:
			val2 = sol.get(d.get(i)[2])
		val = val1 << val2
		sol.update({i: val})
		unresolved.remove(i)
		ind += 1
		continue
	
	if d.get(i)[1] == "RSHIFT" and \
	  (d.get(i)[0].isnumeric() or d.get(i)[0] in sol.keys()) and \
	  (d.get(i)[2].isnumeric() or d.get(i)[2] in sol.keys()):
		if d.get(i)[0].isnumeric():
			val1 = int(d.get(i)[0])
		else:
			val1 = sol.get(d.get(i)[0])
		
		if d.get(i)[2].isnumeric():
			val2 = int(d.get(i)[2])
		else:
			val2 = sol.get(d.get(i)[2])
		val = val1 >> val2
		sol.update({i: val})
		unresolved.remove(i)
		ind += 1
		continue

	ind += 1

print(sol.get("a"))
