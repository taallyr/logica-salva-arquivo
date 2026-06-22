import json
import csv
import os

def exibir_menu():
    print("Menu:")
    print("1. Ler")
    print("2. Salvar")
    print("3. Sair")
    return input("Digite uma opção do menu (1-3): ")

def solicitar_dados():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    idade = input("Idade: ")
    return {"nome": nome, "sobrenome": sobrenome, "idade": idade}

def validar_formato(nome_arquivo):
    ext = os.path.splitext(nome_arquivo)[1].lower()
    return ext in [".txt", ".csv", ".json"]

def salvar_dados():
    dados = solicitar_dados()
    nome_arquivo = input("Digite o nome do arquivo para salvar: ")
    if not validar_formato(nome_arquivo):
        print("Formato inválido. Use .txt, .csv ou .json.")
        return
    ext = os.path.splitext(nome_arquivo)[1].lower()
    if ext == ".txt":
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome: {dados['nome']}\n")
            arquivo.write(f"Sobrenome: {dados['sobrenome']}\n")
            arquivo.write(f"Idade: {dados['idade']}\n")
    elif ext == ".csv":
        with open(nome_arquivo, "w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["nome", "sobrenome", "idade"])
            escritor.writerow([dados["nome"], dados["sobrenome"], dados["idade"]])
    else:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    print("Dados salvos com sucesso.")

def ler_arquivo():
    nome_arquivo = input("Digite o nome do arquivo para ler: ")
    if not os.path.exists(nome_arquivo):
        print("Arquivo não encontrado.")
        return
    if not validar_formato(nome_arquivo):
        print("Formato inválido. Use .txt, .csv ou .json.")
        return
    ext = os.path.splitext(nome_arquivo)[1].lower()
    if ext == ".txt":
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            print(arquivo.read())
    elif ext == ".csv":
        with open(nome_arquivo, "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print("; ".join(linha))
    else:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            print(json.dumps(dados, ensure_ascii=False, indent=4))

def main():
    while True:
        opcao = exibir_menu()
        if opcao == "1":
            ler_arquivo()
        elif opcao == "2":
            salvar_dados()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()