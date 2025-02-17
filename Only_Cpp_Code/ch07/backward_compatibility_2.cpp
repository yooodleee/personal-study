// 파일 읽기 인스턴스 생성
using namespace std;

#include <iostream>

file_reader_original *file_reader_original::get_reader_instance() {
    file_reader_original *reader = nullptr;

    switch (file_reader_original::read_header()) 
    {   // 파일 헤더를 읽어 버전 확인
    case 1:
        /* code */
        reader = new file_reader_v0100();   // v1.0으로 파일 리더기 생성
        break;
    
    case2:
    default:
        reader = new file_reader_v0200();   // v2.0으로 파일 리더기 생성
        break;
    }

    return reader;
}