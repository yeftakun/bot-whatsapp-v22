@echo off
setlocal enabledelayedexpansion

set "javascriptFile=hwkal.js"

for /f "tokens=* delims=" %%a in ('type %javascriptFile% ^| findstr /i "global.sessionName"') do (
    set "line=%%a"
    set "line=!line:*global.sessionName=!"
    set "sessionName=!line:~4,-1!"
)

if not defined sessionName (
    echo Variabel global.sessionName tidak ditemukan dalam file JavaScript.
    goto :end
)

set "folderName=!sessionName!"

if exist "!folderName!" (
    rd /s /q "!folderName!"
    echo Folder '!folderName!' berhasil dihapus.
) else (
    echo Folder '!folderName!' tidak ditemukan.
)

:end
endlocal
