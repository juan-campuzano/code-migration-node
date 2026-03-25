from flask import Flask, jsonify
import requests
import numpy as np
import pandas as pd
import yaml
import uuid
from sqlalchemy import create_engine, text
from PIL import Image
import io
import base64
from cryptography.fernet import Fernet

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
        'message': 'Python App with Outdated Dependencies',
        'uuid': str(uuid.uuid4()),
    })


@app.route('/data')
def data():
    # Using numpy (1.26.4) and pandas (2.1.4) — intentionally outdated
    arr = np.array([1, 2, 2, 3, 3, 4])
    unique_vals = np.unique(arr).tolist()

    df = pd.DataFrame({'values': unique_vals})
    summary = df.describe().to_dict()

    return jsonify({
        'unique_values': unique_vals,
        'summary': summary,
    })


@app.route('/config')
def config():
    # Using PyYAML (5.1) — intentionally outdated (current is 6.x)
    raw = """
app:
  name: python-app
  version: 1.0.0
  debug: true
"""
    parsed = yaml.safe_load(raw)
    return jsonify(parsed)


@app.route('/db')
def db():
    # Using SQLAlchemy (1.4.54) — intentionally outdated (current is 2.x)
    engine = create_engine('sqlite:///:memory:')
    with engine.connect() as conn:
        conn.execute(text('CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT)'))
        conn.execute(text("INSERT INTO items (name) VALUES ('alpha'), ('beta'), ('gamma')"))
        result = conn.execute(text('SELECT * FROM items'))
        rows = [{'id': row[0], 'name': row[1]} for row in result]
    return jsonify({'items': rows})


@app.route('/image')
def image():
    # Using Pillow (10.0.1) — intentionally outdated (current is 11.x)
    img = Image.new('RGB', (64, 64), color=(255, 100, 50))
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    encoded = base64.b64encode(buf.getvalue()).decode('utf-8')
    return jsonify({'format': 'PNG', 'size': '64x64', 'data': encoded})


@app.route('/encrypt')
def encrypt():
    # Using cryptography (38.0.4) — intentionally outdated (current is 44.x)
    key = Fernet.generate_key()
    fernet = Fernet(key)
    message = b'Hello, Migration Tooling!'
    token = fernet.encrypt(message)
    decrypted = fernet.decrypt(token)
    return jsonify({
        'original': message.decode(),
        'decrypted': decrypted.decode(),
        'match': message == decrypted,
    })


@app.route('/fetch')
def fetch():
    # Using requests (2.28.2) — intentionally outdated (current is 2.32.x)
    response = requests.get('https://httpbin.org/get', timeout=5)
    return jsonify({'status_code': response.status_code})


if __name__ == '__main__':
    import os
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug)
