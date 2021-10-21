
def upper_case_conversion(string: str):
    # string = "small coffee"
    # newstring = []
    # for i in string.split(" "):
    #     i = (i[0].upper() + i[1:].lower())
    #     newstring.append(i)
    #     x = " ".join(newstring)
    # print(x)
    
    # list comprehension applied to combine code into one liner return
    return " ".join([(i[0].upper() + i[1:].lower()) for i in string.split(" ")])
