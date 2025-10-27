git remote add origin https://github.com/vitugrey/finance-flow.git
git branch -M main
git push -u origin main


./.venv/bin/uvicorn API.main:app --host 0.0.0.0 --port 8000


