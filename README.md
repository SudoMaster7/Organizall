# **📌 Organizall**  

**Sistema de Gestão de Tarefas e Projetos Pessoais**  

Um organizador pessoal desenvolvido em **Django** e **Bootstrap** para gerenciar tarefas, projetos e metas com eficiência, seguindo metodologias como **GTD (Getting Things Done)** e **Matriz de Eisenhower**.  

---

## **🚀 Funcionalidades**  
✔️ **Gestão de Tarefas** (criação, edição, exclusão e marcação de status)  
✔️ **Organização por Projetos** (com barra de progresso e prazos)  
✔️ **Dashboard Integrado** (visão geral de tarefas e projetos)  
✔️ **Autenticação de Usuários** (registro e login seguro)  
✔️ **Design Responsivo** (funciona em desktop e mobile)  
✔️ **Filtros e Busca** (próximas atualizações)  

---

## **🛠️ Tecnologias Utilizadas**  
- **Backend:** Python + Django  
- **Frontend:** Bootstrap 5 + CSS  
- **Banco de Dados:** SQLite (dev) / PostgreSQL (prod)  
- **Versionamento:** Git + GitHub  

---

## **📦 Como Rodar o Projeto Localmente?**  

### **Pré-requisitos**  
- Python 3.10+  
- Git  

### **Passo a Passo**  
1. **Clone o repositório**  
   ```bash
   git clone https://github.com/SudoMaster7/Organizall.git
   cd Organizall
   ```

2. **Crie e ative um ambiente virtual**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```

3. **Instale as dependências**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**  
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional)**  
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor**  
   ```bash
   python manage.py runserver
   ```
   Acesse: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**  

---

## **📌 Próximas Atualizações**  
🔹 **Módulo Financeiro** (controle de gastos e orçamentos)  
🔹 **Relatórios em PDF/Excel** (exportação de dados)  
🔹 **Sistema de Notificações** (lembretes por e-mail)  
🔹 **API REST** (para integração com apps mobile)  

---

## **📄 Licença**  
Este projeto está sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.  

---

## **📬 Contato**  
💡 **Quer contribuir ou reportar um bug?**  
👉 Abra uma **[Issue](https://github.com/SudoMaster7/Organizall/issues)** ou envie um **Pull Request**!  

✉️ **Email:** [moraesleonardobrito@gmail.com](mailto:moraesleonardobrito@gmail.com)  

---

<div align="center">
  <sub>Desenvolvido com ❤️ por <a href="https://github.com/SudoMaster7">SudoMaster7</a></sub>
</div>

