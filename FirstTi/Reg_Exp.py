# Дана строка email_str, извлечь имейлы из текста
import re

email_str = 'По всем вопросам обращаться по email ghjh@mail.com или email начальника ghelji@mail.com'

reg_exp1 = r'[\w\.-]+@[\w\.-]+'

emails = re.findall(reg_exp1, email_str)

for email in emails:
    print(email)


# Нужно выветси только тк строки, где "кот" отдельное слово

cats_list = [
    "кот в сапогах",
    "кошка и кот",
    "котофей",
    "котяра",
]

reg_exp2 = r'\bкот\b'

for cat in cats_list:
    if re.search(reg_exp2, cat):
        print(cat)
