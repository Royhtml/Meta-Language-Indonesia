@echo off
echo Menginstall package %1 untuk bahasa Meta...
@echo off
if "%1"=="install" (
    shift
    call %~dp0meta_install.bat %*
) else (
    set PYTHONPATH=%~dp0..\Lib
    python %~dp0..\Lib\meta_runner.py %*
)
echo Selesai.