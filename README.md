# Langchain Agent with Wikipedia & SQL Database

## 📋 Zadání / Assignment

Navrhněte a vytvořte agenta pomocí frameworku Langchain, který pracuje s nástroji (Tools) a odpovídá na dotazy přes LLM.

**Framework:** Langchain  
**Nástroje:** Wikipedia, SQL Database

## 🎯 Funkcionalita / Features

Agent disponuje následujícími schopnostmi:

1. **Wikipedia Tool** - Vyhledávání informací na Wikipedii
2. **SQL Database Tool** - Dotazování SQLite databáze

### Databáze obsahuje:
- **Tabulka `employees`**: informace o zaměstnancích (jméno, oddělení, plat, datum nástupu)
- **Tabulka `products`**: informace o produktech (název, kategorie, cena, skladem)

## 🛠️ Instalace / Installation

### Požadavky / Requirements
- Python 3.10 nebo vyšší
- OpenAI API klíč

### Postup instalace:

1. **Vytvořte virtuální prostředí:**
```powershell
python -m venv venv
```

2. **Aktivujte virtuální prostředí:**
```powershell
.\venv\Scripts\Activate.ps1
```

3. **Nainstalujte závislosti:**
```powershell
pip install langchain langchain-openai langchain-community python-dotenv wikipedia
```

Nebo pomocí uv:
```powershell
uv pip install -e .
```

4. **Nastavte API klíč:**
   - Zkopírujte `.env.example` jako `.env`
   - Vyplňte svůj OpenAI API klíč

```powershell
Copy-Item .env.example .env
# Poté editujte .env soubor a doplňte API klíč
```

## 🚀 Spuštění / Running

```powershell
python main.py
```

## 💡 Příklady použití / Usage Examples

### Dotazy na Wikipedia:
```
You: Who is Albert Einstein?
You: What is Python programming language?
You: Tell me about Prague
```

### SQL dotazy:
```
You: Show me all employees in the Engineering department
You: What products cost less than $100?
You: Who has the highest salary?
You: List all electronic products
```

### Kombinované dotazy:
```
You: Find information about databases on Wikipedia
You: Show me employees in sales and tell me about sales techniques
```

## 📊 Struktura projektu / Project Structure

```
homework_agent/
│
├── main.py              # Hlavní soubor s agentem
├── pyproject.toml       # Definice závislostí
├── .env                 # API klíče (necommitovat!)
├── .env.example         # Příklad konfigurace
├── README.md            # Tento soubor
└── sample_database.db   # SQLite databáze (vytvoří se automaticky)
```

## 🔧 Technické detaily / Technical Details

### Použité nástroje:
- **LangChain**: Framework pro tvorbu AI agentů
- **OpenAI GPT-4**: Jazykový model
- **Wikipedia API**: Přístup k Wikipedii
- **SQLite**: Relační databáze

### Implementované tools:
1. `WikipediaQueryRun` - vestavěný Langchain tool pro Wikipedia
2. `query_sql_database` - vlastní tool pro SQL dotazy

## 🔒 Bezpečnost / Security

- SQL tool povoluje pouze SELECT dotazy (read-only)
- API klíče jsou ukládány v `.env` souboru (gitignored)
- Databáze je lokální SQLite bez externího přístupu

## 📝 Poznámky / Notes

- Agent automaticky vybere správný nástroj na základě dotazu
- Lze kombinovat více nástrojů v jednom dotazu
- Databáze se vytvoří automaticky při prvním spuštění

## 👨‍💻 Autor / Author

Vypracováno jako domácí úkol pro předmět AI Developer

## 📄 Licence / License

Tento projekt je vytvořen pro vzdělávací účely.
