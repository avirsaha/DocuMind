import unittest
from ...pytextflow import tokenization


class TestTokenizationAlgorithm(unittest.TestCase):
    def test_tokenizer(self) -> None:
        input_string = "this is python 3 11 4"
        expected_tokens = ["this", "is", "python", "3", "11", "4"]

        actual_tokens = tokenization.tokenizer(input_string)
        self.assertEqual(
            actual_tokens,
            expected_tokens,
            f"Tokens do not match: {actual_tokens} != {expected_tokens}",
        )

    def test_tokenizer_empty_string(self) -> None:
        input_string = ""
        expected_tokens = []

        actual_tokens = tokenization.tokenizer(input_string)
        self.assertEqual(
            actual_tokens,
            expected_tokens,
            f"Tokens do not match: {actual_tokens} != {expected_tokens}",
        )

    def test_tokenizer_only_numbers(self) -> None:
        input_string = "123 456 789"
        expected_tokens = ["123", "456", "789"]

        actual_tokens = tokenization.tokenizer(input_string)
        self.assertEqual(
            actual_tokens,
            expected_tokens,
            f"Tokens do not match: {actual_tokens} != {expected_tokens}",
        )

    def test_tokenizer_special_characters(self) -> None:
        input_string = "hello! how are you?"
        expected_tokens = ["hello!", "how", "are", "you?"]

        actual_tokens = tokenization.tokenizer(input_string)
        self.assertEqual(
            actual_tokens,
            expected_tokens,
            f"Tokens do not match: {actual_tokens} != {expected_tokens}",
        )


if __name__ == "__main__":
    # Use TextTestRunner with failfast and colored output options
    unittest.TextTestRunner(verbosity=2).run(
        unittest.TestLoader().loadTestsFromTestCase(TestTokenizationAlgorithm)
    )
