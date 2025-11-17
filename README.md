# Langchain Agent - Domácí úkol

## Zadání

Cílem bylo vytvořit agenta pomocí frameworku Langchain, který umí pracovat s různými nástroji a odpovídat na dotazy.

**Použitý framework:** Langchain  
**Nástroje:** Wikipedia a SQL databáze

## Co agent umí

Agent má dva hlavní nástroje:

1. **Wikipedia** - může hledat informace na Wikipedii
2. **SQL databáze** - umí se dotazovat do SQLite databáze

### Databáze:
- **Tabulka `employees`**: zaměstnanci (jméno, oddělení, plat, datum nástupu)
- **Tabulka `products`**: produkty (název, kategorie, cena, počet kusů)

## Instalace

### Co je potřeba
- Python 3.10 nebo novější
- OpenAI API klíč

### Jak to nainstalovat:

1. **Vytvoření virtuálního prostředí:**
```powershell
python -m venv venv
```

2. **Aktivace virtuálního prostředí:**
```powershell
.\venv\Scripts\Activate.ps1
```

3. **Instalace balíčků:**
```powershell
pip install langchain langchain-openai langchain-community python-dotenv wikipedia
```

Nebo:
```powershell
uv pip install -e .
```

4. **Nastavení API klíče:**
   - Vytvořte soubor `my_api_key.py`
   - Napište do něj: `API_KEY = "váš-api-klíč-zde"`

## Spuštění

```powershell
python main.py
```

## Příklady použití

### Dotazy na Wikipedia:
```
You: Who is Albert Einstein?
You: What is Python programming language?
```

### SQL dotazy:
```
You: Show me all employees in the Engineering department
You: What products cost less than $100?
```

## Struktura projektu

```
homework_agent/
│
├── main.py              # Hlavní program s agentem
├── demo.py              # Demo ukázka
├── test_agent.py        # Testy
├── my_api_key.py        # API klíč (necommitovat!)
├── pyproject.toml       # Závislosti
└── README.md            # Tento soubor
```

## Technické detaily

### Použité technologie:
- **LangChain** - framework pro AI agenty
- **OpenAI GPT-4o-mini** - jazykový model
- **Wikipedia API** - přístup k Wikipedii
- **SQLite** - databáze

### Jak to funguje:
1. `WikipediaQueryRun` - vestavěný tool z Langchainu pro Wikipedia
2. `query_sql_database` - vlastní tool pro SQL dotazy (jenom SELECT)

## Poznámky

- Agent sám vybere správný nástroj podle toho, na co se ptáte
- SQL tool má jenom read-only přístup (bezpečnost)
- Databáze se vytvoří automaticky při prvním spuštění

## Autor

Domácí úkol pro předmět AI Developer
