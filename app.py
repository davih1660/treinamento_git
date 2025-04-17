import requests

def ola_mundo():
 response = requests.get("https://api.github.com")
 print (f"Olá, turma! API Status: {response}")

if __name__ == "__main__":
 ola_mundo()