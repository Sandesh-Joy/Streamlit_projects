import streamlit as st
import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    cfg = st.secrets["postgres"]
    return psycopg2.connect(
        host=cfg["host"], port=cfg.get("port", 5432),
        dbname=cfg["database"], user=cfg["user"],
        password=cfg["password"],
        sslmode=cfg.get("sslmode", "prefer"),
        cursor_factory=RealDictCursor,
    )

def initialize_database():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
