def rotate(l,n):
	return l[n:] + l[:n]

N = input()
nums = [int(i) for i in raw_input().split()]
PMEAN=0
# keep rotating the array...get all the PMEANS
for z in xrange(N):
	newPMEAN=0
	for i in xrange(N):
		newPMEAN=(nums[i]*(i+1))+newPMEAN
	if newPMEAN > PMEAN: 
		PMEAN = newPMEAN
	nums = rotate(nums,z+1)
print PMEAN