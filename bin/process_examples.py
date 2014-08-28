#!/usr/bin/env python

import json
import os
import re
import sys

source = os.getenv('EXAMPLE_SOURCE', None)
if source is None:
    print "The environment variable 'EXAMPLE_SOURCE' must be set"
    sys.exit(1)

dest = os.getenv('DEST', None)
if dest is None:
    print "The environment variable 'DEST' must be set"
    sys.exit(1)

# Read the given file in as a JSON object
def read_json(fn):
    fd = open(fn, 'r')
    try:
        json_str = fd.read()
        jo = json.loads(json_str)
    finally:
        fd.close()
    return jo

def write_markdown(jo, fn):

    fd = open(fn, 'w')
    try:
        fd.write('{\n')
        fd.write('\t"title": "%s",\n' % (jo['name'], ))
        fd.write('\t"layout": "default"\n')
        fd.write('}\n')

        if 'note' in jo:
            fd.write('%s\n' % (jo['note'], ))

        if 'args' in jo:
            fd.write('# Arguments\n')
            for line in json.dumps(jo['args'], indent=2).split('\n'):
                fd.write('\t%s\n' % (line, ))

        fd.write('# Query\n')
        for line in json.dumps(jo['query'], indent=2).split('\n'):
            fd.write('\t%s\n' % (line, ))

        fd.write('# Results\n')
        for line in json.dumps(jo['result'], indent=2).split('\n'):
            fd.write('\t%s\n' % (line, ))
    finally:
        fd.close()

def numbers_only(x):
    r = re.compile('(\d+)')
    l = r.split(x)
    return [int(y) if y.isdigit() else y for y in l]

index = open(os.path.join(dest, 'index.md'), 'w')
index.write('{\n')
index.write('\t"title": "jsonq examples",\n')
index.write('\t"layout": "default"\n')
index.write('}\n')

for root, dirs, files in os.walk(source):

    path_splits = os.path.split(root)
    if 'schema' == path_splits[-1]:
        continue
    index.write('# %s\n' % (path_splits[-1], ))

    files.sort(key = numbers_only)
    for f in files:
        if not f.endswith('.json'):
            continue
        dest_dir = os.path.join(dest, path_splits[-1])
        file_splits = f.split('.')
        example = file_splits[0]
        dest_file = example + '.md'
        if not os.access(dest_dir, os.F_OK):
            os.mkdir(dest_dir)

        try:
            jo = read_json(os.path.join(root, f))
            index.write('[%s](%s)\n\n' % (jo['name'], path_splits[-1] + '/' + example))

        except ValueError as e:
            print "Error reading %s" % (os.path.join(root, f))
            raise e

        write_markdown(jo, os.path.join(dest_dir, dest_file))

index.close()
