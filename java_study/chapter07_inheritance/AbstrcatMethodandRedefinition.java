/*
추상 메서드와 재정의

추상 클래스는 실체 클래스가 공통적으로 가져야 할 필드와 메서드들을 정의해놓은 추상적인 클래스로, 실체 클래스의 멤버(필드, 메서드)를 통일하는 데
목적이 있다. 모든 실체들이 가지고 있는 메서드의 실행 내용이 동일하다면 추상 클래스에 메서드를 작성하는 것이 좋다.

하지만 메서드의 선언만 통일하고, 실행 내용은 실체 클래스마다 달라야 하는 경우가 있다. 예를 들어, 모든 동물은 소리를 내기 때문에 Animal 추상
클래스에서 sound()라는 메서드를 정의했다고 가정하자. 그렇다면 어떤 소리를 내도록 해야한느데, 이것은 실체 클래스에서 직접 작성해야 될 부분이다.
왜냐하면 동물은 다양한 소리를 내므로 이것을 추상 클래스에서 통일적으로 작성할 수 없기 때문이다. 그렇다고 해서 sound() 메서드를 실체 클래스에서
작성하도록 하면 sound() 메서드를 잊어버리고 작성하지 않을 경우 동물은 소리를 낸다는 것에 위배된다.

이런 경우를 위해서 추상 클래스는 추상 메서드를 선언할 수 있다. 추상 메서드는 abstract 키워드와 함께 메서드와 함께 메서드의 선언부만 있고 메서드
실행 내용은 중괄호가 없는 메서드를 말한다. 다음은 추상 메서드를 선언하는 방법을 보여준다.
[public | protected] abstract 리턴타입 메서드이름(매개변수, ...);

추상 클래스 설계 시 하위 클래스가 반드시 실행 내용을 채우도록 강제하고 싶은 메서드가 있을 경우 해당 메서드를 추상 메서드로 선언한다.
자식 클래스는 반드시 추상 메서드를 재정의해서 실행 내용을 작성해야 하는데, 그렇지 않으면 컴파일 에러가 발생한다. 이것이 추상 메서드의 위력이다.

다음은 Animal 클래스를 추상 클래스로 선언하고 sound() 메서드를 추상 메서드로 선언한 것이다. 어떤 소리를 내는지 결정할 수 없지만 동물은 소리를
낸다는 공통적인 특징을 규정하기 위해 sound() 메서드를 추상 메서드로 선언했다.
public abstract class Animal {
    public abstract void sound();
}

Animal 클래스를 상속하는 하위 클래스는 동물마다 고유한 소리를 내도록 sound() 메서드를 재정의해야 한다.
예를 들어 Dog는 멍멍, Cat는 야옹 소리를 내도록 Dog와 Cat 클래스에서 sound() 메서드를 재정의해야 한다.
 */

// 추상메서드 선언
public abstract class Animal {  // 추상 클래스
    public String kind;

    public void breath() {
        System.out.println("숨을 쉽니다.");
    }
    public abstract void sound();   // 추상메서드
}

// 추상메서드 재정의
public class Dog extends Animal {
    public Dog() {
        this.kind = "포유류";
    }

    @java.lang.Override
    public void sound() {
        System.out.println("멍멍");   // 추상 메서드 재정의
    }
}

public class Cat extends Animal {
    public Cat() {
        this.kind = ㅍ"포유류";
    }

    @java.lang.Override
    public void sound() {
        System.out.println("야옹");   // 추상 메서드 재정의
    }
}

public class AnimalExample {
    public static void mian(String[] args) {
        Dog dog = new Dog();
        Cat cat = new Cat();
        dog.sound();
        cat.sound();
        System.out.println("----------");

        //변수의 자동 타입 변환
        Animal animal = null;
        animal = new Dog(); // 자동 타입 변환 및 재정의된 메서드 호출
        animal.sound();
        animal= new Cat();  // 자동 타입 변환 및 재정의된 메서드 호출
        animal.sound();
        System.out.println("----------");

        //메서드의 다형성
        animalSound(new Dog()); // 자동 타입 변환
        animalSound(new Cat()); // 자동 타입 변환
    }

    public static void animalSound(Animal animal) {
        animal.sound(); // 재정의된 메서드 호출
    }
}