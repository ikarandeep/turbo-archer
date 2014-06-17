
def search(a,b):

    # create an empty dictionary
    seen = {}


    seen[a] = True
    q = []

    for x in adj[a]:
        if x != b:
            seen[x] = True
            q.append(x)
    s = len(q) + 1
    
    while q:
        n = q.pop()
        for x in adj[n]:
            if x not in seen:
                seen[x] = True
                q.append(x)
                s += 1
    
    return (s+1)%2

# split the input 
# N is the number of vertices
# M is the number of edges
[N,M] = [int(x) for x in raw_input().split(' ')]

# create a list of edges
edges = []

# create a dictionary 
adj = {}

# add an empty list to all items in the adj dictionary
for a in xrange(1,N+1):
    adj[a] = []

# iterate through the range of edges
for a in xrange(M):
    # split the line
    [x,y] = [int(z) for z in raw_input().split(' ')]

    # for the list at X, append Y as an adjacent
    adj[x].append(y)

    # for the list at Y append X as an adjacent
    adj[y].append(x)

    # append the combination to the edges list
    edges.append((x,y))

count = 0

# for each edge
for e in edges:
    (x,y) = e
    if search(x,y):
        count += 1
        adj[x].remove(y)
        adj[y].remove(x)

print count