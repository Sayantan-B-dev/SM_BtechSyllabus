# Working with Lists

**Course:** Python Programming  
**Module:** 3 | **Lecture:** 4  
**Date:** 19-Aug-2026  
**Faculty:** PRANAB GHARAI  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Python Programming using Problem Solving Approach By Reema Thareja Page: 146-204

## Adding Elements to a List

### `append()` -- Add at the End

`append(x)` adds a single element `x` to the end of the list. It modifies the list in-place and returns `None`.

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# Appending a list adds the entire list as ONE element
fruits.append(["date", "elderberry"])
print(fruits)
# ['apple', 'banana', 'cherry', ['date', 'elderberry']]
```

### `extend()` -- Add Multiple Elements

`extend(iterable)` adds each element of the iterable to the end of the list. Unlike `append`, it does not add the iterable as a single element.

```python
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]

# Compare with append
c = [1, 2, 3]
c.append([4, 5, 6])
print(c)  # [1, 2, 3, [4, 5, 6]]

# extend works with any iterable (string, tuple, range)
nums = [1, 2]
nums.extend(range(3, 6))
print(nums)  # [1, 2, 3, 4, 5]
```

### `insert()` -- Add at a Specific Position

`insert(index, element)` inserts an element at the given index. Elements to the right are shifted.

```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print(fruits)  # ['apple', 'banana', 'cherry']

# Insert at the beginning
fruits.insert(0, "apricot")
print(fruits)  # ['apricot', 'apple', 'banana', 'cherry']

# Insert at the end (same as append)
fruits.insert(len(fruits), "date")
print(fruits)  # ['apricot', 'apple', 'banana', 'cherry', 'date']
```

## Removing Elements

### `remove()` -- Remove by Value

`remove(x)` removes the **first occurrence** of value `x`. Raises `ValueError` if the value is not found.

```python
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")  # removes the FIRST banana
print(fruits)  # ['apple', 'cherry', 'banana']

# fruits.remove("grape")  # ValueError: list.remove(x): x not in list
```

### `pop()` -- Remove by Index (and Return)

`pop(index)` removes the element at the given index and **returns** it. If no index is given, it removes and returns the last element.

```python
fruits = ["apple", "banana", "cherry", "date"]

# Pop the last element
last = fruits.pop()
print(last)   # date
print(fruits) # ['apple', 'banana', 'cherry']

# Pop at a specific index
second = fruits.pop(1)
print(second)  # banana
print(fruits)  # ['apple', 'cherry']
```

### `del` Statement

The `del` statement removes an element at a given index (or a slice). It does not return the removed value.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Delete a single element
del fruits[1]
print(fruits)  # ['apple', 'cherry', 'date', 'elderberry']

# Delete a slice
del fruits[1:3]
print(fruits)  # ['apple', 'elderberry']

# Delete the entire list
del fruits
# print(fruits)  # NameError: name 'fruits' is not defined
```

## Searching and Counting

### `index()` -- Find Position of a Value

`index(x)` returns the index of the **first** occurrence of `x`. Raises `ValueError` if not found. You can also specify start and end bounds.

```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

print(fruits.index("banana"))      # 1 (first occurrence)
print(fruits.index("banana", 2))   # 3 (search starting from index 2)
print(fruits.index("banana", 2, 4)) # 3 (search between index 2 and 4)

# fruits.index("grape")  # ValueError: 'grape' is not in list
```

### `count()` -- Count Occurrences

`count(x)` returns the number of times `x` appears in the list.

```python
nums = [1, 2, 2, 3, 2, 4, 2, 5]
print(nums.count(2))  # 4
print(nums.count(1))  # 1
print(nums.count(9))  # 0
```

## Sorting and Reversing

### `sort()` -- In-Place Sort

`sort()` sorts the list in ascending order **in-place** (modifies the original list). It returns `None`.

