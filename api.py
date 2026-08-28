from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Motor Antifraude API")

class Transacao(BaseModel):
    valor: float
    hora: int
    novo_destinatario: str
    transacoes_ultima_hora: int

@app.get("/")
def raiz():
    return {
        "sistema": "Motor Antifraude",
        "status": "Online",
        "versao": "1.5"
    }

@app.post("/analisar")
def analisar_transacao(transacao: Transacao):
    return {
        "mensagem": "Transação recebida com sucesso na Web!",
        "dados_recebidos": transacao
    }