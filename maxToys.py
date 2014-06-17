# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
  #Compute and return final answer over here
  # iterate through the..pop the min each time until you rupees
  total = 0
  count = 0
  print prices
  while total < rupees:
  	amount = prices.pop(prices.index(min(prices)))
  	total+=amount
  	count+=1
  total-=amount
  count-=1
  return count

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)
