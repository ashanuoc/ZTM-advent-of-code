with open("data.txt") as file:
    data = file.readlines()

arr = []
for line in data:
    x = [int(i) for i in line.split()]
    arr.append(x)


def is_safe(arr):
    length = len(arr)
    if arr[0] < arr[length - 1]:
        for i in range(0, length - 1):
            if (arr[i + 1] - arr[i]) not in range(1, 4):
                return False
    elif arr[0] > arr[length - 1]:
        for i in range(0, length - 1):
            if (arr[i] - arr[i + 1]) not in range(1, 4):
                return False
    elif arr[0] == arr[length - 1]:
        return False

    return True


def is_safe_with_dampener(arr):
    if is_safe(arr):
        return True

    for i in range(len(arr)):
        modified_arr = arr[:i] + arr[i + 1:]
        if is_safe(modified_arr):
            return True

    return False


count = 0

for a in arr:
    if is_safe_with_dampener(a):
        count += 1

print(count)
