@echo off
set PATH_BACKUP=%PATH%
set INCLUDE_BACKUP=%INCLUDE%
set "PATH=c:\Program Files\Geosoft\Desktop Applications 9\bin;%PATH%"
set "INCLUDE=%CD%\include;%INCLUDE%" 
ninja
set PATH=%PATH_BACKUP%
set INCLUDE=%INCLUDE_BACKUP%
set PATH_BACKUP=
set INCLUDE_BACKUP=