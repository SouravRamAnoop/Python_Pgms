# Create the dictionary with graph elements
# graph = {
#    "a" : ["b","c"],
#    "b" : ["a", "d"],
#    "c" : ["a", "d"],
#    "d" : ["e"],
#    "e" : ["d"]
# }
# # Print the graph
# print(graph)

# #for accessesing vertices
class graph:
   def __init__(self,grph=None):
      self.grph = grph
# Get the keys of the dictionary
   def getVertices(self):
      return list(self.grph.keys())
# Create the dictionary with graph elements
graph_elements = {
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements)
print(g.getVertices())