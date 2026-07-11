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

def decimal_to_binary(r):
    return bin(r)[2:]


def decimal_to_octal(r):
    return  oct(r)[2:]

def decimal_to_hexadecimal(r):
    return hex(r)[2:].upper()

@app.get("/fromD/{decimal_num}/{target_system}")
def from_decimal(decimal_num, target_system):
    if target_system == "binario":
        return ({"r": decimal_to_binary(decimal_num)})
    elif target_system == "octal":
        return ({"r": decimal_to_octal(decimal_num)})
    elif target_system == "hexadecimal":
        return ({"r": decimal_to_hexadecimal(decimal_num)})
    else:
        return ({"r": "Sistema numérico de destino no válido"})

@app.get("/toD{num}/{source_system})
def to_decimal(num, source_system):
    if source_system == "binario":
        return ({"r": int(num, 2)})
    elif source_system == "octal":
        return ({"r": int(num, 8)})
    elif source_system == "hexadecimal":
        return ({"r": int(num, 16)})
    else:
        return ({"r": "Sistema numerico de destino no valido"})

