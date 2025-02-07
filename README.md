# CurlTextReceiver

`CurlTextReceiver` is a minimal FastAPI application that accepts text input via a POST request and saves it to a file. The saved files include a timestamp for unique identification.

## Features
- Accepts plain text data via a POST request.
- Saves the text to a file with a timestamp in the file name.
- Ensures the save directory exists.

## Requirements
- Python +3.12
- FastAPI +0.63
- Pydantic +1.9
- Uvicorn +0.34

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/curl-receiver.git
   cd curl-receiver
    ```
   
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
   
3. Install the dependencies:
   ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the app using Uvicorn:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```
   
2. Start the app using the run script:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

3. Send a POST request to save plain text:
   ```bash
    curl -X POST "http://localhost:8000/save/" -d 'Hi, there!'
    ```
   
4. Send a POST request to save a file's content:
   ```bash
    curl -X POST "http://localhost:8000/save/" -d file.txt
    ```
   
5. Check the saved file in the `saved` directory:
   ```bash
    ll saved
   -rw-r--r--  1 user.name  staff    10B Feb  6 13:32 saved_2025-02-06_13-32-36.txt
   -rw-r--r--  1 user.name  staff     4B Feb  6 13:32 saved_2025-02-06_13-32-42.txt
   -rw-r--r--  1 user.name  staff     3B Feb  6 13:33 saved_2025-02-06_13-33-29.txt
    ```

6. Send a POST or GET request to erase all saved texts:
   ```bash
   curl -X POST "http://localhost:8000/clear/"
   curl -X GET "http://localhost:8000/clear/"
   ```
   
7. Check all files are erased:
   ```bash
    ll saved
    total 0
    ```
   
8. Send a POST or GET to check api status:
   ```bash
   curl -X POST "http://localhost:8000/"
   curl -X GET "http://localhost:8000/"
   curl -X POST "http://localhost:8000/status/"
   curl -X GET "http://localhost:8000/status/"
   ```
   