import hashlib

f=open('sha1_hash_table.txt','w')

i=1

while i < 10000:
	result = hashlib.sha1(str(i).encode('utf-8')).hexdigest()
	f.write(result+'@'+str(i)+'\n')

	i=i+1;

f.close()
print ("Successful")

# 9e68b941fd96f1bf527ed09293dccf778f16f514@5235