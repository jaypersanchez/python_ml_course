import json
import psycopg2
import torch
import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from dotenv import load_dotenv

load_dotenv()

# Database connection parameters from environment variables
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')

try:
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname=db_name, user=db_user, password=db_password, host=db_host
    )
    cur = conn.cursor()

    # Commit changes
    conn.commit()

except psycopg2.DatabaseError as e:
    print(f"Database error: {e}")
finally:
    # Close the cursor and connection to clean up
    if cur is not None:
        cur.close()
    if conn is not in [None, 'closed']:
        conn.close()

print("Database operation completed")