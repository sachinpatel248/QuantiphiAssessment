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
1. **`python main.py`** file to start **FastAPI** server and check [http://127.0.0.1:8181](http://127.0.0.1:8181) OR
2. **`python gradio_app.py`** for **Gradio** app and check [http://127.0.0.1:8181](http://127.0.0.1:8182)


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


## Note
1. Have not finished building the fully parameterised app for creating pipelines due to insufficient system RAM. You can adjust all necessary settings in **`env_var_files/.env.local`** to run app as desired. Going forward we can predfined the embedding & llm models, enabling us to utilise different input files to create a new vector database collection for conducting Q&A.
2. Hugging Face embedding model **`all-mpnet-base-v2`**
3. Hugging Face LLM model for QnA **`google/gemma-1.1-2b-it`**
4. Check postman collection to make request
