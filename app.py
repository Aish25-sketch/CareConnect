from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

def create_database():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS support (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            category TEXT,
            message TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            interest TEXT,
            availability TEXT
        )
    """)

    # Add availability to databases created with the earlier version.
    columns = [row[1] for row in cursor.execute("PRAGMA table_info(volunteers)")]
    if "availability" not in columns:
        cursor.execute("ALTER TABLE volunteers ADD COLUMN availability TEXT")

    connection.commit()
    connection.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/support", methods=["POST"])
def support():
    data = request.get_json()
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO support (name, email, category, message) VALUES (?, ?, ?, ?)",
        (data["name"], data["email"], data["support_type"], data["message"])
    )

    connection.commit()
    connection.close()
    return jsonify({"message": "Thanks. Your request has been received."})


@app.route("/volunteer", methods=["POST"])
def volunteer():
    data = request.get_json()
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO volunteers (name, email, interest, availability) VALUES (?, ?, ?, ?)",
        (data["name"], data["email"], data["interest"], data.get("availability", ""))
    )

    connection.commit()
    connection.close()
    return jsonify({"message": "Thanks for offering to help. We'll be in touch."})


@app.route("/dashboard")
def dashboard():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM support")
    support_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM volunteers")
    volunteer_count = cursor.fetchone()[0]

    connection.close()
    return render_template(
        "dashboard.html",
        support_count=support_count,
        volunteer_count=volunteer_count
    )


create_database()

if __name__ == "__main__":
    app.run(debug=True)