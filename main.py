from fastapi import FastAPI

app = FastAPI()

medicamentos = [
    {
        "id": 1,
        "nombre": "Aspirina",
        "dosis": "1 mg",
        "unidad": "mg",
        "precio": "100",
        "descripcion": "Este medicamento es para tratar la fiebre y la tos.",
        "categoria": "Antiinflamatorios",
        "imagen": "https://www.medicamentosalud.com/wp-content/uploads/2020/03/aspirina.jpg",
    },
    {
        "id": 2,
        "nombre": "Ibuprofeno",
        "dosis": "1 mg",
        "unidad": "mg",
        "precio": "100",
        "descripcion": "Este medicamento es para tratar la fiebre y la tos.",
        "categoria": "Antiinflamatorios",
        "imagen": "https://www.medicamentosalud.com/wp-content/uploads/2020/03/ibuprofeno.jpg",
    },
    {
        "id": 3,
        "nombre": "Levofloxacino",
        "dosis": "1 mg",
        "unidad": "mg",
        "precio": "100",
        "descripcion": "Este medicamento es para tratar la fiebre y la tos.",
        "categoria": "Antiinflamatorios",
        "imagen": "https://www.medicamentosalud.com/wp-content/uploads/2020/03/levofloxacino.jpg",
    },
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/medicamentos")
def read_medicamentos():
    return {"medicamentos": medicamentos}


   