def classmate(name, gender=True):


    gender_text = "男生"
    if not gender:
        gender_text = '女生'

    print('%s是%s' % (name, gender_text))

classmate('xiaoming',True)
classmate('laowang')

