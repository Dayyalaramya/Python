word = "education"
count = 0

for ch in word:
    if ch in "aeiou":
        count += 1

print("Number of vowels =", count)