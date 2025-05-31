import sys
print(f"sys.prefix: {sys.prefix}")
print(f"sys.base_prefix: {sys.base_prefix}")
if sys.prefix == sys.base_prefix:
    print("You are not in a virtual environment.")
else:
    print("You are in a virtual environment.")