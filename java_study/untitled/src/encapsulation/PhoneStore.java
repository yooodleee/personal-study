package encapsulation;

public class PhoneStore {
    private Phone phone;

    public PhoneStore(Phone phone) {
        this.phone = phone; // PhoneStore 객체를 생성할 때 호출
    }

    // 구입하려는 모델과 예산이 매개변수
    public Phone sellPhone(String model, double budget) {
        String phoneModel = phone.getModel();

        // 고객이 원하는 모델과 대리점에서 가지고 있는 핸드폰 모델이 같고,
        // 핸드폰의 가격이 예산보다 작거나 같으면
        if (model.equals(phoneModel) && budget >= phone.getPrice()) {
            registerPayment();
            discountPromotion();
            saveData();
            return phone;
        }
        else return null;
    }

    private void registerPayment() {
        System.out.println("대리점: 요금제를 등록합니다. 약정을 등록합니다.");
    }

    private void discountPromotion() {
        System.out.println("대리점: 프로모션으로 할인합니다.");
    }

    private void saveData() {
        System.out.println("대리점: 데이터를 저장하고 새로운 폰으로 이동합니다.");
    }
}
