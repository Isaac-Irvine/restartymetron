#!/usr/bin/env python
from sys import argv
from os import system
from time import time, sleep

if len(argv) > 1 and argv[1].lower() in ('help', '-h'):
    print('Restartymetron is a program that will restart any program unless it fails in less than the timeout')
    print('usage: restartymetron.py <timeout> <command>')
    print('time out is in seconds')
    print('e.g. restartymetron.py 120 java -jar server.jar')
    exit()

if len(argv) < 3:
    print('Not enough arguments.')
    print('for help use: restartymetron.py help')
    exit()

timeout = int(argv[1])
command = ' '.join(argv[2:])

print("Restartymetron: Starting program")

last_time = time()
system(command)

while last_time + timeout < time():
    last_time = time()
    print("Restartymetron: Restarting program in 60s unless interrupted...")
    sleep(60)
    system(command)

print("Restartymetron: program ended before timeout")
