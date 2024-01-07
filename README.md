# Python-Riddles
Repository in which I store my ways of solving riddles in Python.

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

## Riddle 2 - Anagram Check

**Problem:** Given two strings, check if they are anagrams of each other.

Here are some reasons why this approach for the anagram function is effective:

**Efficiency:** The solution counts character occurrences in both strings, resulting in a time complexity of O(n) where 'n' is the total number of characters in the input strings. It iterates through the strings twice to create character count dictionaries, ensuring an efficient comparison.
**Space Efficiency:** It uses dictionaries (char_count_s1 and char_count_s2) to store character occurrences, requiring additional space proportional to the number of unique characters in the strings, making it space-efficient.
**Readability and Simplicity:** The code is structured for readability and simplicity. It utilizes clear variable names and comments to explain the purpose of each step, making it easy to understand.

**Solution:** To be found in the file *"Anagram Check.py"*

## Riddle 3 - Missing Finder

**Problem:** Given two arrays, find the missing element from the second array that is not present in the first array.

Here are some reasons why this approach for the finder function is effective:

**Efficiency:** The function uses the Counter class from the collections module to count occurrences of elements in arr1, resulting in a time complexity of O(n) where 'n' is the length of arr1. It efficiently subtracts counts of elements in arr2 from arr1, identifying the missing element.
**Handling Different Lengths:** The function correctly handles scenarios where arr2 might have one fewer element than arr1. It compares the counts and identifies the missing element or handles cases where the missing element isn't found.

**Solution:** To be found in the file *"Riddle 3 - Missing Finder.py"*
