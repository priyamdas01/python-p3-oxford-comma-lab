def oxford_comma(items):
    str = ", ".join(items)
    if len(items) == 2:
        str = " and ".join(items)
    else:
        str = str.replace(f", {items[-1]}", f", and {items[-1]}")
    return str