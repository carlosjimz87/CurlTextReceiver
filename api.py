import os
from datetime import datetime
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Determine the save path
if "PYTHONANYWHERE_DOMAIN" in os.environ:
    ROOT_PATH = f"/home/{os.getenv('USER')}/saved/"
else:
    ROOT_PATH = "./saved/"

# Ensure the directory exists
os.makedirs(ROOT_PATH, exist_ok=True)


# Endpoint to save text or binary files
@app.route("/save", methods=["POST"])
@app.route("/save/", methods=["POST"])
def save_text():
    if "file" not in request.files:
        return jsonify({"message": "No file provided!"}), 400

    uploaded_file = request.files["file"]
    original_filename = secure_filename(uploaded_file.filename or "uploaded")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Case: text file → decode and save as .txt
    if original_filename.lower().endswith(".txt"):
        try:
            file_content = uploaded_file.read().decode("utf-8", errors="replace")
            file_name = f"saved_{timestamp}.txt"
            file_path = os.path.join(ROOT_PATH, file_name)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(file_content)
        except Exception as e:
            return jsonify({"message": "Error reading text file", "error": str(e)}), 500

    # Case: any other file → save directly
    else:
        file_name = f"{timestamp}_{original_filename}"
        file_path = os.path.join(ROOT_PATH, file_name)
        try:
            uploaded_file.save(file_path)
        except Exception as e:
            return jsonify({"message": "Error saving file", "error": str(e)}), 500

    return jsonify({"message": "File saved successfully!", "file_path": file_path})


# Endpoint to clear all saved texts
@app.route("/clear", methods=["POST", "GET"])
@app.route("/clear/", methods=["POST", "GET"])
def erase_texts():
    file_list = os.listdir(ROOT_PATH)
    if not file_list:
        return jsonify({"message": "No files to delete!"})

    # Delete all files in the save directory
    for file_name in file_list:
        os.remove(os.path.join(ROOT_PATH, file_name))

    return jsonify({"message": "All saved texts and files have been erased!"})


# Health check endpoint
@app.route("/", methods=["POST", "GET"])
@app.route("/status", methods=["POST", "GET"])
@app.route("/status/", methods=["POST", "GET"])
def health_check():
    return jsonify({"status": "API is running!"})


# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
