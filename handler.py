def read_circuit_file(name):
    file = open("isc_sample_files/" + name,'r')
    lines = file.readlines()

    data = []
    flag = False

    for i in range(len(lines)):
        if(lines[i][0] != '*'):
            flag = True
        
        if(flag):
            splited = lines[i].split()
            if(len(splited) <= 3):
                data[-1] = data[-1] + splited
            elif(splited[2] == 'from'):
                for i in data:
                    if splited[3] in i:
                        splited.append(i[0])
                        break
                data.append(splited)
            else:
                data.append(splited)

    return data



def read_input_file(address):
    file = open(address, 'r')
    lines = file.readlines()
    data = []
    for i in range(1, len(lines)):
        splited = lines[i].split()
        if len(splited) == 1:
            splited.append('Z')
        data.append(splited)

    return data



def find_node_data(id, circuit_data):
    for item in circuit_data:
        if(item[0] == id):
            return item
    return None



def find_gate_output(data, node_values):
    if(data != None):
        if(data[2] == 'and'):
            return AND(data[-2], data[-1], node_values)
        elif(data[2] == 'nand'):
            return NAND(data[-2], data[-1], node_values)
        elif(data[2] == 'or'):
            return OR(data[-2], data[-1], node_values)
        elif(data[2] == 'nor'):
            return NOR(data[-2], data[-1], node_values)
        elif(data[2] == 'xor'):
            return XOR(data[-2], data[-1], node_values)
        elif(data[2] == 'xnor'):
            return XNOR(data[-2], data[-1], node_values)
        elif(data[2] == 'not'):
            return NOT(data[-1], node_values)
        elif(data[2] == 'buff'):
            return BUFF(data[-1], node_values)
        elif(data[2] == 'from'):
            return BUFF(data[-1], node_values)
        else:
            print("unknown gate")
            return None



def AND(id1, id2, node_values):
    value1 = node_values[id1]
    value2 = node_values[id2]
    if(value1 == '0' or value2 =='0'):
        return '0'
    elif(value2 =='1' and value1 == '1'):
        return '1'
    elif(value1 == 'd_f' and value2 == '1') or (value2 == 'd_f' and value1 == '1'):
        return 'd_f'
    elif(value1 == 'd_not_f' and value2 == '1') or (value2 == 'd_not_f' and value1 == '1'):
        return 'd_not_f'
    else:
        return 'U'



def NAND(id1, id2, node_values):
    value1 = node_values[id1]
    value2 = node_values[id2]
    if(value1 == '0' or value2 == '0'):
        return '1'
    elif(value2 == '1' and value1 == '1'):
        return '0'
    elif(value1 == 'd_f' and value2 == '1') or (value2 == 'd_f' and value1 == '1'):
        return 'd_not_f'
    elif(value1 == 'd_not_f' and value2 == '1') or (value2 == 'd_not_f' and value1 == '1'):
        return 'd_f'
    else:
        return 'U'


def OR(id1, id2, node_values):
    value1 = node_values[id1]
    value2 = node_values[id2]
    if(value1 == '1' or value2 == '1'):
        return '1'
    elif(value2 == '0' and value1 == '0'):
        return '0'
    elif(value1 == 'd_f' and value2 == '0') or (value2 == 'd_f' and value1 == '0'):
        return 'd_f'
    elif(value1 == 'd_not_f' and value2 == '0') or (value2 == 'd_not_f' and value1 == '0'):
        return 'd_not_f'
    else:
        return 'U'
    


def NOR(id1, id2, node_values):
    value1 = node_values[id1]
    value2 = node_values[id2]
    if(value1 == '1' or value2 == '1'):
        return '0'
    elif(value2 =='0' and value1 == '0'):
        return '1'
    elif(value1 == 'd_f' and value2 == '0') or (value2 == 'd_f' and value1 == '0'):
        return 'd_not_f'
    elif(value1 == 'd_not_f' and value2 == '0') or (value2 == 'd_not_f' and value1 == '0'):
        return 'd_f'
    else:
        return 'U'


