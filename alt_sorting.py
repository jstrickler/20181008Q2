#!/usr/bin/env python

data = [
    'chr1', 'chr2', 'chrUN', 'chrX', 'chr22', 'chr10', 'chr3', 'chr19',
    'chry', 'chr8'
]

def by_number(item):
    raw_num = item.replace('chr', '').lower()
    if raw_num == 'x':
        return 999999
    elif raw_num == 'y':
        return 1000000
    elif raw_num.isdigit():
        return int(raw_num)
    else:
        return 1000001

sorted_data = sorted(data, key=by_number)
print(sorted_data)
