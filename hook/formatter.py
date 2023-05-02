from dataclasses import dataclass
import ast


@dataclass
class Formatter:
    """
    Formatter class
    """

    @staticmethod
    def print_formatted_list(string_list):
        """

        :param string_list:
        """
        # Unir os elementos da lista em uma única string
        formatted_string = ''.join(string_list)

        # Remover os caracteres indesejados no início e no final da string
        formatted_string = formatted_string.strip('["\n]')

        # Remover as quebras de linha desnecessárias e imprimir cada item em um formato legível
        formatted_string = formatted_string.replace('\\n', '\n').strip('"\n')
        print(formatted_string)

    @staticmethod
    def show_request_result(result):
        """
        :param result: Result from request
        """
        for file, errors in result['code'].items():
            print("*" * 50)
            print(f"Result for File: {file}:")
            for line, messages in errors.items():
                formatted_messages = "\n\t".join(messages)
                print(f"Line {line}:\n\t{formatted_messages}")
        print("*" * 50)
        print("Insight:")
        Formatter.print_formatted_list(result["insight"])
        print("*" * 50)



result = {
    "code": {
        "apagar2.py": {
            "1": [
                "[F401] 'datetime' imported but unused"
            ],
            "3": [
                "[E302] expected 2 blank lines, found 1"
            ],
            "8": [
                "[E305] expected 2 blank lines after class or function definition, found 1",
                "[E501] line too long (135 > 79 characters)"
            ]
        },
        "hook/formatter.py": {
            "32": [
                "[E501] line too long (94 > 79 characters)"
            ]
        }
    },
    "insight": [
        "[\"\\n\\n1. The indentation in both codes could be improved to make the code easier to read.\\n2. The code in apagar2.py could be re",
        "factored to make use of an efficient data structure than a string.\\n3. The show_in_code_format() function in hook/formatter.py c",
        "ould be refactored to be more efficient and make use of built-in methods.\\n4. Descriptive variable names could be used to promot",
        "e readability and clarity.\"]"
    ]
}
