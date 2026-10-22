@echo off
rem NEW DESIGN: the working copy we redesign. Serves it at http://localhost:8770 and opens it.
rem Keep this window open while viewing; close it to stop the server.
cd /d "%~dp0"
cd "05-design\new-design"
start "" http://localhost:8770/
python -m http.server 8770