def XOR(id1, id2, node_values):
    value1 = node_values[id1]
    value2 = node_values[id2]
    if(value1 == 'U' or value2 == 'U' or value1 == 'Z' or value2 == 'Z'):
        return 'U'
    elif(value1 == value2):
        return '0'
    elif(value1 == 'd_f' and value2 == '0') or (value2 == 'd_f' and value1 == '0'):
        return 'd_f'
    elif(value1 == 'd_f' and value2 == '1') or (value2 == 'd_f' and value1 == '1'):
        return 'd_not_f'
    elif(value1 == 'd_not_f' and value2 == '0') or (value2 == 'd_not_f' and value1 == '0'):
        return 'd_not_f'
    elif(value1 == 'd_not_f' and value2 == '1') or (value2 == 'd_not_f' and value1 == '1'):
        return 'd_f'
    else:
        return '1'


def XNOR(id1, id2, node_values):
    value1 = node_values[id1]
    value2 = node_values[id2]
    if(value1 == 'U' or value2 == 'U' or value1 == 'Z' or value2 == 'Z'):
        return 'U'
    elif(value1 == value2):
        return '1'
    elif(value1 == 'd_f' and value2 == '0') or (value2 == 'd_f' and value1 == '0'):
        return 'd_not_f'
    elif(value1 == 'd_f' and value2 == '1') or (value2 == 'd_f' and value1 == '1'):
        return 'd_f'
    elif(value1 == 'd_not_f' and value2 == '0') or (value2 == 'd_not_f' and value1 == '0'):
        return 'd_f'
    elif(value1 == 'd_not_f' and value2 == '1') or (value2 == 'd_not_f' and value1 == '1'):
        return 'd_not_f'
    else:
        return '0'


def NOT(id, node_values):
    value = node_values[id]
    if(value == 'U' or value == 'Z'):
        return 'U'
    elif(value == '0'):
        return '1'
    elif(value == '1'):
        return '0'
    elif(value == 'd_f'):
        return 'd_not_f'
    elif(value == 'd_not_f'):
        return 'd_f'

        
def BUFF(id, node_values):
    value = node_values[id]
    if(value == 'U' or value == 'Z'):
        return 'U'
    elif(value == '0'):
        return '0'
    elif(value == '1'):
        return '1'
    elif(value == 'd_f'):
        return 'd_f'
    elif(value == 'd_not_f'):
        return 'd_not_f'


def get_node_values(input_data, circuit_data):
    node_values = {}
    for item in input_data:
        node_values[item[0]] = item[1]

    for item in circuit_data:
        if(item[0] not in node_values):
            line = find_node_data(item[0], circuit_data)
            gate_output = find_gate_output(line, node_values)
            node_values[item[0]] = gate_output
    return node_values



# fault equivalence and fault dominance

def equivalence_faults_check(circuit_data):
    for item in circuit_data:

        if item[2] != 'inpt' and item[2] != 'from':

            for data in circuit_data:
                if data[0] == item[-1]:
                    inpt1 = data
                elif data[0] == item[-2]:
                    inpt2 = data

            if item[2] == 'and' and '>sa0' in item:
                if '>sa0' in inpt1:
                    inpt1[inpt1.index('>sa0')] = '***'
                if '>sa0' in inpt2:
                    inpt2[inpt2.index('>sa0')] = '***'

            elif item[2] == 'nand' and '>sa1' in item:
                if '>sa0' in inpt1:
                    inpt1[inpt1.index('>sa0')] = '***'
                if '>sa0' in inpt2:
                    inpt2[inpt2.index('>sa0')] = '***'

            elif item[2] == 'or' and '>sa1' in item:
                if '>sa1' in inpt1:
                    inpt1[inpt1.index('>sa1')] = '***'
                if '>sa1' in inpt2:
                    inpt2[inpt2.index('>sa1')] = '***'

            elif item[2] == 'nor' and '>sa0' in item:
                if '>sa1' in inpt1:
                    inpt1[inpt1.index('>sa1')] = '***'
                if '>sa1' in inpt2:
                    inpt2[inpt2.index('>sa1')] = '***'

            elif item[2] == 'not' and '>sa0' in item:
                if '>sa1' in inpt1:
                    inpt1[inpt1.index('>sa1')] = '***'

            elif item[2] == 'not' and '>sa1' in item:
                if '>sa0' in inpt1:
                    inpt1[inpt1.index('>sa0')] = '***'

            elif item[2] == 'buff' and '>sa0' in item:
                if '>sa0' in inpt1:
                    inpt1[inpt1.index('>sa0')] = '***'

            elif item[2] == 'buff' and '>sa1' in item:
                if '>sa1' in inpt1:
                    inpt1[inpt1.index('>sa1')] = '***'



