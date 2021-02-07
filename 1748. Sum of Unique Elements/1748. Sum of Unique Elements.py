def func():
    nums = [1,3,4,4,3]
    sum = 0
    # Converting nums to a set which gives us 
    s = set(nums)
    # s = [1,3,4]
    for i in s: 
        if nums.count(i)==1:
            sum +=i
    print(sum)
func() 