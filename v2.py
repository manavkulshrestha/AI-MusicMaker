legal_dict = {
	'C': ('A','E'),
	'D': ('B','F'),
	'E': ('C','G'),
	'F': ('D','A'),
	'G': ('E','B'),
	'A': ('F','C'),
	'B': ('G','D'),
}

rawnotes = {
	'C':	0,
	'C#':	0.5,
	'D':	1,
	'D#':	1.5,
	'E':	2,
	'F':	3,
	'F#':	3.5,
	'G':	4,
	'G#':	4.5,
	'A':	5,
	'A#':	5.5,
	'B':	6,
}

note_to_num_dict = {
	'C0':	0,
	'C#0':	0.5,
	'D0':	1,
	'D#0':	1.5,
	'E0':	2,
	'F0':	3,
	'F#0':	3.5,
	'G0':	4,
	'G#0':	4.5,
	'A0':	5,
	'A#0':	5.5,
	'B0':	6,

	'C1':	7,
	'C#1':	7.5,
	'D1':	8,
	'D#1':	8.5,
	'E1':	9,
	'F1':	10,
	'F#1':	10.5,
	'G1':	11,
	'G#1':	11.5,
	'A1':	12,
	'A#1':	12.5,
	'B1':	13,

	'C2':	14,
	'C#2':	14.5,
	'D2':	15,
	'D#2':	15.5,
	'E2':	16,
	'F2':	17,
	'F#2':	17.5,
	'G2':	18,
	'G#2':	18.5,
	'A2':	19,
	'A#2':	19.5,
	'B2':	20,

	'C3':	21,
	'C#3':	21.5,
	'D3':	22,
	'D#3':	22.5,
	'E3':	23,
	'F3':	24,
	'F#3':	24.5,
	'G3':	25,
	'G#3':	25.5,
	'A3':	26,
	'A#3':	26.5,
	'B3':	27,

	'C4':	28,
	'C#4':	28.5,
	'D4':	29,
	'D#4':	29.5,
	'E4':	30,
	'F4':	31,
	'F#4':	31.5,
	'G4':	32,
	'G#4':	32.5,
	'A4':	33,
	'A#4':	33.5,
	'B4':	34,
}

num_to_note_dict = {
	0		:'C4',
	0.5		:'C#4',
	1		:'D4',
	1.5		:'D#4',
	2		:'E4',
	3		:'F4',
	3.5		:'F#4',
	4		:'G4',
	4.5		:'G#4',
	5		:'A4',
	5.5		:'A#4',
	6		:'B4',

	7		:'C4',
	7.5		:'C#4',
	8		:'D4',
	8.5		:'D#4',
	9		:'E4',
	10		:'F4',
	10.5	:'F#4',
	11		:'G4',
	11.5	:'G#4',
	12		:'A4',
	12.5	:'A#4',
	13		:'B4',

	14		:'C4',
	14.5	:'C#4',
	15		:'D4',
	15.5	:'D#4',
	16		:'E4',
	17		:'F4',
	17.5	:'F#4',
	18		:'G4',
	18.5	:'G#4',
	19		:'A4',
	19.5	:'A#4',
	20		:'B4',

	21		:'C4',
	21.5	:'C#4',
	22		:'D4',
	22.5	:'D#4',
	23		:'E4',
	24		:'F4',
	24.5	:'F#4',
	25		:'G4',
	25.5	:'G#4',
	26		:'A4',
	26.5	:'A#4',
	27		:'B4',

	28		:'C4',
	28.5	:'C#4',
	29		:'D4',
	29.5	:'D#4',
	30		:'E4',
	31		:'F4',
	31.5	:'F#4',
	32		:'G4',
	32.5	:'G#4',
	33		:'A4',
	33.5	:'A#4',
	34		:'B4',
}

def num_to_note(num):
	return num_to_note_dict[num%34]

class Note:
	letter = None

	def __init__(self, letter, octave):
		self.letter = f'{letter}{octave}'
	def __repr__(self):
		return f'{self.letter}'
	def get_num(self):
		return note_to_num_dict[self.letter]
	def equals(self, that):
		if that.letter == self.letter:
			return True
		return False
	def	equals_ignore_octave(that):
		if abs(note_to_num_dict[self.letter]-note_to_num_dict[that.letter]) == 7:
			return True
		return False

class Node:
	parent_index = None
	note = None
	children_index = None

	def __init__(self, note, children_index=None, parent_index=None):
		self.note = note
		self.children_index = children_index
	def __repr__(self):
		return ''.join(['{',str(self.note),',',str(self.children_index),'}'])

input_ = ['D','F','E','D','G','F','A','G','F','E','D']#sample input, TODO:I

#cantus firmus generation from input
cantus_firmus = [Note(input_[0],2)]
for i, x in enumerate(input_[1:]):
	#i is really i+1
	cantus_firmus.append(((rawnotes[input_[i+1]])-rawnotes[input_[i]], Note(x,2)))
print(cantus_firmus)

base_tree = [[[]] for i in range(11)]
base_tree[0] = [[Node(Note(cantus_firmus[0].letter,-1), children_index=0, parent_index=None)]]

def is_legal(cf_note, base_note):
	return True

#base tree generation
for i in range(0, len(cantus_firmus)-1):
	children_link = 0
	cf_delta_mag = abs(cantus_firmus[i+1][0])
	cf_note = Note(cantus_firmus[i+1][1],2)

	parent_link = 0
	for children in base_tree[i]:
		for child in children:
			possibilities_delta = None

			if cf_delta_mag == 1:
				#step
				possibilities_delta = [-1,1]#TODO - ask Max
			else:
				#leap
				possibilities_delta = [-1,1]

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