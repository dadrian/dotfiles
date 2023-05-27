<#
.SYNOPSIS
    Invokes the specified batch file and retains any environment variable changes it makes.
.DESCRIPTION
    Invoke the specified batch file (and parameters), but also propagate any
    environment variable changes back to the PowerShell environment that
    called it.
.PARAMETER Path
    Path to a .bat or .cmd file.
.PARAMETER Parameters
    Parameters to pass to the batch file.
.EXAMPLE
    C:\PS> Invoke-BatchFile "$env:ProgramFiles\Microsoft Visual Studio 9.0\VC\vcvarsall.bat"
    Invokes the vcvarsall.bat file. All environment variable changes it makes will be
    propagated to the current PowerShell session.
.NOTES
    Author: Lee Holmes

    Copied from PSCX
#>
function Invoke-BatchFile
{
    param([string]$Path, [string]$Parameters)

    $tempFile = [IO.Path]::GetTempFileName()

    ## Store the output of cmd.exe. We also ask cmd.exe to output
    ## the environment table after the batch file completes
    cmd.exe /c " `"$Path`" $Parameters && set " > $tempFile

    ## Go through the environment variables in the temp file.
    ## For each of them, set the variable in our local environment.
    Get-Content $tempFile | Foreach-Object {
        if ($_ -match "^(.*?)=(.*)$") {
            Set-Content "env:\$($matches[1])" $matches[2]
        }
        else {
            $_
        }
    }

    Remove-Item $tempFile
}

function Initialize-VC
{
    param([string]$Parameters)


    $BuildTools2019 = "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build"
    $BuildTools2022 = "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build"

    $Community2019 = "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build"
    $Community2022 = "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build"

    if (Test-Path -Path $Community2022) {
        $VCDIR = $Community2022
    } elseif (Test-Path -Path $Community2019) {
        $VCDIR = $Community2019
    } elseif (Test-Path -Path $BuildTools2022) {
        $VCDIR = $BuildTools2022
    } elseif (Test-Path -Path $BuildTools2019) {
        $VCDIR = $BuildTools2019
    } else {
        Write-Error "Unable to find Visual Studio"
        Return
    }

    if (!($Parameters)) {
        $Parameters = "x64"
    }

    Write-Host "Using $VCDIR"
    Write-Host "Using $Parameters"
    Invoke-BatchFile $VCDIR\vcvarsall.bat $Parameters
}
