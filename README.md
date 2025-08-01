# ENGLISH:

---

# Pao-Do-Sirio

Simple web project to help manage supermarket orders. I built it to replace the paper notebook my dad used in his business.

## Why I made this

My father used to write supermarket orders in a notebook. I created this site so he and his employees could check orders from a computer or phone—no more paper.

## How it works

The site is built using **Flask (Python)** and **HTML**. Very basic and easy to use.

## Step-by-step setup (with Render)

If you want to host the project online (not just on a local network), here’s how to do it using [Render](https://render.com):

### 1. Create a Render Account

- Go to [Render](https://render.com), create an account, and log in.

### 2. Create a PostgreSQL Database

- Go to the **Dashboard**
- Click **"New +"** > **"PostgreSQL"**
- Name your database (e.g., `pao_do_sirio_db`)
- Wait for Render to finish setting it up
- Once done, go to the **"Connection"** tab of the database
- Copy the **Internal Database URL** or **External Database URL** (depending on whether your app runs inside Render or not)

### 3. Set Up Your Web Service

- Go back to the **Dashboard**
- Click **"New +"** > **"Web Service"**
- Connect your GitHub repository (`Pao-Do-Sirio`)
- Pick a name for the service (e.g., `pao-do-sirio`)
- Set the **Build Command**:  
  pip install -r requirements.txt

pgsql
Copiar
Editar

- Set the **Start Command** (depends on your app structure):  
  gunicorn app:app

markdown
Copiar
Editar

### 4. Add Environment Variables

- Inside your web service, go to the **"Environment"** tab
- Click **"Add Environment Variable"**
- Add this:
  DATABASE_URL = your_render_database_url_here

markdown
Copiar
Editar

- Your Flask app should read this variable to connect to the database.

### 5. Deploy

- Click **"Deploy"**
- Wait for Render to build and deploy the app
- Once it’s done, Render will give you a URL like:  
  `https://pao-do-sirio.onrender.com`

## Project Link

👉 [GitHub – Mehranzin/Pao-Do-Sirio](https://github.com/Mehranzin/Pao-Do-Sirio)

---

# PORTUGUÊS:

## Pão-Do-Sírio

Projeto web simples para gerenciar pedidos de supermercados. Criei para substituir o caderno que meu pai usava na empresa.

## Por que criei isso

Meu pai anotava os pedidos dos supermercados em um caderno. Fiz esse site pra que ele e os funcionários pudessem acessar os pedidos pelo celular ou computador, sem depender de papel.

## Como funciona

O site foi feito com **Flask (Python)** e **HTML**. Interface simples, direta e sem enrolação.

## Passo a passo para colocar no ar (usando Render)

Se quiser hospedar o site online (fora da rede local), aqui está o caminho usando o [Render](https://render.com):

### 1. Crie uma conta no Render

- Acesse [Render](https://render.com) e crie sua conta.
- Faça login.

### 2. Crie um banco de dados PostgreSQL

- No **painel principal**, clique em **"New +"** > **"PostgreSQL"**
- Dê um nome pro banco (ex: `pao_do_sirio_db`)
- Aguarde a criação do banco
- Depois, vá na aba **"Connection"** do banco
- Copie a **Internal Database URL** ou **External Database URL** (dependendo se o app vai rodar dentro do Render ou não)

### 3. Configure o serviço web

- Volte pro **painel principal** do Render
- Clique em **"New +"** > **"Web Service"**
- Conecte o repositório GitHub do projeto (`Pao-Do-Sirio`)
- Dê um nome pro serviço (ex: `pao-do-sirio`)
- Configure os comandos:
- **Build Command**:
  ```
  pip install -r requirements.txt
  ```
- **Start Command** (ajuste conforme seu app Flask):
  ```
  gunicorn app:app
  ```

### 4. Adicione as variáveis de ambiente

- Vá até a aba **"Environment"** do serviço
- Clique em **"Add Environment Variable"**
- Adicione:
  DATABASE_URL = sua_url_do_banco_do_render_aqui

yaml
Copiar
Editar

- Seu código Flask deve estar configurado para ler essa variável e se conectar ao banco.

### 5. Faça o Deploy

- Clique em **"Deploy"**
- Espere o site ser criado
- O Render vai te entregar um link do tipo:  
  `https://pao-do-sirio.onrender.com`

---

Mehran Louksa Mesrob
["flow.page/mehranlouksa"](https://flow.page/mehranlouksa)
