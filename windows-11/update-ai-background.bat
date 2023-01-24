:loop
curl -o "C:\Users\%USERNAME%\Downloads\ai-background.jpg" http://lape.si:8080/apps/ai-background/combined
reg add "HKCU\Control Panel\Desktop" /v WallPaper /f /t REG_SZ /d "C:\Users\%USERNAME%\Downloads\ai-background.jpg"
RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True
timeout /t 30
goto loop