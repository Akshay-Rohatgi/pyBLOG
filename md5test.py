import hashlib
text = "default_pass"


hash_object = hashlib.md5(text.encode())
md5_hash = hash_object.hexdigest()
print(md5_hash)