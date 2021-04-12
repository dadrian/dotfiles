@echo off

REM The actual script is likely in: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build

SET COMMUNITY2019="C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build"

IF EXIST %COMMUNITY2019% %COMMUNITY2019%\vcvarsall.bat x64
