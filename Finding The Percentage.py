if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(0, n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = sum(scores)/float(len(scores))
    query_name = input()
    print("%.2f" % student_marks[query_name])
        