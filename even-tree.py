def GetSubtreeSizes(edges):
	subtreeSizes = dict()
	RecGetSubTreeSizes(1,edges,subtreeSizes)
	return subtreeSizes

def RecGetSubTreeSizes(nodeID,edges,subtreeSizes):

	# Base Case: Leaf node.
	if nodeID not in edges:
		subtreeSizes[nodeID] = 1

	else:
		subtreeSize = 0

		# compute the size of the subtree beginning at each child node.
		for childID in edges[nodeID]:
			RecGetSubTreeSizes(childID, edges,subtreeSizes)
			subtreeSize += subtreeSizes[childID]


		# Update the size of the subtree beginning at the current node
		# adding 1 to account for the current node)
		subtreeSizes[nodeID] = 1 + subtreeSize

def NumEdgesRemoved(edges, subtreeSizes):
	numRemoved = 0
	# perform an iterative BFS starting at the root node.
	nodeStack = [1]
	while len(nodeStack) > 0:
		nodeID = nodeStack.pop()
		# base case: leaf node.
		if nodeID not in edges:
			continue
		else:
			# count the number of edges we can remove from the subtree beginning
			# at each child node
			for childID in edges[nodeID]:
				
				# remove the edge between the current root node and current child
				# node the resultant subtree will have an even number of nodes in it
				if subtreeSizes[childID] & 1 == 0:
					numRemoved +=1
				nodeStack.append(childID)

	return numRemoved

def main():
	numNodes,numEdges = [int(z) for z in raw_input().split()]

	# create an empty dictionary to store the edges
	edges = dict()


	for i in range(numEdges):
		# read the number of nodes and edges to expect
		nodeID, childID = sorted([int(z) for z in raw_input().split()])
		if nodeID not in edges:
			edges[nodeID] = []

		# keep track of this edge in a data structure
		edges[nodeID].append(childID)


	subtreeSizes = GetSubtreeSizes(edges)
	print NumEdgesRemoved(edges, subtreeSizes)

if __name__ == "__main__":
	main()
