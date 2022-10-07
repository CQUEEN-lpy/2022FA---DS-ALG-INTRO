from Sorting.OBJ import Student
import random

def Coungting_Sort(l, k):
    count_l = []
    tmp_l = l.copy()
    for i in range(0, k+1):
        count_l.append(0)

    for i in l:
        count_l[i.grade] += 1

    for i in range(1, k+1):
        count_l[i] = count_l[i-1] + count_l[i]

    for i in range(len(l)-1, -1, -1):
        count_l[l[i].grade] += -1
        tmp_l[count_l[l[i].grade]] = l[i]

    return tmp_l




if __name__ == '__main__':
    num = 10
    grade_range = 10
    l = []
    for i in range(0, num):
        name = 'S' + str(i)
        height = round(random.random() * 200, 2)
        grade = random.randint(0, grade_range)
        l.append(Student(name, height, grade))

    l = Coungting_Sort(l, grade_range)
    for i in l:
        print(i.grade)

