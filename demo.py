"""
Demo script - shows the agent in action with example queries
"""

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from my_api_key import API_KEY
import sqlite3
import os

# Set API key
os.environ["OPENAI_API_KEY"] = API_KEY

# Initialize database
def initialize_database():
    """Create a sample SQLite database"""
    db_path = "sample_database.db"
    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL,
            hire_date TEXT
        )
    """)
    
    employees_data = [
        (1, 'John Smith', 'Engineering', 85000, '2020-03-15'),
        (2, 'Jane Doe', 'Marketing', 72000, '2019-07-22'),
        (3, 'Bob Johnson', 'Engineering', 95000, '2018-01-10'),
        (4, 'Alice Williams', 'HR', 65000, '2021-05-18'),
        (5, 'Charlie Brown', 'Sales', 78000, '2020-09-30'),
    ]
    
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", employees_data)
    
    cursor.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL,
            stock_quantity INTEGER
        )
    """)
    
    products_data = [
        (1, 'Laptop', 'Electronics', 1200.00, 50),
        (2, 'Mouse', 'Electronics', 25.00, 200),
        (3, 'Desk Chair', 'Furniture', 350.00, 30),
        (4, 'Monitor', 'Electronics', 450.00, 75),
        (5, 'Notebook', 'Stationery', 5.00, 500),
    ]
    
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?)", products_data)
    
    conn.commit()
    conn.close()

@tool("query_sql_database")
def query_sql_database(sql_query: str) -> str:
    """Execute a SQL query on the sample SQLite database."""
    try:
        conn = sqlite3.connect("sample_database.db")
        cursor = conn.cursor()
        
        if not sql_query.strip().upper().startswith("SELECT"):
            return "Error: Only SELECT queries are allowed."
        
        cursor.execute(sql_query)
        results = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        conn.close()
        
        if not results:
            return "No results found."
        
        output = "\n".join([" | ".join(column_names)])
        output += "\n" + "-" * 50 + "\n"
        
        for row in results:
            output += " | ".join(str(value) for value in row) + "\n"
        
        return output
        
    except Exception as e:
        return f"Error executing query: {str(e)}"

# Initialize
print("=" * 70)
print("🤖 LANGCHAIN AGENT DEMO - Wikipedia & SQL Database")
print("=" * 70)
print()

initialize_database()
print("✓ Database initialized\n")

# Setup tools
wikipedia_api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=500)
wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_api_wrapper)

# Create agent
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
agent = create_agent(
    llm,
    tools=[wikipedia_tool, query_sql_database],
    system_prompt="""You are a helpful AI assistant with access to Wikipedia and a SQL database.

When asked about general knowledge, use Wikipedia to find information.
When asked about employees or products, use the SQL database.

The database contains:
- employees table: id, name, department, salary, hire_date
- products table: id, product_name, category, price, stock_quantity

Be concise, accurate, and helpful in your responses."""
)

# Example queries to demonstrate
examples = [
    {
        "query": "Who is Albert Einstein?",
        "description": "Wikipedia Query - General Knowledge"
    },
    {
        "query": "Show me all employees in the Engineering department",
        "description": "SQL Query - Database Search"
    },
    {
        "query": "What products cost less than $100?",
        "description": "SQL Query - Price Filter"
    }
]

# Run examples
for i, example in enumerate(examples, 1):
    print(f"\n{'='*70}")
    print(f"📝 Example {i}: {example['description']}")
    print(f"{'='*70}")
    print(f"\n❓ Query: {example['query']}")
    print(f"\n🔄 Processing...\n")
    
    try:
        conversation = {
            "messages": [
                {"role": "user", "content": example['query']}
            ]
        }
        
        response = agent.invoke(conversation)
        answer = response["messages"][-1].content
        
        print(f"💡 Agent Response:")
        print(f"{'-'*70}")
        print(answer)
        print(f"{'-'*70}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

print(f"\n{'='*70}")
print("✅ Demo Complete!")
print("=" * 70)
print("\nTo run the interactive agent, use: python main.py")
