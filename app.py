from flask import Flask, render_template, request, redirect
import pyodbc
import os

app = Flask(__name__)

server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")
driver = "{ODBC Driver 18 for SQL Server}"

if not all([server, database, username, password]):
    raise Exception("Faltan variables de entorno de la base de datos")

connection_string = (
    f"DRIVER={driver};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)

def get_connection():
    return pyodbc.connect(connection_string)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='tasks' AND xtype='U')
        CREATE TABLE tasks (
            id INT PRIMARY KEY IDENTITY(1,1),
            title NVARCHAR(100),
            done BIT
        )
    """)

    conn.commit()
    conn.close()


init_db()

@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")

    if title:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            (title, 0)
        )

        conn.commit()
        conn.close()

    return redirect("/")


@app.route("/done/<int:task_id>")
def mark_done(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET done = 1 WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)