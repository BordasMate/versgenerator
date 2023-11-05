from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML_TEMPLATE = """
<!doctype html>
<html lang="hu">
<head>
  <meta charset="utf-8">
  <title>Vers Generátor</title>
  <style>
    .content-container {
      text-align: center;  /* Középre igazítja a címet és a div-et */
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
    .center-div {
      background-color: white;
      border: 1px solid black;
      width: 400px;
      height: 220px;
      color: black;
      text-align: left;
      padding: 20px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      margin-top: 20px;  /* Távolság a cím és a div között */
    }
    body {
      margin: 0;
      height: 100vh;
      background-color: #f0f0f0;  /* Világos háttér a kiemeléshez */
    }
    h1 {
      color: black;
      margin: 0;  /* Eltávolítja a cím alapértelmezett külső margóját */
    }
  </style>
<script>
  let socket = new WebSocket("ws://localhost:8001/ws");
  socket.onmessage = function(event) {
    const versekElem = document.getElementById('versek');
    versekElem.innerHTML += event.data;
    let sorok = versekElem.innerHTML.split("<br>");
    if (sorok.length > 10) {
      sorok = sorok.slice(sorok.length - 10);
      versekElem.innerHTML = sorok.join("<br>");
    }
  };
</script>
</head>
<body>
  <div class="content-container">
    <h1>A párduc</h1>
    <div class="center-div" id="versek"></div>
  </div>
</body>
</html>"""

@app.get("/")
async def get():
    return HTMLResponse(HTML_TEMPLATE)

# Ezt a fájlt egyedül futtatjuk a webserver számára
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
