import pandas as pd
import os


# 엑셀 파일들이 있는 폴더 경로
folder_path = '../asset'


# 모든 액셀 파일 읽어서 하나로 합치기
combined_df = pd.DataFrame()

for file in os.listdir(folder_path):
    if file.endswith('.xlsx') or file.endswith('xls'):
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path)
        combined_df = pd.concat([combined_df, df], ignore_index=True)


# 합쳐진 데이터를 새로운 엑셀로 저장
combined_df.to_excel('merged_interview_questions.xlsx', index=False)