```python
numbers = [4, 2, 9, 1, 5, 3]
numbers.sort()
print(numbers)  # [1, 2, 3, 4, 5, 9]

# Descending order
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1]

# Sorting strings (alphabetical)
words = ["banana", "apple", "cherry", "date"]
words.sort()
print(words)  # ['apple', 'banana', 'cherry', 'date']
```

### `sorted()` -- Return a New Sorted List

`sorted()` returns a **new** sorted list without modifying the original.

```python
numbers = [4, 2, 9, 1, 5]
sorted_nums = sorted(numbers)
print(sorted_nums)  # [1, 2, 4, 5, 9]
print(numbers)      # [4, 2, 9, 1, 5]  -- original unchanged

# Descending
print(sorted(numbers, reverse=True))  # [9, 5, 4, 2, 1]
```

### `reverse()` -- In-Place Reverse

`reverse()` reverses the list in-place. It returns `None`.

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
```

## `clear()` -- Remove All Elements

`clear()` removes all elements from the list, leaving an empty list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # []
```

## Complete Method Reference Table

| Method | Description | Modifies in-place? | Returns |
|--------|-------------|-------------------|---------|
| `append(x)` | Adds x to the end | Yes | `None` |
| `extend(iter)` | Adds each element of iterable | Yes | `None` |
| `insert(i, x)` | Inserts x at index i | Yes | `None` |
| `remove(x)` | Removes first occurrence of x | Yes | `None` |
| `pop(i)` | Removes and returns element at i | Yes | The element |
| `pop()` | Removes and returns last element | Yes | The element |
| `del lst[i]` | Deletes element at i | Yes | Nothing |
| `index(x)` | Returns index of first x | No | Integer |
| `count(x)` | Counts occurrences of x | No | Integer |
| `sort()` | Sorts ascending | Yes | `None` |
| `reverse()` | Reverses order | Yes | `None` |
| `clear()` | Removes all elements | Yes | `None` |

---

## Practice Problems

**Problem 1:** Start with `nums = [3, 1, 4, 1, 5, 9, 2, 6]`. Perform these operations in order:
- Append `5` to the end
- Insert `0` at the beginning
- Remove the first occurrence of `1`
- Pop the element at index 3
- Sort the list in descending order

<details>
<summary>Answer</summary>

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.append(5)
nums.insert(0, 0)
nums.remove(1)
popped = nums.pop(3)
nums.sort(reverse=True)
print(nums)     # [9, 6, 5, 4, 3, 2, 0]
print(popped)   # 5
```
</details>

**Problem 2:** Write a program that takes a list of numbers and removes all occurrences of a specific value using a loop and `remove()`. Test with `nums = [1, 2, 3, 2, 4, 2, 5]` and remove all `2`s.

<details>
<summary>Hint</summary>

Be careful: removing elements while iterating forward can skip elements. Iterate over a copy or use a while loop.

```python
nums = [1, 2, 3, 2, 4, 2, 5]
while 2 in nums:
    nums.remove(2)
print(nums)  # [1, 3, 4, 5]
```
</details>

**Problem 3:** Use `extend()` to add all elements of `[10, 20, 30]` to `base = [1, 2, 3]`. Then use `append()` to add `[40, 50]` as a single element. Print the final list.

<details>
<summary>Answer</summary>

```python
base = [1, 2, 3]
base.extend([10, 20, 30])
base.append([40, 50])
print(base)  # [1, 2, 3, 10, 20, 30, [40, 50]]
```
</details>

**Problem 4:** Use `index()` and `count()` to find the position and number of occurrences of `"apple"` in `fruits = ["banana", "apple", "cherry", "apple", "date"]`.

<details>
<summary>Answer</summary>

```python
fruits = ["banana", "apple", "cherry", "apple", "date"]
print(fruits.index("apple"))  # 1
print(fruits.count("apple"))  # 2
```
</details>

**Problem 5:** Write code that creates a list `[1, 2, 3, 4, 5]`, reverses it in-place, then clears it. Print the list after each operation.

<details>
<summary>Answer</summary>

```python
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)  # [5, 4, 3, 2, 1]
nums.clear()
print(nums)  # []
```
</details>
