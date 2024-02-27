Projeto de Gerenciamento Financeiro em Python:
Este projeto consiste em um aplicativo de gerenciamento financeiro desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica. O sistema permite aos usuários registrar suas despesas e receitas, visualizar totais, gráficos de barra e pizza, categorizar transações e obter uma análise detalhada de seus gastos e receitas.

Funcionalidades:
Registro de Transações: Os usuários podem inserir despesas e receitas, especificando a categoria, data e valor.
Visualização de Dados: Apresentação dos dados em tabelas e gráficos para uma análise visual.
Categorização: Possibilidade de categorizar as transações para uma organização mais eficiente.
Login Seguro: Sistema de login com autenticação para acesso seguro ao aplicativo.
Banco de Dados SQLite: Utilização do SQLite para armazenar os dados de forma persistente.

Componentes do Projeto:
Main: Contém a interface principal do aplicativo, com widgets para inserção de dados, visualização de tabelas e gráficos.
View: Módulo responsável pelas operações de leitura e escrita no banco de dados, incluindo inserção, deleção e consulta de dados.
Login: Interface de login que verifica as credenciais do usuário antes de permitir o acesso ao aplicativo.
CriarBD: Script para criação do banco de dados SQLite e das tabelas necessárias.

Tecnologias utilizadas:

Python: Linguagem de programação principal.
Tkinter: Biblioteca para construção da interface gráfica.
SQLite: Banco de dados embutido para armazenamento dos registros financeiros.
Pandas: Utilizado para manipulação de dados, especialmente na geração de gráficos.
Matplotlib: Biblioteca para criação de gráficos.
PIL (Pillow): Utilizado para manipulação de imagens, como logotipos.
tkcalendar: Para seleção de datas na interface.
Os: Para integração com o sistema operacional, utilizado no login.

Como Executar o Projeto:

Clone o repositório para o seu ambiente local.
Certifique-se de ter o Python instalado em seu sistema.
Execute o arquivo criarbd.py para criar o banco de dados.
Inicie o aplicativo executando login.py.
Faça login com usuário "ruan" e senha "123456".
Registre suas despesas e receitas, categorizando-as conforme desejado.
Visualize totais mensais e gráficos para análise financeira.
