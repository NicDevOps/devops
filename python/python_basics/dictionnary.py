from pprint import pprint
records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}

# for value in records.values():
#     value[1] = value[1][:-4] + '.org'

for value in records.values():
    print(value[1])
    value[1] = value[1].replace('.com','.org')
    print(value[1])
# for y in records:
#     print(records[y][1])



pprint(records)