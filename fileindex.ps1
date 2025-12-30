# fileindex - Fast local file indexing and search tool
# Entry point for Windows PowerShell systems

param(
    [Parameter(ValueFromRemainingArguments=$true)]
    $args
)

python -m fileindex.main @args
