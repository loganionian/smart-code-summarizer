import unittest
from smart_code_summarizer.main import summarize_function_code, summarize_module_code

class TestSmartCodeSummarizer(unittest.TestCase):
    def test_summarize_function_code(self):
        code = 'def add(a, b): return a + b'
        summary = summarize_function_code(code)
        self.assertIn('adds two numbers', summary)

    def test_summarize_module_code(self):
        code = 'def add(a, b): return a + b\n\ndef subtract(a, b): return a - b'
        summary = summarize_module_code(code)
        self.assertIn('contains functions for addition and subtraction', summary)

if __name__ == "__main__":
    unittest.main()