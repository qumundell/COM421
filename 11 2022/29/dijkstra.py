import sys
import heapq
from heapq import heappush, heappop

class Node:
    def __init__(self, name):
        self.data = [sys.maxsize, self]
        self.name = name
        self.edges = []
        self.parent = None
        self.used = False

    def connect_edge(self, edge):
        self.edges.append(edge)

    def add_parent(self, node):
        self.parent = node

    def get_name(self):
        return self.name

class Edge:
    def __init__(self, start_node, end_node, weight):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight


class Graph:
    def __init__(self):
        self.allNodes = []
        self.openList = []

    def addToAllNodes(self, node):
        self.allNodes.append(node)

    def add_edge(self, node1, node2, dist):
        forward_edge = Edge(node1, node2, dist)
        backwards_edge = Edge(node2, node1, dist)

        node1.connect_edge(forward_edge)
        node2.connect_edge(backwards_edge)

    def addToOpenList(self, node):
        self.openList.append(node)


    def algorithm(self, search, goal):
        start_node = self.find_start(search)
        start_node.data[0] = 0
        if start_node is None:
            print("The node you tried to start from did not exist")
        else:
            curNode = start_node
            done = False
            while done is False:
                if curNode.get_name() == goal:
                    return self.print_route(curNode)
                curNode.used = True
                for edge in curNode.edges:
                    if edge.end_node.used == False:

                        edge.end_node.data = [curNode.data[0] + edge.weight, edge.end_node]
                        heappush(self.openList, edge.end_node.data)

                self.openList[0][1].parent = curNode
                curNode = self.openList[0][1]




    def print_route(self, node):
        return(node)


    def find_start(self, search):
        for i in range(len(self.allNodes)):
            if search == self.allNodes[i].get_name():
                return self.allNodes[i]
        return None

def run():
    graph = Graph()
    london = Node("London")
    brussels = Node("Brussels")
    paris = Node("Paris")
    amsterdam = Node("Amsterdam")
    cologne = Node("Cologne")
    frankfurt = Node("Frankfurt")
    stuttgart = Node("Stuttgart")
    munich = Node("Munich")

    graph.addToAllNodes(london)
    graph.addToAllNodes(brussels)
    graph.addToAllNodes(paris)
    graph.addToAllNodes(amsterdam)
    graph.addToAllNodes(cologne)
    graph.addToAllNodes(frankfurt)
    graph.addToAllNodes(stuttgart)
    graph.addToAllNodes(munich)

    graph.add_edge(london, brussels, 370)
    graph.add_edge(london, paris, 461)
    graph.add_edge(amsterdam, brussels, 211)
    graph.add_edge(amsterdam, cologne, 263)
    graph.add_edge(cologne, brussels, 211)
    graph.add_edge(cologne, frankfurt, 190)
    graph.add_edge(paris, brussels, 305)
    graph.add_edge(paris, frankfurt, 572)
    graph.add_edge(paris, stuttgart, 624)
    graph.add_edge(stuttgart, frankfurt, 207)
    graph.add_edge(frankfurt, munich, 393)
    graph.add_edge(stuttgart, munich, 221)

    start = input("Where are you starting from?")
    goal = input("Where are you going?")
    graph.algorithm(start,goal)


run()
