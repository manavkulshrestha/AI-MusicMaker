class Node:
	note = None
	children_index = None

	def __init__(self, note, children_index=None):
		self.note = note
		self.children_index = children_index
	def __repr__(self):
		return ''.join(['{',self.note,',',str(self.children_index),'}'])

base_tree = [[[]] for i in range(4)]
base_tree[0] = [[Node('A', 0)]]

print('1: ',base_tree)

for i in range(0, 3):
	children_link = 0

	for children in base_tree[i]:
		for child in children:

			print(child)

			new_children = []
			for delta in ['A','B','C']:
				new_children.append(Node(delta, children_link))
				children_link += 1

			base_tree[i+1].append(new_children)
			if(base_tree[i+1][0] == []):
				print('TRUE')
				del base_tree[i+1][0]

print(base_tree)
for i, x in enumerate(base_tree):
	print(str(i)+': '+str(x))