# primitive D-Cube

def pdf(circuit_data, input_data, circuit_name):    
    for item in circuit_data:
        if '>sa0' in item:
            item[item.index('>sa0')] = 'd_f'
            fault_dic = fault_prop('d_f', item, circuit_data)
            get_fault_vec(fault_dic, input_data, '%s sa0' % item[1], circuit_name)
        if '>sa1' in item:
            item[item.index('>sa1')] = 'd_not_f'
            fault_dic = fault_prop('d_not_f', item, circuit_data)
            get_fault_vec(fault_dic, input_data, '%s sa1' % item[1], circuit_name)



# D-Drive and fault propagation path

def fault_prop(primitive_fault_value, item, circuit_data):
    prop_matrix = {}
    prop_matrix[item[0]] = primitive_fault_value
    gate = d_frontier(prop_matrix, circuit_data, 0)
    temp = list(prop_matrix.keys())[-1]
    while gate != None:
        if (gate[-1] == temp):
            if ('and' in gate) or ('nand' in gate):
                prop_matrix[gate[-2]] = '1'
            elif ('or' in gate) or ('nor' in gate) or ('xor' in gate) or ('xnor' in gate):
                prop_matrix[gate[-2]] = '0'
            prop_matrix[gate[0]] = find_gate_output(gate, prop_matrix)

            for data in circuit_data:
                if 'from' in data and data[0] == gate[-2]:
                    for i in circuit_data:
                        if i[-1] == data[-1] or i[0] == data[-1]:
                            prop_matrix[i[0]] = prop_matrix[data[0]]
                    break

        elif (gate[-2] == temp):
            if ('and' in gate) or ('nand' in gate):
                prop_matrix[gate[-1]] = '1'
            elif ('or' in gate) or ('nor' in gate) or ('xor' in gate) or ('xnor' in gate):
                prop_matrix[gate[-1]] = '0'
            prop_matrix[gate[0]] = find_gate_output(gate, prop_matrix)
            
            for data in circuit_data:
                if 'from' in data and data[0] == gate[-1]:
                    for i in circuit_data:
                        if i[-1] == data[-1] or i[0] == data[-1]:
                            prop_matrix[i[0]] = prop_matrix[data[0]]
                    break

        temp = gate[0]

        if 'from' in gate:
            for data in circuit_data:
                if data[-1] == gate[-1]or data[0] == gate[-1]:
                    prop_matrix[data[0]] = prop_matrix[gate[0]]
        
        gate = d_frontier(prop_matrix, circuit_data, gate[0])
        
    return consistency(circuit_data, prop_matrix)
        
        
import random


# D-Frontier and update it

def d_frontier(prop_matrix, circuit_data, checked):
    for item in reversed(circuit_data):
        if (item[0] == checked):
            return None
        elif (item[-1] in prop_matrix) or (item[-2] in prop_matrix):
            return item
    return None



# consistency check and forward/backward implication

