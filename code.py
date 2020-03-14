from hashlib import sha256
import secrets, mpmath

def divide(n):
        return (2 ** 256) / int(n, 16)

def run(n):
  input = 'c79855a0f5344b655b8bc30220b545e2ef25b88b723745b7fed976d46e260c91' # hash of https://is.gd/Bartha
  result = 0
  count = 0
  x = int(2**n)
  while result < x:
    data = str(secrets.randbits(257)) + " " + input
    result = divide(sha256(data.encode('utf-8')).hexdigest())
    count += 1
  return [data, int(result), count]

print(run(22))
