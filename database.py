import sqlite3

# ✅ Create database & table if not exists
def init_db():
    conn = sqlite3.connect("chatbot.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ✅ Insert a new FAQ
def add_faq(question, answer):
    conn = sqlite3.connect("chatbot.db")
    c = conn.cursor()
    c.execute("INSERT INTO faq (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()

# ✅ Fetch all FAQs
def get_all_faqs():
    conn = sqlite3.connect("chatbot.db")
    c = conn.cursor()
    c.execute("SELECT question, answer FROM faq")
    data = c.fetchall()
    conn.close()
    return data
