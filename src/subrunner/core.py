import subprocess
import shutil

from typing import List
from dataclasses import dataclass

from .ui import run_with_rich
from .exceptions import CommandNotFoundError

@dataclass(frozen=True)
class CommandResult:
    returncode: int
    stdout: str
    stderr: str

class CommandRunner:
    """A lightweight and modern wrapper around the built-in 'subprocess' module

    designed to execute external CLI utilities with optional Rich logging support."""
    def __init__(self, core_commamd):
        self.core_command = core_commamd

    def run(
        self,
        commands: List[str],
        timeout: float | None = None,
        cwd: str | None = None,
        rich: bool = False,
    ) -> CommandResult:
        """Executes the core command with the provided arguments.

        Args:
            commands (List[str]): A list of command arguments to pass to the core utility.
            timeout (float | None, optional): Maximum time in seconds to wait for the process to complete.
                Defaults to None.
            cwd (str | None, optional): Working directory where the command should be executed.
                Defaults to None.
            rich (bool, optional): If True, streams the output in real-time using Rich formatting.
                Defaults to False.

        Returns:
            CommandResult: An object containing the return code, standard output, and standard error.

        Raises:
            CommandNotFoundError: If the core command executable is not found in the system PATH."""
        if not shutil.which(self.core_command):
            raise CommandNotFoundError(f'Command {self.core_command} not founded in system!')

        if rich:
            returncode = run_with_rich(
                [self.core_command] + commands,
                timeout=timeout
            )

            return CommandResult(returncode=returncode, stdout="", stderr="")
        else:
            result = subprocess.run(
                [self.core_command] + commands,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=cwd
            )

            return CommandResult(
                returncode=result.returncode,
                stdout=result.stdout,
                stderr=result.stderr,
            )

