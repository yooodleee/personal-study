"""
Python pydantic이란?


1) 파이썬의 type annotation을 활용해서 data validation(검증)과
    setting 관리를 해주는 라이브러리.
2) runtime에 type hint를 적용하고 데이터가 invalid할 때 친숙한
    오류를 제공한다.
"""

from pydantic import BaseModel


class OpenaiApiRequestForm(BaseModel):
    userSendMessage: str    # str(문자열)-> type hint
    