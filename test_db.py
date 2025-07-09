# test_db.py
from db_config import get_connection

try:
    conn = get_connection()
    print("Connected to DB ✅")
    conn.close()
except Exception as e:
    print("❌ DB Connection failed:", e)
