my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]


my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print("____________________________________________________")
print('My foods:')
for i in my_foods:
    print(i)
print('*****************')
print('Friend foods')
for i in friend_foods:
    print(i)