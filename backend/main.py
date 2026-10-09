"""
Api deportiva para conectar los partidos con Flutter
"""


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index() -> dict:
    """
    Pagina principal de la api
    """
    return {"mensaje": "Hola a todos"}


@app.get("/salud")
def salud_de_la_api() -> dict:
    """
    Muestra si la api funciona
    """
    return {"funciona": True}
