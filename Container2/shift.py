#!/usr/bin/python
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/shifts')
def get_shifts():
    conn = sqlite3.connect('shifts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM shifts')
    shifts = c.fetchall()
    conn.close()
    return jsonify(shifts)

if __name__ == '__main__':
    app.run()
