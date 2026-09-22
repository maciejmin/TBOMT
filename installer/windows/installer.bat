cls
@echo off
echo Instalacja TBOMT, poczekaj to może potrwać do kilku minut na starszych urządzeniach. W tym czasie zainstalujemy zależności i uruchomimy grę automatycznie!
winget install python3
curl -O "https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/program.py"
python program.py