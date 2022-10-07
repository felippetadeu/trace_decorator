import uvicorn
from src.api.api import API
from src.configuration import Configuration

if __name__=="__main__":
    app: API = Configuration.start_app()

    Configuration.start_apm(__name__)
    uvicorn.run(app.web_application)