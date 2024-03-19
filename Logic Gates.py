from gatelibrary import *

def truth_table(index):
    return gate_data[index]['truth_table']
    
def gate_func(index):
    return gate_data[index]['func']

def menu():
    print('Would you like: ')
    for n, data in enumerate(gate_data):
        print(f'{n+1}) {data["name"]}')
    
    item = int(input(': '))
    
    res = input('Would you like to see the truth table (1) or enter two inputs for an output (2)?: ')
    if res == '1':
        print(truth_table(item - 1))
    else:
        func = gate_func(item - 1)
        num = int(input('\nEnter 1 or 0: '))
        
        if func != not_gate:
            num1 = int(input('Enter 1 or 0: '))
            print(f' Output = {func(num, num1)}')
        else:
            print(f' Output = {func(num)}')


gate_data = [
    {
        'name': 'AND gate',
        'func': and_gate,
        'truth_table': f"""
             - AND -
             0, 0, {and_gate(0,0)}
             0, 1, {and_gate(0,1)}
             1, 0, {and_gate(1,0)}
             1, 1, {and_gate(1,1)}""" }, 
    {
        'name': 'OR gate',
        'func': or_gate,
        'truth_table': f"""
             - OR -
             0, 0, {or_gate(0,0)}
             0, 1, {or_gate(0,1)}
             1, 0, {or_gate(1,0)}
             1, 1, {or_gate(1,1)}""" },
    {
        'name': 'NOT gate',
        'func': not_gate,
        'truth_table': f"""
            - NOT -
            0, {not_gate(0)}
            1, {not_gate(1)}""" },
    {
        'name': 'XOR gate',
        'func': xor_gate,
        'truth_table': f"""
             - XOR -
             0, 0, {xor_gate(0,0)}
             0, 1, {xor_gate(0,1)}
             1, 0, {xor_gate(1,0)}
             1, 1, {xor_gate(1,1)}""" },
    
    {
        'name': 'NAND gate',
        'func': nand_gate,
        'truth_table': f"""
             - NAND -
             0, 0, {nand_gate(0,0)}
             0, 1, {nand_gate(0,1)}
             1, 0, {nand_gate(1,0)}
             1, 1, {nand_gate(1,1)}""" },
    
    {
        'name': 'NOR gate',
        'func': nor_gate,
        'truth_table': f"""
             - NOR -
             0, 0, {nor_gate(0,0)}
             0, 1, {nor_gate(0,1)}
             1, 0, {nor_gate(1,0)}
             1, 1, {nor_gate(1,1)}""" },
    
    {
        'name': 'XNOR gate',
        'func': xnor_gate,
        'truth_table': f"""
             - XNOR -              
             0, 0, {xnor_gate(0,0)}
             0, 1, {xnor_gate(0,1)}
             1, 0, {xnor_gate(1,0)}
             1, 1, {xnor_gate(1,1)}""" }
]


menu()

