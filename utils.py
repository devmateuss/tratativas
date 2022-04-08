import secrets

def create_random_numbers(number: int):
    try:
        random_numbers = secrets.randbits(number)

    except Exception:
        raise TypeError("Erro ao gerar numeros aleatórios")

    return random_numbers

