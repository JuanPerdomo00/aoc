#!/usr/bin/python3
# -*- coding: utf8 -*-
# By: Jakepy

def read_lined_file():
    with open('./input.txt', 'r', encoding='utf-8') as f:
        file = f.readlines()
        enum = {}

        lista = [ls.replace('\n', '') for ls in file]
        
        for line in lista:
            numbers = ''.join(ch for ch in line if ch.isdigit())
            if numbers:
                enum[line.strip()] = numbers        

        return enum



def main():
    suma = []
    for _, value in read_lined_file().items():
        value += value if len(value) == 1 else ""
        value = value[0] + value[-1] if len(value) >= 3 else value
        suma.append(int(value))
    
    print(sum(suma))

if __name__ == "__main__":
    main()
