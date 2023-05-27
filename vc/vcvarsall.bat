@echo off
REM The actual script is likely in: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build

SET BUILDTOOLS2022="C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build"
SET COMMUNITY2019="C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build"
SET COMMUNITY2022="C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build"

SET VCDIR=%BUILDTOOLS2022%

IF EXIST %VCDIR% %VCDIR%\vcvarsall.bat x64
