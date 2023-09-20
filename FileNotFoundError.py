import unittest
from plagiarism_checker import calculate_similarity

class PlagiarismCheckerTest(unittest.TestCase):
    def test_file_not_found(self):
        # 准备测试数据
        original_file = "nonexistent_file.txt"
        copied_file = "copied_file.txt"

        # 执行测试
        with self.assertRaises(FileNotFoundError):
            calculate_similarity(original_file, copied_file)

if __name__ == '__main__':
    unittest.main()