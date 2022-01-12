# 해시 알고리즘
import hashlib
hash = input()
print(hashlib.sha256(hash.encode()).hexdigest())
