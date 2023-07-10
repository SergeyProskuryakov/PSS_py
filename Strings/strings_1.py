# доказать, что все 4 типа строк идентичны

stroka_1 = 'abc'
stroka_2 = "abc"
stroka_3 = '''abc'''
stroka_4 = """abc"""
if stroka_1 == stroka_2 == stroka_3 == stroka_4:
    print('строки равны')