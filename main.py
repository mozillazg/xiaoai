# -*- coding: utf-8 -*-

import os
import aiml
import sys
from aiml.Kernel import k

loadfiles = ['aiml_set/main.xml']

def loadlearnfiles(kernel, files):
    for file in files:
        kernel.learn(file)

if __name__ == '__main__':
    loadlearnfiles(k, loadfiles)
    while True:
        print k.respond(raw_input('>').decode(sys.stdin.encoding)).decode('utf8')
