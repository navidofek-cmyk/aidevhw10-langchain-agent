# 🚀 QUICK START GUIDE

## ⚡ Nejrychlejší způsob spuštění / Fastest Way to Run

### 1️⃣ Přejděte do složky projektu
```powershell
cd c:\ubuntu\pythonPlay\aidevhw10\homework_agent
```

### 2️⃣ Spusťte setup script
```powershell
.\setup.ps1
```

### 3️⃣ Zkopírujte a upravte .env soubor
```powershell
Copy-Item .env.example .env
notepad .env
```
**Vložte svůj OpenAI API klíč:**
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 4️⃣ Spusťte agenta
```powershell
python main.py
```

---

## 📋 Co agent umí / What the Agent Can Do

### ✅ Wikipedia Queries
```
You: Who is Albert Einstein?
You: What is Python programming language?
You: Tell me about artificial intelligence
```

### ✅ SQL Database Queries
```
You: Show me all employees in the Engineering department
You: What products cost less than $100?
You: Who has the highest salary?
You: List all electronic products
```

---

## 🎯 Struktura projektu / Project Structure

```
homework_agent/
├── main.py                 # ⭐ Hlavní soubor - spustitelný agent
├── test_agent.py          # 🧪 Testy
├── README.md              # 📖 Kompletní dokumentace
├── DOCUMENTATION.md       # 📚 Technická dokumentace
├── QUICKSTART.md          # ⚡ Tento soubor
├── requirements.txt       # 📦 Python závislosti
├── pyproject.toml         # 🔧 Konfigurace projektu
├── setup.ps1              # 🚀 Instalační script
├── .env.example           # 🔑 Příklad konfigurace
└── .gitignore             # 🚫 Git ignore rules
```

---

## 🆘 Řešení problémů / Troubleshooting

### ❌ Problem: Import errors
```powershell
pip install -r requirements.txt
```

### ❌ Problem: OpenAI API error
Zkontrolujte:
1. Máte platný API klíč v `.env`
2. API klíč je správně naformátovaný (začína "sk-")
3. Máte dostatek kreditů na OpenAI účtu

### ❌ Problem: Database not found
Agent vytvoří databázi automaticky při prvním spuštění. Pokud chybí:
```powershell
python main.py  # Spustí se a vytvoří databázi
```

---

## 📤 Odevzdání na GitHub / GitHub Submission

### 1. Vytvořte nový repository na GitHubu

### 2. Inicializujte git a nahrajte kód:
```powershell
cd homework_agent
git init
git add .
git commit -m "Initial commit: Langchain agent with Wikipedia and SQL"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 3. Odevzdejte odkaz v Google Classroom

---

## 💡 Tipy / Tips

1. **Testování**: Nejdřív spusťte `python test_agent.py` pro ověření funkčnosti
2. **Experimentování**: Zkuste různé dotazy, agent se učí z kontextu
3. **Rozšíření**: Můžete přidat další tools (weather API, web scraping, atd.)
4. **Dokumentace**: Vše je zdokumentováno v README.md a DOCUMENTATION.md

---

## 📞 Kontakt / Support

Pokud máte otázky ke kódu:
1. Zkontrolujte README.md
2. Přečtěte si DOCUMENTATION.md
3. Spusťte test_agent.py pro diagnostiku

---

**✅ Projekt je ready to submit!**

Obsahuje:
- ✅ Funkční Langchain agent
- ✅ Wikipedia tool
- ✅ SQL database tool
- ✅ Kompletní dokumentaci
- ✅ Testy
- ✅ Setup scripty
- ✅ .gitignore a best practices
