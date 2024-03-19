window.addEventListener('load', async function(){
    let userID = document.getElementById("userID").value
    let data = await fetch(`http://127.0.0.1:8000/api/carts/?user_id=${userID}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    });
    let carts = await data.json();
    let checkContainer = document.getElementById("checkContainer")
    
    toti = 0
    for (let cart of carts) {
        toti += cart.total_price
        checkContainer.innerHTML += `
        <li>${cart.product.title} × ${cart.quantity} <span>$${cart.total_price}</span></li>
        `
        }
    let totiContainer = document.getElementById("toti")
    totiContainer.innerHTML += `

    <span class="count">$${toti}</span>
    `

})

// document.getElementById('buyID').addEventListener('click', function() {
//     console.log('salam');
// })

// if('{{request.user}}'!=='AnonymousUser'){
//     console.log('Salam');
//     document.getElementById('checkout').addEventListener('click', function(){
//         var selectedColor;
//         var selectedSize;
//         var selectedQuantity=document.getElementById('quantity').value;
//         console.log(selectedColor);
//         console.log(selectedSize);
//         console.log(selectedQuantity);

//         propertColor.forEach(function(element) {
//             if (element.classList.contains('aktiv')) {
//                 selectedColor=element.getAttribute('value');
//             }
//         });
//         propertSize.forEach(function(element) {
//             if (element.classList.contains('aktiv')) {
//                 selectedSize=element.getAttribute('value');
//             }
//         });
       

//         location=`/payment/checkout/?prod={{variant.slug}}&color=${selectedColor}&size=${selectedSize}&quantity=${selectedQuantity}`
//     })
//     }