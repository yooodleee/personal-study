import os
import fitz # PyMUPDF
from tqdm import tqdm
from PyPDF2 import PdfFileReader, PdfFileWriter


# pdf 파일 불러오기
pdfReader = PdfFileReader("[CJ ENM]사업보고서(2025.03.19).pdf", "rb")

# 새로 만들 pdf 객체 생성
pdfWriter = PdfFileWriter()

# 기존의 1번 페이지를 가져와서 새로 만든 pdf에 붙여 넣기
pdfWriter.add_page(pdfReader.pages[1])

# 1번 페이지가 붙여진 새로운 pdf 파일을 현재 경로에 원하는 이름으로 저장
pdfWriter.write(open("./[CJ ENM]사업보고서.pdf", "wb"))