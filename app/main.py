from fastapi import FastAPI, File, UploadFile
import httpx

app = FastAPI(title="Voice Command API")

@app.post("/voice-command/")
async def handle_voice_command(file: UploadFile = File(...)):
    audio_data = await file.read()
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.baidu.com/api/v1/voice_to_text",
            files={"file": audio_data},
            headers={"Authorization": "Bearer your_access_token"}
        )
        text = response.json().get("text", "")

    return {"command": text, "status": "Processed"}