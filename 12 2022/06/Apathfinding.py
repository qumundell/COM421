import sys
import heapq
from heapq import heappush, heappop


class Node:
    def __init__(self, name):
        self.data = [sys.maxsize, self]
        self.f_val = 0
        self.name = name
        self.edges = []
        self.parent = None
        self.used = False
        self.is_on_open_list = False
        self.sld = 0

    def connect_edge(self, edge):
        self.edges.append(edge)

    def connect_sld(self, weight):
        self.sld = weight

    def add_parent(self, node):
        self.parent = node

    def get_name(self):
        return self.name

    def get_straight_line_distance(self):
        return self.sld

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.f_val < other.f_val


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

    def add_sld(self, node1, node2, dist):
        forward_edge = Edge(node1, node2, dist)
        backwards_edge = Edge(node2, node1, dist)

        node1.connect_sld(dist)

    def addToOpenList(self, node):
        self.openList.append(node)

    def algorithm(self, search, goal):
        start_node = self.find_start(search)
        if start_node is None:
            return "The node you tried to start from did not exist"
        else:
            start_node.data[0] = 0
            curNode = start_node
            done = False
            heappush(self.openList, start_node)
            while len(self.openList) >= 0:
                curNode = heappop(self.openList)
                print(curNode.name)
                curNode.used = True
                if curNode.get_name() == goal:
                    return self.print_route(curNode)

                for edge in curNode.edges:
                    if edge.end_node.used is not True:
                        g_val = curNode.data[0] + edge.weight
                        h_val = edge.end_node.sld
                        if g_val + h_val < edge.end_node.data[0]:
                            print(f"Found a shorter route to {edge.end_node.data[1]} which is {g_val}")
                            edge.end_node.f_val = g_val + h_val
                            edge.end_node.data[0] = g_val
                            # reparenting - i.e. set the parent of the remote node to be the current node
                            edge.end_node.parent = curNode

                        # if the remote node is not on the open list, add it to the open list
                        if edge.end_node.is_on_open_list is False:
                            heappush(self.openList, edge.end_node)
                            edge.end_node.is_on_open_list = True

                if len(self.openList) == 0:
                    return "The node you were looking for did not exist"
                print(self.openList)


    def print_route(self, node):
        done = False
        while done is False:
            if node.parent == None:
                return (node.name)
            else:
                print(node.name, end=" <- ")
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
    birmingham = Node("Birmingham")
    lyon = Node("Lyon")
    bordeaux = Node("Bordeaux")
    nice = Node("Nice")

    graph.add_sld(birmingham, nice, 1188)
    graph.add_sld(brussels, nice, 823)
    graph.add_sld(paris, nice, 686)
    graph.add_sld(lyon, nice, 299)
    graph.add_sld(bordeaux, nice, 637)
    graph.add_sld(amsterdam, nice, 980)
    graph.add_sld(cologne, nice, 805)

    graph.addToAllNodes(london)
    graph.addToAllNodes(brussels)
    graph.addToAllNodes(paris)
    graph.addToAllNodes(amsterdam)
    graph.addToAllNodes(cologne)
    graph.addToAllNodes(birmingham)
    graph.addToAllNodes(bordeaux)
    graph.addToAllNodes(lyon)
    graph.addToAllNodes(nice)

    graph.add_edge(london, brussels, 370)
    graph.add_edge(london, paris, 461)
    graph.add_edge(london, birmingham, 191)
    graph.add_edge(amsterdam, brussels, 211)
    graph.add_edge(cologne, brussels, 211)
    graph.add_edge(paris, brussels, 306)
    graph.add_edge(paris, bordeaux, 584)
    graph.add_edge(paris, lyon, 465)
    graph.add_edge(lyon, nice, 472)
    graph.add_edge(bordeaux, nice, 803)

   # start = input("Where are you starting from?")
    #goal = input("Where are you going?")
    start = "London"
    goal = "Nice"
    print(graph.algorithm(start, goal))


run()
