# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:52:39 2022

@author: Hadi.Mosadegh
"""
# Initializing the assumed tree

graph = {
        'A' : ['B','C','D'],
        'B' : ['E','F'],
        'C' : ['G','H'],
        'D' : ['I','J','K'],
        'E' : ['L','M'],
        'F' : [],
        'G' : [],
        'H' : [],
        'I' : [],
        'J' : [],
        'K' : [],
        'L' : [],
        'M' : []
        }

# Initializing visited and unvisited lists
visited = list()
unvisited = list()

#Starting the search with root node
unvisited.append('A')
# While loop  for searching the tree based on BFS logic
def BFS(tree,visited,unvisited):
    while len(unvisited)>0:
        selected_node = unvisited[0]
        #Here, we expand the selected_note based on the given tree
        #In fact, we can expand the node based on the problem rules
        for offspring in tree[selected_node]:
            #In order to prevent getting stock in loops, we can check if the node has
            #been visted before or not.
            if offspring not in visited:
                unvisited.append(offspring)
        unvisited.remove(selected_node)
        visited.append(selected_node)
        print(selected_node)

BFS(graph,visited,unvisited)