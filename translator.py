#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def binary(value, bits):
    return "{0:b}".format(int(value)).zfill(bits)

def hexadecimal(value):
    return hex(int(value, 2)).zfill(6).strip('x')

if __name__ == "__main__":
    pc = 0

    registers_h = ['.a', '.b']
    rr = ['01', '10']
    l = ['0', '1']
    ic = ['10', '11']

    repo_name = "./Assembly/"
    file_name = repo_name+sys.argv[1]
    file = open(file_name, "r")

    with file as f:
        content = f.readlines()

    instructions = ['\n'] * len(content)

    for i in range(0, len(content)):
        pc += 1
        line = content[i].strip('\n')
        pcount = binary(pc, 5)

        func = line.split(" ", 1)
        params = func[1:][0].replace(' ', '').split(",")
        command = func[0]

        if command == "input":
            instructions[i] = pcount + '0' + '001' + '000' + rr[registers_h.index(params[0])] + '11' + binary(params[1], 8)
        elif command == "print":
            instructions[i] = pcount + '0' + '00' + l[registers_h.index(params[0])] + '10000' + '00' + '00000000'
        elif command == "add":
            instructions[i] = pcount + '0' + '100' + '000' + rr[registers_h.index(params[0])] + '00' + '00000000'
        elif command == "sub":
            instructions[i] = pcount + '0' + '101' + '000' + rr[registers_h.index(params[0])] + '00' + '00000000'
        elif command == "mov":
            instructions[i] = pcount + '0' + '00' + l[registers_h.index(params[0])] + '000' + rr[registers_h.index(params[0])] + '00' + '00000000'
        elif command == "inc":
            instructions[i] = pcount + '0' + '0' + ic[registers_h.index(params[0])] + '000' + rr[registers_h.index(params[0])] + '00' + '00000000'
        elif command == "and":
            instructions[i] = pcount + '0' + '110' + '10000' + '00' + '00000000'
        elif command == "or":
            ##### 0 111 10000 00 00000000
            instructions[i] = pcount + '0' + '111' + '10000' + '00' + '00000000'




    print instructions