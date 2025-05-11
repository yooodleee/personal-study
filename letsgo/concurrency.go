package main

import (
		"fmt"
		"time"
)

func speak(text string, delay time.Duration) {
		for i := 0; i < 5; i++ {
				fmt.Println(text)
				fmt.Sleep(delay)
		}
}

func main() {
		go speak("Hello", 1 * time.Second)
		go speak("World", 2 * time.Second)
		
		// 메인 고루틴이 고루틴의 완료를 기다립니다
		time.Sleep(10 * time.Second)
		fmt.Println("Done")
}