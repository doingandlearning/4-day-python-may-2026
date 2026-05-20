import os

files = [f for f in os.listdir('.') if f.endswith('.json')]
print(files)