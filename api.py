from fastapi import FastAPI
from pydantic import BaseModel
from services import DetectorFraude

app = FastAPI(title="Motor Antifraude API")
detector = DetectorFraude()
historico_analises = []

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
        "versao": "1.6"
    }

@app.post("/analisar")
def analisar_transacao(transacao: Transacao):
    risco, motivos = detector.calcular_risco(transacao)
    classificacao = detector.classificar_risco(risco)

    resultado_para_historico = {
        "valor_transferido": transacao.valor,
        "risco_calculado": risco,
        "status": classificacao
    }

    historico_analises.append(resultado_para_historico)

    return {
        "risco_pontuacao": risco,
        "classificacao": classificacao,
        "motivos": motivos     
    }

@app.get("/historico")
def ver_historico():
    return {
        "total_analises": len(historico_analises),
        "historico": historico_analises
    }