import hashlib
import time
import sys

#TODO1: bruteforce all combination of lower case upper case, substitution
#dog -> (d,D) (o,O,0) (g,G)

def gen_comb(passw,idx):
  if idx>=len(passw):
    return [passw]
  if passw[idx].isdigit():
    return gen_comb(passw,idx+1)
  if passw[idx] == 'o':
    return gen_comb(passw[:idx]+'o'+passw[idx+1:],idx+1)+gen_comb(passw[:idx]+'O'+passw[idx+1:],idx+1)+\
           gen_comb(passw[:idx]+'0'+passw[idx+1:],idx+1)
  elif passw[idx] == 'l':
    return gen_comb(passw[:idx]+'l'+passw[idx+1:],idx+1)+gen_comb(passw[:idx]+'L'+passw[idx+1:],idx+1)+\
           gen_comb(passw[:idx]+'1'+passw[idx+1:],idx+1)
  elif passw[idx] == 'i':
    return gen_comb(passw[:idx]+'i'+passw[idx+1:],idx+1)+gen_comb(passw[:idx]+'I'+passw[idx+1:],idx+1)+\
           gen_comb(passw[:idx]+'1'+passw[idx+1:],idx+1)
  else:
    return gen_comb(passw[:idx]+passw[idx].lower()+passw[idx+1:],idx+1)+\
           gen_comb(passw[:idx]+passw[idx].upper()+passw[idx+1:],idx+1)



#TODO1: ########################################################

hash_value = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"
file = open("tenk-most-common.txt",'r')

for line in file:
  comb = gen_comb(line.strip(),0)
  for passw in comb:
    m = hashlib.sha1(passw.encode()).hexdigest()
    if m == hash_value:
      print("original password: "+passw.strip())
      print("method: sha1")
      break
    m = hashlib.md5(passw.encode()).hexdigest()
    if m == hash_value:
      print("original password: "+passw.strip())
      print("method: md5")
      break
    
file.close()


#TODO2: ########################################################

rainbow_table = {}
file = open("tenk-most-common.txt",'r')

# Start the timer
start_time = time.time()  

for line in file:
  comb = gen_comb(line.strip(),0)
  for passw in comb:
    m = hashlib.sha1(passw.encode()).hexdigest()
    rainbow_table[m] = passw

# End the timer
end_time = time.time()
elapsed_time = end_time - start_time
rainbow_table_size = sys.getsizeof(rainbow_table)

print(f"Elapsed time: {elapsed_time} seconds")
print(f"Size of rainbow_table: {rainbow_table_size} bytes")

file.close()


#TODO3 ########################################################
#calculate mean time -> get C

file = open("tenk-most-common.txt",'r')
acc_time = 0
passw_count = 0

for line in file:
  comb = gen_comb(line.strip(),0)
  for passw in comb:
    passw_count += 1
    start_time = time.time()  
    m = hashlib.sha1(passw.encode()).hexdigest()
    end_time = time.time()
    acc_time += (end_time - start_time)

print(f"Hash(sha1) mean time: {acc_time/passw_count} seconds per password")

file.close()

#(95**n password)* c second/password


