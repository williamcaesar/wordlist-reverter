#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Example of use of Raptor Wordlist editor."""
from raptor import Raptor
import argparse
actions = ['reverse', 'write', 'hello']


def setup_args():
    """Setups CLI arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        dest='file',
                        help='Input file',
                        type=str)

    parser.add_argument('-o', '--output',
                        dest='output',
                        help='Output file',
                        type=str)

    parser.add_argument('-i', '--init',
                        dest='init',
                        help='Line to start the cut',
                        type=int)

    parser.add_argument('-e', '--end', dest='end',
                        help='Line to end the cut',
                        type=int)

    parser.add_argument('-a', '--action', dest='action',
                        help='The action to be done',
                        choices=actions,
                        type=str)
    args = parser.parse_args()
    return args


args = setup_args()
word = Raptor(args.file, args.output)
action = args.action
word.write_reverted()
