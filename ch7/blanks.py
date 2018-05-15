word = "hello"
blank = "_" * len(word)
correct = "eo"

print(blank)
for i in range(len(word)):
    if word[i] in correct:
        # strings are immutable, build a string from splices
        blank = blank[:i] + word[i] + blank[i + 1:]
print(blank)
