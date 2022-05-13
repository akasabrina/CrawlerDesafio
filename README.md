# CrawlerDesafio
crawler inicial
 
 O proposito dele é:
 
  1. Abrir uma página do Chrome
  2. Entrar no site TripAdvisor
  3. Clica em aceitar os Cookies
  4. Clicar na barra de pesquisa e escreve "Congresso Nacional - Brasília"
  5. Escolher a terceira opção que aparecer
  6. Vai carregar a página referente a opção
  7. E vai coletar os dados da avalição e do número de avaliações que aquele lugar possuir

# Bibliotecas 
SELENIUM: pip e driver

 1. Entrar no site https://selenium-python.readthedocs.io/ 
 2. Clicar em instalação
 3. Instalação do pip no terminal(“pip install selenium”), instruções do 1.2 ou 1.3
 4. Baixar o driver para o seu tipo de browser, instrução do 1.5
 5. Atenção: o driver utilizado no codigo é do chrome e da versão do meu browser(101). fique atento quanto a isso.

BEAUTIFUL SOUP: pip

 1. instalação do pip no terminal(“pip install  bs4”)

É extremamente importante que tudo esteja apropriadamente instalado, pois, é fundamental para o funcionamento do web crawler!!!

Caso já tenha as bibliotecas na sua máquina pode pular essa etapa.

# Como descobrir a versão do seu browser

  1. As instruções são parecidas para outros browsers
  2. No chrome vá nos 3 pontinhos no canto superior direito
  3. Em ajuda, clique no "Sobre o Google Chrome"
    
# Utilizando o crawler
  1. O driver utilizado é do chrome
  2. Utilizando uma IDE de sua preferência (Vscode, sublime text ou outro)
  3. Copie e cole todo o código do web_crawler.py na sua IDE
  4. Salve o arquivo como "crawler.py" sem as aspas
  5. e execute.
