# Rychlý start

## Jak to co nejrychleji spustit

### 1. Přejít do složky projektu
```powershell
cd c:\ubuntu\pythonPlay\aidevhw10\homework_agent
```

### 2. Spustit setup
```powershell
.\setup.ps1
```

### 3. Vytvořit soubor s API klíčem
```powershell
# Vytvořte soubor my_api_key.py a napište do něj:
API_KEY = "váš-openai-klíč"
```

### 4. Spustit agenta
```powershell
python main.py
```

---

## Co můžete zkoušet

### Wikipedia dotazy:
```
You: Who is Albert Einstein?
You: What is Python programming language?
```

### SQL dotazy do databáze:
```
You: Show me all employees in the Engineering department
You: What products cost less than $100?
You: Who has the highest salary?
```

## 🎯 Struktura projektu / Project Structure

```
homework_agent/
├── main.py                 # ⭐ Hlavní soubor - spustitelný agent
├── test_agent.py          # 🧪 Testy
├── README.md              # 📖 Kompletní dokumentace
---

## Struktura projektu

```
homework_agent/
├── main.py                # Hlavní program
├── demo.py                # Demo ukázka
├── test_agent.py          # Testy
├── README.md              # Základní info
├── DOCUMENTATION.md       # Technická dokumentace
├── QUICKSTART.md          # Tento soubor
├── requirements.txt       # Python balíčky
├── my_api_key.py          # API klíč (necommitovat!)
└── .gitignore             # Git ignore
```

---

## Řešení problémů

### Import errors:
```powershell
pip install -r requirements.txt
```

### OpenAI API error:
Zkontrolujte:
1. Je správně API klíč v my_api_key.py
2. Klíč začíná na "sk-"
3. Máte kredity na OpenAI účtu

### Database not found:
Databáze se vytvoří automaticky při prvním spuštění.

---

## Nahrání na GitHub

### 1. Vytvořit repository na GitHubu

### 2. Nahrát kód:
```powershell
cd homework_agent
git init
git add .
git commit -m "Langchain agent - domaci ukol"
git branch -M main
git remote add origin https://github.com/VASE_JMENO/VASE_REPO.git
git push -u origin main
```

### 3. Odevzdat odkaz v Google Classroom

---

## Tipy

1. **Testování**: Nejdřív spustit `python test_agent.py`
2. **Experimentování**: Zkusit různé dotazy
3. **Rozšíření**: Dají se přidat další tools

---

**Projekt je hotový a připravený k odevzdání!**

Co obsahuje:
- Funkční Langchain agent
- Wikipedia tool
- SQL database tool
- Dokumentace
- Testy
