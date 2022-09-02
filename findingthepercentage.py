if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input() 
    total = 0
    
    for i in range(len(student_marks[query_name])):
        new_num = student_marks[query_name][i]
        total = total + new_num

    print("{:.2f}".format(total/len(student_marks[query_name])))
