from flask import Flask, render_template, redirect, url_for, request, session
import csv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for using sessions

# Sample data for puzzles (you can expand this)
puzzles = [
    {"id": 1, "type": "crossword", "content": "Crossword on GHG"},
    {"id": 2, "type": "match", "content": "Match renewable energy with their resources"},
    {"id": 3, "type": "message", "content": "Message on Global warming"},
    {"id": 4, "type": "map", "content": "Mark on Map with the greenest area"},
    {"id": 5, "type": "calculate", "content": "Calculate individual Carbon footprint"},
]

clues = ["Clue 1", "Clue 2", "Clue 3", "Clue 4", "Final Clue"]

CSV_FILE = 'user_data.csv'

# Ensure the CSV file exists and has the correct headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Role', 'Page'])

@app.route('/')
def index():
    return redirect(url_for('collect_data'))

@app.route('/collect_data')
def collect_data():
    return render_template('collect_data.html')

@app.route('/start', methods=['POST'])
def start_game():
    session['name'] = request.form['name']
    session['role'] = request.form['role']
    # Log the initial data
    log_user_data(session['name'], session['role'], 'start_game')
    return redirect(url_for('show_puzzles'))

@app.route('/show_puzzles')
def show_puzzles():
    log_user_data(session['name'], session['role'], 'show_puzzles')
    return render_template('index.html', puzzles=puzzles, name=session.get('name'), role=session.get('role'))

@app.route('/quit')
def quit():
    log_user_data(session['name'], session['role'], 'quit')
    return "You have quit the game."

@app.route('/puzzle/<int:puzzle_id>')
def puzzle(puzzle_id):
    puzzle = next((p for p in puzzles if p['id'] == puzzle_id), None)
    if puzzle:
        log_user_data(session['name'], session['role'], f'puzzle{puzzle_id}')
        return render_template(f'puzzle{puzzle_id}.html', puzzle=puzzle, name=session.get('name'), role=session.get('role'), avatar_state=None)
    return redirect(url_for('index'))

@app.route('/final')
def final():
    log_user_data(session['name'], session['role'], 'final')
    return render_template('final.html', clues=clues, name=session.get('name'), role=session.get('role'))

@app.route('/puzzle5', methods=['GET', 'POST'])
def puzzle5():
    if request.method == 'POST':
        carbon_footprint = request.form.get('carbonFootprint')
        if carbon_footprint:
            # Store carbon footprint in session or local storage as needed
            return redirect(url_for('final'))
        else:
            return "Please enter your carbon footprint."
    log_user_data(session['name'], session['role'], 'puzzle5')
    return render_template('puzzle5.html', name=session.get('name'), role=session.get('role'), avatar_state=None)

def log_user_data(name, role, page):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, role, page])

if __name__ == '__main__':
    app.run(debug=True)
