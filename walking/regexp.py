import re

# emails_str = "По всем вопроосам пишите на email ilja@mail.ru либо email руководителя andrew@mail.ru"
# reg_exp = r'[\w\.-]+@[\w\.-]+'
# emails = re.findall(reg_exp, emails_str)
# for email in emails:
#     print(email)

cats_list = [
    'кот в сапогах',
    'кошка и кот',
    'котофей',
    'кат яра'
]

reg_exp = r'\bкот\b'
for cat in cats_list:
    if re.search(reg_exp, cat):
        print(cat)


