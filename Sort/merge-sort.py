import random

def merge_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers
    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    #自分で自分を呼び出す再起関数とは？
    # ┗終了条件を持つ
    # ┗毎回状態を変え、終了条件に近づく
    # ┗それ自身を再帰的に呼び出す

    merge_sort(left)
    merge_sort(right)


    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    while j< len(right):
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers


if __name__ == '__main__':
    nums = [6, 2, 9, 5, 7, 1, 4]
    #nums = [random.randint(0, 1000) for i in range(5)]
    print(merge_sort(nums))

#windowsからの最後のpushです