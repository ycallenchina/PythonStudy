

import hashlib

md5=hashlib.sha256()

md5.update('effy.2'.encode('utf-8'))
print(md5.hexdigest())

