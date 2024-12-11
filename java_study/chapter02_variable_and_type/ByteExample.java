public class ByteExample {
    public static void main(String[] args) {
        byte var1 = -128;
        byte var2 = -30;
        byte var3 = 0;
        byte var4 = 30;
        byte var5 = 127;
        byte var6 = 128;    //컴파일 에러(Type mismatch:cannot convert from int to byte)
        // byte 저장되는 값의 허용 범위는 -128~127까지, var6 = 128이므로 compile error

        System.out.println("var1: " + var1);
        System.out.println("var2: " + var2);
        System.out.println("var3: " + var3);
        System.out.println("var4: " + var4);
        System.out.println("var5: " + var5);
//      System.out.println("var6: " + var6);
    }
}