#TODO:
# figure out octave stuff
# ask Max about rules, implement
# gui
# upper

legal_dict = {
	'C': ('A','E'),
	'D': ('B','F'),
	'E': ('C','G'),
	'F': ('D','A'),
	'G': ('E','B'),
	'A': ('F','C'),
	'B': ('G','D'),
}

note_to_num_dict = {
	'C': 0,
	'C#': 0.5,
	'D': 1,
	'D#': 1.5,
	'E': 2,
	'F': 3,
	'F#': 3.5,
	'G': 4,
	'G#': 4.5,
	'A': 5,
	'A#': 5.5,
	'B': 6,
}

num_to_note_dict = {
	0: 'C',
	0.5: 'C#',
	1: 'D',
	1.5: 'D#',
	2: 'E',
	3: 'F',
	3.5: 'F#',
	4: 'G',
	4.5: 'G#',
	5: 'A',
	5.5: 'A#',
	6: 'B',
}

def num_to_note(num, octave):
	return Note(num_to_note_dict[num%7],octave)

class Note:
	letter = None
	octave = None

	def __init__(self, letter, octave):
		self.letter = letter
		self.octave = octave
	def __repr__(self):
		return f'{self.letter}'
	def get_num(self):
		return note_to_num_dict[self.letter]

class Node:
	parent_index = None
	note = None
	children_index = None

	def __init__(self, note, children_index=None, parent_index=None):
		self.note = note
		self.children_index = children_index
	def __repr__(self):
		return ''.join(['{',str(self.note),',',str(self.children_index),'}'])

input_ = ['D','F','E','D','G','F','A','G','F','E','D']#sample input, TODO: GUI

#cantus firmus generation from input
cantus_firmus = [Note(input_[0],0)]
for i, x in enumerate(input_[1:]):
	#i is really i+1
	cantus_firmus.append((note_to_num_dict[input_[i+1]]-note_to_num_dict[input_[i]], Note(x,0)))
print(cantus_firmus)

base_tree = [[[]] for i in range(11)]
base_tree[0] = [[Node(Note(cantus_firmus[0].letter,-1), children_index=0, parent_index=None)]]

print(base_tree)

def is_legal(cf_note, base_note):
	#checks if base note is legal as per cantus firmus
	x = base_note.letter
	if x in [legal_dict[cf_note.letter]]:
		return True
	return True

#base tree generation
for i in range(0, len(cantus_firmus)-1):
	children_link = 0
	cf_delta_mag = abs(cantus_firmus[i+1][0])
	cf_note = Note(cantus_firmus[i+1][1].letter,0)

	parent_link = 0
	for children in base_tree[i]:
		for child in children:
			possibilities_delta = None

			if cf_delta_mag == 1:
				#step
				possibilities_delta = list(range(0,0))#TODO - ask Max
			else:
				#leap
				possibilities_delta = [-1, 1]

			new_children = []
			for delta in possibilities_delta:
				base_note = num_to_note(child.note.get_num()+delta,-1);
				if is_legal(cf_note, base_note):
					new_children.append(Node(base_note, children_index=children_link, parent_index=parent_link))
					children_link += 1

			base_tree[i+1].append(new_children)
			if(base_tree[i+1][0] == []):
				del base_tree[i+1][0]
			parent_link += 1

print(base_tree)


