# 웹 크롤링 예시입니다. 크롤링 코드 작성 시 참고하세요!!

# Selenium을 사용해서 웹 자동화를 위해 크롬 웹 드라이버를 설치해야합니다.

# 기존 셀레니움 웹 드라이버 모듈 임포트
from selenium import webdriver
# 기존 셀레니움 웹 드라이버 by 모듈 임포트
from selenium.webdriver.common.by import By 

# 세션 시작 ()에 기존에는 투트가 필요합니다.
driver = webdriver.Chrome()
# 암시적 대기 전략 수립(2초를 기다립니다.)
driver.implicitly_wait(2)

# 웹 페이지로 이동합니다.
driver.get('https://crawlingstudy-dd3c9.web.app/03/')

# 웹 드라이버에서 'ul.lst_major li' 태그들을 리스트 형태로 반환합니다.
# By로 지정한 찾아올 태그의 형식이 CSS_SELECTOR라는 것입니다.
li_tags = driver.find_elements(By.CSS_SELECTOR, 'ul.lst_major li')

# 밑에 반복문에서 li 태그들을 리스트로 담습니다.
major_list = []

for li in li_tags:
    # a_tag-> 'a'라는 태그를 리스트 형태로 반환합니다.
    a_tag = li.find_element(By.CSS_SELECTOR, 'a').text 
    # span_tag-> 'span'이라는 태그를 리스트 형태로 반환합니다.
    # replace-> ,(콤마)를 없앱니다.
    span_tag = li.find_element(By.CSS_SELECTOR, 'span').text.replace(',', '')
    # 반복문에서 리스트 형태로 반환했던 a_tag와 span 태그를 major_list에 추가합니다.
    major_list.append([a_tag, span_tag])

print(major_list)
# major_list의 길이를 출력합니다.
print(len(major_list))

# 웹 드라이버를 종료합니다.
driver.quit()