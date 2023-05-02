from dataclasses import dataclass, field
import requests
from hook.formatter import Formatter


@dataclass
class Requester:
    """
    Requester Class
    """

    code_list: list
    URL: str = "http://127.0.0.1:8000/api/v1/code/"
    request: requests = requests
    data: dict = field(default=None)

    def __post_init__(self):
        self.data = {"code_list": self.code_list}

    def post(self):
        """
        :param code_list: A list of str codes.
        :return: boolean
        """
        # Dados a serem enviados para a API
        data = {"code_list": self.code_list}

        # Fazer a chamada para a API e enviar os dados
        api_url = self.URL
        response = self.request.post(api_url, json=data)
        # Verificar se a chamada foi bem-sucedida
        if response.status_code == 200:
            # Sprint(response)
            # Processar os resultados da avaliação
            result = response.json()
            print(Formatter.show_request_result(result))

            result_code_values = result["code"].values()
            all_empty = all(item == {} for item in result_code_values)

            if all_empty:
                print("PASSED: PEP8")
                return True
            else:
                print("NOT OK...")
                # print(result)
                # Retornar True ou False, dependendo do resultado da avaliação
                return False
        else:
            print("Falha ao chamar a API:", response.status_code)
            return False
