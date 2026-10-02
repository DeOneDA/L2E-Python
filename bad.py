# print("About to crash")
# print(10 / 0)
import sys

print("stdout version")
print("stderr version", file = sys.stderr)
