import re

# Define token types
KEYWORDS = {
    "if", "else", "while", "for", "return", "int", "float", "char", "void", "break", "continue"
}

OPERATORS = {
    "+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">="
}

SPECIAL_SYMBOLS = {
    "(", ")", "{", "}", ";", ","
}

# Token patterns using regex
TOKEN_REGEX = [
    ("NUMBER", r"\b\d+(\.\d+)?\b"),
    ("IDENTIFIER", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    ("OPERATOR", r"==|!=|<=|>=|[+\-*/=<>]"),
    ("SPECIAL_SYMBOL", r"[(){};,]"),
    ("WHITESPACE", r"\s+"),
    ("UNKNOWN", r".")
]


def lexical_analyzer(code):
    tokens = []
    
    combined_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_REGEX)
    
    for match in re.finditer(combined_regex, code):
        kind = match.lastgroup
        value = match.group()
        
        if kind == "WHITESPACE":
            continue
        
        if kind == "IDENTIFIER" and value in KEYWORDS:
            kind = "KEYWORD"
        
        tokens.append((kind, value))
    
    return tokens


# Example usage
if __name__ == "__main__":
    source_code = """
    int a = 10;
    float b = 20.5;
    if (a < b) {
        return a;
    }
    """
    
    result = lexical_analyzer(source_code)
    
    print("TOKENS:")
    for token in result:
        print(token)