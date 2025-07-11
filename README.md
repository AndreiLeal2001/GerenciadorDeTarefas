# 🧠 Gerenciador de Tarefas (Python CLI)

Este é um projeto simples e funcional de **Gerenciador de Tarefas** criado com **Python puro**, utilizando a interface de linha de comando (CLI). Ele serve como ferramenta de organização pessoal e também como exercício de prática para quem está desenvolvendo habilidades em programação backend com Python.

---

## 🎯 Objetivo

Permitir ao usuário cadastrar, listar, concluir e excluir tarefas diretamente via terminal, com uma estrutura clara e separada em módulos para promover boas práticas de desenvolvimento e reutilização de código.

---

## 🛠️ Funcionalidades

- ✅ Adicionar tarefas com descrição personalizada
- 📋 Listar tarefas com status de conclusão
- ✔️ Concluir tarefas específicas
- 🗑️ Excluir tarefas pelo índice
- 🧱 Estrutura modular com boa legibilidade
- 🧪 Preparado para testes unitários com `pytest`
- 🔍 Comentado e documentado para facilitar compreensão

---

## 📂 Estrutura do Projeto

gerenciador_de_tarefas/      ← Diretório principal do projeto
├── main.py                  ← Arquivo que inicia o programa e exibe o menu
├── tarefas.py               ← Módulo com a classe GerenciadorDeTarefas e sua lógica
├── utils.py                 ← (Opcional) Funções auxiliares como validações
├── storage.py               ← (Opcional) Funções para salvar/carregar tarefas em JSON
├── tarefas.json             ← (Opcional) Arquivo de armazenamento de tarefas
├── test_tarefas.py          ← (Opcional) Testes unitários usando pytest
└── README.md                ← Documentação do projeto (este arquivo)

📌 Aprendizados aplicados
Organização de código em módulos

Programação orientada a objetos

Manipulação de listas e dicionários

Validação de entradas do usuário

Escrever testes automatizados com pytest

Uso de docstring para documentação de funções

👨‍💻 Autor
Desenvolvido por Andrei, em processo de evolução e prática da linguagem Python e da lógica de programação.
