from node import Node
from graph import Graph

list = []
z1 = Node("z1",[],[],4)
z2 = Node("z2",[],[],6)
z3 = Node("z3",[],[],4)
z4 = Node("z4",[],[],2)
z5 = Node("z5",[],[],3)
z6 = Node("z6",[],[],1)
z7 = Node("z7",[],[],5)
z8 = Node("z8",[],[],3)
z9 = Node("z9",[],[],9)
z10 = Node("z10",[],[],6)
z11 = Node("z11",[],[],3)
z12 = Node("z12",[],[],7)

z1.addKids([z7])
z2.addKids([z7])
z3.addKids([z8])
z4.addKids([z9])
z5.addKids([z9])
z6.addKids([z10])
z7.addKids([z10])
z8.addKids([z11])
z9.addKids([z11])
z10.addKids([z12])
z11.addKids([z12])


list.clear()
list.append(z1)
list.append(z2)
list.append(z3)
list.append(z4)
list.append(z5)
list.append(z6)
list.append(z7)
list.append(z8)
list.append(z9)
list.append(z10)
list.append(z11)
list.append(z12)


#graph = Graph(list)