# Dokumentace projektu / Project Documentation

## 📚 Přehled / Overview

Tento projekt implementuje inteligentního agenta pomocí frameworku **Langchain**, který kombinuje schopnosti velkého jazykového modelu (LLM) s externími nástroji pro dotazování databází a vyhledávání informací.

## 🎯 Splnění zadání / Assignment Requirements

### ✅ Framework: Langchain
- Použit framework Langchain pro vytvoření agenta
- Agent využívá `create_agent` funkci pro integraci LLM s nástroji
- Model: OpenAI GPT-4o-mini

### ✅ Nástroje / Tools:

#### 1. Wikipedia Tool
- **Typ:** Vestavěný Langchain Community tool
- **Účel:** Vyhledávání obecných znalostí a informací
- **Implementace:** `WikipediaQueryRun` s `WikipediaAPIWrapper`
- **Příklady použití:**
  - "Who is Albert Einstein?"
  - "What is Python programming language?"
  - "Tell me about Prague"

#### 2. SQL Database Tool
- **Typ:** Vlastní custom tool
- **Účel:** Dotazování relační databáze SQLite
- **Implementace:** Dekorátor `@tool` s funkcí `query_sql_database`
- **Bezpečnost:** Povoleny pouze SELECT dotazy (read-only)
- **Databázové schéma:**
  ```sql
  TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL,
    hire_date TEXT
  )
  
  TABLE products (
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL,
    stock_quantity INTEGER
  )
  ```
- **Příklady použití:**
  - "Show me all employees in Engineering"
  - "What products cost less than $100?"
  - "Who has the highest salary?"

## 🏗️ Architektura / Architecture

```
┌─────────────┐
│    User     │
└──────┬──────┘
       │ Query
       ▼
┌─────────────────────────────┐
│   Langchain Agent           │
│   (GPT-4o-mini)            │
└──────┬──────────────┬───────┘
       │              │
       ▼              ▼
┌──────────────┐  ┌──────────────┐
│ Wikipedia    │  │ SQL Database │
│ Tool         │  │ Tool         │
└──────────────┘  └──────────────┘
       │              │
       ▼              ▼
┌──────────────┐  ┌──────────────┐
│ Wikipedia    │  │ SQLite       │
│ API          │  │ Database     │
└──────────────┘  └──────────────┘
```

## 💻 Technické řešení / Technical Implementation

### 1. Agent Initialization
```python
agent = create_agent(
    llm=ChatOpenAI(model="gpt-4o-mini"),
    tools=[wikipedia_tool, query_sql_database],
    system_prompt="..."
)
```

### 2. Tool Selection
Agent automaticky vybírá správný nástroj na základě:
- Analýzy dotazu uživatele
- Popisů nástrojů (descriptions)
- Kontextu konverzace

### 3. Execution Flow
1. Uživatel zadá dotaz
2. Agent analyzuje dotaz pomocí LLM
3. Agent rozhodne, který nástroj použít
4. Nástroj provede akci (Wikipedia API nebo SQL query)
5. Agent zpracuje výsledek a odpoví uživateli

## 🔧 Instalace a spuštění / Installation & Running

### Rychlá instalace:
```powershell
cd homework_agent
.\setup.ps1
```

### Manuální instalace:
```powershell
# 1. Vytvoření virtual environment
python -m venv venv

# 2. Aktivace
.\venv\Scripts\Activate.ps1

# 3. Instalace závislostí
pip install -r requirements.txt

# 4. Konfigurace
Copy-Item .env.example .env
# Editovat .env a doplnit OPENAI_API_KEY

# 5. Spuštění
python main.py
```

## 📊 Příklady interakcí / Interaction Examples

### Příklad 1: Wikipedia dotaz
```
You: Who is Albert Einstein?
Agent: Albert Einstein was a German-born theoretical physicist 
       who developed the theory of relativity...
```

### Příklad 2: SQL dotaz
```
You: Show me all employees in the Engineering department
Agent: Here are the employees in Engineering:
       - John Smith (Salary: $85,000)
       - Bob Johnson (Salary: $95,000)
```

### Příklad 3: Kombinovaný dotaz
```
You: Tell me about databases and show me our products
Agent: [Použije Wikipedia pro info o databázích]
       [Použije SQL pro seznam produktů]
```

## 🛡️ Bezpečnostní opatření / Security Measures

1. **SQL Injection Protection**
   - Povoleny pouze SELECT dotazy
   - Validace SQL příkazů před spuštěním

2. **API Keys**
   - Ukládány v .env souboru (gitignored)
   - Nikdy necommitovány do repozitáře

3. **Database Access**
   - Read-only přístup přes SQL tool
   - Lokální SQLite databáze bez externího přístupu

## 📈 Možná rozšíření / Possible Extensions

1. **Více nástrojů:**
   - Web scraping (Beautiful Soup)
   - API integrace (weather, stocks, news)
   - File operations
   - Email sending

2. **Pokročilé SQL funkce:**
   - Agregační dotazy
   - JOIN operace
   - Vizualizace dat

3. **Konverzační paměť:**
   - Chat history
   - Context awareness
   - Multi-turn conversations

4. **MCP integrace:**
   - Model Context Protocol
   - Standardizované tool rozhraní

## 🧪 Testování / Testing

Spuštění testů:
```powershell
python test_agent.py
```

Testy ověřují:
- ✅ Inicializaci databáze
- ✅ Funkčnost Wikipedia tool
- ✅ Funkčnost SQL tool
- ✅ Odpovědi agenta

## 📝 Závěr / Conclusion

Projekt úspěšně demonstruje:
- ✅ Použití Langchain frameworku
- ✅ Integraci LLM s externími nástroji
- ✅ Kombinaci vestavěných a custom nástrojů
- ✅ Praktickou aplikaci AI agentů
- ✅ Bezpečné dotazování databází
- ✅ Modulární a rozšiřitelnou architekturu

Agent je plně funkční, testovaný a připravený k použití nebo dalšímu rozšíření.

---

**Autor:** AI Developer Student  
**Framework:** Langchain  
**LLM:** OpenAI GPT-4o-mini  
**Datum:** Listopad 2025
