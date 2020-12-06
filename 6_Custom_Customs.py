from Custom_Customs_input import input

result = 0
for group in input.split("\n\n"):
    answers = group.split('\n')
    common_answers = set(answers[0])
    for answer in answers:
        common_answers = common_answers.intersection(answer)
        if not common_answers:
            break
    print(common_answers)
    result += len(common_answers)

print(result)
