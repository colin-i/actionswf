@{' 2>nul&::'={\"<<BATCH_SCRIPT 2>/dev/null;#"}}[0]<#
@ECHO OFF
REM ===== Batch Script Begin =====
ECHO Batch detected. The script can run in /bin/sh. Exiting...
GOTO :eof
REM ====== Batch Script End ======
TYPE CON >NUL
BATCH_SCRIPT
#>

echo \" <<'POWERSHELL_SCRIPT' >/dev/null # " | Out-Null
# ===== PowerShell Script Begin =====
echo "PowerShell detected. The script can run in /bin/sh. Exiting..."
return
# ====== PowerShell Script End ======
<#
POWERSHELL_SCRIPT
#>

`dirname $0`/oaalternative.sh "$@"
