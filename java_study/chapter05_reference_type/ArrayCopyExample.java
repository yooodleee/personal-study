/*System.arraycopy()로 배열 복사*/
public class ArrayCopyExample {
    public static void main(String[] args) {
        String[] oldStrArray = {"Java", "array", "copy"};
        String[] newStrArray = new String[5];

        System.out.println(oldStrArray, 0, newStrArray, 0, oldStrArray.length);

        for (int i=0; i< newStrArray.length; i++) {
            System.out.println(newStrArray[i] + ", ");
        }
    }
}
/*
객체를 참조하는 배열

기본 타입 배열은 각 항목에 직접 값을 갖고 있지만, 참조 타입(클래스, 인스턴스) 배열은 각 항목에 객체의 번지를 가지고 있다.
예를 들어 String은 클래스이므로 String[] 배열은 각 항목에 문자열이 아니라, String 객체의 번지를 가지고 있다.
즉 String[] 배열은 String 객체를 참조하게 된다.

따라서 String[] 배열의 항목도 결국 String 변수와 동일하게 취급되어야 한다.
예를 들어 String[] 배열 항목 간에 문자열을 비교하기 위해서는 == 연산자 대신 equals() 메서드를 사용해야 한다.
== 는 객체의 번지를 비교하기 때문에 문자열을 비교하는 데는 사용할 수 없다.

strArray[0]과 strArray[1] 배열 항목을 -- 연산하면 결과는 true가 나온다.
이유는 두 배열 객체가 동일한 String 객체를 참조하기 때문이다.
반면에 String 객체를 new 연산자로 생성하면 무조건 새로운 String 객체가 생성되기 때문에 strArray[0]과 strArray[2] 배열 항목을
== 연산하면 결과는 false가 나온다.


배열 복사

배열은 한 번 생성하면 크기를 변경할 수 없기 때문에, 더 많은 저장 공간이 필요하다면 더 큰 배열을 새로 만들고 이전 배열로부터 항목 값들을
복사해야 한다. 배열 간의 항목 값들을 복사하려면 for 문을 사용하거나 System.arraycopy() 메서드를 사용해야 한다.

oldIntArray     -> copy ->      newIntArray
[1,2,3]                         [1, 2, 3, 0, 0]

복사되지 않은 항목은 int[] 배열의 기본 초기값 0이 그대로 유지된다.
이번에는 System.arraycopy() 메서드를 이요해서 배열을 복사해보자. System.arraycopy()를 호출하는 방법은 다음과 같다.
System.arraycopy(Object src, int srcPos, Object dest, int destPos, int length);

src 매개값은 원본 배열이고, srcPos는 원본 배열에서 복사할 항목의 시작 인덱스이다. dest 매개값은 새 배열이고, destPos는 새 배열에서
붙여넣을 시작 인덱스이다. 마지막으로 length는 복사할 개수이다. 예를 들어, 원본 배열이 arr1이고 새 배열이 arr2일 경우 arr1의 모든 항목을
arr2에 복사하려면 다음과 같이 System.arraycopy() 메서드를 호출하면 된다.
System.arraycopy(arr1, 0, arr2, 0, arr1.length);


oldStrArray                     newStrArray
[ , , ]     -> copy ->      [ , , , null, null]

"java"       "array"         "copy"
String 객체   String 객체   String 객체

참조 타입 배열이 복사되면 복사되는 값이 객체의 번지이므로 새 배열의 항목은 이전 배열의 항복이 참조하는 객체와 동일하다.
 */