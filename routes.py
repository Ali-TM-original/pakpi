from fastapi import APIRouter
from pydantic import BaseModel
from datahandler import TextDataHandler
from jsondatahandler import JsonDataHandler

router = APIRouter()


class Data(BaseModel):
    Authorization: str


@router.get("/")
def home():
    return "HELLO WORLD"


@router.get("/chuck")
def chuck():
    obj = TextDataHandler.chuck()
    return {'data': {obj}}


@router.get("/dogfact")
def dog_fact():
    obj = JsonDataHandler.dog_facts()
    return {'data': {obj}}


@router.get("/randomfacts")
def random_facts():
    obj = TextDataHandler
    x = obj.random_facts()
    return {'data': {x}}


@router.get("/yomama")
def yomama():
    obj = JsonDataHandler.yomama()
    return {'data': {obj}}


@router.get("/pickup")
def pickup():
    return {'data': {'name': 'Ali', "age": "28"}}


@router.get("/roast")
def roasts():
    obj = TextDataHandler
    x = obj.random_roasts()
    return {'data': {x}}


@router.get("/jokes")
def jokes():
    obj = JsonDataHandler.stupid()
    return {'data': {obj}}


@router.get("/catfacts")
def cat_facts():
    obj = JsonDataHandler.cat_facts()
    return {'data': {obj}}
