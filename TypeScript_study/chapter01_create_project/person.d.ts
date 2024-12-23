// @types/person.d.ts

// 다음과 같은 모양을 갖는 객체 인터페이스
export interface Person {
    name: string;
    age: number;
}

// 기존 인터페이스를 확장하는 인터페이스
// JSDoc 주석으로는 이를 구현하기 힘들다.
export interface Student extends Person {
    semester: number;
}

// index.js
/**@typedef { import ("../@types/person").Person} Person */

// index.js, 이어서

/**
 * @param {Person} person
 */
function printPerson(person) {
    console.log(person.name);
}