console.log("Hello World");

let x = 10;
console.log(x);

// String
let str = "Sakib";
console.log(str);

// Number
let num = 1212;
console.log(num);

// BigInt
let y = 135263748829832944354232432n;
console.log(y);

let w = 10;
w = 21;

// null & undefined
let o = null;
let t;
console.log(t);

// Operators
let c = 10;
console.log(c == "10");   // true
console.log(c === "10");  // false

// IF ELSE
if (c == 10) {
    console.log("Value Matched");
} else {
    console.log("Not Matched");
}

// SWITCH
switch (c) {
    case 10:
        console.log("Value is 10");
        break;
    case 20:
        console.log("Value is 20");
        break;
    default:
        console.log("Don't matched");
}

// Loop
let colors = ["red", "black", "blue"];

for (let color of colors) {
    console.log(color);
}

for (let i = 0; i < colors.length; i++) {
    console.log(colors[i]);
}

// While Loop
const numbers = [10, 20, 30];
let s = 0;

while (s < numbers.length) {
    console.log(numbers[s]);
    s++;
}

numbers.forEach(r => {
    console.log(r);
});

// Array
const myarray = ["a", "b", "c"];
console.log(myarray);
console.log(myarray[0]);

myarray.push("akash");
console.log(myarray);

// Function
function ghorardim() {
    console.log("Ghorardim");
}
ghorardim();

// IIFE
(function () {
    console.log("Ghorardim2");
})();

// Arrow Function
const ghorardim3 = () => {
    console.log("ghorardim3");
};

ghorardim3();

//Array Methods
const names = ["raj","Taj","Jan","Sun"]

function add_lej(item)
{
    return item + "___"
}

const name_mod = names.map(add_lej)
console.log(name_mod)


//Python er dictionary js er object pri same 
//Object
const person = {
    name : "Sohag",
    age : 25,
    hobbies :["Reading" , "Travelling","Coding","Gaming"]
}

console.log(person)
console.log("person age is :",person.age)

//DOM --> Document Object Model

const kidnapped = document.getElementsByTagName("h1")
console.log(kidnapped)