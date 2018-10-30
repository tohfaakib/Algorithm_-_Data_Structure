def binary_src(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (high + low) // 2
        # print(mid)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


list = [1, 3, 5, 7, 9, 10, 20, 23, 56, 60, 100]
item = int(input("enter search item: "))
print(item, " is in index: ", binary_src(list, item))
