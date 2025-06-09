import functools

def factorial(n):
    return 1 if n==0 else functools.reduce(lambda x, y: x * y, range(1, n + 1))

def calculate_permutations(n_items, chosen_items): #P(n,r)=n!/(n-r)!
    factorial_n = factorial(n_items)
    factorial_n_r = factorial(n_items-chosen_items)
    permutations_result = factorial_n / factorial_n_r
    return permutations_result

def calculate_combinations(n_items, chosen_items):#C(n,r)=n!/(r!(n-r)!)
    divisor = factorial(chosen_items) * factorial(n_items-chosen_items)
    factorial_n = factorial(n_items)
    combinations_result = factorial_n / divisor
    return combinations_result


def count_inversions(permutation):
    inversions = 0
    n = len(permutation)
    for i in range(n):
        for j in range(i + 1, n):
            if permutation[i] > permutation[j]:
                inversions += 1
    return inversions
    
def combinatorics_calculations():
    while True:    
        print("Choose an option:")
        print("0. Exit")
        print("1. Calculate Permutations")
        print("2. Calculate Combinations")
        print("3. Count Inversions")
        choice = input("Enter the number of the chosen option: ")
        if choice == "0":
            print("Good bye!")
            break
        elif choice in ['1', '2']:
            print("--------------------------------------------")
            n_items = int(input("Enter the number of items: "))
            chosen_items = int(input("Enter the number of items to choose: "))
            print("--------------------------------------------")
            if choice == '1':
                result = calculate_permutations(n_items, chosen_items)
                print("=======================")
                print(f"Permutations: {result}")
                print("=======================")
            elif choice == '2':
                result = calculate_combinations(n_items, chosen_items)
                print("=======================")
                print(f"Combinations: {result}")
                print("=======================")
        elif choice == '3':
            print("--------------------------------------------")
            permutation = list(map(int, input("Enter the permutation (space-separated): ").split()))
            inversion_count = count_inversions(permutation)
            print("=======================")
            print(f"Number of inversions: {inversion_count}")
            print("=======================")
        else:
            print("--------------------------------------------")
            print("Invalid option. Please try again.")
            print("--------------------------------------------")
            
if __name__ == "__main__":
    combinatorics_calculations()