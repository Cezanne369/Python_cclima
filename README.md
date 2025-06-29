🌤️ Projeto Previsão do Tempo com Python

Este projeto é uma aplicação simples em Python que coleta dados climáticos de uma cidade utilizando uma API externa e registra as informações em um arquivo .csv. Ele pode ser executado diariamente para manter um histórico da temperatura, sensação térmica, umidade, clima e velocidade do vento.

🌟 Objetivo

Registrar previsões meteorológicas de forma automatizada para posterior análise ou simples monitoramento pessoal.

⚙️ Tecnologias e Ferramentas Usadas

Python 3 — linguagem de programação principal.

requests — biblioteca para fazer requisições HTTP.

pandas — utilizada para manipulação e concatenação de dados em formato de tabela (DataFrame).

datetime — usada para registrar data e hora da coleta.

API externa (oculta) — chave e cidade estão definidas no arquivo api.py, que é ignorado no controle de versão por segurança.

📁 Estrutura do Projeto

sTempo/
├── Clima.py          # Script principal que coleta e salva os dados climáticos
├── api.py            # Arquivo que contém as configurações da API (não versionado)
├── weather forecast.csv  # Arquivo gerado automaticamente com os dados climáticos
└── .gitignore        # Arquivos e pastas ignorados no Git

▶️ Como usar

Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
venv\Scripts\activate  # No Windows

Instale as dependências:

pip install requests pandas

Configure sua API:
No arquivo api.py (não incluso), defina as variáveis:

URL = "https://api.openweathermap.org/data/2.5/weather?q=SUA_CIDADE&appid=SUA_CHAVE&units=metric&lang=pt_br"
CIDADE = "Nome da cidade"

Execute o script:

python Clima.py

🗃️ Saída

O script cria (ou atualiza) um arquivo chamado weather forecast.csv com os seguintes dados:

date_hours: data e hora da coleta

city: cidade consultada

temperature: temperatura atual (°C)

thermal sensation: sensação térmica (°C)

weather: descrição do clima (ex: "nublado")

humidity: umidade relativa do ar (%)

wind: velocidade do vento (km/h)

❗ Observações

Este projeto foi feito para fins educacionais e de prática pessoal.

A chave da API foi ocultada por segurança e não está incluída no repositório.

Você pode adaptar este projeto para várias cidades, automatizá-lo com agendamento, ou integrá-lo com Power BI para dashboards.

✍️ Autor

Jean Paul Cézanne Silva BorjaEstudante de Sistemas de Informação