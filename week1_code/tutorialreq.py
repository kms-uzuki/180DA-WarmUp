#!/usr/bin/env

import random
import time
import sys

print("printing 10 random ints between 0 and 100...")

for i in range(0,10):
	print(random.randint(0,100), end=' ')
	sys.stdout.flush()
	time.sleep(0.5)
print('\nDone!')
