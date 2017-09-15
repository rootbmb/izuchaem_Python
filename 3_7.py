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
print(len(guest))
print('guest'+ ':', guest[0])
print('guest'+ ':', guest[1])
print('guest'+ ':', guest[2])
print('guest'+ ':', guest[3])
print('guest'+ ':', guest[4])
print('guest'+ ':', guest[5])

print()
print('guest:2')

t1 = guest.pop()
print('guest -', t1.title())
t2 = guest.pop()
print('guest -', t2 )
t3 = guest.pop()
print('guest -', t3)
t4 = guest.pop()
print('guest -', t4)

print('guest'+ ':', guest[0])
print('guest'+ ':', guest[1])
del guest[1]
del guest[0]
print(guest)