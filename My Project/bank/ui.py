from .config import BANK_NAME
def ask(prompt):
    return input(f"{prompt} :").strip()

def banner(title):
    print(f"\n{BANK_NAME}")
    