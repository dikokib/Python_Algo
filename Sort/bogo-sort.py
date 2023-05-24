import random

#型アノテーションと型ヒントで親切
def in_order(numbers: list[int]) -> bool:
    #リスト内包括表記でシンプル
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
    # for i in range(len(numbers)-1):
    #     if numbers[i] >  numbers[i+1]:
    #         return False
    # return True

def bogo_sort(numbers: list[int]) -> list[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers

if __name__ == '__main__':
    print(bogo_sort([1, 3, 5, 2, 8]))