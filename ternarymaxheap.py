import math
import networkx as nx
# def get_tree_levels(G, root):
#     levels = {}
#     for node in G.nodes():
#         path_length = nx.shortest_path_length(G, root, node)
#         if path_length in levels:
#             levels[path_length].append(node)
#         else:
#             levels[path_length] = [node]
#     print("Please understand this, before continuing",levels)
#     return levels
# def ternary_tree_positions(G, root,width, sep=2):
#     pos = {root: (0, 0)}
#     levels=get_tree_levels(G,root)
#     parent=root
#     for level in levels:
#         level_nodes = [n for n in G.nodes() if nx.shortest_path_length(G, root, n) == level]
#
#
#         n = len(level_nodes)
#
#         for i, node in enumerate(level_nodes):
#             if node not in pos:
#                 x = (i-(n - 1) // 2) * (2*sep+2)
#                 y = -level
#                 pos[node] = (x, y)
#
#             if level:
#                 print("\n\nThis is i:",i)
#
#                 children = list(nx.neighbors(G,node))[1:]
#                 parent = list(nx.neighbors(G,node))[0]
#                 print("These are children:",children)
#                 for i,child in enumerate(children):
#                     print("Debug list:",list(nx.neighbors(G,node)),"parent:",parent,"Position of the parent:",pos[parent])
#                     if i%3 == 0:
#                         pos_left = (pos[node][0] - (sep/((level**level))), -level - 1)
#                         pos[child] = pos_left
#                     elif i%3 == 1:
#                         pos_middle = (pos[node][0], -level - 1)
#                         pos[child] = pos_middle
#                     elif i%3 == 2:
#                         pos_right = (pos[node][0]+ (sep/((level**level))), -level - 1)
#                         pos[child] = pos_right
#                     print("Child:",child,"\nDescendants/Children(used somewhere):",list(nx.neighbors(G,node))[1:],"\nNode:",node)
#                     print(" The position: for the node above ",pos[node])
#
#     return pos
class TernaryMaxHeap():
    def __init__(self):
        self.heap_list = [0]
        self.size = 0


    def __str__(self):
        string = ""
        for ind, val in enumerate(self.heap_list):
            string += f"|{val}"
        return string + "|"


    def __len__(self):
        return len(self.heap_list)


    def __contains__(self, item):
        return item in self.heap_list


    def is_empty(self):
        return len(self.heap_list) - 1 == 0


    def find_max(self):
        if self.size > 0:
            return self.heap_list[1]
        return None


    def insert(self, item):
        self.heap_list.append(item)
        self.size += 1
        self.percolate_up(self.size)


    def del_max(self):
        max_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.heap_list.pop()
        self.size = self.size - 1
        self.percolate_down(1)
        return max_val


    def max_child(self, index):
        if index*3+1<=self.size :

            if self.heap_list[index * 3] >= (self.heap_list[index * 3 + 1]) and self.heap_list[index * 3] >= (self.heap_list[index*3-1]):
                return index*3
            if self.heap_list[index * 3+1] >= (self.heap_list[index * 3 ]) and self.heap_list[index * 3+1] >=(self.heap_list[index * 3 -1]):
                return index * 3 + 1
            else:return index*3-1
        elif index * 3 + 1 > self.size and (index * 3<=self.size):
            if self.heap_list[index * 3] >= (self.heap_list[index*3-1]):
                return index*3
            else:
                return index*3-1
        elif  index * 3 + 1 > self.size and (index * 3>self.size):
            if (index*3-1<=self.size):
                return index*3-1

    def build_heap(self, alist):
        self.heap_list = [0] + alist[:]
        self.size = len(alist)
        index = math.floor((len(alist)-2)/3)+1
        while (index > 0):
            self.percolate_down(index)
            index -= 1
        # for i in alist:
        #     self.insert(i)
    def percolate_up(self, index):
        while math.floor((index-2)/3)+1> 0:

            if self.heap_list[index] > self.heap_list[math.floor((index-2)/3)+1]:
                temp = self.heap_list[math.floor((index-2)/3)+1]
                self.heap_list[math.floor((index-2)/3)+1] = self.heap_list[index]
                self.heap_list[index] = temp
            index=math.floor((index-2)/3)+1


    def percolate_down(self, index):
        while (index * 3-1) <= self.size:
            mc = self.max_child(index)
            # print("Debug: index",mc,"value:",self.heap_list[mc],"heap list(in progression):",self.heap_list)
            if self.heap_list[index] < self.heap_list[mc]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[mc]
                self.heap_list[mc] = temp
            index = mc


