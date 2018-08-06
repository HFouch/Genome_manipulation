import random
import numpy as np

positions = []
range_of_sequence_blocks = []
for i in range(1, 1001):
    range_of_sequence_blocks.append(i)
    positions.append((1,7))

list_of_sequence_blocks = []
list_of_sequence_blocks_length = 0
range_of_sequence_blocks_length = 1000
print(len(range_of_sequence_blocks))
print(range_of_sequence_blocks[len(range_of_sequence_blocks)-1])
while len(range_of_sequence_blocks) > 0:
    random_position = random.randint(0, len(range_of_sequence_blocks)-1)
    sequence_block = range_of_sequence_blocks[random_position]
    if list_of_sequence_blocks_length == 0:

        inversion_status = random.randint(0,1)
        if inversion_status == 0:
            list_of_sequence_blocks.append(sequence_block)
        else:
            list_of_sequence_blocks.append(-sequence_block)
        range_of_sequence_blocks.remove(sequence_block)

        list_of_sequence_blocks_length += 1
        print(list_of_sequence_blocks)
        print(list_of_sequence_blocks_length)

    else:
        consecutive1 = sequence_block -1
        consecutive2 = sequence_block + 1
        while list_of_sequence_blocks[list_of_sequence_blocks_length-1] == consecutive1 or list_of_sequence_blocks[list_of_sequence_blocks_length-1] == consecutive2:
            random_position = random.randint(0, len(range_of_sequence_blocks))
            sequence_block = range_of_sequence_blocks[random_position]
            consecutive1 = sequence_block - 1
            consecutive2 = sequence_block + 1

        inversion_status = random.randint(0,1)
        if inversion_status == 0:
            list_of_sequence_blocks.append(sequence_block)
        else:
            list_of_sequence_blocks.append(-sequence_block)

        range_of_sequence_blocks.remove(sequence_block)

        list_of_sequence_blocks_length += 1

np.savetxt('sequence_blocks.txt', np.c_[list_of_sequence_blocks], '%0.0f')
print(positions[:8])

names = np.array(list_of_sequence_blocks)
position = np.array(positions)
names_positions = np.column_stack((names, position))

print(names_positions[:8])

np.savetxt('sequence_blocks_file.txt', np.c_[names_positions], '%0.0f', delimiter='\t')