note_to_num = {
	'C': 0,
	'D': 1,
	'E': 2,
	'F': 3,
	'G': 4,
	'A': 5,
	'B': 6,
}

num_to_note = {
	0: 'C',
	1: 'D',
	2: 'E',
	3: 'F',
	4: 'G',
	5: 'A',
	6: 'B',
}

# def print_cantus_firmus(cf):
# 	current_note = note_to_num[cf[0][0]]
# 	for x in cantus_firmus[1:]:
# cantus_firmus = [['D', 1], ['F', 1], ['E', 1], ['D', 1], ['G', 1], ['F', 1], ['A', 1], ['G', 1], ['F', 1], ['E', 1], ['D', 1]]
# cantus_firmus = [('D', 1), 2, -1, -1, 3, -1, ]
input_ = ['D','F','E','D','G','F','A','G','F','E','D']
cantus_firmus = [input_[0]]
for i, x in enumerate(input_[1:]):
	#i is really i+1
	cantus_firmus.append((note_to_num[input_[i+1]]-note_to_num[input_[i]], x))
print(cantus_firmus)

upper = [[] for i in range(11)]
base = [[] for i in range(11)]

base[0] = cantus_firmus[0]
for i, x in enumerate(cantus_firmus):
	




