
import re

def valid_mult_ops(text: str) -> list[tuple[int,int]]:
    """
    Given a string of text, find all occurences of pattern mult(x,y).
    Collect x and y, convert them to integers, and return as list.
    """
    mult_pattern = r"mul\((\d+),(\d+)\)"
    return [(int(x), int(y)) for x,y in re.findall(mult_pattern, text)]


# Parsing numbers
input = None
with open("day3_input.txt", "r") as f:
    input = f.read().replace("\n", "")

# Part 1
nums = valid_mult_ops(input)
total = sum(num1*num2 for num1, num2 in nums)

print(f"The sum of mult(num1,num2) operations are: {total}")

# Part 2

# Filter the input string to remove any invalid pieces
# Remove parts that look like: "don't()...do()"
dont_pattern = r"don\'t\(\)"
do_pattern = r"do\(\)"
ignore_pattern = dont_pattern + r".*?" + do_pattern

filtered_input = re.sub(pattern=ignore_pattern,
                        repl="",
                        string=input)

# If don't still in string, remove all of string after it.
dont_idx = filtered_input.find(r"don't")
if dont_idx != -1:
    filtered_input = filtered_input[:dont_idx]

# Treat like Part 1 again.
valid_nums = valid_mult_ops(filtered_input)
valid_total = sum(num1*num2 for num1,num2 in valid_nums)

print("Ignoring mult operations between don't()...do().\n"
    f"The sum of mult(num1,num2) operations are: {valid_total}")

