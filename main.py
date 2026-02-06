from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI()


@app.get("/current-time")
def get_current_time():
    now = datetime.now(timezone.utc)
    return {"current_time": now.isoformat()}
