def saudacao(nome):
    if not isinstance(nome, str):
        return f"Olá, {nome}!"
    limpo = nome.strip()
    if not limpo:
        return "Olá!"
    return f"Olá, {limpo}!"


def despedida(nome):
    if not isinstance(nome, str):
        return f"Adeus, {nome}!"
    limpo = nome.strip()
    if not limpo:
        return "Adeus!"
    return f"Adeus, {limpo}!"
