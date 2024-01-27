# Python-Riddles
Repository in which I store my ways of solving riddles in Python.

**License:** This project is licensed under the MIT License.

## Riddle 1 - Unique Pairs
**Problem:** Given an integer array, output all the unique pairs that sum up to a specific value k.

Here are some reasons why the given approach for the pair_sum function is good:

**Efficiency:** This solution traverses the array only once, resulting in a time complexity of O(n). By utilizing a set (seen) to store numbers and another set (result) to store unique pairs, it avoids unnecessary iterations and quickly identifies pairs that sum up to the target value k.
**Space Efficiency:** The use of sets (seen and result) ensures uniqueness without requiring additional data structures or complex manipulations. The set data structure provides fast lookup times (close to O(1)) when checking for the presence of elements.
**Avoids Duplicates:** By using a set to store unique pairs, it inherently avoids the generation of duplicate pairs that have the same elements but in a different order (e.g., (a, b) and (b, a)). The sorting of pairs before adding them to result ensures consistency and avoids duplicates.
**Readability and Simplicity:** The code is concise, clear, and easy to understand. It uses intuitive variable names (seen, result) that make the logic easy to follow. The use of comments further enhances readability by explaining the purpose of certain operations.
**Scalability:** The solution remains efficient even for larger arrays since it maintains a linear time complexity, making it scalable for handling larger datasets without a significant increase in time or space requirements.
Overall, this approach strikes a balance between efficiency, readability, and simplicity, making it a good choice for finding unique pairs that sum up to a specific value within an array.

**Solution:** To be found in file *"Riddle 1 - Unique Pairs.py"*

```python:
def pair_sum(arr, k):
    """
    Find unique pairs in the given array whose sum equals the specified target value.

    Args:
    - arr (list of int): The input array containing integers.
    - k (int): The target sum value.

    Returns:
    - list of tuples: A list of unique pairs (tuple) whose sum equals the target value 'k'.
    
    The function iterates through the input array, searching for pairs whose sum equals the target value 'k'.
    It stores unique pairs in a set and returns a list containing these unique pairs.
    Pairs are sorted to maintain consistency in the result (smaller number first).
    """
    seen = set()  # Store unique pairs
    result = set()  # Store final unique pairs to return

    for num in arr:
        complement = k - num
        if complement in seen:
            # Sort the pair to maintain consistency
            pair = (min(num, complement), max(num, complement))
            result.add(pair)
        seen.add(num)

    return list(result)
```

## Riddle 2 - Anagram Check

**Problem:** Given two strings, check if they are anagrams of each other.

Here are some reasons why this approach for the anagram function is effective:

**Efficiency:** The solution counts character occurrences in both strings, resulting in a time complexity of O(n) where 'n' is the total number of characters in the input strings. It iterates through the strings twice to create character count dictionaries, ensuring an efficient comparison.
**Space Efficiency:** It uses dictionaries (char_count_s1 and char_count_s2) to store character occurrences, requiring additional space proportional to the number of unique characters in the strings, making it space-efficient.
**Readability and Simplicity:** The code is structured for readability and simplicity. It utilizes clear variable names and comments to explain the purpose of each step, making it easy to understand.

**Solution:** To be found in the file *"Anagram Check.py"*

```python:
def anagram(s1, s2):
    """
    Check if two strings are anagrams of each other.

    An anagram is when two strings can be written using the exact same letters 
    (so you can just rearrange the letters to get a different phrase or word).

    Args:
    - s1 (str): The first input string.
    - s2 (str): The second input string.

    Returns:
    - bool: True if s1 and s2 are anagrams, False otherwise.
    """
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    # Check if the lengths of the strings are equal
    if len(s1) != len(s2):
        return False

    # Create dictionaries to count character occurrences
    char_count_s1 = {}
    char_count_s2 = {}

    # Count occurrences of characters in s1
    for char in s1:
        char_count_s1[char] = char_count_s1.get(char, 0) + 1

    # Count occurrences of characters in s2
    for char in s2:
        char_count_s2[char] = char_count_s2.get(char, 0) + 1

    # Check if the character counts are equal
    return char_count_s1 == char_count_s2
```

## Riddle 3 - Missing Finder

**Problem:** Given two arrays, find the missing element from the second array that is not present in the first array.

Here are some reasons why this approach for the finder function is effective:

**Efficiency:** The function uses the Counter class from the collections module to count occurrences of elements in arr1, resulting in a time complexity of O(n) where 'n' is the length of arr1. It efficiently subtracts counts of elements in arr2 from arr1, identifying the missing element.
**Handling Different Lengths:** The function correctly handles scenarios where arr2 might have one fewer element than arr1. It compares the counts and identifies the missing element or handles cases where the missing element isn't found.

**Solution:** To be found in the file *"Riddle 3 - Missing Finder.py"*

```python:
from collections import Counter

def finder(arr1, arr2):
    """
    Finds the missing element in arr2 compared to arr1.

    Args:
    - arr1 (list): First input array
    - arr2 (list): Second input array

    Returns:
    - Any: The missing element if found, None otherwise
    """
    count = Counter(arr1)

    for item in arr2:
        count[item] -= 1

    # Find the element with a count that isn't zero
    for key, value in count.items():
        if value != 0:
            return key

    # Check if arr2 is shorter by one element
    if len(arr1) > len(arr2):
        for key, value in count.items():
            if value == -1:
                return key

    # Handle scenarios where the missing element is not found
    return None
```

## Riddle 4 - Continuous Sum

**Problem:** Find the largest sum of a contiguous subarray within the given array.

Here are some reasons why this approach for the large_cont_sum function is good:

**Efficiency:** The function uses a linear iteration through the array, maintaining two variables current_sum and max_sum. It updates current_sum as it traverses the array, keeping track of the maximum contiguous sum encountered in max_sum.
**Space Efficiency:** It uses a constant amount of additional space, maintaining only two variables for the current sum and maximum sum, ensuring space efficiency.
**Readability and Simplicity:** The code is structured for readability and simplicity. It utilizes intuitive variable names and comments to explain the purpose of each step, making it easy to understand.

**Solution:** To be found in the file *"Riddle 4 - Continuous Sum.py"*
