from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: { "item": "lata", "precoUnitario": 2, "quantidade": 5, "peso": 350, "medida": "ml" },
    2: { "item": "garrafa", "precoUnitario": 6, "quantidade": 15, "peso": 2, "medida": "l" },
    3: { "item": "garrafa", "precoUnitario": 4, "quantidade": 5, "peso": 750, "medida": "ml" },
    4: { "item": "lata mini", "precoUnitario": 0.50, "quantidade": 5, "peso": 200, "medida": "ml" },
}

@app.get("/")
async def home():
    return { "message": "Hello Python" }

@app.get("/vendas")
async def vendasSize():
    return { "length": len(vendas) }

@app.get("/vendas/{id_venda}")
async def getVenda(id_venda: int):
    if id_venda in vendas :
        return vendas[id_venda]
    else:
        return { "message": "ID does not exists!" }