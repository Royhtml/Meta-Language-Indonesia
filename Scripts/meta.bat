@echo off
title Meta Language Interpreter

REM ============================================================================
REM META LANGUAGE V1.0
REM ============================================================================

REM Cek perintah install
if "%1"=="install" (
    echo Installing Python packages...
    pip install %2 %3 %4 %5 %6 %7 %8 %9
    if errorlevel 1 (
        echo [ERROR] Gagal install package
        pause
        exit /b 1
    )
    echo [SUCCESS] Package berhasil diinstall
    goto :eof
)

REM Cek apakah ada argumen
if "%1"=="" (
    call :show_help
    goto :eof
)

REM Dapatkan direktori script
set "SCRIPT_DIR=%~dp0"
set "META_RUNNER=%SCRIPT_DIR%..\Lib\meta_runner.py"

REM Cek apakah meta_runner.py ada
if not exist "%META_RUNNER%" (
    echo [ERROR] File meta_runner.py tidak ditemukan!
    echo Lokasi: %META_RUNNER%
    echo.
    echo Pastikan struktur direktori:
    echo   ^<root^>\
    echo     ├─ bin\
    echo     │   └─ meta.bat
    echo     └─ Lib\
    echo         └─ meta_runner.py
    echo.
    pause
    exit /b 1
)

REM Cek apakah Python terinstall
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python tidak ditemukan!
    echo.
    echo Silakan install Python dari https://www.python.org/downloads/
    echo Pastikan "Add Python to PATH" dicentang saat install
    echo.
    pause
    exit /b 1
)

REM Tampilkan informasi jika debug mode
if "%1"=="--debug" (
    echo.
    echo ================================================================================
    echo                      META LANGUAGE INTERPRETER v3.1 - DEBUG MODE
    echo ================================================================================
    echo.
    echo [INFO] Menjalankan debug mode...
    echo [INFO] File: %2
    echo [INFO] Meta Runner: %META_RUNNER%
    echo.
)

REM Jalankan interpreter dengan semua argumen
python "%META_RUNNER%" %*

REM Cek error level
if errorlevel 1 (
    echo.
    echo ================================================================================
    echo [ERROR] Program gagal dijalankan
    echo ================================================================================
    echo.
    echo Tips:
    echo   1. Cek apakah file .meta ada
    echo   2. Cek sintaks program Anda
    echo   3. Gunakan 'meta --debug file.meta' untuk melihat detail
    echo.
    if "%1"=="--debug" (
        pause
    )
    exit /b 1
)

if "%1"=="--debug" (
    echo.
    echo ================================================================================
    echo [SUCCESS] Debug mode selesai
    echo ================================================================================
    echo.
    if "%2"=="" (
        pause
    )
)

goto :eof

:show_help
echo.
echo ================================================================================
echo                         META LANGUAGE INTERPRETER v1.0
echo ================================================================================
echo.
echo PENGGUNAAN:
echo   meta ^<file.meta^> [argumen...]     - Menjalankan program
echo   meta --debug ^<file.meta^>          - Menjalankan dengan debug mode
echo   meta --help                         - Menampilkan bantuan ini
echo   meta install ^<package^>            - Install package Python
echo.
echo CONTOH:
echo   meta program.meta
echo   meta program.meta arg1 arg2
echo   meta --debug salah.meta
echo   meta install requests
echo.
echo DEBUG MODE:
echo   Mode debug akan menampilkan:
echo   - Hasil konversi Meta ke Python per baris
echo   - Kode Python lengkap hasil konversi
echo   - Error detail dengan lokasi yang tepat
echo.
echo STRUCTUR DIREKTORI:
echo   ^<root^>\
echo     ├─ bin\
echo     │   └─ meta.bat         (file ini)
echo     └─ Lib\
echo         └─ meta_runner.py   (interpreter utama)
echo.
echo ================================================================================
pause
goto :eof