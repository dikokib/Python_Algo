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
    print('****************************')
    print("left:",left)
    print("right:",right)


    merge_sort(left)
    merge_sort(right)

    print('マージ終わった')

    numbers = left + right

    print("最後",numbers)

    return numbers


if __name__ == '__main__':
    nums = [6, 2, 9, 5, 7, 1, 4]
    #nums = [random.randint(0, 1000) for i in range(5)]
    print(merge_sort(nums))