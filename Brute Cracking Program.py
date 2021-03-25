import sys
import os
import time
#Gets input file
inputNum = open('info.txt','r', encoding="utf-8")
clck = time.perf_counter()
for line in inputNum:
	#splits lines up
	nums = line.split()
	str = ""
	i = 0
	for i in range(len(nums)):
		#seperates parts of lines, into first six, last four and hash
		str += nums[i]
		str += " "
		i += 1
	cmd = "python3 Hashing.py %s"%(str)
	os.system(cmd)
clock = time.perf_counter()
print(f'Cracked in: {clock - clck:0.4f} seconds')


