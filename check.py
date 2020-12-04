# check how much work a hash is worth

import secrets, mpmath, binascii, argon2, sys

def divide(n):
  return (2 ** 1024) // int(str(n)[2:-1], 16)

def run(salt, min):
  salt = str(salt)
  input = 'c79855a0f5344b655b8bc30220b545e2ef25b88b723745b7fed976d46e260c91' # hash of https://is.gd/Bartha
  result = divide(binascii.hexlify(argon2.argon2_hash(input,salt)))
  return result > min

#print(run(str(sys.argv[1]), int(sys.argv[2]))
#print(run(93030099920246021383870012056218634088444129896882436080405974462911109459767, 100))
print(run(sys.argv[1], int(sys.argv[2])))
