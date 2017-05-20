import hashlib

f=open('md5_hash_table.txt','w')

i=1

while i < 10000:
	result = hashlib.md5(str(i).encode('utf-8')).hexdigest()
	f.write(result+'@'+ str(i)+'\n')
	
	i=i+1;

f.close()
print ("Successful")

# c4ca4238a0b923820dcc509a6f75849b 1
# 373e4c5d8edfa8b74fd4b6791d0cf6dc@4734