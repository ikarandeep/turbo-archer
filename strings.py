chars = [i for i in raw_input()]
charsUnique = set(chars)
counts = [chars.count(char) for char in charsUnique]
print(list(charsUnique)[counts.index(max(counts))])
print(list(charsUnique)[counts.index(min(counts))])