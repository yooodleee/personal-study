import os.path
from fastapi.middleware.cors import CORSMiddleware


import colorama


import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI


from deep_learning.controller.deep_learning_controller import deepLearningRouter
from dice.controller.dice_controller import diceResultRouter
from system_initializer.init import SystemInitializer
from task_manager.manager import TaskManager
from include.socket_server.socket_server.initializer.init_domain import DomainInitializer



DomainInitializer.initEachDomain()      # 각 도메인 초기화
SystemInitializer.initSystemDomain()    # 시스테 도메인 초기화

app = FastAPI()

load_dotenv()


# ALLOWED_ORIGINS에 정의된 정보들을 ,(쉼표)를 제거하고 가져옴.
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")


# app에 middelware에 대해 등록할 정보를 추가함.
app.add_middleware( 
    CORSMiddleware,         # CORSMiddleware 추가
    allow_origins=origins,  # allow_origins 추가
    allow_credentials=True, # allow_credentials 추가
    allow_methods=["*"],    # allow_methods 추가
    allow_headers=["*"],    # allow_headers 추가
)

# router들을 등록한다.
app.include_router(deepLearningRouter)
app.include_router(diceResultRouter)


# 실행되는 파일(이 파일 이름이 main이라면) 의심의 여지 없이
# 아래 구문을 적용한다.
if __name__ == "__main__":
    colorama.init(autoreset=True)   # print문에 색을 입혀준다.

    TaskManager.createSocketServer()
    uvicorn.run(    # uvicorn으로 app을 실행하고 post, port를 지정해준다.
        app, 
        host=os.getenv('HOST'), 
        port=int(os.getenv('FASTAPI_PORT'))
    )
