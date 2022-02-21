students = [
    {"name": "阿土",
     "age": 20,
     "gender": True,
     "height": 1.7,
     "weight": 75.0},
    {"name": "小美",
     "age": 19,
     "gender": False,
     "height": 1.6,
     "weight": 45.0},
]
find_name = "阿土"
for ss in students:
    print(ss)
    if ss['name'] == find_name:
        print('找到了%s' % find_name)
        break