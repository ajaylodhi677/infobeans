from rich.console import Console
# # print("[bold green]Hello[/bold green]")
# # print("[bold yellow]Hello python[/bold yellow]")
# # console=Console()
# # console.print("[bold red]Hello [/bold red]")
# # console.print("[bold italic blue]Python is awesome[/bold italic blue]")
# # console.print("[bold green]Name:Ajay[/bold green] [bold Yellow]Age:22[/bold yellow]")
# # from rich.console import Console
# # from rich.table import Table
# # from rich.panel import Panel

# # console = Console()

# # table = Table(title="Student Details")

# # table.add_column("Name")
# # table.add_column("Age")
# # table.add_column("Course")
# # table.add_column("Marks")

# # table.add_row("Ajay", "22", "Python", "85")
# # table.add_row("Rahul", "23", "Java", "78")
# # table.add_row("Neha", "21", "SQL", "91")

# # console.print(table)
# # print()
console=Console()
from rich.panel import Panel
panel=Panel("hello")
console.print(panel)
import winsound
winsound.Beep(1000,500000)
print(__name__)
#if __name__ == "__main__":
    #print("Demo2 is running directly")