"""
filter(function,iterable)
"""

def fun(val):
    letters=["a","e","i","o","u"]
    if val in letters:
        return True
    else:
        return False


str1="python"
filtered=filter(fun,str1)
print(list(filtered))
