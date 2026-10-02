# Python Calculator with Execution Time

A simple calculator built for a Parallel and Distributed Computing assignment.
It runs as a command-line program and as a Streamlit web app.

**Live demo:** https://<your-app-name>.streamlit.app

## Features
- Addition, subtraction, multiplication, division, and power
- Shows the execution time of every calculation
- Handles invalid input and division by zero
- Command-line and web (Streamlit) interfaces

## Requirements
- Python 3.8+
- Streamlit (only for the web app): `pip install -r requirements.txt`

## How to Run

Command line:
```bash
git clone https://github.com/<your-username>/python-calculator.git
cd python-calculator
python calculator.py
```

Web app:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Example
```
Enter expression (e.g. 12 * 5): 12 * 5
Result: 60.0
Execution time: 1.20 microseconds
```

## Project Structure
```
python-calculator/
├── calculator.py      # calculator logic + CLI
├── app.py             # Streamlit web interface
├── requirements.txt
└── README.md
```

## Author
Your Name — Your University, Course Name
