@echo off
rem OLD DESIGN: the saved copy of the live homepage (read-only reference). Serves it at http://localhost:8765 and opens it.
rem Keep this window open while viewing; close it to stop the server.
cd /d "%~dp0"
cd "03-current-site\old-design"
start "" http://localhost:8765/
python -m http.server 8765
