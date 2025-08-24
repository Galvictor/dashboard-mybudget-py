# 📊 Dashboard MyBudget

Um dashboard interativo para controle de orçamento pessoal desenvolvido com Python, Dash e Bootstrap.

## 🚀 Funcionalidades

-   **Dashboard Responsivo**: Interface moderna e responsiva usando Dash Bootstrap Components
-   **Gráficos Interativos**: Visualizações de dados com Plotly Express
-   **Tema Personalizado**: Estilo visual customizado com SCSS
-   **Tabelas Dinâmicas**: Exibição de dados em formato tabular
-   **Design Responsivo**: Funciona perfeitamente em dispositivos móveis e desktop

## 🛠️ Tecnologias Utilizadas

-   **Python 3.x**
-   **Dash**: Framework web para aplicações analíticas
-   **Dash Bootstrap Components**: Componentes Bootstrap para Dash
-   **Plotly Express**: Biblioteca para criação de gráficos interativos
-   **Pandas**: Manipulação e análise de dados
-   **SCSS**: Pré-processador CSS para estilos customizados

## 📋 Pré-requisitos

-   Python 3.7 ou superior
-   pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. **Clone o repositório:**

    ```bash
    git clone <url-do-repositorio>
    cd dash-mybudget-py
    ```

2. **Crie um ambiente virtual:**

    ```bash
    python -m venv .venv
    ```

3. **Ative o ambiente virtual:**

    - **Windows (PowerShell):**
        ```powershell
        .venv\Scripts\Activate.ps1
        ```
    - **Windows (CMD):**
        ```cmd
        .venv\Scripts\activate.bat
        ```

4. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Como Executar

1. **Ative o ambiente virtual** (se ainda não estiver ativo)
2. **Execute o aplicativo:**
    ```bash
    python index.py
    ```
3. **Acesse no navegador:**
    ```
    http://localhost:8050
    ```

## 🏗️ Arquitetura do Projeto

O projeto foi estruturado seguindo boas práticas de separação de responsabilidades:

### **`app.py`** - Configuração do Servidor

-   Configuração da aplicação Dash
-   Compilação de SCSS
-   Carregamento de temas
-   Configuração de estilos externos
-   Inicialização do servidor

### **`index.py`** - Layout Principal + Roteamento

-   Layout principal com sidebar + conteúdo
-   Sistema de roteamento com `dcc.Location`
-   Callbacks para mudança de páginas
-   **Arquivo principal de execução** (`python index.py`)

### **`components/`** - Componentes Modulares

-   **`sidebar.py`**: Barra lateral de navegação
-   **`dashboard.py`**: Conteúdo principal do dashboard
-   Componentes independentes com atributo `.layout`
-   Estrutura preparada para futuras páginas

## 📁 Estrutura do Projeto

```
dash-mybudget-py/
├── app.py              # Configuração do servidor Dash
├── index.py            # Layout principal da aplicação
├── components/         # Componentes modulares
│   ├── sidebar.py      # Barra lateral de navegação
│   └── dashboard.py    # Conteúdo principal
├── assets/
│   ├── custom.scss     # Estilos SCSS customizados
│   └── custom.css      # CSS compilado (gerado automaticamente)
├── data.csv            # Dados de exemplo
├── requirements.txt    # Dependências do projeto
└── README.md          # Este arquivo
```

## 🎨 Personalização

### Modificando Estilos

-   Edite o arquivo `assets/custom.scss` para personalizar o visual
-   O CSS é compilado automaticamente quando o aplicativo é executado

### Alterando Dados

-   Modifique o DataFrame no arquivo `components/dashboard.py`
-   Conecte a uma fonte de dados externa (banco de dados, API, etc.)

### Mudando o Tema

-   Altere o tema Bootstrap modificando a linha:
    ```python
    load_figure_template("minty")  # Troque "minty" por outro tema
    ```

## 📊 Dados de Exemplo

O dashboard atual inclui dados de exemplo com:

-   Categorias de gastos (Alimentação, Transporte, Lazer)
-   Valores correspondentes
-   Gráfico de barras interativo
-   Tabela responsiva

## 🔧 Desenvolvimento

### Modo Debug

O aplicativo roda em modo debug por padrão, permitindo:

-   Recarregamento automático ao alterar código
-   Mensagens de erro detalhadas
-   Ferramentas de desenvolvimento

### Adicionando Novos Componentes

1. **Para componentes simples**: Adicione-os ao layout em `index.py`
2. **Para componentes reutilizáveis**: Crie na pasta `components/`
3. **Para interatividade**: Implemente callbacks no `index.py`

### Estrutura de Arquivos

-   **`app.py`**: Mantenha apenas configurações do servidor
-   **`index.py`**: Layout principal + roteamento + callbacks
-   **`components/`**: Crie componentes modulares com atributo `.layout`

## 🐛 Solução de Problemas

### Erro: "app.run_server has been replaced by app.run"

-   **Solução**: Use `app.run()` em vez de `app.run_server()`
-   **Causa**: Mudança na API do Dash em versões mais recentes

### Dependências não encontradas

-   **Solução**: Verifique se o ambiente virtual está ativo
-   **Comando**: `pip install -r requirements.txt`

### Problemas de estilo

-   **Solução**: Verifique se o arquivo `custom.css` foi gerado
-   **Causa**: Problemas na compilação do SCSS

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas, abra uma issue no repositório.

---

**Desenvolvido com ❤️ usando Python e Dash**
