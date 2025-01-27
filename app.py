from flask import Flask, render_template
import serial
import time

app = Flask(__name__)

bluetooth = serial.Serial('COM3', 9600)
time.sleep(2)

@app.route('/')
def index():
    data = None
    try:
        if bluetooth.in_waiting > 0:
            data = bluetooth.readline().decode('utf-8').strip()
    except Exception as e:
        data = f"Error: {e}"

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
