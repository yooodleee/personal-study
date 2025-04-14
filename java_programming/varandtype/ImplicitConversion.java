package varandtype;

public class ImplicitConversion {
    public static void main(String[] args) {
        byte bNum = 10;
        int iNum = bNum;        // byte 형 값이 int 형 변수로 대입

        System.out.println(bNum);
        System.out.println(iNum);

        int iNum2 = 20;
        float fNum = iNum2;     // int 형 값이 float 형 변수로 대입됨

        System.out.println(iNum);
        System.out.println(fNum);

        double dNum;
        dNum = fNum + iNum;
        System.out.println(dNum);
    }
}


/**
 * 10
 * 10
 * 10
 * 20.0
 * 30.0
 */