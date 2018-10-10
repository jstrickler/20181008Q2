#!/usr/bin/env python
import shlex
from glob import glob

from subprocess import run, PIPE, CalledProcessError

raw_cmd = 'netstat -anz'
cmd = shlex.split(raw_cmd)
print(cmd)

file_args = glob('*.txt')
print(file_args)

try:
    result = run(cmd + file_args, stdout=PIPE, stderr=PIPE, check=True)
except CalledProcessError as err:
    print("RETURN CODE:", err.returncode)
else:
    print(result.stdout[:100].decode())
    print(result.stderr.decode())
    print(result.returncode)


x = run('sleep 5'.split())
print('done')
