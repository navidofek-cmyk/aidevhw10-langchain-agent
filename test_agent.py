"""
Test script for the Homework Agent
Tests Wikipedia and SQL database functionality
"""

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from my_api_key import API_KEY
import sqlite3
import os

# Import the database initialization function
import sys
sys.path.append(os.path.dirname(__file__))

def initialize_test_database():
    """Create a sample SQLite database with employee data"""
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
    ]
    
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", employees_data)
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
        
        output = " | ".join(column_names) + "\n"
        output += "-" * 50 + "\n"
        for row in results:
            output += " | ".join(str(value) for value in row) + "\n"
        
        return output
    except Exception as e:
        return f"Error: {str(e)}"

def run_tests():
    print("=" * 60)
    print("🧪 Testing Homework Agent")
    print("=" * 60)
    
    # Initialize database
    print("\n1. Initializing test database...")
    initialize_test_database()
    print("   ✓ Database created")
    
    # Setup tools
    print("\n2. Setting up tools...")
    wikipedia_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
    wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_api_wrapper)
    print("   ✓ Wikipedia tool ready")
    print("   ✓ SQL tool ready")
    
    # Create agent
    print("\n3. Creating agent...")
    os.environ["OPENAI_API_KEY"] = API_KEY
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    agent = create_agent(
        llm,
        tools=[wikipedia_tool, query_sql_database],
        system_prompt="You are a helpful assistant. Use tools when needed."
    )
    print("   ✓ Agent created")
    
    # Test queries
    test_queries = [
        ("SQL Test", "How many employees are in the Engineering department?"),
        ("Wikipedia Test", "Who is Isaac Newton?"),
    ]
    
    print("\n4. Running test queries...\n")
    
    for test_name, query in test_queries:
        print(f"   📝 {test_name}: {query}")
        try:
            conversation = {"messages": [{"role": "user", "content": query}]}
            response = agent.invoke(conversation)
            result = response["messages"][-1].content
            print(f"   ✓ Response: {result[:100]}...")
            print()
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            print()
    
    print("=" * 60)
    print("✅ All tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
