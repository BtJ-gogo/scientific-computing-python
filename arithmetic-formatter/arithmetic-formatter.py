def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def arithmetic_arranger(problems, show_answers=False):
    output_list = []
    output = []
    answers_list = []
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        answers = []
        for problem in problems:
            write_char = ''
            problem = problem.replace(' ', '')
            for i in range(len(problem)):
                #number
                if problem[i].isdigit():
                    write_char += problem[i]
                    if i == len(problem) - 1:
                        if len(write_char) < 5:
                            answers.append(write_char)
                        else:
                            return 'Error: Numbers cannot be more than four digits.'
                #other
                else:
                    if problem[i] in ['+', '-']:
                        if len(write_char) < 5:
                            answers.append(write_char)
                        else:
                            return 'Error: Numbers cannot be more than four digits.'
                        answers.append(problem[i])
                        write_char = ''
                    elif problem[i] in ['/', '*']:
                        return "Error: Operator must be '+' or '-'."
                    else:
                        return "Error: Numbers must only contain digits."
            answers_list.append(answers)
            answers = []
        #cal
        for i in range(len(answers_list)):
            if '+' in answers_list[i]:
                answers_list[i].append(str(int(answers_list[i][0]) + int(answers_list[i][2])))
            elif '-' in answers_list[i]:
                answers_list[i].append(str(int(answers_list[i][0]) - int(answers_list[i][2])))
        #print
        count = 0
        for i, answers in enumerate(answers_list):
            #文字の最大数
            max_len = max(len(j) for j in answers[0:3]) + 2
            #文字数+2になるまで空白をいれる
            for j, answer in enumerate(answers):
                if is_number(answer):
                    answer = int(answer)
                    if j == 2:
                        output.append(f"{' ' * count * 4}"+f"{answer:{max_len}d}".replace(' ',answers_list[i][1],1))
                        output.append(f'{" " * count * 4}{"-" * max_len}')
                        print(max_len)
                    else:
                        output.append(f"{' ' * count * 4}{answer:{max_len}d}")
            output_list.append(output)
            output = []
            count = 1
        line_1 = line_2 = line_3 = line_4 =''
        for outputs in output_list:
            line_1 +=outputs[0]
            line_2 +=outputs[1]
            line_3 +=outputs[2]
            line_4 +=outputs[3]
    if show_answers: 
        return line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4
    else:
        return line_1 + "\n" + line_2 + "\n" + line_3
#arithmetic_arranger(["3801 - 2", "123 + 49"])
aaa = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
print(aaa)
print("  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------")
#print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
