# 🧠 Gerenciador de Tarefas (Python CLI)

Este projeto é um **Gerenciador de Tarefas em Python puro**, com interface de linha de comando (CLI). Ele foi desenvolvido com foco em boas práticas de programação backend: modularização, persistência de dados, testes automatizados e organização profissional. Ideal para incluir em portfólios ou como ponto de partida para projetos mais avançados.

---

## 🎯 Objetivo

Permitir ao usuário adicionar, listar, concluir e excluir tarefas diretamente via terminal, com salvamento automático em arquivo `.json`.

---

## 🛠️ Funcionalidades

- ✅ Adicionar tarefas com descrição personalizada
- 📋 Listar tarefas com status de conclusão
- ✔️ Concluir tarefas específicas
- 🗑️ Excluir tarefas pelo índice
- 💾 Salvamento automático das tarefas
- ⬆️ Carregamento imediato de tarefas salvas ao iniciar o programa
- 🧱 Código modular e comentado
- 🧪 Suporte a testes unitários com `pytest`

---

## 📦 Estrutura do Projeto

```plaintext
gerenciador_de_tarefas/
├── main.py               ← Executa o programa e mostra o menu
├── tarefas.py            ← Classe principal com a lógica do gerenciador
├── storage.py            ← Módulo para salvar/carregar tarefas com JSON
├── test_tarefas.py       ← Arquivo de testes usando pytest
├── tarefas.json          ← Arquivo local de tarefas salvas (ignorado no GitHub)
├── README.md             ← Este arquivo de documentação
├── .gitignore            ← Arquivos que não devem ser versionados
└── .gitattributes        ← Controle de formatação e linguagem no Git

💾 Persistência de Dados
O sistema salva automaticamente todas as tarefas em tarefas.json sempre que são adicionadas, concluídas ou excluídas.

As tarefas são carregadas automaticamente ao iniciar o software.

O sistema ignora o arquivo no repositório (está no .gitignore) para manter privacidade.

Funções como salvar_tarefas() e carregar_tarefas() estão no módulo storage.py.

🧪 Testes automatizados
Com pytest, você pode verificar se os métodos principais estão funcionando corretamente:
pip install pytest
pytest test_tarefas.py

🧱 Ambiente virtual (venv)
Você pode criar um ambiente isolado para instalar dependências:
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows

Instale os pacotes: pip install pytest
E registre as dependências: pip freeze > requirements.txt

🚀 Como executar
Clone o repositório:
git clone https://github.com/seu-usuario/gerenciador-de-tarefas.git
cd gerenciador-de-tarefas

Ative o ambiente virtual (veja instruções acima)
python main.py

📌 Aprendizados aplicados
Programação orientada a objetos com Python

Separação de código em módulos

Persistência com JSON

Validação de entrada e tratamento de exceções

Documentação com docstrings

Testes automatizados com pytest

Organização de projeto estilo backend profissional

🧭 Próximos passos (roadmap)
Exportar tarefas para .txt ou .csv

Interface gráfica com Tkinter

API REST com Flask ou FastAPI

Autenticação de usuários

Integração com banco de dados (sqlite, PostgreSQL)

👨‍💻 Autor
Desenvolvido por Andrei, como projeto pessoal e estudo de backend com Python.
