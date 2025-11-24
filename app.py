import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
try:
    from werkzeug.security import check_password_hash, generate_password_hash
except Exception:
    import hashlib
    import hmac
    import binascii

    def generate_password_hash(password: str) -> str:
        """Generate a salted PBKDF2-HMAC-SHA256 hash stored as salt_hex$dk_hex."""
        salt = os.urandom(16)
        dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
        return binascii.hexlify(salt).decode() + "$" + binascii.hexlify(dk).decode()

    def check_password_hash(stored_hash: str, password: str) -> bool:
        """Verify a password against a stored salt$hash produced by generate_password_hash."""
        try:
            salt_hex, dk_hex = stored_hash.split("$", 1)
        except ValueError:
            return False
        salt = binascii.unhexlify(salt_hex)
        dk = binascii.unhexlify(dk_hex)
        new_dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
        return hmac.compare_digest(dk, new_dk)

from helpers import login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    
    return render_template("index.html", username = session["username"])



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()
    error="h"
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            error ="must provide username"
            return render_template("login.html", error = error)

        # Ensure password was submitted
        elif not request.form.get("password"):
            error = "must provide password"
            return render_template("login.html", error = error)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            error = "invalid username and/or password"
            return render_template("login.html", error = error)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html", error = error)


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    rows = db.execute(
        "SELECT * FROM users WHERE username = ?", request.form.get("username")
    )
    error = "h"
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            error = "must provide username"
            return render_template("register.html", error = error)

        # Ensure password was submitted
        elif not request.form.get("password") or not request.form.get("confirmation"):
            error = "must provide password"
            return render_template("register.html", error = error)

        # Ensure passwords match
        elif not (request.form.get("password") == request.form.get("confirmation")):
            error = "Passwords do not match"
            return render_template("register.html", error = error)

        # Ensure username is not taken
        elif len(rows) == 1:
            error = "username taken"
            return render_template("register.html", error = error)

        # store user info
        username = request.form.get("username")
        hash = generate_password_hash(request.form.get("password"))
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]
        return redirect("/")
    else:
        return render_template("register.html", error = error)