def consistency(circuit_data, prop_matrix):

    cons_matrix = {}

    # 1- check prop_matrix and identify unvalued lines
    
    unvalued_data = []
    for data in circuit_data:
        temp = 0
        if data[0] in prop_matrix:
            temp += 1
        if temp == 0:
            unvalued_data.append(data)
    

    # 2- give value to unvalued lines by means of prop_matrix >> cons_matrix

    # backward implication
    temp_list = []
    for data in reversed(circuit_data):
        for item in list(prop_matrix.items()):
            if (item[0] == data[0]) and ('not' in data) and (prop_matrix[data[0]] == '1'):
                for i in unvalued_data:
                    if data[-1] == i[0]:
                        cons_matrix[data[-1]] = '0'
                        temp_list.append(i)
                break
            elif (item[0] == data[0]) and ('not' in data) and (prop_matrix[data[0]] == '0'):
                for i in unvalued_data:
                    if data[-1] == i[0]:
                        cons_matrix[data[-1]] = '1'
                        temp_list.append(i)
                break
            elif (item[0] == data[0]) and ('and' in data) and (prop_matrix[data[0]] == '1'):
                for i in unvalued_data:
                    if data[-1] == i[0]:
                        cons_matrix[data[-1]] = '1'
                        temp_list.append(i)
                    if data[-2] == i[0]:
                        cons_matrix[data[-2]] = '1'
                        temp_list.append(i)
                break
            elif (item[0] == data[0]) and ('nand' in data) and (prop_matrix[data[0]] == '0'):
                for i in unvalued_data:
                    if data[-1] == i[0]:
                        cons_matrix[data[-1]] = '1'
                        temp_list.append(i)
                    if data[-2] == i[0]:
                        cons_matrix[data[-2]] = '1'
                        temp_list.append(i)
                break
            elif (item[0] == data[0]) and ('or' in data) and (prop_matrix[data[0]] == '0'):
                for i in unvalued_data:
                    if data[-1] == i[0]:
                        cons_matrix[data[-1]] = '0'
                        temp_list.append(i)
                    if data[-2] == i[0]:
                        cons_matrix[data[-2]] = '0'
                        temp_list.append(i)
                break
            elif (item[0] == data[0]) and ('nor' in data) and (prop_matrix[data[0]] == '1'):
                for i in unvalued_data:
                    if data[-1] == i[0]:
                        cons_matrix[data[-1]] = '0'
                        temp_list.append(i)
                    if data[-2] == i[0]:
                        cons_matrix[data[-2]] = '0'
                        temp_list.append(i)
                break


    for i in temp_list:
        unvalued_data.remove(i)
        

    # forward implication
    for data in unvalued_data:
        inpt1, inpt2 = '*', '*'
        if 'from' in data:
            for item in list(prop_matrix.items()):
                if data[-1] == item[-1] or item[0] == data[-1]:
                    cons_matrix[data[0]] = BUFF(item[0], prop_matrix)
                    unvalued_data.remove(data)
                    break

        elif 'not' in data:
            for item in list(prop_matrix.items()):
                if item[0] == data[-1]:
                    cons_matrix[data[0]] = NOT(item[0], prop_matrix)
                    unvalued_data.remove(data)
                    break

        elif 'buff' in data:
            for item in list(prop_matrix.items()):
                if item[0] == data[-1]:
                    cons_matrix[data[0]] = BUFF(item[0], prop_matrix)
                    unvalued_data.remove(data)
                    break

        elif 'and' in data:
            for item in list(prop_matrix.items()):
                if item[0] == data[-1]:
                    inpt1 = item[0]
                elif item[0] == data[-2]:
                    inpt2 = item[0]
            if inpt1 != '*' and inpt2 != '*':
                cons_matrix[data[0]] = AND(inpt1, inpt2, prop_matrix)
                unvalued_data.remove(data)

        elif 'nand' in data:
            for item in list(prop_matrix.items()):
                if item[0] == data[-1]:
                    inpt1 = item[0]
                elif item[0] == data[-2]:
                    inpt2 = item[0]
            if inpt1 != '*' and inpt2 != '*':
                cons_matrix[data[0]] = NAND(inpt1, inpt2, prop_matrix)
                unvalued_data.remove(data)

        elif 'or' in data:
            for item in list(prop_matrix.items()):
                if item[0] == data[-1]:
                    inpt1 = item[0]
                elif item[0] == data[-2]:
                    inpt2 = item[0]
            if inpt1 != '*' and inpt2 != '*':
                cons_matrix[data[0]] = OR(inpt1, inpt2, prop_matrix)
                unvalued_data.remove(data)

        elif 'nor' in data:
            for item in list(prop_matrix.items()):
                if item[0] == data[-1]:
                    inpt1 = item[0]
                elif item[0] == data[-2]:
                    inpt2 = item[0]
            if inpt1 != '*' and inpt2 != '*':
                cons_matrix[data[0]] = NOR(inpt1, inpt2, prop_matrix)
                unvalued_data.remove(data)

        elif 'xor' in data:
            for item in list(prop_matrix.items()):
                if item[0] == data[-1]:
                    inpt1 = item[0]
                elif item[0] == data[-2]:
                    inpt2 = item[0]
            if inpt1 != '*' and inpt2 != '*':
                cons_matrix[data[0]] = XOR(inpt1, inpt2, prop_matrix)
                unvalued_data.remove(data)

        elif 'xnor' in data:
            for item in list(prop_matrix.items()):
                if item[0] == data[-1]:
                    inpt1 = item[0]
                elif item[0] == data[-2]:
                    inpt2 = item[0]
            if inpt1 != '*' and inpt2 != '*':
                cons_matrix[data[0]] = XNOR(inpt1, inpt2, prop_matrix)
                unvalued_data.remove(data)
        
    # 3- give value to items in prop_matrix and regenerate them by means of cons_matrix >> regen_prop_matrix
    output_matrix = prop_matrix.copy()
    for key, value in cons_matrix.items():
        output_matrix[key] = value
    
    return output_matrix




