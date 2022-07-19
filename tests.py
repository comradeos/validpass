import unittest, os
os.chdir(os.path.dirname(__file__))
from main import is_valid, valid_pass_counter

class TestMain(unittest.TestCase):

    def test_is_valid_true(self):
        line = 'a 1-5: abc345435345dj' # правильный формат строки
        result = is_valid(line)
        self.assertEqual(result, True)

    def test_is_valid_false_empty(self):
        line = '' # пустая строка
        result = is_valid(line)
        self.assertEqual(result, False)

    def test_is_valid_false_wrong_line_format(self):
        line = '!@%#$&!^@$%&!^%@#*$@#&' # неверный формат строки
        result = is_valid(line)
        self.assertEqual(result, False)

    def test_valid_pass_counter_2(self):
        result = valid_pass_counter('file_1') # файл из условия
        self.assertEqual(result, 2)
    
    def test_valid_pass_counter_3(self):
        result = valid_pass_counter('file_2') # файл из 4х паролей с 1 невалидным паролем
        self.assertEqual(result, 3)
                
    def test_valid_pass_counter_1(self):
        result = valid_pass_counter('file_3') # файл с одним валидным паролем, остальные строки в неверном формате
        self.assertEqual(result, 1)
    
    def test_valid_pass_counter_empty_file(self):
        result = valid_pass_counter('file_4') # пустой файл
        self.assertEqual(result, 0)
                 
    def test_valid_pass_counter_no_file(self):
        result = valid_pass_counter('no_such_file') # отсутствующий файл
        self.assertEqual(result, 0)
        
    def test_valid_pass_counter_empty_filename(self):
        result = valid_pass_counter('') # имя файла не введено
        self.assertEqual(result, 0)
            
if __name__ == '__main__':
    unittest.main()