import subprocess
import sys

from typing import List

from rich.console import Console
from rich.panel import Panel

console = Console()

def run_with_rich(commands: List[str], timeout: float | None = None, cwd: str | None = None):
    commands_list = " ".join(commands) 


    console.print(Panel(
        f'[bold cyan]{commands_list}[/bold cyan]',
        title='[bold green]Subrunner: Executing Command[/bold green]',
        border_style='blue',
        expand=False
    ))

    try:
        process = subprocess.Popen(
            commands,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            cwd=cwd
        )

        if process.stdout:
            for line in process.stdout:
                sys.stdout.write(line)
                sys.stdout.flush()

        if process.stderr:
                for line in process.stderr:
                    console.print(f'[red]{line.rstrip()}[/red]')

        returncode = process.wait(timeout=timeout)

        if returncode == 0:
            console.print('\n[bold green]✔ Command executed successfully![/bold green]')
        else:
            console.print(f'\n[bold red]✖ Command failed with exit code {returncode}[/bold red]')

        return returncode
    
    except subprocess.TimeoutExpired:
        process.kill()
        console.print(f'\n[bold red]✖ Error: Command timed out after {timeout} seconds.[/bold red]')
        return -1
    except Exception as e:
        console.print(f'\n[bold red]✖ Unexpected error: {e}[/bold red]')
        return -1

