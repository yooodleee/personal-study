/*float 타입과 double 타입*/
public class FloatDoubleExample {
    public static void main(String[] args) {
        // 실수값 저장
        //float var1 = 3.14;    -> compile error(Type mismatch)
        float var2 = 3.14f;
        double var3 = 3.14;

        // 정밀도 계산
        float var4 = 0.1234567890123456789f;
        double var5 = 0.1234567890123456789;

        System.out.println("var2 : " + var2);   // 3.14
        System.out.println("var3 : " + var3);   //3.14
        System.out.println("var4 : " + var4);   //0.123456789
        System.out.println("var5 : " + var5);   //double 타입인 var5가 float 타입인 var4보다 2배 이상 정밀한 값으로 출력
        // 0.1234567890123456789

        //e 사용하기
        double var6 = 3e6;
        float var7 = 3e6F;
        double var8 = 2e-3;
        System.out.println("var6 : " + var6);   // 3000000.0
        System.out.println("var7 : " + var7);   //3000000.0
        System.out.println("var8 : " + var8);   // 0.002
    }
}