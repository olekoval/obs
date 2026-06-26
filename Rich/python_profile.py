try:
    from rich import pretty, inspect
    from rich import print as rprint
    
    pretty.install()
    print("✨ Rich успішно інтегровано в REPL!")
except ImportError:
    pass