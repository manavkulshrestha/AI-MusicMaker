legal_dict = {
	'C': ('A','E'),
	'D': ('B','F'),
	'E': ('C','G'),
	'F': ('D','A'),
	'G': ('E','B'),
	'A': ('F','C'),
	'B': ('G','D'),
}

illegal_dict = {
	'C': ('B','G','D'),
	'D': ('C','A','E'),
	'E': ('D','B','F'),
	'F': ('E','C','G'),
	'G': ('F','D','A'),
	'A': ('G','E','B'),
	'B': ('A','F','C'),
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
	0		:'C0',
	0.5		:'C#0',
	1		:'D0',
	1.5		:'D#0',
	2		:'E0',
	3		:'F0',
	3.5		:'F#0',
	4		:'G0',
	4.5		:'G#0',
	5		:'A0',
	5.5		:'A#0',
	6		:'B0',

	7		:'C1',
	7.5		:'C#1',
	8		:'D1',
	8.5		:'D#1',
	9		:'E1',
	10		:'F1',
	10.5	:'F#1',
	11		:'G1',
	11.5	:'G#1',
	12		:'A1',
	12.5	:'A#1',
	13		:'B1',

	14		:'C2',
	14.5	:'C#2',
	15		:'D2',
	15.5	:'D#2',
	16		:'E2',
	17		:'F2',
	17.5	:'F#2',
	18		:'G2',
	18.5	:'G#2',
	19		:'A2',
	19.5	:'A#2',
	20		:'B2',

	21		:'C3',
	21.5	:'C#3',
	22		:'D3',
	22.5	:'D#3',
	23		:'E3',
	24		:'F3',
	24.5	:'F#3',
	25		:'G3',
	25.5	:'G#3',
	26		:'A3',
	26.5	:'A#3',
	27		:'B3',

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

def is_int(x):
	try:
		value = int(value)
		return True
	except ValueError:
		return False

def num_to_note(num):
	if(num < 0 or num > 34):
		raise MemoryError('Went off octave range')
	return Note(num_to_note_dict[num%34][:-1], int(num_to_note_dict[num%34][-1]))

def pprint_2d(l):
	for i, e in enumerate(l):
		print(f'{i}. {e}')

class Note:
	letter = None
	octave = None

	def __init__(self, letter, octave):
		self.letter = letter
		self.octave = octave
	def __repr__(self):
		return f'n{self.letter}{self.octave}'
	def get_num(self):
		return note_to_num_dict[f'{self.letter}{self.octave}']
	def equals(self, that):
		if that.letter is self.letter and that.octave is self.octave:
			return True
		return False
	def	equals_ignore_octave(that):
		if that.letter is this.letter:
			return True
		return False
	def get_rawletter():
		return self.letter[0]

class Node:
	parent_index = None
	note = None
	children_index = None

	def __init__(self, note, children_index=None, parent_index=None):
		self.parent_index = parent_index
		self.note = note
		self.children_index = children_index
	def __repr__(self):
		return ''.join(['{',str(self.parent_index),',',str(self.note),',',str(self.children_index),'}'])

input_ = ['D','F','E','D','G','F','A','G','F','E','D']#sample input, TODO:I

#cantus firmus generation from input
cantus_firmus = [Note(input_[0],2)]
for i, x in enumerate(input_[1:]):
	#i is really i+1
	cantus_firmus.append(((rawnotes[input_[i+1]])-rawnotes[input_[i]], Note(x,2)))
print(cantus_firmus)

base_tree = [[[]] for i in range(11)]
base_tree[0] = [[Node(Note(cantus_firmus[0].letter,3), children_index=0, parent_index=None)]]

def is_legal(prev_cf_note, cf_note, prev_base_note, base_note):
	if base_note.letter in legal_dict[cf_note.letter]:
		return True
	if base_note.letter in illegal_dict[cf_note.letter]:
		return False
	return True

#base tree generation
same_count = 0
same_thresh = 2
opp_count = 0
opp_thresh = 2
for i in range(0, len(cantus_firmus)-1):
	children_link = 0
	next_cf_delta_mag = abs(cantus_firmus[i+1][0])
	next_cf_note = cantus_firmus[i+1][1]

	parent_link = 0
	for children in base_tree[i]:
		for child in children:
			possibilities_delta = None

			if next_cf_delta_mag == 1:
				#step
				possibilities_delta = [-1,1]#TODO - ask Max
			else:
				#leap
				possibilities_delta = [-1,1]

			new_children = []
			for delta in possibilities_delta:
				new_base_note = num_to_note(child.note.get_num()+delta)
				cf_note = cantus_firmus[0] if i == 0 else cantus_firmus[i][1]
				boval = is_legal(cf_note, next_cf_note, child.note, new_base_note)
				if boval != False:
					if boval == None:
						#allowed, pass
						#not allowed, continue
						cf_diff = next_cf_note.get_num()-cf_note.get_num() # - means down
						base_diff = new_base_note.get_num()-child.note.get_num() # - means down
						if ((cf_diff < 0 and base_diff > 0) or (cf_diff > 0 and base_diff < 0)) and (opp_count < opp_thresh) or (i <= 1 or i == len(cantus_firmus)-2):	
							if not (i <= 1 or i == len(cantus_firmus)-2):
								opp_count += 1
							pass
						elif new_base_note.equals(child.note) and ((same_count < same_thresh) or (i <= 1 or i == len(cantus_firmus)-2)):
							if not (i <= 1 or i == len(cantus_firmus)-2):
								same_count += 1
							pass
						else:
							continue

					new_children.append(Node(new_base_note, children_index=children_link, parent_index=parent_link))
					children_link += 1


			base_tree[i+1].append(new_children)
			if(base_tree[i+1][0] == []):
				del base_tree[i+1][0]
			parent_link += 1

pprint_2d(base_tree)