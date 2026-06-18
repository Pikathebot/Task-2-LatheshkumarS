# Expense Tracker

A simple command-line Expense Tracker program written in Python that dynamically tracks and accumulates your financial transactions. It runs in a continuous loop and formats the final sum.

## Features

- **Continuous Accumulation**: Prompts for continuous expense entry, adding each amount to a running total initialized outside the loop.
- **Defensive Input Validation**: Catches `ValueError` to handle invalid, non-numeric inputs (like text or symbols) gracefully without crashing.
- **Graceful Shutdown (Kill Switch)**: Breaks the execution loop safely when typing sentinel command values (`quit`, `stop`, or `exit`).
- **Formatted Currency Output**: Prints the final total formatted as currency (e.g. `Final Total: $110.00`) upon exit.
