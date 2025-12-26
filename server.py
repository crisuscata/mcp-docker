from mcp.server.fastmcp import FastMCP
import random

# Inicializamos el servidor con un nombre identificativo
mcp = FastMCP("d12-server")

@mcp.tool()
def roll_d12() -> int:
    """
    Lanza un dado de 12 caras (D12).
    Utiliza esta herramienta cuando necesites un número aleatorio entre 1 y 12,
    o para tomar decisiones de azar en juegos y escenarios de rol.
    """
    result = random.randint(1, 12)
    return result

# Punto de entrada para que Docker lo ejecute
if __name__ == "__main__":
    mcp.run()