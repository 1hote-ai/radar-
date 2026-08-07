from fastapi import FastAPI

app = FastAPI(title="Radar API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
