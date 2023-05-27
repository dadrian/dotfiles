Copy-Item .\PowerShell\Profile.ps1 $profile
ROBOCOPY ${PSScriptRoot}\nvim\nvim $HOME\AppData\Local\nvim /E /XD $HOME\AppData\Local\nvim\plugged
ROBOCOPY ${PSScriptRoot}\vc $HOME\bin vcvarsall.bat
ROBOCOPY ${PSScriptRoot}\vscode\user $HOME\scoop\apps\vscode\current\data\user-data\User settings.json

