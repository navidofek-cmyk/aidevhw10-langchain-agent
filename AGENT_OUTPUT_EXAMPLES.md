# Příklady výstupů agenta

## Tady je vidět jak agent funguje v praxi

---

## Příklad 1: Dotaz na Wikipedia

### Otázka:
```
"Who is Albert Einstein?"
```

### Co agent udělá:
1. Přečte si otázku
2. Rozhodne se: "Tohle je o osobě - potřebuju Wikipedia"
3. Zavolá Wikipedia nástroj
4. Wikipedia API najde info o "Albert Einstein"
5. Agent naformátuje odpověď

### Odpověď agenta:
```
Albert Einstein (14 March 1879 – 18 April 1955) was a German-born 
theoretical physicist renowned for developing the theory of relativity. 
He also made significant contributions to quantum theory. His mass–energy 
equivalence formula, E = mc², is one of the most famous equations in the 
world. Einstein was awarded the Nobel Prize in Physics in 1921 for his 
services to theoretical physics, particularly for his discovery of the 
law of the photoelectric effect.
```

**Agent sám vybral Wikipedia nástroj!**

---

## Příklad 2: SQL dotaz do databáze

### Otázka:
```
"Show me all employees in the Engineering department"
```

### Co agent udělá:
1. Přečte si otázku
2. Rozhodne se: "Tohle je o databázi zaměstnanců - potřebuju SQL"
3. Zavolá SQL nástroj
4. Vygeneruje SQL: `SELECT * FROM employees WHERE department = 'Engineering'`
5. Spustí dotaz
6. Naformátuje výsledky

### Odpověď agenta:
```
Here are the employees in the Engineering department:

1. **John Smith**
   - Salary: $85,000
   - Hire Date: March 15, 2020

2. **Bob Johnson**
   - Salary: $95,000
   - Hire Date: January 10, 2018
```

**Agent sám vybral SQL nástroj!**

---

## Příklad 3: SQL dotaz s filtrem

### Otázka:
```
"What products cost less than $100?"
```

### Co agent udělá:
1. Přečte si otázku
2. Rozhodne se: "Tohle je o produktech s cenou - potřebuju SQL"
3. Zavolá SQL nástroj
4. Vygeneruje SQL: `SELECT * FROM products WHERE price < 100`
5. Spustí dotaz
6. Naformátuje výsledky

### Odpověď agenta:
```
The products that cost less than $100 are:

1. **Mouse**
   - Category: Electronics
   - Price: $25.00
   - Stock Quantity: 200

2. **Notebook**
   - Category: Stationery
   - Price: $5.00
   - Stock Quantity: 500
```

**Agent sám vybral SQL nástroj!**

---

## Jak to funguje - klíčové body:

### 1. Výběr nástroje (automatický)
```python
agent = create_agent(
    llm,
    tools=[wikipedia_tool, query_sql_database],
    system_prompt="..."
)
```
- Agent přečte otázku
- Rozhodne se který nástroj použít
- Není potřeba nic programovat ručně

### 2. Spuštění nástroje
```python
response = agent.invoke(conversation)
```
- Agent zavolá správný nástroj
- Získá data
- Naformátuje odpověď

### 3. Pochopení přirozeného jazyka
```
Uživatel: "Who is Albert Einstein?"
  → Agent si myslí: "Dotaz na osobu → Použiju Wikipedia"

Uživatel: "Show me employees in Engineering"
  → Agent si myslí: "Databázový dotaz → Použiju SQL"
```

---

## Kompletní výstup z demo (z terminálu):

```
======================================================================
LANGCHAIN AGENT DEMO - Wikipedia & SQL Database
======================================================================

✓ Database initialized

======================================================================
Example 1: Wikipedia Query
======================================================================

Query: Who is Albert Einstein?

Processing...

Agent Response:
----------------------------------------------------------------------
Albert Einstein (14 March 1879 – 18 April 1955) was a German-born 
theoretical physicist renowned for developing the theory of relativity...
----------------------------------------------------------------------

======================================================================
Example 2: SQL Query
======================================================================

Query: Show me all employees in the Engineering department

Processing...

Agent Response:
----------------------------------------------------------------------
Here are the employees in the Engineering department:

1. **John Smith**
   - Salary: $85,000
   - Hire Date: March 15, 2020

2. **Bob Johnson**
   - Salary: $95,000
   - Hire Date: January 10, 2018
----------------------------------------------------------------------

======================================================================
Example 3: SQL Query - Price Filter
======================================================================

Query: What products cost less than $100?

Processing...

Agent Response:
----------------------------------------------------------------------
The products that cost less than $100 are:

1. **Mouse**
   - Category: Electronics
   - Price: $25.00
   - Stock Quantity: 200

2. **Notebook**
   - Category: Stationery
   - Price: $5.00
   - Stock Quantity: 500
----------------------------------------------------------------------

======================================================================
Demo Complete!
======================================================================
```

---

## Co se děje na pozadí:

### Krok 1: Vstup od uživatele
```python
conversation = {
    "messages": [{"role": "user", "content": "Who is Albert Einstein?"}]
}
```

### Krok 2: Agent zpracovává
```
[Agent si myslí]
1. Analyzuji otázku: "Who is Albert Einstein?"
2. Tohle je otázka na obecné znalosti o osobě
3. Mám 2 nástroje: Wikipedia a SQL Database
4. Wikipedia je na tohle nejlepší
5. Volám WikipediaQueryRun...
6. Dostal jsem odpověď z Wikipedie
7. Formátuji odpověď pro uživatele...
```

### Krok 3: Spuštění nástroje
```python
# Langchain interně dělá:
wikipedia_result = wikipedia_tool.run("Albert Einstein")
```

### Krok 4: Odpověď
```python
response = agent.invoke(conversation)
print(response["messages"][-1].content)
```

---

## Důkaz že používám Langchain:

1. **Framework:** Langchain `create_agent`
2. **Nástroje:** Langchain `WikipediaQueryRun` + vlastní `@tool` dekorátor
3. **LLM:** Langchain `ChatOpenAI`
4. **Automatický výběr nástrojů:** Langchain rozhoduje který nástroj použít
5. **Přirozený jazyk:** Langchain rozumí co se ptám

**Domácí úkol plně demonstruje použití Langchainu!**
