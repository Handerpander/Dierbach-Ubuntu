for ch in 'Hello':
    print(ch)

sum = 0
for k in range(1, 11):
    sum = sum + k

k = 0
nums =[10, 20, 30, 40]
item_to_find = 40
found_item = False

while k < len(nums) and not found_item:
    if nums[k] == item_to_find:
        found_item = True
    else:
        k = k + 1

    if found_item:
        print('item found')
    else:
        print('item not found')
        
