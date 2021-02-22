from fastapi import FastAPI, Depends
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from ModCalender import ModCalender
from datetime import datetime

app = FastAPI(
    title = 'Calendar Sample',
    description = 'FastAPI Example',
    version = '1.0'
)

templates = Jinja2Templates(directory="templates")
jinja_env = templates.env

def index(request: Request):
    today = datetime.now()
    cal = ModCalender()
    cal = cal.formatyear(2021, 4)

    return templates.TemplateResponse('index.html',
                                    {'request': request,
                                    'calender': cal})

def blank(request: Request, year, month, day):
    return templates.TemplateResponse('blank.html',
                                    {'request': request,
                                     'year': year,
                                    'month': month,
                                    'day': day})
