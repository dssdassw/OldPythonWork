@echo off
:while
set /p filetorun=Enter the name of the file you want to run: %=%
if %filetorun%==exit goto end
python "%filetorun%"
pause
goto while
:end
pause