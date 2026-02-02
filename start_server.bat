@echo off
echo Starting Local VR Server...
echo Please open your browser to: http://localhost:8000/vr-tour.html
python -m http.server 8000
pause
