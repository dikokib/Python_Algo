import random

def insertion_sort(numbers: list[int]) -> list[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i] #temporary(一時的な)
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j+1] = temp

    return numbers



if __name__ == '__main__':
    nums = [random.randint(0, 1000) for i in range(10)]
    print(insertion_sort(nums))