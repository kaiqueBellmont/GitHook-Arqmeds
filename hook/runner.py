from dataclasses import dataclass
import subprocess
from .requester import Requester


@dataclass
class Runner:
    @staticmethod
    def run():
        """
        Main class
        """
        try:
            # Capturar as mudanças em estágio (staged changes) usando o comando git diff
            output = subprocess.check_output(
                ["git", "diff", "--staged", "--name-only"], universal_newlines=True
            )
            # Filtrar apenas os arquivos .py modificados, excluindo os __init__.py
            arquivos_modificados = [
                arquivo
                for arquivo in output.split("\n")
                if arquivo.endswith(".py") and not arquivo.endswith("__init__.py")
            ]
            ## print(arquivos_modificados)

            # Criar uma lista de JSONs com os nomes dos arquivos e as alterações
            code_list = []
            for arquivo in arquivos_modificados:
                try:
                    with open(arquivo, "r") as file:
                        code = file.read()
                        code_json = {
                            arquivo: code
                        }  # Nome do arquivo como chave e código como valor
                        code_list.append(code_json)
                except IOError as e:
                    print("Erro ao abrir o arquivo:", e)
                    exit(1)

            if not Requester(code_list).post():
                exit(1)
        except subprocess.CalledProcessError as e:
            print("Erro ao capturar as mudanças em estágio:", e)
            exit(1)


Runner.run()
