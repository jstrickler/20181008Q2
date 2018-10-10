#!/usr/bin/env python
import os
from datetime import datetime

FOLDER = 'DATA'
FILE = 'alice.txt'

file_path = os.path.join(FOLDER, FILE)

print("File path:", file_path)

print(os.path.getsize(file_path))

print("Dir name:", os.path.dirname(file_path))
print("Base name:", os.path.basename(file_path))
print("Abs path:", os.path.abspath(file_path))
print("Abs path:", os.path.splitext(file_path))

print(os.path.splitext('foo.bar.blah.baz'))

raw_ts = os.path.getmtime(file_path)
print('raw timestamp:', raw_ts)
ts = datetime.fromtimestamp(raw_ts)
print("Timestamp:", ts)
print('-' * 60)

for file_obj in os.scandir('NOTEBOOKS'):
    print(file_obj.name, file_obj.is_file())





