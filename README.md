dotfiles
========

Don't use these.Don't use these.Don't use these.Don't use these.

#### Install:

```console
$ make install
$ # optional
$ make osx
```
This will create symlinks in your home directory back to this repository.

#### Windows

General philosophy is to have as little intermingling between CMD and Git Bash as possible, and to default to Windows-y ways of doing things over Unix.

**scoop.bat** contains the minimum list of things to `scoop install`. Run this after installing scoop via the directions at [scoop.sh](https://scoop.sh). In theory, this is safe to run more than once, but it's slow.

**windows.bat** uses Robocopy to place app configuration files in the correct location for GUI apps. It does not set up CLI-only things (e.g. SSH). This is same to run more than once, and should be ran after `scoop.bat`.

**wsl.bat** sets up WSL. Run this as _Administrator_ before installing Docker.

Docker must be installed from their site (Docker Desktop), not scoop. It will likely require reboots.
