import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from node import Node
from graph import Graph
from data import *
#from data2 import *
from networkx.drawing.nx_agraph import graphviz_layout
import plotly.express as px

def start(list):
    for node in list:
        if not node.kids:
            node.di = 1-node.time
            #print("Set di "+str(node.di)+" to "+str(node.name))
            return setDi(list)

def setDi(list):
    for node in list:
        print(node.name)
    while any(x.di==None for x in list):
        for node in list:
            if node.kids:                  
                if node.kids[0].di and node.di==None:
                    node.di = max(1+node.kids[0].di,1-node.time)
                    print("\n"+str(node.name)+", di*="+str(node.di))
                    #print("Set di "+str(node.di)+" to "+str(node.name))
    return list

def makeListForTimeline(list,cpu):
    jobs = []
    tasks_in_row = [[] for _ in range(len(list))]
    to_add = []
    i = 0

    while any(x.on_machine==False for x in list):
            
        for node in list:
            if not node.parents and not node.on_machine:
                if node not in to_add:
                    to_add.append(node)
            elif not any(x.on_machine==False for x in node.parents) and node.parents and not node.on_machine:
                #print("\nAdding "+str(node.name))
                if node not in to_add:
                    to_add.append(node)
        to_add = sorted(to_add, key=lambda x : (x.di,x.name), reverse=True)

        '''print("\nTO_ADD")
        for node in to_add:
            print(node.name, end=" ")
        print("\n")'''

        if len(to_add)<cpu:
            cpu_temp = len(to_add)
        else:
            cpu_temp = cpu

        for x in reversed(range(cpu_temp)):
            #print("Added "+str(to_add[x].name)+" to cpu no. "+str(i))
            to_add[x].on_machine = True
            tasks_in_row[i].append(to_add[x])
            for node in list:
                if node.name == to_add[x].name:
                    node.on_machine = True
                    node.latency = i+1-node.time
            del to_add[x]

        i += 1

    tasks_in_row = ([x for x in tasks_in_row if x])

    '''for col in tasks_in_row:
        for task in col:
            print(task.name, end=" ")
        print("\n")'''

    for col in range(len(tasks_in_row)):
        for row in range(len(tasks_in_row[col])):
            task = tasks_in_row[col][row]
            if len(tasks_in_row[col])<cpu:
                row = cpu-row-1
            jobs.append(dict(Name=task.name, Start=col, Finish=len(tasks_in_row), Row=row+1, Time=1, Di=task.di))

    for task in list:
        print(str(task.name)+", di*="+str(task.di)+", latency="+str(task.latency))

    return jobs

result = start(list)
timeline_list = makeListForTimeline(result,4)
Lmax = max(node.latency for node in result)
print("\nLMax = "+str(Lmax)+"\n")

#for node in result:
#    print(str(node.name)+", di="+str(node.di))

graph = Graph(result)
graph.showGraph([])
graph.showTimeline(timeline_list)       


