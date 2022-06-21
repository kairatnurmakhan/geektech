Geektech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bug': {'fails', 'errors', 'stack'}
}
del Geektech['bug']
new_courses = ['GeekCamp', 'FULL STACK', 'UX|UI', 'IOS', 'Алгоритм', 'English']
Geektech['address'] = 'Ibraimova 103'
Geektech['Tel'] = '+996 770 00 46 30'
Geektech['Insta'] = 'geektech__kg'
Geektech['courses'].extend(new_courses)
Geektech['courses'] = tuple(Geektech['courses'])
for k, v in Geektech.items():
    print(f'{k}:{v}')
print(Geektech.keys())
print(Geektech.values())
