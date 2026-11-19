def saudacao(nome):
    if not isinstance(nome, str):
        return f"Olá, {nome}!"
    limpo = nome.strip()
    if not limpo:
        return "Olá!"
    return f"Olá, {limpo}!"
