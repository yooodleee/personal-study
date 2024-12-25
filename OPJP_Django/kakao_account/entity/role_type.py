from django.db import models


# RoleType 테이블을 살펴봅시다.
# 살짝 이상한 부분이 있지만 우선 Account 테이블에서 RoleType 테이블 정보를 참조(Foreignkey)한 것으로 보아 
# 필요한 정보가 있는 것 같습니다.
# 처음부터 각각 관리자(ADMIN), 일반 사용자?(고객인 것 같군요), 구독권(SUBSCRIBE)를 테이블에 담아줍니다.
# 이 정보들이 왜 필요해서 테이블에 담게 되는 건지는 Account 테이블로 이동해서 자세하게 살펴보도록 하겠습니다.
class RoleType(models.TextChoices):
    ADMIN = 'ADMIN'
    NORMAL = 'NORMAL'
    SUBSCRIBE = 'SUBSCRIBE'