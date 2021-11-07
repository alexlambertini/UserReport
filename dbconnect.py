import sqlite3
from datetime import date
from classes import ShowPopup


def gravar_dados():

    try:
        banco = sqlite3.connect('relatorios.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados (nome text, email text, telefone integer, caso text, data integer)")
        cursor.execute("INSERT INTO dados (nome, email, telefone, caso, data) VALUES (?,?,?,?,?)", (nome , email, telefone, caso, data_atual))
        cursor.close()
        banco.commit()     

        print("foi")

    except:
        print("erro")


# Mensagens Poup
#sucesso = ShowPopup('Informação', 'Seus dados foram gravados com sucesso!')
#erro = ShowPopup('Informação', 'Erro ao gravar dados!')

