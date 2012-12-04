#!/usr/bin/python

"""analyze.py

Run an analysis of a directory of non-translated ("O") and
translated ("T") files. Analysis will be performed based on
selected properties and output to stdout in ARFF format, suitable
for use with weka."""

import os
import sys
import translationese

def analyze_file(f, module):
    analysis = translationese.Analysis(f)

    return module.quantify(analysis)

def analyze_directory(dir_to_analyze, expected_class, module, stream):
    for filename in os.listdir(dir_to_analyze):
        with open(os.path.join(dir_to_analyze, filename)) as f:
            result = analyze_file(f, module)

            stream.write(expected_class)
            stream.write(",")

            line = ",".join([str(result[x]) for x in module.attributes])
            print >> stream, line

def main(module, o_dir, t_dir, stream=sys.stdout):
    attributes = module.attributes

    print >> stream, "@relation translationese"
    print >> stream, "@attribute class { T, O }"

    for attribute in attributes:
        print >> stream, "@attribute %s numeric" % repr(attribute)

    print >> stream
    print >> stream, "@data"

    analyze_directory(o_dir, "O", module, stream)
    analyze_directory(t_dir, "T", module, stream)

def usage(due_to_error=True):
    print """\
Usage: %s MODULE O_DIR T_DIR

    MODULE  Analysis module
    O_DIR   Directory containing non-translated texts
    T_DIR   Directory containing translated texts""" % sys.argv[0]
    if due_to_error: sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 4: usage()

    module_name, o_dir, t_dir = sys.argv[1:]

    module = __import__("translationese.%s" % module_name, \
                        fromlist=module_name)

    main(module, o_dir, t_dir)
