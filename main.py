import handler
import time

circuit_name = input('Enter the name of iscas file: ')
input_file = input('Enter the name of input file: ')

total_test_time = time.time()
iscas_result = handler.read_circuit_file(circuit_name)
input_data = handler.read_input_file("input/%s" % input_file)
output = handler.get_node_values(input_data, iscas_result)

with open('output/output_'+ circuit_name, 'w') as file:
    file.write('node' + '\t\t' + 'value\n')
    file.write('------\t------\n')
    for item in list(output.items()):
        file.write('  ' + item[0] + '   =>   ' + item[1] + '\n')
print('Total test time: ' + str(round(time.time() - total_test_time, 3)))

d_algo_time = time.time()
handler.equivalence_faults_check(iscas_result)

with open('fault/fault_%s' % circuit_name, 'w') as file:
        file.write('\t\t'.join(["test_vector","fault"]) +'\n')
        file.write('-----------\t\t------\n')

with open('fault/comp_fault_%s' % circuit_name, 'w') as file:
        file.write('\t\t\t\t\t\t\t\t'.join(["test_vector","fault(s)"]) +'\n')
        file.write('-----------\t\t-------------------------------\n')

handler.pdf(iscas_result, input_data, circuit_name)
print('D Algorithm time: ' + str(round(time.time() - d_algo_time, 3)))


comp_time = time.time()
handler.compress_fault_vec(circuit_name)
print('Test vector compression time: ' + str(round(time.time() - comp_time, 4)))
