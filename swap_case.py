def swap_case(s):
    str_arr = []
    for i in s:
        if i == i.lower():
            str_arr.append(i.upper())
        
        elif i == i.upper():
            str_arr.append(i.lower())
        
        else:
            str_arr.append(i)
            
    str = ("").join(str_arr)
    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)