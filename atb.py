#TODO:
# figure out octave stuff
# ask Max about rules, implement
# gui
# upper

note_to_num_dict = {
	'C': 0,
	'D': 1,
	'E': 2,
	'F': 3,
	'G': 4,
	'A': 5,
	'B': 6,
}

num_to_note_dict = {
	0: 'C',
	1: 'D',
	2: 'E',
	3: 'F',
	4: 'G',
	5: 'A',
	6: 'B',
}

def note_to_num(note):
	return note_to_num_dict[note]

def num_to_note(num):
	if num < 0:
		num += 7
	return num_to_note_dict[num%7]

class Node:
	note = None
	children_index = None

	def __init__(self, note, children_index=None):
		self.note = note
		self.children_index = children_index
	def __repr__(self):
		return ''.join(['{',self.note,',',str(self.children_index),'}'])

input_ = ['D','F','E','D','G','F','A','G','F','E','D']#sample input, TODO: GUI

#cantus firmus generation from input
cantus_firmus = [input_[0]]
for i, x in enumerate(input_[1:]):
	#i is really i+1
	cantus_firmus.append((note_to_num(input_[i+1])-note_to_num(input_[i]), x))
print(cantus_firmus)

base_tree = [[[]] for i in range(11)]
base_tree[0] = [[Node(cantus_firmus[0], 0)]]

print(base_tree)

def is_dissonant(cf_note, base_note):
	#checks if base note is legal as per cantus firmus
	return False

#base tree generation
for i in range(0, len(cantus_firmus)-1):
	children_link = 0
	cf_delta_mag = abs(cantus_firmus[i+1][0])
	cf_note_num = note_to_num(cantus_firmus[i+1][1])

	for children in base_tree[i]:
		for child in children:
			possibilities_delta = None
			
			elif cf_delta_mag == 1:
				#step
				possibilities_delta = list(range(-1, 2))#TODO - ask Max
			else:
				#leap
				possibilities_delta = list(range(-1, 2))

			new_children = []
			for delta in possibilities_delta:
				base_note = num_to_note(note_to_num(child.note)+delta);
				if not is_dissonant(cf_note_num, base_note):
					new_children.append(Node(base_note, children_link))
					children_link += 1

			base_tree[i+1].append(new_children)
			if(base_tree[i+1][0] == []):
				del base_tree[i+1][0]

print(base_tree)


