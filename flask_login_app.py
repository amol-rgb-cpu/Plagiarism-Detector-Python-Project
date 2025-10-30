import sqlite3
import os
from flask import Flask, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

# --- Configuration ---

app = Flask(__name__)

# The secret key is essential for securing session cookies
app.config['SECRET_KEY'] = 'your_super_secret_key_needs_to_be_long_and_random'
app.config['SESSION_PERMANENT'] = False

# Database path for relative or absolute reliability
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'user.db')

# --- Database Functions ---

def get_db_connection():
    """Establishes and returns a SQLite database connection."""
    if not os.path.exists(DATABASE):
        raise FileNotFoundError(f"Database file not found at: {DATABASE}. Connection aborted.")
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db_connection(e=None):
    """Closes the database connection if it was opened."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

app.teardown_appcontext(close_db_connection)

def create_users_table_if_not_exists(conn, force_recreate=False):
    """Creates the users table or ensures its schema is correct."""
    if force_recreate:
        print("Forcing recreation of 'users' table (data will be lost).")
        conn.execute("DROP TABLE IF EXISTS users;")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        );
    """)
    conn.commit()

def init_db(create_new_db=False):
    """Initializes the database by checking for file existence and table schema."""
    if not os.path.exists(DATABASE):
        print(f"Skipping database initialization: '{DATABASE}' file not found.")
        return
    try:
        conn = get_db_connection()
        create_users_table_if_not_exists(conn, force_recreate=create_new_db)
        print(f"Database table check successful at {DATABASE}.")
    except FileNotFoundError:
        pass
    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")
    finally:
        close_db_connection()

# Run initialization when the app starts
with app.app_context():
    init_db(create_new_db=False)

# --- New Debugging Route ---

@app.route('/init-db-force')
def init_db_force_route():
    """Route to force initialization and overwrite the existing 'users' table."""
    with app.app_context():
        init_db(create_new_db=True)
    flash("Database table re-initialized (OLD USERS DELETED!). Please register a new account.", 'warning')
    return redirect(url_for('register'))

# --- Authentication Middleware ---

@app.before_request
def check_authentication():
    """Enforces login for all but public auth routes."""
    public_routes = ['login', 'register', 'splash', 'init_db_force_route', 'static']
    logged_in = session.get('logged_in')
    current_endpoint = request.endpoint
    if not logged_in and current_endpoint not in public_routes:
        return redirect(url_for('splash'))

# --- Routes ---

@app.route('/splash')
def splash():
    """Renders the welcome/splash page."""
    if session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('splash.html')

@app.route('/')
def index():
    """The main application page, requiring authentication."""
    if not session.get('logged_in'):
        return redirect(url_for('splash'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        try:
            conn = get_db_connection()
            conn.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                         (username, hashed_password))
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except FileNotFoundError as e:
            flash(f'Database Error: {e}', 'error')
            return render_template('register.html')
        except sqlite3.IntegrityError:
            flash('Username already taken. Please choose another.', 'error')
            return render_template('register.html')
        except Exception as e:
            flash(f'An error occurred during registration: {e}', 'error')
            return render_template('register.html')
        finally:
            if 'db' in g:
                close_db_connection()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            conn = get_db_connection()
            user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
            if user and check_password_hash(user['password_hash'], password):
                session['logged_in'] = True
                session['username'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password.', 'error')
                return render_template('login.html')
        except FileNotFoundError as e:
            flash(f'Database Error: {e}', 'error')
            return render_template('login.html')
        except Exception as e:
            flash(f'A server error occurred during login: {e}', 'error')
            return render_template('login.html')
        finally:
            if 'db' in g:
                close_db_connection()
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    """Handles user logout."""
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
