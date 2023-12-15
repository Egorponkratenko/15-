# Ежегодно одиннадцатиклассники в школах сдают ЕГЭ,
# получая за каждый экзамен целое количество баллов в диапазоне от 0 до 100.
# У нас имеется информация о N учениках.
# Каждый ученик может сдавать любое количество экзаменов,
# а экзамены можно сдавать в любом порядке.
# Во входных данных в явном виде указываются название предметов, по которым проходил экзамен, и полученные баллы.
# Необходимо посчитать следующие значения:
# сумму баллов за все предметы у каждого ученика
# средний балл по каждому предмету среди всех учеников
data = {
    'Вова' : {'аенглийский' :20,'биология' :60,'физика' :99},
'вася' : {'рус' :22,'матем' :62,'информатика' :100} ,
'петя' : {'химия' :23,'биология' :43,'физика' :99}
}

for name , subjects in data.items():
    print(f'{name}:{sum(subjects.values())}')
    subject_scores = {}
for line in data.values():
    for subject in line.keys():
        if subject in subject_scores:
            subject_scores[subject].append(line[subject])
        else:
            subject_scores[subject]= [line[subject]]
print(subject_scores)
for subject,score in subject_scores.items():
    print(f'{subject}:{sum(score)/len(score)}')