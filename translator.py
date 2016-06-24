#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def binary(value, bits):
    return "{0:b}".format(int(value)).zfill(bits)

def hexadecimal(value):
    aux = hex(int(value, 2)).zfill(6)
    if len(aux) > 6:
        aux = aux[1:]
    return aux

if __name__ == "__main__":
    pc = 0

    registers_h = ['.a', '.b']
    rr = ['01', '10']
    l = ['0', '1']
    ic = ['10', '11']

    repo_name = "./Assembly/"
    repo_name_hex = "./Test/"
    file_name = sys.argv[1]
    file = open(repo_name+file_name, "r")

    with file as f:
        content = f.readlines()

    instructions = ['\n'] * len(content)
    inst_hex = []
    file.close()

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
            instructions[i] = pcount + '0' + '00' + l[registers_h.index(params[1])] + '000' + rr[registers_h.index(params[0])] + '00' + '00000000'
        elif command == "inc":
            instructions[i] = pcount + '0' + '0' + ic[registers_h.index(params[0])] + '000' + rr[registers_h.index(params[0])] + '00' + '00000000'
        elif command == "and":
            instructions[i] = pcount + '0' + '110' + '10000' + '00' + '00000000'
        elif command == "or":
            instructions[i] = pcount + '0' + '111' + '10000' + '00' + '00000000'
        elif command == "jump":
            instructions[i] = pcount + '1' + '001' + '10000' + '11' + binary(params[0], 8)
        elif command == "load":
            instructions[i] = pcount + '0' + '001' + '01000' + '11' + binary(params[0], 8)
            pc += 1
            instructions.insert(i, binary(pc, 5) + '0' + '001' + '000' + rr[registers_h.index(params[0])] + '01' + '00000000')
        elif command == "end":
            instructions[i] = '00000' + '0' + '000' + '00000' + '00' + '00000000'

    for i in range(0, len(instructions)):
        inst_hex.append(hexadecimal(instructions[i]))
        inst_hex[i] = inst_hex[i].replace('x', '')

    file_name = file_name.split(".")
    file_name = file_name[0]+".hex"
    output = open(repo_name_hex+file_name, "w+")

    output.write("v2.0 raw\n")
    for i in range(0, len(inst_hex)):
        output.write(inst_hex[i]+"\n")