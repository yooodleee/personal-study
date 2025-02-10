export const CartState = () => ({
	cartItemList: [] as CartItem[],
	cartItem: null as CartItem | null,
});

type CartItem = {
	companyReportId: 0;
    companyReportName: "",
    companyReportPrice: 0;
};