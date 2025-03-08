from flask import Flask, jsonify
import random

app = Flask(__name__)

verses = [
    "Right now, I'm in a state of mind",
    "I want to be in like all the time",
    "Ain't got no tears left to cry",
    "So I'm pickin' it up, pickin' it up",
    "I'm pickin' it up, pickin' it up",
    "I'm so f***in' grateful for my ex"
]

@app.route('/generate-verse', methods=['GET'])
def generate_verse():
    verse = random.choice(verses)
    return jsonify({"verse": verse})

if __name__ == '__main__':
    app.run(debug=True)