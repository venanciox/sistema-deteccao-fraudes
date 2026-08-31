import json
import os
from fastapi import FastAPI
from pydantic import BaseModel, Field
from services import DetectorFraude

app = FastAPI(title="Motor Antifraude API")
detector = DetectorFraude()

arquivo_dados = "banco_historico.json"

if os.path.exists(arquivo_dados):
    with open(arquivo_dados, "r", encoding="utf-8") as arquivo:
        historico_analises = json.load(arquivo)
else:
    historico_analises = []

class Transacao(BaseModel):
    valor: float = Field(gt=0)
    hora: int = Field(ge=0, le=23)
    novo_destinatario: str = Field(pattern="^(s|n|S|N)$")
    transacoes_ultima_hora: int = Field(ge=0)

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
        "status": classificacao,
        "motivos": motivos
    }

    historico_analises.append(resultado_para_historico)

    with open(arquivo_dados, "w", encoding="utf-8") as arquivo:
        json.dump(historico_analises, arquivo, indent=4, ensure_ascii=False)

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