# Find the length of the set it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

it_companies.add('twitter')

print(it_companies)


# Insert multiple IT companies at once to the set it_companies

new_it_companies = {"meta", "x", "intell"}

it_companies.update(new_it_companies)
print(it_companies)

# Remove one of the companies from the set it_companies

it_companies.discard('Amazon')

# Print the updated set
print(it_companies)

# remove Method:

# Removes the specified element from the set.
# Raises a KeyError if the element is not found in the set.

# discard Method:

# Removes the specified element from the set if it is present.
# Does not raise an error if the element is not found.

# Given sets A and B
A = {1, 2, 3}
B = {3, 4, 5}

# 1. Join A and B
join_result = A.union(B)  # Result: {1, 2, 3, 4, 5}

# 2. Find A intersection B
intersection_result = A.intersection(B)  # Result: {3}

# 3. Is A subset of B
is_subset = A.issubset(B)  # Result: False

# 4. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)  # Result: False

# 5. Join A with B and B with A
joined_sets = A.union(B), B.union(A)  # Results: ({1, 2, 3, 4, 5}, {1, 2, 3, 4, 5})

# 6. What is the symmetric difference between A and B
symmetric_difference_result = A.symmetric_difference(B)  # Result: {1, 2, 4, 5}

# 7. Delete the sets completely using python
del A, B

# Verify deletion (this will raise a NameError)
try:
    print(A, B)
except NameError as e:
    print(f"Sets A and B are deleted: {e}")

# Given list of ages
ages_list = [25, 30, 25, 35, 40, 30, 25]

# 1. Convert ages to a set and compare lengths
ages_set = set(ages_list)
list_length = len(ages_list)
set_length = len(ages_set)

# 2. Explain the difference between string, list, tuple, and set
# String: Immutable sequence of characters (e.g., "Hello")
# List: Mutable ordered sequence (e.g., [1, 2, 3])
# Tuple: Immutable ordered sequence (e.g., (1, 2, 3))
# Set: Unordered collection of unique elements (e.g., {1, 2, 3})

# 3. Count unique words in the sentence
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
num_unique_words = len(unique_words)

# 4. Compare lengths and print results
length_comparison_result = "List is bigger" if list_length > set_length else "Set is bigger"

print(f"Length of List: {list_length}")
print(f"Length of Set: {set_length}")
print(length_comparison_result)

print("\nData Type Explanation:")
print("String: Immutable sequence of characters")
print("List: Mutable ordered sequence")
print("Tuple: Immutable ordered sequence")
print("Set: Unordered collection of unique elements")

print(f"\nNumber of Unique Words in the Sentence: {num_unique_words}")

