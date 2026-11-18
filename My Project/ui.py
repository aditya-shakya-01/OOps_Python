from .config import BANK_NAME

def banner(title):
    line="="*60
    print(f"\n{line}\n  {BANK_NAME} | {title}\n{line}")

def ask(prompt):
    return input(f"{prompt} :").strip()


def menu(title,options):
    banner