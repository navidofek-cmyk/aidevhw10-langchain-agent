"""
Langchain Agent with Wikipedia and SQL Database Tools
Homework Assignment - AI Developer Course

This agent can:
1. Search and retrieve information from Wikipedia
2. Query SQL databases
3. Answer questions using LLM with tool integration
"""

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from my_api_key import API_KEY
import sqlite3
import os

# ===================================
# SQL Database Tool
# ===================================

# Create a sample database with some data
def initialize_database():
    """Create a sample SQLite database with employee data"""
    db_path = "sample_database.db"
    
    # Remove existing database if present
    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create employees table
    cursor.execute("""
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL,
            hire_date TEXT
        )
    """)
    
    # Insert sample data
    employees_data = [
        (1, 'John Smith', 'Engineering', 85000, '2020-03-15'),
        (2, 'Jane Doe', 'Marketing', 72000, '2019-07-22'),
        (3, 'Bob Johnson', 'Engineering', 95000, '2018-01-10'),
        (4, 'Alice Williams', 'HR', 65000, '2021-05-18'),
        (5, 'Charlie Brown', 'Sales', 78000, '2020-09-30'),
    ]
    
    cursor.executemany(
        "INSERT INTO employees VALUES (?, ?, ?, ?, ?)",
        employees_data
    )
    
    # Create products table
    cursor.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL,
            stock_quantity INTEGER
        )
    """)
    
    # Insert sample products
    products_data = [
        (1, 'Laptop', 'Electronics', 1200.00, 50),
        (2, 'Mouse', 'Electronics', 25.00, 200),
        (3, 'Desk Chair', 'Furniture', 350.00, 30),
        (4, 'Monitor', 'Electronics', 450.00, 75),
        (5, 'Notebook', 'Stationery', 5.00, 500),
    ]
    
    cursor.executemany(
        "INSERT INTO products VALUES (?, ?, ?, ?, ?)",
        products_data
    )
    
    conn.commit()
    conn.close()
    print(f"✓ Database initialized: {db_path}")


@tool(
    "query_sql_database",
    description="Execute SQL queries on the sample database. Use this to get information about employees or products. The database has 'employees' table (id, name, department, salary, hire_date) and 'products' table (id, product_name, category, price, stock_quantity)."
)
def query_sql_database(sql_query: str) -> str:
    """Execute a SQL query on the sample SQLite database.
    
    Args:
        sql_query: A valid SQL SELECT query string
        
    Returns:
        Query results as a formatted string
    """
    try:
        conn = sqlite3.connect("sample_database.db")
        cursor = conn.cursor()
        
        # Security: Only allow SELECT queries
        if not sql_query.strip().upper().startswith("SELECT"):
            return "Error: Only SELECT queries are allowed for safety."
        
        cursor.execute(sql_query)
        results = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        
        conn.close()
        
        if not results:
            return "No results found."
        
        # Format results as a table
        output = "\n".join([" | ".join(column_names)])
        output += "\n" + "-" * (len(output) - 1) + "\n"
        
        for row in results:
            output += " | ".join(str(value) for value in row) + "\n"
        
        return output
        
    except Exception as e:
        return f"Error executing query: {str(e)}"


# ===================================
# Wikipedia Tool
# ===================================

# Initialize Wikipedia tool
wikipedia_api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=500)
wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_api_wrapper)

# ===================================
# Create Agent
# ===================================

# Initialize the database with sample data
initialize_database()

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = API_KEY

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Create agent with tools
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

# ===================================
# Main Interaction Loop
# ===================================

def main():
    print("=" * 60)
    print("🤖 Langchain Agent with Wikipedia & SQL Database")
    print("=" * 60)
    print("\nAvailable capabilities:")
    print("  • Search Wikipedia for general knowledge")
    print("  • Query SQL database for employees and products data")
    print("\nType 'quit' or 'exit' to end the session\n")
    print("-" * 60)
    
    # Example queries
    example_queries = [
        "Who is Albert Einstein?",
        "Show me all employees in the Engineering department",
        "What products cost less than $100?",
        "What is Python programming language?",
    ]
    
    print("\n💡 Example queries you can try:")
    for i, query in enumerate(example_queries, 1):
        print(f"  {i}. {query}")
    print("\n" + "-" * 60 + "\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Goodbye!")
                break
            
            if not user_input:
                continue
            
            # Create conversation
            conversation = {
                "messages": [
                    {"role": "user", "content": user_input}
                ]
            }
            
            # Invoke agent
            print("\n🔄 Processing...\n")
            response = agent.invoke(conversation)
            
            # Print response
            print("Agent:", response["messages"][-1].content)
            print("\n" + "-" * 60 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")
            print("-" * 60 + "\n")


if __name__ == "__main__":
    main()
