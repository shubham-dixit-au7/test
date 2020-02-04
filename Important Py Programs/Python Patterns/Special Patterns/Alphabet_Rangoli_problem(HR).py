# Question-(HR Problem) (URL-https://www.hackerrank.com/challenges/alphabet-rangoli/problem?h_r=internal-search)

# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# #size 3  (characters-9)

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5 (characters-17)

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# #size 10 (characters-37)

# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------
# The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

# Input Format

# Only one line of input containing N, the size of the rangoli.

# Constraints

# 0 < N < 27

# Output Format

# Print the alphabet rangoli in the format explained above.

# Sample Input

# 5
# Sample Output

# --------e--------       (8 * "-" + "e" + 8 * "-")
# ------e-d-e------       (6 * "-" + "e" + "-" + "d" + "-" + "e" + 6 * "-")
# ----e-d-c-d-e----       (4 * "-" + "e" + "-" + "d" + "-" + "c" + "-" + "d" + "-" + "e" + 4 * "-")
# --e-d-c-b-c-d-e--       (2 * "-" + "e" + "-" + "d" + "-" + "c" + "-" + "b" + "-" + "c" + "-" + "d" + "-" + "e" + 2 * "-")
# e-d-c-b-a-b-c-d-e       (0 * "-" + "e" + "-" + "d" + "-" + "c" + "-" + "b" + "-" + "a" + "-" + "b" + "-" + "c" + "-" + "d" + "-" + "e" + 0 * "-")
# --e-d-c-b-c-d-e--       (2 * "-" + "e" + "-" + "d" + "-" + "c" + "-" + "b" + "-" + "c" + "-" + "d" + "-" + "e" + 2 * "-")
# ----e-d-c-d-e----       (4 * "-" + "e" + "-" + "d" + "-" + "c" + "-" + "d" + "-" + "e" + 4 * "-")
# ------e-d-e------       (6 * "-" + "e" + "-" + "d" + "-" + "e" + 6 * "-")
# --------e--------       (8 * "-" + "e" + 8 * "-")







value = int(input("Enter the size of Alphabet Rangoli -> ")) 
for line in range(1,(value + 1)):
    print("-" * (2* (value - line)), end="")
    s1=(chr(96 + value))
    s2=""
    for char in range (1,line):
        s1= s1 + ("-" + (chr(96 + value - char)))
    s2= s1[::-1]
    print(s1 + s2[1:], end="")
    print("-"*(2*(value-line)))

for line in range(value-1,0,-1):
    print("-" * (2* (value - line)), end="")
    s1=(chr(96 + value))
    s2=""
    for char in range (1,line):
        s1= s1 + ("-" + (chr(96 + value - char)))
    s2= s1[::-1]
    print(s1 + s2[1:], end="")
    print("-"*(2*(value-line)))

    
    


