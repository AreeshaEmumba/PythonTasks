import unittest
from unittest.mock import patch
from main import run_command, extract_info_from_file, write_to_output_file  # Replace with your actual module name

class TestProgram(unittest.TestCase):

    @patch('main.subprocess.run')
    def test_run_command_string(self, mock_subprocess):
        # Mock a successful subprocess result with a string output
        mock_subprocess.return_value.returncode = 0
        mock_subprocess.return_value.stdout = "Sample String Output\n"

        result = run_command("echo Sample String")
        self.assertEqual(result, "Sample String Output", "Failed to fetch string value correctly")

    @patch('main.subprocess.run')
    def test_run_command_not_found(self, mock_subprocess):
        # Mock a failed subprocess result
        mock_subprocess.return_value.returncode = 1
        mock_subprocess.return_value.stdout = ""

        result = run_command("nonexistent_command")
        self.assertEqual(result, "Not Found", "Failed to return 'Not Found' for invalid command")

    @patch('main.subprocess.run')
    def test_run_command_integer(self, mock_subprocess):
        # Mock a subprocess result with an integer output
        mock_subprocess.return_value.returncode = 0
        mock_subprocess.return_value.stdout = "123\n"

        result = run_command("echo 123")
        self.assertEqual(result, "123", "Failed to fetch integer value correctly")

    @patch('main.subprocess.run')
    def test_run_command_float(self, mock_subprocess):
        # Mock a subprocess result with a float output
        mock_subprocess.return_value.returncode = 0
        mock_subprocess.return_value.stdout = "123.45\n"

        result = run_command("echo 123.45")
        self.assertEqual(result, "123.45", "Failed to fetch float value correctly")

    @patch('main.run_command')
    def test_extract_info_from_file(self, mock_run_command):
        # Mock specific pattern results
        mock_run_command.side_effect = lambda x: "Mocked Value" if "mock_pattern" in x else "Not Found"

        patterns = {
            "Mocked Key": "mock_pattern {file}",
            "Another Key": "another_pattern {file}"
        }
        result = extract_info_from_file("mock_file_path", patterns)

        self.assertEqual(result["Mocked Key"], "Mocked Value", "Failed to fetch mocked string value")
        self.assertEqual(result["Another Key"], "Not Found", "Failed to handle missing pattern correctly")

if __name__ == '__main__':
    unittest.main()
