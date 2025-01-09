<div align="center">
   <h1><b>Diário Online</b></h1><br><br>

   <a href="" target="_blank">![License](https://img.shields.io/badge/license-MIT-blue.svg)</a>
   ![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
   ![Django](https://img.shields.io/badge/Django-darkgreen)
   ![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-orange)
   ![Chart.js](https://img.shields.io/badge/Chart-Js-gold)
   ![Pillow](https://img.shields.io/badge/Pillow-white)
   ![SQLite](https://img.shields.io/badge/SQLite-magenta.svg)

</div>

<div>
<h2>📖 Descrição</h2>

<a>Este projeto foi desenvolvido como parte da Pystack Week Returnal e contém o código-fonte de um sistema web criado com o framework Django, que permite aos usuários criarem, visualizarem e gerenciarem diários pessoais online. O projeto apresenta funcionalidades como o registro de anotações diárias, associação de tags, seleção de pessoas envolvidas e a exibição de estatísticas em gráficos interativos.</a>
  
</div>

<h2>🎯 Funcionalidades</h2>

- **Cadastro de anotações:** Os usuários podem criar anotações diárias com título, texto e tags.

- **Associação de pessoas:** Permite associar pessoas cadastradas às anotações.

- **Visualização de diários por data:** Os usuários podem visualizar todas as anotações realizadas em uma data específica.

- **Exclusão de diários:** É possível excluir todas as anotações de um dia específico.

- **Gráficos interativos:** Apresenta estatísticas sobre as anotações, como o número de diários por pessoa e a frequência de uso de tags.

</div>

<div>

<h2>👨🏻‍💻 Tecnologias Utilizadas</h2>

- **Python 3.8**

- **Django:** Framework web utilizado para o desenvolvimento do backend.

- **SQLite:** Banco de dados utilizado para armazenar as informações.

- **Tailwind CSS:** Framework CSS utilitário para estilização da interface.

- **Chart.js:** Biblioteca JavaScript para exibição de gráficos interativos.
  
</div>

<div>
<h2>💾 Instalação e Configuração</h2>

1. **Clonar o repositório**
```bash
git clone https://github.com/LuccaGiovane/PSW-DiarioOnline.git
cd PSW-DiarioOnline
```

2. **Criar o ambiente virtual**
   
     2.1 Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
     2.2 Windows:
     ```bash
     python -m venv venv
     venv\Scripts\Activate
     ```

3. **Configurar arquivos estáticos e de mídia no `settings.py`** <br>
Adicione as seguintes linhas ao arquivo `settings.py` para configurar os diretórios de arquivos estáticos e de mídia:
```bash
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'templates/static']
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

4. **Executar migrações**
```bash
python manage.py migrate
```

5. **Iniciar o servidor**
```bash
python manage.py runserver
```
Acesse a aplicação no navegador através do endereço:
```bash
http://127.0.0.1:8000/diario/
```

</div>

<div>
  <h2>📁 Estrutura do Projeto</h2>

  ```bash
  .
  ├── core
  │   ├── __init__.py
  │   ├── asgi.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  ├── diario
  │   ├── migrations
  │   ├── templates
  │   │   ├── base.html
  │   │   ├── home.html
  │   │   ├── escrever.html
  │   │   └── pessoa.html
  │   ├── static
  │   │   └── waves.png
  │   ├── admin.py
  │   ├── apps.py
  │   ├── models.py
  │   ├── tests.py
  │   ├── urls.py
  │   └── views.py
  ├──  manage.py
  └──  LICENSE

  ```
</div>

<div>
  <h2>🔎 Funcionalidades Detalhadas</h2>

<h3>1. Cadastro de Anotações</h3>
  
  <p>Os usuários podem realizar anotações diárias através da página Escrever. Cada anotação pode conter:</p>
 
  - **`Título`** 
  - **`Texto`**
  - **`Tags`**: Seleção de tags predefinidas (Viagem, Trabalho). 
  - **`Pessoas`**: Seleção de pessoas cadastradas previamente.
  <br>
  
<h3>2. Listagem e Visualização de Diários</h3>
  
  <p>A página principal exibe as três últimas anotações realizadas. Além disso, os usuários podem visualizar todas as anotações de uma data específica utilizando um seletor de data.</p>
  <br>
  
<h3>3. Cadastro de Pessoas</h3>
  
  <p>Na página Pessoa, é possível cadastrar novas pessoas que podem ser associadas às anotações. Cada pessoa possui:</p>
  
  **`Nome`** <br>
  **`Foto`**
  <br><br>
  
<h3>4. Gráficos Interativos</h3>
  
  <p>A página principal também apresenta gráficos interativos, que exibem:</p>
  <p>Número de anotações por pessoa (gráfico de barras)</p>
  <p>Tags mais usadas (gráfico de pizza)</p>
  <br>
  
<h3>5. Exclusão de Diários</h3>
  <p>Os usuários podem excluir todas as anotações de uma data específica utilizando a opção Excluir todas as anotações.</p>
</div>

<br>

<div>
  <h2>📑 Licença</h2>

  <p>Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.</p>
</div>

<div>
  <h2>🤝🏻 Contribuições</h2>

  <p>Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.</p>
</div>
