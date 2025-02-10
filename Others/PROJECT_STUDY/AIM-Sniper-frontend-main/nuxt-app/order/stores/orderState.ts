export const orderState = () => ({
	orderItemList: [] as orderItem[],
	oredrItem: null as orderItem | null,
    orderList : [] as order[],
    order: null as order | null,
});

type orderItem = {
	companyReportId: 0;
    companyReportName: "",
    companyReportTitleImage: "",
    companyReportPrice: 0;
};

type order = {
    orderId: 0,
    orderData: "",
    totalPrice:0,
    totalQuantity: 0,
}