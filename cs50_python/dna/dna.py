import csv
from pprint import pprint

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

# def search_dna(dna, d):
#     n = len(d)
#     count = 0
#     x = (len(dna)//n) * n
#     print(x)
#     for i in range(0, len(dna), n):
#         # if i == len(dna) - n:
#         #     break
#         if dna[i:i + n] == d:
#             count += 1
#     return count   
    
# def match_dna(dna, d, l):
#     count = 0
#     for key, value in d.items():
#         for str_count in value:
#             if int(str_count) == search_dna(dna, l[value.index(str_count)]):
#                 count += 1
#         if count == len(l):
#             return key

def match_dna(dna, persons, list_str):

    print(persons)
    print(list_str)
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
    
    pprint(sequences)
    largest_sequences = 0

    for s in sequences:
        n = len(s)
        if n > largest_sequences:
            largest_sequences = n

    return largest_sequences
    

    # for i in range(len(dna)):
    #     x = dna.index(d, i, len(dna))
    #     if x == -1:
    #         print("found")
            

def main():

    text_path = '/home/nick/projects/devops/cs50_python/dna/sequences/6.txt'
    # csv_path = '/home/nick/projects/devops/cs50_python/dna/databases/small.csv'
    csv_path = '/home/nick/projects/devops/cs50_python/dna/databases/large.csv'

    list_str = []
    dict_person = {}

    dna = read_text(text_path)

    create(read_csv(csv_path), dict_person, list_str)
    # d = list_str[0]

    # count_dna(dna, list_str)
    # print(dict_person)
    # print(list_str)
    match = match_dna(dna , dict_person, list_str)
    # x = search_dna(dna, d)
    # print(x)
    print(match)
    


if __name__ == '__main__':
    main()

   



