# 7. Экзамен на получение водительских прав
PASS_EXAM = 15

def main():
    right_answers = 0
    wrong_answers = 0
    wrong_qst_number = 0
    wrong_qst_solution = ''
    right_qst_solution = ''
    solution = ['A', 'C', 'A', 'A', 'D',
               'B', 'C', 'A', 'C', 'B',
               'A', 'D', 'C', 'A', 'D',
               'C', 'B', 'B', 'D', 'A']

    infile = open('F:\python_test_files\student_solution_fail.txt', 'r')
    student_solution = infile.readlines()
    infile.close()

    for index in range(len(student_solution)):
        student_solution[index] = student_solution[index].rstrip('\n')

    for index in range(len(student_solution)):
        if solution[index] == student_solution[index]:
            right_answers += 1
        else:
            wrong_answers += 1
            wrong_qst_number = index+1
            wrong_qst_solution = student_solution[index]
            right_qst_solution = solution[index]

            print(f'Неверный ответ: Впорос №{wrong_qst_number},\n'
                  f'Ваш ответ: {wrong_qst_solution},\n'
                  f'Верный ответ: {right_qst_solution};\n')
    
    if right_answers >= PASS_EXAM:
        print('Экзамен сдан')
        print(f'Правильных ответов: {right_answers}')
        print(f'Неправильных ответов: {wrong_answers}')
    else:
        print('Экзамен не сдан')
        print(f'Правильных ответов: {right_answers}')
        print(f'Неправильных ответов: {wrong_answers}')


if __name__ == '__main__':
    main()
