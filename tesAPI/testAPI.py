import json
from fastapi import FastAPI
with open("mahasiswa.json", "r") as read_file: 
    data = json.load(read_file)
app = FastAPI()
@app.get('/mahasiswa/{item_id}')
async def read_mahasiswa(item_id: int):
    for mahasiswa_item in data['mahasiswa']:
        if mahasiswa_item['NIM'] == item_id:
            return mahasiswa_item
    raise HTTPException(
        status_code=404, detail=f'Item not found')