commands = [
    ("v35", -5),
    ("v16n36", -6),
    ("v16n65", -6),
    ("v25n36", -7),
    ("v06n62", -8),
    ("v05n09", -9),
    ("v99", -10)
]

def double_str(num: int) -> str:
    if num < 0:
        return "-" + str(num)
    if num < 10:
        return "0" + str(num)
    return str(num)