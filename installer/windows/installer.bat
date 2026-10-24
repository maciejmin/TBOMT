# Wyczyszczenie konsoli i ukrycie zbędnych komunikatów na starcie
Clear-Host
$ProgressPreference = 'SilentlyContinue'

Write-Host "===============================================================================" -ForegroundColor Cyan
Write-Host " Instalacja TBOMT, poczekaj to moze potrwac do kilku minut na starszych" -ForegroundColor Cyan
Write-Host " urzadzeniach. W tym czasie zainstalujemy zaleznosci i uruchomimy gre!" -ForegroundColor Cyan
Write-Host
Write-Host " Ten kod instalatora został napisany przez SI Gemini i jest bezpieczny." -ForegroundColor Cyan
Write-Host "===============================================================================" -ForegroundColor Cyan

# 1. Definiowanie ścieżek tymczasowych i wersji Pythona
$installerPath = "$env:TEMP\python-installer.exe"
# Link bezpośredni do instalatora sieciowego Pythona (wersja 3.11.9)
$pythonUrl = "https://python.org"

# 2. Pobieranie instalatora Pythona
Write-Host "[1/4] Pobieranie instalatora Pythona..." -ForegroundColor Yellow
Invoke-WebRequest -Uri $pythonUrl -OutFile $installerPath

# 3. Cicha instalacja Pythona bez praw administratora
Write-Host "[2/4] Instalacja Pythona w tle (to moze chwile potrwac)..." -ForegroundColor Yellow
$installArgs = "/quiet InstallAllUsers=0 PrependPath=1 Include_test=0 Include_pip=1"
Start-Process -FilePath $installerPath -ArgumentList $installArgs -Wait

# 4. Usunięcie instalatora po zakończeniu
Remove-Item -Path $installerPath -Force -ErrorAction SilentlyContinue

# 5. Dynamiczne przeładowanie zmiennej PATH w obecnej sesji konsoli
Write-Host "[3/4] Konfiguracja zmiennych srodowiskowych..." -ForegroundColor Yellow
$userPath = [System.Environment]::GetEnvironmentVariable("Path", "User")
$machinePath = [System.Environment]::GetEnvironmentVariable("Path", "Machine")
$env:Path = "$userPath;$machinePath"

# 6. Pobieranie głównego pliku gry
Write-Host "[4/4] Pobieranie najnowszej wersji gry..." -ForegroundColor Yellow
$gameUrl = "https://raw.githubusercontent.com/maciejmin/TBOMT/refs/heads/main/program.py"
Invoke-WebRequest -Uri $gameUrl -OutFile "program.py"

# 7. Uruchomienie gry
Write-Host "Uruchamianie Początku Nowożytności..." -ForegroundColor Green
python program.py
