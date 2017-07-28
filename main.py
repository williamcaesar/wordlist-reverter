#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import optparse
parser = optparse.OptionParser()
parser.add_option('-f', '--file')
parser.add_option('-o','--output')
parser.parse_args()
options = parser.values

def format_file():
    file = open(options.__dict__['file'], 'r')
    objfile = file.readlines()
    return objfile

def revert(list):
    reversed_final = []
    rlist = reversed(list)
    for eachit in rlist:
        reversed_final.append(eachit)
    return reversed_final

def write_in(list):
    file = open(options.__dict__['output'],'w')
    for eachit in list:
        file.write(eachit)


def main():
    x = revert(format_file())
    write_in(x)

if __name__ == '__main__':
    main()