from passlib.context import CryptContext
from db import get_connection, initialize_database

_passwords = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(username: str, email: str, password: str) -> None:
    initialize_database()
    hashed = _passwords.hash(password)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
                (username, email, hashed),
            )

def verify_user(username: str, password: str):
    initialize_database()
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT username, email, password_hash FROM users WHERE username = %s",
                (username,),
            )
            user = cur.fetchone()
    if user and _passwords.verify(password, user["password_hash"]):
        return {"username": user["username"], "email": user["email"]}
    return None
