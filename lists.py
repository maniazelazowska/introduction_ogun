#lists experiments
def total(list_of_numbers):
    total_sum = 0
    for i in range(len(list_of_numbers)):
        total_sum += list_of_numbers[i]
    return total_sum
    
def main():
    print(total([2, 5, 1]))


main()