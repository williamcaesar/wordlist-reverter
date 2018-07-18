#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Edit wordlists."""


class Raptor(object):
    """Modifies wordlists."""

    def __init__(self, input_file, output_file):
        """Init the class."""
        self.input_file = input_file
        self.output_file = output_file

    def __str__(self):
        """Write a sound."""
        return('rawwrr!')

    def cut_from(self, wordlist, start):
        """Cut a wordlist starting from a item."""
        new_word = []
        i = 0
        while (i < len(wordlist)):
            if start <= i:
                new_word.append(wordlist[i])
            i += 1
        return new_word

    def cut_until(self, wordlist, stop):
        """Cut a wordlist from the start to a designated end."""
        new_word = []
        i = 0
        while (i < len(wordlist)):
            if stop >= i:
                new_word.append(wordlist[i])
            i += 1
        return new_word

    def write_reverted(self):
        """Write a reverted wordlist to a file."""
        reverted = revert(format_file(self.input_file))
        write(reverted, self.output_file)


def format_file(file_path):
    """Prepare the file to use."""
    file = open(file_path, 'r')
    objfile = file.readlines()
    file.close()
    return objfile


def write(input, output):
    """Write a input list to a file."""
    file = open(str(output), 'w')
    for each in input:
        file.write(each)
    file.close()


def revert(wlist):
    """Return a reversed list."""
    reversed_final = []
    rlist = reversed(wlist)
    for each in rlist:
        reversed_final.append(each)
    return reversed_final
