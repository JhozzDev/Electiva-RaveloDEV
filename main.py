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

@app.get("/calculate/{r}")
def Numbers(r: int):
    data = 0
    if r == 1:
       data = 1
    else: 
        data =2
    return {data}



def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]

def decimal_to_octal(decimal_num):
    return oct(decimal_num)[2:]

def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num)[2:].upper()

def from_decimal(decimal_num, target_system):
    if target_system == "binario":
        return decimal_to_binary(decimal_num)
    elif target_system == "octal":
        return decimal_to_octal(decimal_num)
    elif target_system == "hexadecimal":
        return decimal_to_hexadecimal(decimal_num)
    else:
        return "Sistema numérico de destino no válido"

def to_decimal(num, source_system):
    if source_system == "binario":
        return int(num, 2)
    elif source_system == "octal":
        return int(num, 8)
    elif source_system == "hexadecimal":
        return int(num, 16)
    else:
        return "Sistema numérico de origen no válido"


