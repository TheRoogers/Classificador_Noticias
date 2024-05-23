# Projeto de Classificação de Notícias - Teste técnico - Cientista de Dados Jr. - AeC

Este projeto visa criar um classificador de notícias baseado em categorias usando técnicas de aprendizado de máquina.

## Análise de Dados Exploratória (EDA)

A Análise de Dados Exploratória (EDA) é uma etapa crucial no processo de entendimento dos dados, que visa resumir suas principais características frequentemente utilizando métodos visuais. Nesta seção, descrevemos as etapas de EDA realizadas no nosso conjunto de dados.

### 1. Carregamento dos Dados

Os dados foram carregados utilizando a biblioteca Pandas. As colunas do conjunto de dados são:

- `title`: Título da notícia.
- `text`: Texto da notícia.
- `date`: Data da publicação.
- `category`: Categoria principal da notícia.
- `subcategory`: Subcategoria da notícia.

### 2. Verificação de Linhas Duplicadas

Checamos a existência de linhas duplicadas no conjunto de dados e removemos as duplicatas encontradas.

### 3. Verificação de Formato e Colunas

Verificamos a estrutura do DataFrame, incluindo os tipos de dados de cada coluna para garantir que estão no formato adequado.

### 4. Descrição Estatística

Realizamos uma descrição estatística dos dados para entender as características gerais do conjunto de dados, como contagem, média, desvio padrão, valores mínimos e máximos das colunas numéricas.

### 5. Verificação de Valores Nulos

Checamos a presença de valores nulos nas colunas do conjunto de dados.

### 6. Distribuição das Categorias

Analisamos a distribuição das categorias e subcategorias para entender a proporção de cada uma no conjunto de dados.

### 7. Análise de Dados Temporais

#### 7.1 Contagem de Publicações por Ano

Realizamos uma análise temporal para entender a distribuição das notícias ao longo dos anos.

#### 7.2 Contagem de Publicações por Mês e Ano

Analisamos a contagem de publicações por mês e ano para identificar padrões sazonais.

### 8. Distribuição do Comprimento dos Títulos por Palavras

Analisamos a distribuição do comprimento dos títulos em termos de contagem de palavras.

### 9. Distribuição do Comprimento dos Textos por Palavras

Analisamos a distribuição do comprimento dos textos em termos de contagem de palavras.

### 10. Nuvem de Palavras

#### 10.1 Nuvem de Palavras para os Títulos

Geramos uma nuvem de palavras para os títulos das notícias para visualizar as palavras mais frequentes.

#### 10.2 Nuvem de Palavras para o Texto

Geramos uma nuvem de palavras para os textos das notícias para visualizar as palavras mais frequentes.

### 11. Exportação dos Dados Tratados

Exportamos o DataFrame tratado para um arquivo CSV chamado `result.csv`.

### Conclusões da EDA

Após a realização da EDA, obtivemos uma compreensão clara sobre a estrutura e características do conjunto de dados. Esta análise nos forneceu insights valiosos que guiaram as etapas subsequentes de pré-processamento e modelagem dos dados.

## Algoritmo de Classificação de Notícias

Nesta seção, descrevemos o processo de criação e avaliação do algoritmo de classificação de notícias.

### 1. Pré-processamento de Texto

Antes de treinar o modelo de machine learning, realizamos o pré-processamento dos textos das notícias. As etapas de pré-processamento incluíram:

- Remoção de stopwords
- Tokenização
- Lemmatização

### 2. Vetorização de Texto

Utilizamos a técnica de TF-IDF (Term Frequency-Inverse Document Frequency) para transformar os textos das notícias em vetores numéricos. Limitamos o número de características a 3000 para reduzir a dimensionalidade.

### 3. Treinamento do Modelo

Treinamos um modelo de classificação Naive Bayes utilizando os vetores TF-IDF. Dividimos os dados em conjuntos de treinamento(80%) e teste(20%) para avaliar o desempenho do modelo.

### 4. Avaliação do Modelo

Avaliação do modelo foi realizada utilizando as métricas de precisão, recall e f1-score. A tabela abaixo resume os resultados:

| Métrica     | cotidiano | educacao | ... | Média   |
|-------------|-----------|----------|-----|---------|
| Precisão    | 0.79      | 0.81     | ... | 0.85    |
| Recall      | 0.87      | 0.86     | ... | 0.78    |
| F1-Score    | 0.83      | 0.83     | ... | 0.80    |

### 5. Salvamento dos Modelos

Os modelos treinados e o vetor TF-IDF foram salvos em arquivos pickle na pasta data para serem utilizados na API.

### Conclusões do Algoritmo de Classificação

O modelo Naive Bayes, treinado com vetores TF-IDF, apresentou um bom desempenho na classificação das notícias, com uma média de F1-Score de 0.80.


## API de Classificação de Notícias

A API foi construída utilizando o framework Flask, que é uma estrutura leve e flexível para construção de aplicações web em Python. O código principal está no arquivo app.py, onde definimos os endpoints da API e suas funcionalidades. O endpoint /classify recebe uma requisição POST com o título e o texto da notícia, utiliza um modelo de classificação previamente treinado para prever a categoria da notícia e retorna essa categoria. Já o endpoint / serve o arquivo index.html, que contém um formulário para inserção do título e texto da notícia, permitindo a classificação através de uma interface web.

### Endpoints da API

#### 1. `POST /classify`

Este endpoint classifica o texto da notícia enviado no corpo da solicitação.

- **URL**: `/classify`
- **Método HTTP**: `POST`
- **Corpo da Solicitação**:
  - `text`: O texto da notícia.
- **Resposta**:
  - `category`: A categoria prevista para a notícia.

#### Exemplo de Requisição usando o Postman

1. Abra o Postman.
2. Selecione o método `POST`.
3. Insira a URL `http://127.0.0.1:5000/classify`.
4. Vá para a aba "Body" e selecione "raw" e "JSON".
5. Insira o JSON no corpo da requisição, por exemplo:

```json
{
    "text": "Os mercados internacionais estão observando um crescimento contínuo devido a..."
}
```
#### 2. `/`

Este endpoint é para o teste da API no Navegador

Para testar a API no navegador, abra o navegador e acesse http://127.0.0.1:5000. Onde será carregado a página index.html, onde você pode inserir o texto da notícia e obter a classificação.

### Executando a API no Docker

O Dockerfile é um arquivo de configuração utilizado para construir a imagem Docker da aplicação. Ele define as instruções para montar o ambiente de execução da aplicação dentro de um contêiner Docker. No Dockerfile, especificamos a imagem base a ser utilizada, as dependências necessárias para a aplicação (definidas no arquivo requirements.txt), o diretório de trabalho, o comando para instalar as dependências, a exposição da porta onde a aplicação estará executando e o comando para iniciar a aplicação Flask.

#### Passos para Construir e Executar o Contêiner Docker

Construir a imagem Docker:
1. No terminal, navegue até o diretório onde o Dockerfile está localizado e execute:

    ```sudo docker build -t api_classificador . ```

2. Após construir a imagem, execute o contêiner com o seguinte comando:

    ```sudo docker run -p 5000:5000 api_classificador ```

## Conclusão
A API está configurada para classificar notícias. Pode ser facilmente testada e integrada com outras aplicações, utilizando ferramentas como Postman para enviar requisições e Docker para garantir um ambiente consistente e reproduzível.