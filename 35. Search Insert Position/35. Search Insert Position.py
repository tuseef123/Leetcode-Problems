def func():
    # nums = [1,3,5,6]
    # target = 0
    nums = [1]
    target = 0
    for i,j in enumerate(nums):
        if j == target:
            print (i)
            break
        elif j > target:
            print(i)
            break
        elif i ==len(nums)-1 and i != target:
            print(len(nums))
        # print(i,j)
func()