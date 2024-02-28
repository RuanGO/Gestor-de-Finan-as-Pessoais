import sys
import sqlite3 as lite
from datetime import datetime

# importing pandas
import pandas as pd

# Criando conexão
con = lite.connect('dados.db')

# Inserir categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)

# Inserir receitas
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

# Inserir gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)
       

#Funções para deletar

# Deletar receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)

# Deletar gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)

# Ver Categorias
def ver_categorias():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

# Ver Receitas
def ver_receitas():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

# Ver Gastos
def ver_gastos():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

#função para dados da tabela
def tabela():
    gastos = ver_gastos()
    receitas = ver_receitas()


    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista


def total_receitas():
    with con:
        cur = con.cursor()
        cur.execute("SELECT SUM(valor) FROM Receitas")
        total = cur.fetchone()[0]
        return total if total else 0


def total_gastos():
    with con:
        cur = con.cursor()
        cur.execute("SELECT SUM(valor) FROM Gastos")
        total = cur.fetchone()[0]
        return total if total else 0


#função para dados do gráfico de barras
def bar_valores():
    #receita total...........
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    #despesas total...........
    gastos = ver_gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])

    gastos_total = sum(gastos_lista)

    #Saldo total-------------
    saldo_total = receita_total - gastos_total

    return [receita_total, gastos_total,saldo_total]


#função grafico pie
def pie_valores():
    gastos = ver_gastos()
    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    dataframe = pd.DataFrame(tabela_lista, columns= ['id','categoria','Data', 'valor'])
    dataframe = dataframe.groupby('categoria')['valor'].sum()

    lista_quantias = dataframe.values.tolist()
    lista_categorias = []

    for i in dataframe.index:
        lista_categorias.append(i)

    return([lista_categorias,lista_quantias])



#função porcentagem
def porcentagem_valor():
    receita_total = total_receitas()
    gastos_total = total_gastos()
    if receita_total == 0:
        return 0, 0
    total = ((receita_total - gastos_total)/ receita_total) * 100
    receita_porcentagem = (receita_total/receita_total) * total
    gastos_porcentagem = (gastos_total/receita_total) * total
    return round(total, 2), round(receita_porcentagem, 2), round(gastos_porcentagem, 2)


    #despesas total...........
    gastos = ver_gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])

    gastos_total = sum(gastos_lista)

    #Porcentagem total-------------
    total = ((receita_total - gastos_total)/ receita_total) * 100

    return [total]


