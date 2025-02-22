from fastapi import FastAPI
import uvicorn
from utils import setup_logger, ConfigManager
from routers import root, post_router, get_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="/ArtMaker_StyleGan_Tensorflow/src/web/static"), name="static")

app.include_router(root)
app.include_router(post_router)
app.include_router(get_router)

async def startup_event():
    ini_path = "/ArtMaker_StyleGan_Tensorflow/src/config.ini"
    config = ConfigManager(ini_path)
    ini_dict = config.get_config_dict()
    logger = setup_logger(ini_dict)
    
    logger.info("DASHBOARD STARTED")

    app.state.logger = logger
    app.state.ini_dict = ini_dict

app.on_event("startup")(startup_event)
