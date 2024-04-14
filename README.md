# QuantiphiAssessment

## Colab Notebook for quick testing [Colab: QA-RAG Pipeline](https://colab.research.google.com/drive/1M3qIodbAFiMqdQcuORo7GmTi-w-gHo0w)


## API & Gradio setup for different environments


### 1. Local

For development in local using VS code. Run below commands. This will create virtual environment, activate it, install packages

> Prerequisites - Python 3.12.2, pip

<table>
<tr>
<th> Windows </th>
<th> Mac/Linux </th>
</tr>
<tr>
<td>

```
python -m venv env
.\env\Scripts\activate
pip install -r .\requirements.txt
```
</td>

<td>
  
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
</td>
</tr>
</table>

Now run 
1. **`python main.py`** file to start **FastAPI** server. OR
2. **`python gradio_app.py`** for **Gradio** app


### 2. Using docker on WINDOWS
From **`root`** directory run below command for fastapi server

```
docker-compose -f docker-compose-local.yml --env-file env_var_files/.env.local up -d
```

**NOTE:** From `Dockerfile` - Commnent & Uncomment below code to switch **FastAPI** with **Gradio** App
```
EXPOSE ${PORT}
CMD  uvicorn main:app --host ${HOST} --port ${PORT}

# EXPOSE ${GRADIOPORT}
# CMD python gradio_app.py
```
