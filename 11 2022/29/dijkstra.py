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
        self.is_on_open_list = False

    def connect_edge(self, edge):
        self.edges.append(edge)

    def add_parent(self, node):
        self.parent = node

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name

class Edge:
    def __init__(self, start_node, end_node, weight):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight

    def __str__(self):
        return f"{self.start_node} to {self.end_node}, weight: {self.weight}"

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
        if start_node is None:
            print("The node you tried to start from did not exist")
        else:
            start_node.data[0] = 0
            curNode = start_node
            done = False
            nodecheckdone = False
            heappush(self.openList, start_node)
            while len(self.openList) > 0:
                if curNode.get_name() == goal:
                    return self.print_route(curNode)
                curNode.used = True
                for edge in curNode.edges:
                    if edge.end_node.used == False:
                        if curNode.data[0] + edge.weight < edge.end_node.data[0]:
                            edge.end_node.data[0] = curNode.data[0] + edge.weight
                            # reparenting - i.e. set the parent of the remote node to be the current node


                        # if the remote node is not on the open list, add it to the open list






                curNode = heappop(self.openList)[1]




    def print_route(self, node):
        done = False
        finale = node.name
        while done is False:
            if node.parent == None:
                return(finale)
            else:
                print(node.name)
            node = node.parent




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
    print(graph.algorithm(start,goal))


run()
