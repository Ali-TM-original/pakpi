import jwt
import random
import string

letters = string.ascii_lowercase
token = ''.join(random.choice(letters) for i in range(10))


encoded = jwt.encode({'tok': token}, "secret", algorithm="HS256")
print("encoded: "+encoded)


""" USE FOR LATER PROJECTS """
decoded = jwt.decode(encoded, "secret", algorithms=["HS256"])
print(f"decoded :{decoded['tok']}")
