/* products=[
    {
        "id" :1,
        "name" :"Product1",
        "price" : "$10",
        "description" : "Description for product1",
        "image" : "https://picsum.photos/200"

    },

       {
        "id" :2,
        "name" :"Product2",
        "price" : "$20",
        "description" : "Description for product2",
        "image" : "https://picsum.photos/200"

    },
       {
        "id" :3,
        "name" :"Product3",
        "price" : "$15",
        "description" : "Description for product3",
        "image" : "https://picsum.photos/200"

    }
]


const productLists =document.getElementById("product-list")
products.forEach(product => {
    const productCard = `<div class="bg-white p-4 rounded-lg shadow">
        <img src="${product.image}" class="w-full h-40 object-cover rounded">
        <h2 class="text-lg font-semibold mt-2">${product.name}</h2>
        ${product.description}
        <p class="text-gray-600">${product.price}</p>
        <button class="mt-2 bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600">
          Buy
        </button>
      </div>`


      productLists.innerHTML+=productCard
}); */


//Array Decleared na kore Online kono source theke data niye asbo eta aro dynamic korbe
//FETCH Function + REST API

const productLists =document.getElementById("product-list")
fetch('https://fakestoreapi.com/products') //ei api te data change hole dynamically amar website o data change hobe
.then(response => response.json())
.then(data => {
data.forEach(product => {
    const productCard = `<div class="bg-white p-4 rounded-lg shadow">
        <img src="${product.image}" alt ="${product.name}"class="w-full h-40 object-cover rounded">
        <h2 class="text-lg font-semibold mt-2">${product.title}</h2>
        ${product.description}
        <p class="text-gray-600">${product.price}</p>
        <button class="mt-2 bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600">
          Buy
        </button>
      </div>`

      productLists.innerHTML += productCard
})

})
.catch(error => console.error('Error fetching Products:' ,error))
//Methods
/* 
GET
POST
PUT/PATCH
DELETE 
*/