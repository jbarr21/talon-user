import logging
import os
import re
import subprocess
import sys

from talon import Context, Module, actions, app, ui
from talon.debug import log_exception

mod = Module()

ctx = Context()

# note: this context match is intentionally made more complex so that it is more specific
# than the context defined in apps/win/windows_terminal/windows_terminal.py (and thereby
# takes precedence).
ctx.matches = rf"""
user.running: aerospace
"""

def aerospace(command: str):
    """Run a bash command using aerospace CLI"""
    print(f"Running aerospace command: {command}")
    try:
        result = subprocess.run(
            ["/opt/homebrew/bin/aerospace"] + command.split(),
            capture_output=True,
            text=True,
            check=True
        )
        if result.returncode != 0:
            raise AssertionError(f"Failed with exist code {result.returncode} when running: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Aerospace command failed: {e}")

@mod.action_class
class Actions:
    def aerospace_workspace(label: str):
        """Switch to aerospace workspace by label"""
        print(f"Switching to aerospace workspace {label.upper()}")
        aerospace(f"workspace {label.upper()}")

