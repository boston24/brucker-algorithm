from node import Node
from graph import Graph

list = []
z1 = Node("z1",[],[],16)
z2 = Node("z2",[],[],20)
z3 = Node("z3",[],[],4)
z4 = Node("z4",[],[],3)
z5 = Node("z5",[],[],15)
z6 = Node("z6",[],[],14)
z7 = Node("z7",[],[],17)
z8 = Node("z8",[],[],6)
z9 = Node("z9",[],[],6)
z10 = Node("z10",[],[],4)
z11 = Node("z11",[],[],10)
z12 = Node("z12",[],[],8)
z13 = Node("z13",[],[],9)
z14 = Node("z14",[],[],7)
z15 = Node("z15",[],[],10)
z16 = Node("z16",[],[],9)
z17 = Node("z17",[],[],10)
z18 = Node("z18",[],[],8)
z19 = Node("z19",[],[],2)
z20 = Node("z20",[],[],3)
z21 = Node("z21",[],[],6)
z22 = Node("z22",[],[],5)
z23 = Node("z23",[],[],4)
z24 = Node("z24",[],[],11)
z25 = Node("z25",[],[],12)
z26 = Node("z26",[],[],9)
z27 = Node("z27",[],[],10)
z28 = Node("z28",[],[],8)
z29 = Node("z29",[],[],7)
z30 = Node("z30",[],[],5)
z31 = Node("z31",[],[],3)
z32 = Node("z32",[],[],5)

z32.addKids([z31])
z31.addKids([z29])
z30.addKids([z29])
z29.addKids([z28])
z28.addKids([z27])
z27.addKids([z26])
z26.addKids([z25])
z25.addKids([z24])
z24.addKids([z5])
z23.addKids([z22])
z22.addKids([z21])
z21.addKids([z18])
z20.addKids([z19])
z19.addKids([z18])
z18.addKids([z17])
z17.addKids([z16])
z16.addKids([z15])
z15.addKids([z11])
z14.addKids([z13])
z13.addKids([z12])
z12.addKids([z5])
z11.addKids([z5])
z10.addKids([z9])
z9.addKids([z8])
z8.addKids([z7])
z7.addKids([z6])
z6.addKids([z1])
z5.addKids([z2])
z4.addKids([z3])
z3.addKids([z1])
z2.addKids([z1])


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
list.append(z13)
list.append(z14)
list.append(z15)
list.append(z16)
list.append(z17)
list.append(z18)
list.append(z19)
list.append(z20)
list.append(z21)
list.append(z22)
list.append(z23)
list.append(z24)
list.append(z25)
list.append(z26)
list.append(z27)
list.append(z28)
list.append(z29)
list.append(z30)
list.append(z31)
list.append(z32)


#graph = Graph(list)