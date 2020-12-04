# this is a program that is desinged to resist ASIC attack
# the purpose of argon2 is to make it so that you cannot lie about how much
# effort you used so easily

import secrets, mpmath, binascii, argon2, sys

def divide(n):
        return (2 ** 1024) // int(n, 16)

def run(x):
  input = 'c79855a0f5344b655b8bc30220b545e2ef25b88b723745b7fed976d46e260c91' # (SHA256) hash of https://is.gd/Bartha
  result = 0
  count = 0
  while result < x:
    salt = str(secrets.randbits(257))
    result = divide(binascii.hexlify(argon2.argon2_hash(input,salt)))
    data = salt
    count += 1
  return [data, int(result), count]

print(run(int(sys.argv[1])))
