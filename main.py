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
            node.latency = 1-node.time
            print("Set latency "+str(node.latency)+" to "+str(node.name))
            return setLatency(list)

def setLatency(list):
    while any(x.latency==None for x in list):
        for node in list:
            if node.kids:                  
                if node.kids[0].latency and node.latency == None:
                    node.latency = max(1+node.kids[0].latency,1-node.time)
                    print("Set latency "+str(node.latency)+" to "+str(node.name))
    return list

for node in start(list):
    print(str(node.name)+", latency="+str(node.latency))

#graph = Graph(start(list))
#graph.showGraph([])
#graph.showTimeline(list_timetable)       
