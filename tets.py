class Node:
	parent_index = None
	note = None
	children_index = None

	def __init__(self, note, children_index=None, parent_index=None):
		self.parent_index = parent_index
		self.note = note
		self.children_index = children_index
	def __repr__(self):
		return ''.join(['{',str(self.parent_index),self.note,',',str(self.children_index),'}'])

base_tree = [[[]] for i in range(4)]
base_tree[0] = [[Node('A', 0)]]

print('1: ',base_tree)

for i in range(0, 3):
	children_link = 0

	par = 0
	for j, children in enumerate(base_tree[i]):
		for k, child in enumerate(children):

			print(child)

			new_children = []
			for delta in ['A','B','C']:
				new_children.append(Node(delta, children_index=children_link, parent_index=par))
				children_link += 1

			base_tree[i+1].append(new_children)
			if(base_tree[i+1][0] == []):
				del base_tree[i+1][0]
			par += 1

print(base_tree)
for i, x in enumerate(base_tree):
	print(str(i)+': '+str(x))