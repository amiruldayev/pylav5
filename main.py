def oneonetwothree():
    print("\t\t\t\t\tTask 1.1")
    str = input()
    print(list(str.lower()))



    print("\t\t\t\t\tTask 1.2")
    char_count = {}

    for char in str:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    result = [(char, count) for char, count in char_count.items()]
    print(result)



    print("\t\t\t\t\tTask 1.3")
    list_vow = []
    list_cons = []
    list_sym = []

    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in str:
        if char.isalpha():
            if char.lower() in vowels:
                list_vow.append(char)
            else:
                list_cons.append(char)
        else:
            list_sym.append(char)
    print("vowels", list_vow)
    print("cons" , list_cons)
    print("symbols" , list_sym)


def onefour():
    print("\t\t\t\t\tTask 1.4")
    list_A = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9,10,2,1,3,4]



    n = len(sorted(list_A))
    q1_idx = n // 4
    q2_idx = q1_idx * 2
    q3_idx = q1_idx * 3

    q1 = sorted(list_A)[:q1_idx]
    q2 = sorted(list_A)[q1_idx:q2_idx]
    q3 = sorted(list_A)[q2_idx:q3_idx]
    q4 = sorted(list_A)[q3_idx:]

    if n % 2 != 0:
        q1.append(0)

    print("Q1:", q1)
    print("Q2:", q2)
    print("Q3:", q3)
    print("Q4:", q4)


def twoone():
    print("\t\t\t\t\tTask 2.1")
    student_name = input("Student name - ")

    assignment_scores = input("scores for assignments = ").split(',')
    assignment_scores = [int(score.strip()) for score in assignment_scores]

    lab_scores = input("labs = ").split(',')
    lab_scores = [float(score.strip()) for score in lab_scores]

    test_scores = input("tests =  ").split(',')
    test_scores = [int(score.strip()) for score in test_scores]

    student = {
        'name': student_name,
        'assignment': assignment_scores,
        'test': test_scores,
        'lab': lab_scores
    }

    print(student)

    print("\t\t\t\t\tTask 2.2")

    assignment_submitted = len(student.get('assignment', [])) == 4
    lab_submitted = len(student.get('lab', [])) == 2
    test_submitted = len(student.get('test', [])) == 2

    # Calculate the submission rate
    submission_rate = assignment_submitted + lab_submitted + test_submitted

    # Create the submission_check dictionary
    submission_check = {student['name']: submission_rate}

    print(submission_check)

#neonetwothree()
#onefour()
twoone()
