from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import random

app = FastAPI()

vers_sorok = [
    "Szeme a rácsok futásába veszve kimerült.",
    "Már semmit se lát.",
    "Ezernyi rács mögött nincsen világ.",
    "Puha lépte acéllá tömörül.",
    "A legparányibb körbe fogva jár.",
    "Az erő tánca egy pont körűl.",
    "A körben egy ájult, nagy akarat áll.",
    "Néha felfut a pupilla néma függönye.",
    "Egy kép beszökik, átvillan a feszült tagokon.",
    "A kép a szívbe ér, és ott megszűnik."
]

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            sor = random.choice(vers_sorok)
            for betu in sor:
                await websocket.send_text(betu)
                await asyncio.sleep(0.05)  # Késleltetés minden betű között
            await websocket.send_text('<br>')
            await asyncio.sleep(0.1)  # Késleltetés a sorok között
    except WebSocketDisconnect:
        print("A kliens kapcsolatot bontott.")

# Ezt a fájlt egyedül futtatjuk a versgenerátor szerver számára
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001)
