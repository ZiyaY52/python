if __name__ == '__main__':
    arr = []
    names = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)

    arr = list(zip(names,scores))
    arr.sort(key = lambda row:(row[1],row[0]))
    scores = (list(set(scores)))
    scores.sort()
    lowest_score = scores[1]
    for i in range (len(arr)):
        if arr[i][1] == lowest_score:
            print(arr[i][0])