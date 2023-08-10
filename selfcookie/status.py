from rich.console import Console

console = Console()


def print_success(message: str) -> None:
    """Print a success message to the console"""
    console.print(f"[green]:heavy_check_mark:[/green] {message}")