# backtrack if inconsistent and update PI stack

def backtrack(prop_matrix, cons_matrix):
    output_matrix = prop_matrix.copy()
    for key, value in cons_matrix.items():
        output_matrix[key] = value
    
    return output_matrix



def get_fault_vec(fault_dic, input_data, fault_value, circuit_name):
    fault_vec = {}
    for data in input_data:
        temp = 0
        for item in list(fault_dic.items()):
            if item[0] == data[0]:
                fault_vec[data[0]] = item[1]
                temp += 1
        if temp == 0:
            fault_vec[data[0]] = '*'
    
    fault_vec_done(fault_vec, fault_value, circuit_name)



def fault_vec_done(fault_vec, fault_value, circuit_name):
    test_vec = ""
    for item in list(fault_vec.items()):
        if item[1] == 'd_f':
            test_vec += 'd'
        elif item[1] == 'd_not_f':
            test_vec += 'd`'
        elif item[1] == '*':
            test_vec += ''.join((random.choice('01x') for i in range(1)))
        else:
            test_vec += item[1]

    with open('fault/fault_%s' % circuit_name, 'a') as file:
        file.write('  ' + test_vec + '    =>\t' + fault_value +'\n\n')




def compress_fault_vec(circuit_name):

    compress_faults = {}

    file = open('fault/fault_%s' % circuit_name, 'r')
    lines = file.readlines()
    test_vec = {}
    splited = []
    flag = False
    for i in range(2, len(lines)):
        splited.append(lines[i].split())
        
    for item in splited:
        if (len(item) != 0) and ('d' not in item[0]) and ('d`' not in item[0]):
            test_vec[item[0]] = item[2] + ' ' + item[3]
    
    keys = list(test_vec.keys())
    values = list(test_vec.values())
    
    for i in range(len(keys)):
        comp_inpt1 = keys[i]
        for j in range(i+1, len(keys)):
            if compressor(comp_inpt1, keys[j]) != None:
                if compressor(comp_inpt1, keys[j]) in compress_faults:
                    if not isinstance(compress_faults[compressor(comp_inpt1, keys[j])], list):
                        compress_faults[compressor(comp_inpt1, keys[j])] = [compress_faults[compressor(comp_inpt1, keys[j])]]
                        compress_faults[compressor(comp_inpt1, keys[j])].append(' & ' + values[j])
                else:
                    compress_faults[compressor(comp_inpt1, keys[j])] = values[i] + ' & ' + values[j]
                comp_inpt1 = compressor(comp_inpt1, keys[j])
    
    for item in list(compress_faults.items()):
        if 'x' in item[0]:
            del compress_faults[item[0]]
        else:
            with open('fault/comp_fault_%s' % circuit_name, 'a') as file:
                file.write('  ' + item[0] + '    =>\t' + str(item[1]) +'\n\n')

def compressor(comp_inpt1, comp_inpt2):
    result = ''
    for i, char in enumerate(comp_inpt1):
        if char == 'x':
            if comp_inpt2[i] == '1':
                result += '1'
            elif comp_inpt2[i] == '0':
                result += '0'
            else:
                result += 'x'
        elif comp_inpt2[i] == 'x':
            if char == '1':
                result += '1'
            elif char == '0':
                result += '0'
            else:
                result += 'x'
        elif char == '1' and comp_inpt2[i] == '1':
            result += '1'
        elif char == '0' and comp_inpt2[i] == '0':
            result += '0'
        else:
            return None
    return result

