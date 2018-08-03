
import random
import numpy as np

class GenomeMutation:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def SNPIntroduction(self, template_sequence, SNP_frequency):

        # SNPIntroduction works exactly as specified, tested 10 times
        # with sequence of length 80
        # results were consistent over all 10 tests.

        random.seed()
        new_sequence = template_sequence
        SNP_count = 0
        SNP_changes = []
        number_of_windows = int(len(new_sequence)/SNP_frequency)
        print(number_of_windows)
        for i in range(0, number_of_windows-1):
            position = random.randint(i*SNP_frequency, i*SNP_frequency+SNP_frequency-1)

            while True:
                SNP = random.choice('ACTG')

                if new_sequence[position] == SNP:
                    continue

                if new_sequence[position] != SNP:
                    new_sequence = new_sequence[0:position] + SNP + new_sequence[position+1:]
                    SNP_count += 1
                    SNP_changes.append((position, SNP))
                    break
        # Note: the number of actual sequence changes will be 25% less than what is specified in the input
        # since the probability of a nucleotide being mutated to the same initial state is 25%

        return new_sequence


    def Inversion(self, template_sequence, start_position, end_position):

        # This function inverts from the actual specified start and stop positions,
        # i.e if 5 and 10 are chosen, it inverts between the 5th and 10th position
        # it does not start "counting" from 0.

        new_sequence = template_sequence
        fragment = template_sequence[start_position-1:end_position-1]
        inverted_fragment = list(fragment[::-1])
        print(inverted_fragment)
        #new_sequence.replace(fragment,inverted_fragment)
        new_sequence = list(new_sequence[0:start_position-1]) + inverted_fragment + list(new_sequence[end_position-1:])
        # This block might also suffer from the same problem as the one below, for example when 5 and 10
        # are chosen as the start and end, inversion happens from positions 5 to position 9. In other words
        # the start position is included in the inversion and the specified end position is not. Did not change it
        # as I didn't know if it was intentional or not.
        return new_sequence

    def Translocation(self, template_sequence, start_position, end_position, new_position):
        new_sequence = template_sequence
        # fragment = template_sequence[start_position-1:end_position-1]
        # Note: taking the "end position-1" resulted in a nucleotide being deleted at the end of the fragment
        # This is probably due to the fact that indexing in this way [:] includes the start and excludes the end
        fragment = template_sequence[start_position - 1:end_position]
        new_sequence = new_sequence[:start_position-1] + new_sequence[end_position:new_position] + fragment + new_sequence[new_position:]
        return new_sequence


class WriteOutputFile:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def WriteOutputFastA(self, filename, sequence_name, sequence):

        f = open(filename, 'w')
        f.write(">" + sequence_name + "\n")
        f.write(sequence)
        f.close()