"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

# First pass solution is a loop through all of the combinations, super ineffecient.

def print_comb1(set):
    for a in set:
        for b in set:
            for c in set:
                for d in set:
                    if f(a) + f(b) == f(c) - f(d):
                        print(f"f({a}) + f({b}) = f({c}) - f({d})")


# print_comb1(q)

# Run time for this would be O(n^4) 
# We can get it down to O(n^2) if we use a caching system or dictionary to avoid repeats.
# From here we can check against the dictionary with the diffs

def print_comb2(set):
    sums = {}
    for a in set:
        for b in set:
            sum = f(a) + f(b)
            if sum not in sums:
                sums[sum] = [(a, b)]
            else:
                sums[sum].append((a, b))

    for c in set:
        for d in set:
            diff = f(c) - f(d)
            if diff in sums:
                for sum in sums[diff]:
                   print(f"f({sum[0]}) + f({sum[1]}) = f({c}) - f({d})") 

# print_comb2(q)

# We can further optimize since addition is communitive and a + b = b + a

def print_comb3(input_set: set):
    sums = {}
    b_set = input_set.copy()

    for a in input_set:
        for b in b_set:
            sum = f(a) + f(b)
            if sum not in sums:
                sums[sum] = [(a, b), (b, a)]
            else:
                sums[sum].append([(a, b), (b, a)])

        b_set.remove(a)

    for c in input_set:
        for d in input_set:
            diff = f(c) - f(d)
            if diff in sums:
                for sum in sums[diff]:
                   print(f"f({sum[0]}) + f({sum[1]}) = f({c}) - f({d})") 


import time

q = set(range(1, 200))

# start_time1 = time.time()
# print_comb1(q)
# end_time1 = time.time()

start_time2 = time.time()
print_comb2(q)
end_time2 = time.time()

start_time3 = time.time()
print_comb3(q)
end_time3 = time.time()

# print(f"Combinations 1 finished in {end_time1 - start_time1}")
print(f"Combinations 2 finished in {end_time2 - start_time2}")
print(f"Combinations 3 finished in {end_time3 - start_time3}")

