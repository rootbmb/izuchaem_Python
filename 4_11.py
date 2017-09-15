names = ['test0', 'test1', 'test2']
for name in names:
    print('I like pepperoni pizza:', name.title())
print('I really love pizza!')
friend_pizzas = names[:]
names.append('test3')
friend_pizzas.append('test4')
print('My favorite pizzas are:', names)
for i in names:
    print(i)

print('My friend’s favorite pizzas are:', friend_pizzas)
for i in friend_pizzas:
    print(i)