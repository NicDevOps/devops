import csv
import sys

def read_csv(csv_path):
    with open(csv_path, newline='') as f:
        data_list = list(csv.reader(f))
        return data_list

def read_text(text):
    with open(text, 'r') as file:
        dna = file.readline().strip()
        return dna

def create(data_list, dict_person, list_str):
    for i in range(len(data_list[0])):
        if i > 0:
            list_str.append(data_list[0][i])
    for i in range(len(data_list)):
        if i > 0:
            dict_person[data_list[i][0]] = []
            for j in range(len(data_list[i])):
                if j > 0:                   
                    dict_person[data_list[i][0]].append(int(data_list[i][j]))


def match_dna(dna, persons, list_str):
    result = []

    for s in list_str:
        sequence_count = search_dna(dna, s)
        result.append(sequence_count)
    print(result)
    for k, v in persons.items():
        if v == result:
            return k


def search_dna(dna, d):
    sequences = []
    current_index = dna.find(d)
    previous_index = 0

    while current_index != -1:
        if current_index - previous_index == len(d):
            sequences[-1].append(current_index)
        else:
            sequences.append([current_index])
        previous_index = current_index
        current_index = dna.find(d, current_index + 1)
    
    largest_sequences = 0

    for s in sequences:
        n = len(s)
        if n > largest_sequences:
            largest_sequences = n

    return largest_sequences
    

def main():
    
    text_path = ''
    csv_path = ''
    argc = len(sys.argv)
    for i in range(argc):
        if i == 1:
            csv_path = sys.argv[i]
        if i == 2:
            text_path = sys.argv[i]

    list_str = []
    dict_person = {}

    dna = read_text(text_path)
    data_list = read_csv(csv_path)

    create(data_list, dict_person, list_str)
    
    match = match_dna(dna , dict_person, list_str)

    print(match)


if __name__ == '__main__':
    main()

   



