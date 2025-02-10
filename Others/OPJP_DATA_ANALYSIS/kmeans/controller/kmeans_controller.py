import os, sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from kmeans.service.kmeans_service_impl import KMeansServiceImpl


kMenasRouter = APIRouter()

async def injectKMeansService() -> KMeansServiceImpl:
    return KMeansServiceImpl()

@kMenasRouter.post("/kmeans-game")
async def requestKMneas(
    kMeansService: KMeansServiceImpl = Depends(injectKMeansService)
):
    
    kMeansResponse = await kMeansService.requestProcess()

    return kMeansResponse