T = input()
for i in xrange(T):
	N,K = [int(i) for i in raw_input().split()]
	A = [int(i) for i in raw_input().split()]
	B = [int(i) for i in raw_input().split()]
	A = sorted(A)
	B = sorted(B,reverse=True)
	z=0
	while A[z]+B[z] >= K and z < len(A):
		z+=1
		if z+1 > len(A):
			break;
	if z == len(A):
		print "YES"
	else:
		print "NO"
# T = input()
# for i in xrange(T):
# 	N,K = [int(i) for i in raw_input().split()]
# 	A = [int(i) for i in raw_input().split()]
# 	B = [int(i) for i in raw_input().split()]

# 	if sum(A)+sum(B) >= (N*K):
# 		print "YES"
# 	else:
# 		print "NO"