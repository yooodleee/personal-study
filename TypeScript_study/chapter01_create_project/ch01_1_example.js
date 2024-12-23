"use strict";
//@ts-check
let a_number = 1000;
if (Math.random() < 0.5) {
    a_number = "Hello, World!"; // Type 'string' is not assignable to type
}
console.log(a_number * 10);
function addVAT(price, vat = 0.2) {
    return price * (1 + vat);
}
//@ts-expect-error
addVAT(1000, "0.2");
//@ts-expect-error
addVAT(1000).toUpperCase();
