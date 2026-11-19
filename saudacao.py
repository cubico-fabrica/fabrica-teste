import re


def _maiuscula_inicial(texto):
    return re.sub(r"(?<!\S)\S", lambda m: m.group().upper(), texto)


def saudacao(nome):
    if not isinstance(nome, str):
        return f"Olá, {nome}!"
    limpo = nome.strip()
    if not limpo:
        return "Olá!"
    return f"Olá, {_maiuscula_inicial(limpo)}!"
