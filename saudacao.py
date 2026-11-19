def saudacao(nome):
    limpo = nome.strip()
    if not limpo:
        return "Olá!"
    return f"Olá, {limpo}!"
