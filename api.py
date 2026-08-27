from fastapi import FastAPI

app = FastAPI(title="Motor Antifraude API")

@app.get("/")
def raiz():
    return {
        "sistema": "Motor Antifraude",
        "status": "Online",
        "versao": "1.4"
    }