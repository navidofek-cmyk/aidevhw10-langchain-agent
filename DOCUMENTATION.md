# Dokumentace projektu

## Přehled

V tomhle projektu jsem vytvořil AI agenta pomocí Langchainu. Agent umí používat různé nástroje - může hledat informace na Wikipedii a dotazovat se do SQL databáze.

## Splnění zadání

### Framework: Langchain
- Použil jsem Langchain framework
- Agent je vytvořený pomocí funkce `create_agent`
- Jako LLM model používám OpenAI GPT-4o-mini

### Nástroje:

#### 1. Wikipedia Tool
- **Typ:** Vestavěný tool z Langchain Community
- **K čemu slouží:** Vyhledávání obecných informací
- **Jak je to implementované:** `WikipediaQueryRun` s `WikipediaAPIWrapper`
- **Příklady:**
  - "Who is Albert Einstein?"
  - "What is Python programming language?"

#### 2. SQL Database Tool
- **Typ:** Vlastní custom tool
- **K čemu slouží:** Dotazování SQLite databáze
- **Jak je to implementované:** Použil jsem dekorátor `@tool` s funkcí `query_sql_database`
- **Bezpečnost:** Povolil jsem jenom SELECT dotazy (read-only)
- **Struktura databáze:**
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

## Jak to funguje (architektura)

```
Uživatel
   ↓
Langchain Agent (GPT-4o-mini)
   ↓          ↓
Wikipedia   SQL Database
   ↓          ↓
Wiki API   SQLite DB
```

## Technické řešení

### Vytvoření agenta:
```python
agent = create_agent(
    llm=ChatOpenAI(model="gpt-4o-mini"),
    tools=[wikipedia_tool, query_sql_database],
    system_prompt="..."
)
```

### Jak agent vybírá nástroj:
Agent se rozhoduje podle:
- Co se uživatel ptá
- Popisů nástrojů
- Kontextu konverzace

### Jak to běží:
1. Uživatel se zeptá
2. Agent pomocí LLM analyzuje otázku
3. Agent vybere správný nástroj
4. Nástroj udělá co má (Wikipedia nebo SQL)
5. Agent odpověď naformátuje a pošle uživateli

## Instalace

### Rychlá instalace:
```powershell
cd homework_agent
.\setup.ps1
```

### Nebo manuálně:
```powershell
# 1. Virtual environment
python -m venv venv

# 2. Aktivace
.\venv\Scripts\Activate.ps1

# 3. Balíčky
pip install -r requirements.txt

# 4. API klíč
# Vytvořit my_api_key.py s API_KEY = "..."

# 5. Spustit
python main.py
```

## Příklady

### Wikipedia dotaz:
```
You: Who is Albert Einstein?
Agent: Albert Einstein was a German-born theoretical physicist...
```

### SQL dotaz:
```
You: Show me all employees in the Engineering department
Agent: Here are the employees in Engineering:
       - John Smith (Salary: $85,000)
       - Bob Johnson (Salary: $95,000)
```

## Bezpečnost

1. **SQL Injection ochrana**
   - Povoleny jenom SELECT dotazy
   - Validace SQL před spuštěním

2. **API klíče**
   - Uloženy v my_api_key.py (gitignored)
   - Nikdy nenahráno na git

3. **Databáze**
   - Read-only přístup
   - Lokální SQLite, bez externího přístupu

## Co by se dalo ještě přidat

1. **Víc nástrojů:**
   - Web scraping
   - API na počasí, akcie atd.
   - Práce se soubory

2. **Lepší SQL:**
   - Agregační dotazy
   - JOINy
   - Grafy z dat

3. **Paměť konverzace:**
   - Chat history
   - Vícestupňové dotazy

## Testování

```powershell
python test_agent.py
```

Testy kontrolují:
- Inicializaci databáze
- Jestli funguje Wikipedia tool
- Jestli funguje SQL tool
- Odpovědi agenta

## Závěr

Projekt splňuje zadání:
- Langchain framework
- LLM s externími nástroji
- Vestavěné i custom nástroje
- Bezpečné dotazování databází

Agent funguje, je otestovaný a připravený k použití.
