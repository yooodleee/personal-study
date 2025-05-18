package encapsulation;

public class PhoneStoreTest {
    public static void main(String[] args) {
        Phone phone = new Phone("아이폰", 100000);
        PhoneStore store = new PhoneStore(phone);
        Customer customer = new Customer("김유영", 100000);
        customer.buyPhone(store);
    }
}
