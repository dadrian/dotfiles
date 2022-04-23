@ECHO OFF
REM Copy nvim files into the nvim folder, excluding the plugged folder
ROBOCOPY %~dp0nvim\nvim %UserProfile%\AppData\Local\nvim /E /XD %UserProfile%\AppData\Local\nvim\plugged
ROBOCOPY %~dp0vc %UserProfile%\bin vcvarsall.bat
ROBOCOPY %~dp0vscode\user %UserProfile%\scoop\apps\vscode\current\data\user-data\User settings.json