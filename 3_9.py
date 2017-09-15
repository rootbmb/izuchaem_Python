guest = ['Test0', 'Test1', 'Tets2']
print('guest'+ ':', guest[0])
print('guest'+ ':', guest[1])
print('guest'+ ':', guest[2])

print(guest[1] + ' no guest')
guest[1] = 'Test3'

print('guest'+ ':', guest[0])
print('guest'+ ':', guest[1])
print('guest'+ ':', guest[2])

print('guest + 3')

guest.insert(0, 'Test4')
guest.insert(2, 'Test5')
guest.append('Test6')
print('guest'+ ':', guest[0])
print('guest'+ ':', guest[1])
print('guest'+ ':', guest[2])
print('guest'+ ':', guest[3])
print('guest'+ ':', guest[4])
print('guest'+ ':', guest[5])
print(len(guest), ' guest number')