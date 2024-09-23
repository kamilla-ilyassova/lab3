from itertools import permutations

def print_permutations():
    user_input = input("String: ")
    perm = permutations(user_input)
    unique_permutations = set([''.join(p) for p in perm])
    
    for p in sorted(unique_permutations):
        print(p)

print_permutations()