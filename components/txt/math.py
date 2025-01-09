import re

greek_letters = {
    "alpha": r"\alpha",
    "beta": r"\beta",
    "gamma": r"\gamma",
    "delta": r"\delta",
    "epsilon": r"\epsilon",
    "zeta": r"\zeta",
    "eta": r"\eta",
    "theta": r"\theta",
    "iota": r"\iota",
    "kappa": r"\kappa",
    "lambda": r"\lambda",
    "mu": r"\mu",
    "nu": r"\nu",
    "xi": r"\xi",
    "pi": r"\pi",
    "rho": r"\rho",
    "sigma": r"\sigma",
    "tau": r"\tau",
    "upsilon": r"\upsilon",
    "phi": r"\phi",
    "chi": r"\chi",
    "psi": r"\psi",
    "omega": r"\omega",
    "Gamma": r"\Gamma",
    "Delta": r"\Delta",
    "Theta": r"\Theta",
    "Lambda": r"\Lambda",
    "Xi": r"\Xi",
    "Pi": r"\Pi",
    "Sigma": r"\Sigma",
    "Upsilon": r"\Upsilon",
    "Phi": r"\Phi",
    "Psi": r"\Psi",
    "Omega": r"\Omega",
}

math_operators = {
    "sum": r"\sum",
    "int": r"\int",
    "prod": r"\prod",
    "lim": r"\lim",
    "max": r"\max",
    "min": r"\min",
    "inf": r"\inf",
    "frac": r"\frac",
    "log": r"\log",
    "approx": r"\approx",
    "sqrt": r"\sqrt",
}

special_chars = {
    r"\_": "_",
    "[": "{",
    "]": "}",
    "|": "\\",
    r"left{": "left[",
    r"right}": "right]",
}


def math(content: str) -> str:
    replacements = {**greek_letters, **math_operators}

    for word, replacement in replacements.items():
        pattern = r'(?<![a-zA-Z])' + re.escape(word) + r'(?![a-zA-Z])'
        content = re.sub(pattern, lambda _: replacement, content)

    for word, replacement in special_chars.items():
        content = content.replace(word, replacement)

    return f"\\({content}\\)"
