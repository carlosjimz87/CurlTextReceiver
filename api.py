import os
from datetime import datetime

from fastapi import FastAPI, Body

app = FastAPI()

if "PYTHONANYWHERE_DOMAIN" in os.environ:
    ROOT_PATH = f"/home/{os.getenv('USER')}/saved_texts/"
else:
    ROOT_PATH = "./saved_texts/"

# Ensure the directory exists
os.makedirs(ROOT_PATH, exist_ok=True)


@app.post("/save-text", include_in_schema=False)
@app.post("/save-text/")
async def save_text(content: str = Body(..., media_type="text/plain")):
    # Generate timestamp for file naming
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"saved_text_{timestamp}.txt"
    file_path = os.path.join(ROOT_PATH, file_name)

    # Save the text
    with open(file_path, "w") as file:
        file.write(content)

    return {"message": "Text saved successfully!", "file_path": file_path}


# create a request to erase all the saved texts
@app.post("/clear", include_in_schema=False)
@app.post("/clear/")
async def erase_texts():
    file_list = os.listdir(ROOT_PATH)
    if not file_list:
        return {"message": "No files to delete!"}

    for file_name in file_list:
        os.remove(os.path.join(ROOT_PATH, file_name))

    return {"message": "All saved texts and files have been erased!"}


@app.get("/")
async def health_check():
    return {"status": "API is running!"}