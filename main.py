from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8001",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def Home():
    return ({
        "status": 404
    })

@app.get("/to1/{r}")
def decimal_to_binary(r):
    return ({"r":bin(r)[2:]})

@app.get("/to2/{r}")
def decimal_to_octal(r):
    return ({"r":oct(r)[2:]})

@app.get("/to3/{r}")
def decimal_to_hexadecimal(r):
    return ({"r":hex(r)[2:].upper()})

@app.post("/fromD")
def from_decimal(decimal_num, target_system):
    if target_system == "binario":
        return decimal_to_binary(decimal_num)
    elif target_system == "octal":
        return decimal_to_octal(decimal_num)
    elif target_system == "hexadecimal":
        return decimal_to_hexadecimal(decimal_num)
    else:
        return "Sistema numérico de destino no válido"

@app.post("/toD")
def to_decimal(num, source_system):
    if source_system == "binario":
        return int(num, 2)
    elif source_system == "octal":
        return int(num, 8)
    elif source_system == "hexadecimal":
        return int(num, 16)
    else:
        return "Sistema numérico de origen no válido"


