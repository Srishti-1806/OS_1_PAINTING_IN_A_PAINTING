python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 7860

#on command prompt type the below command 
#./run.sh 
