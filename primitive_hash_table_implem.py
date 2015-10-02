#with chaining
table = [[] for x in range(10)]

def hash_function(x): return x % 10

def insert(table,input,value): table[hash_function(input)].append((input,value))


insert(table,41,'apple')
print table

insert(table,93,'banana')
print table

insert(table,13,'tangerine')

print table
