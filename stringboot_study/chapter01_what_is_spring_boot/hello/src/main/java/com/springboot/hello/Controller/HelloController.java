/*
컨트롤러 작성하기

컨트롤러에 포함된 로직에서는 애플리케이션의 사용자 또는 클라이언트가 입력한 값에 대한 응답을 수행한다.
특별한 경우를 제외한 모든 요청은 컨트롤러를 통해 진행돼야 한다. 이번 예제는 컨트롤러 내부에서 모든 로직을 처리했지만 데이터를 다루거나
별도의 로직을 처리해야 하는 경우에는 서비스 또는 데이터 엑세스 레이어까지 요청을 전달하는 경우가 일반적이다.
 */
package com.springboot.hello.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @RequestMapping("/hello")
    public String hello(){
        return "Hello World";
    }

}