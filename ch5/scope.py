#same variable name but in different scopes.
def bacon():
    spam = 99
    print(spam)

spam = 42
print(spam)
bacon()
print(spam)
