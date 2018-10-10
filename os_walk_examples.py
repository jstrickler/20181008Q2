#!/usr/bin/env python
import os

START_DIR = '.'

for curr_dir, sub_dirs, file_names in os.walk(START_DIR):
    if '.git' in curr_dir:
        continue
    print(curr_dir)
    for file_name in file_names:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:6d} {file_name}")

