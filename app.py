from flask import Flask, jsonify, request
import os
import uuid
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# In-memory storage for notes
notes = {}

# Routes

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Flask Notes API inside Docker!",
        "total_notes": len(notes)
    })

@app.route("/notes", methods=["GET"])
def get_notes():
    """Return all notes"""
    return jsonify(list(notes.values()))

@app.route("/notes/<note_id>", methods=["GET"])
def get_note(note_id):
    """Return a single note"""
    note = notes.get(note_id)
    if note:
        return jsonify(note)
    return jsonify({"error": "Note not found"}), 404

@app.route("/notes", methods=["POST"])
def create_note():
    """Create a new note"""
    data = request.json
    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "Invalid request"}), 400

    note_id = str(uuid.uuid4())
    note = {
        "id": note_id,
        "title": data["title"],
        "content": data["content"]
    }
    notes[note_id] = note
    logger.info(f"Created note {note_id}")
    return jsonify(note), 201

@app.route("/notes/<note_id>", methods=["PUT"])
def update_note(note_id):
    """Update an existing note"""
    note = notes.get(note_id)
    if not note:
        return jsonify({"error": "Note not found"}), 404

    data = request.json
    note["title"] = data.get("title", note["title"])
    note["content"] = data.get("content", note["content"])
    logger.info(f"Updated note {note_id}")
    return jsonify(note)

@app.route("/notes/<note_id>", methods=["DELETE"])
def delete_note(note_id):
    """Delete a note"""
    if note_id in notes:
        del notes[note_id]
        logger.info(f"Deleted note {note_id}")
        return jsonify({"message": "Note deleted"})
    return jsonify({"error": "Note not found"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
