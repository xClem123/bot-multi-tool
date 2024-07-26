@echo off

echo Nous installons les modules necessaires cela prend environ 1 a 2 minutes.


pip install -r requirements.txt

echo Nous avons bien reussi a tout installer. Veuillez lancer start.bat.

timeout /t 5 >nul

exit
