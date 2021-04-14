@ECHO OFF
REM Copy nvim files into the nvim folder, excluding the plugged folder
ROBOCOPY %~dp0nvim\nvim %UserProfile%\AppData\Local\nvim /E /XD %UserProfile%\AppData\Local\nvim\plugged
