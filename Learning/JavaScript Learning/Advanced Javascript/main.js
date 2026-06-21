console.log("Wellcome to Template Literals")
const test = "Sohag"
let test2 = "everyone"
console.log(`Hello,${test}`)
console.log(`Hello,${test2}`)
console.log(`Hello,${1+2}`)

function greeting()
{
    return "Greeting from me"
}
let output = `Hello, ${test}. ${greeting()}`
console.log(output)


//Destructuring Assignment
    /*Suppose a array const arr = [1,2,3,4];*/

let [a,b,c,d] = [1,2,3,4]
console.log(1) //  o/p:1
console.log(b) //  o/p:2

//OR
let marks = [78,87,97,45]
let [Jhon,sham,sohag,Rabbi] = marks
console.log(sohag) // 97
//list a serially data boshay 

//For Dictionary
const user={
    name : "Sohag",
    age :"24",
    hobby :"Gaming"
}
/*const {name,age,hobby} = user
console.log(hobby,age)  //Gaming 24  */

const {age,name,hobby} = user // age er moddhe age e jabe age thak ar pore thak
console.log(age,name)  //Gaming 24


//Spread and Rest operator(...)
const nums =[1,2,34]
const newNums= [4,3,5]
const newNums2 =[...nums, ...newNums]
console.log(newNums2) //[ 1, 2, 34, 4, 3, 5 ]

//Why ...?

let test3 =[1,2,3]
let test4 = test3
test4[0] = 4
console.log(test4) // [ 4, 2, 3 ] ok
console.log(test3) // [ 4, 2, 3 ] give same o/p how ?
//Reason -> let test4 = test3 akoi address er refference use kore

//solution -> ... operator
let test5 =[1,2,3]
let test6 = [...test5]
test6[0] = 4
console.log(test6) // [ 4, 2, 3 ] ok
console.log(test5) // [ 1, 2, 3 ] now its ok

//CallBack Function
function greeting2()
{
    console.log("Hello Everyone")
}
let helloGreeting = greeting2//akhon greeting2 ke helloGreetiong diye call kora jabe
helloGreeting()
greeting2()  


//
let x = [1,2,3,4,5]
function add(a,b){  //add(a,b) ->callback function
    return a+b
}
//let result = x.reduce(add,0) OR
let result = x.reduce((a,b) => a+b ,0)
console.log(result)
 
//Promise Concept
const promise = new Promise((resolve,reject) => {
    let success = false
    if(success)
    {
        resolve("Everything was fine")
    }else{
        reject("Something was Wrong")
    }
})
promise
  .then((result) =>{
    console.log("Inside Then:")
    console.log(result)
  })
  .catch((result) =>{
    console.log("Inside Catch:")
    console.log(result)
  })
  .finally((result) =>{
    console.log("inside finally:")
    console.log(result)
  })


  //Practical Uses of Promise
  function getGitHubUser(username){
    return new Promise((resolve,reject) =>{
        fetch(`https://api.github.com/users/${username}`)
          .then((response)=>{
            return resolve(response.json())
          })
          .catch((error) => reject(`Network: ${error.message}`))
    })
  }

  getGitHubUser("octocat").then((user) =>{
    console.log("Github User data:" ,user)
  })


  console.log("\n\n\n test \n\n\n")

  //Scoping
  function fun(){
    let hello = 10
    console.log(hello)
  }
 // console.log(hello) //error for scopping


//CLOSURE
function outerFun(){
    let outervariable = 10;

    function innerFun() {
        console.log(outervariable);
    }

    return innerFun;
}

const myclosure = outerFun();
