<h1>Personal Expense Tracker</h1>

<h3>📌 Project Overview</h3>

The Personal Expense Tracker is a web-based application built using Flask and SQLite. It allows users to add, edit, and delete expenses while categorizing them for better financial tracking. The project is structured using Flask's templating system with Bootstrap for UI styling.<br><br>

<h3>🛠️ Tech Stack</h3>

Backend: Flask (Python)<br>
Frontend: HTML, CSS (Bootstrap)<br>
Database: SQLite<br>
Deployment: Ngrok (for temporary public access)<br><br>

<h3>📂 Project Structure</h3>

expense_tracker/ <br>
│── app.py                # Main Flask application <br>
│── models.py             # Database models using SQLAlchemy <br>
│── ngrok_setup.py        # Script for setting up Ngrok <br>
│── expenses.db           # SQLite database (auto-created) <br>
│── requirements.txt      # Python dependencies <br>
│── templates/            # HTML templates <br>
│   │── base.html <br>
│   │── index.html <br>
│   │── add_expense.html <br>
│   │── edit_expense.html <br>
│── static/               # CSS files <br>
│   │── styles.css <br>
│── README.md             # Project documentation <br>
│── .gitignore            # Files to ignore in Git <br>

<h3>🚀 Installation & Setup</h3>

<h4>1️⃣ Clone the Repository</h4>

git clone https://github.com/yourusername/expense_tracker.git <br>
cd expense_tracker <br><br>

<h4>2️⃣ Create a Virtual Environment<br><br></h4>

python -m venv venv<br>
source venv/bin/activate  # For macOS/Linux<br>
venv\Scripts\activate     # For Windows<br>

<h4>3️⃣ Install Dependencies<br><br></h4>

pip install -r requirements.txt<br><br>

<h4>4️⃣ Set Up Database<br><br></h4>

python<br>
>>> from app import db<br>
>>> db.create_all()<br>
>>> exit()<br><br>

<h4>5️⃣ Run the Application<br></h4>

python app.py<br>

Access the app at: http://127.0.0.1:5000<br><br>

<h3>🌍 Deploy Using Ngrok<br></h3>

Ngrok allows you to expose your local server to the internet.<br><br>

<h4>1️⃣ Install Ngrok<br></h4>

Download Ngrok from https://ngrok.com/download.<br><br>

<h4>2️⃣ Run Ngrok to Expose Flask App<br></h4>

ngrok http 5000<br>

Ngrok will generate a public URL (e.g., https://xyz.ngrok.io). Use this to access your app remotely.<br><br>

<h3>📌 Features<br></h3>

✔ Add, Edit, and Delete Expenses✔ Categorize Expenses (Food, Transport, Bills, etc.)✔ Store Data Using SQLite✔ Responsive UI with Bootstrap✔ Deployable Using Ngrok<br><br>

<h3>📝 Contributing<br></h3>

Feel free to contribute by submitting a Pull Request or reporting issues.<br><br>

<h3>🔒 License<br></h3>

This project is open-source and available under the MIT License.<br><br>

<h3>🙌 Author<br></h3>

Your NameGitHub: preetdudhat03<br>
Email: preet.dudhat2006@email.com<br><br>

