from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API FastAPI rodando via Kong + Minikube"}

@app.get("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(
            dbname="mydb",
            user="myuser",
            password="mypassword",
            host="host.minikube.internal",
            port="5432"
        )
        conn.close()
        return {"status": "Conexão com PostgreSQL OK"}
    except Exception as e:
        return {"status": "Erro", "detail": str(e)}
