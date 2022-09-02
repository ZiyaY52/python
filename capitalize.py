def solve(s):
    str_arr = []
    str_arr = s.split()
    str_cap_arr = []

    for i in str_arr:
        str_cap_arr.append(i.capitalize())

    str = " ".join(str_cap_arr)
    return str


if __name__ == '__main__':


    s = input()

    result = solve(s)
    print(result)