window.addEventListener('load', async function() {
    let cartID = document.getElementById("cartID").value
    let productID = document.getElementById("productID").value
    let data = await fetch(`http://127.0.0.1:8000/api/product/${productID}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    });
    let product = await data.json();
    let colorContainer = document.getElementById("colorContainer")

    for (let variant of product.variant) {
        colorContainer.innerHTML += `
        <a href="/product/${variant.get_absolute_url}">
        <li id=${variant.color} value=${variant.color} style="background-color: ${variant.color};">
        </li>
        </a>
        `
        }

    let variantID = document.getElementById("variantID").value
    let data2 = await fetch(`http://127.0.0.1:8000/api/variant/${variantID}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    });
    let variant = await data2.json()
    let sizeContainer = document.getElementById("sizeContainer")
    for (let option of variant.option) {
        sizeContainer.innerHTML += `
        <li value='${option.size}' class="property-size" style="border: 1px solid">${option.size}</li>
        `
    }

    propertSize=document.querySelectorAll('.property-size')
    propertSize[0].classList.add('aktiv')

    for (var i = 0; i < propertSize.length; i++) {
        propertSize[i].addEventListener('click', function () {
            propertSize.forEach(element => element.classList.remove('aktiv'));
            this.classList.add('aktiv');
    
            // Eklenen kısım: Seçilen boyutun sınırını kalınlaştır
            propertSize.forEach(element => {
                if (element.classList.contains('aktiv')) {
                    element.style.border = '3px solid';  // Kalın sınır
                } else {
                    element.style.border = '1px solid';  // Normal sınır
                }
            });
        });
    }


    // if('{{request.user}}'!=='AnonymousUser'){
    //     document.getElementById('checkout').addEventListener('click', function(){
    //         // var selcetedColor;
    //         var selectedSize;
    //         var selectedQuantity=document.getElementById('quantity').value;
    //         console.log(selectedQuantity);
    //         var selectedColor = variant.color
    //         console.log(selectedColor);

    //         propertSize.forEach(function(element) {
    //             if (element.classList.contains('aktiv')) {
    //                 selectedSize=element.getAttribute('value');
    //             }
    //         });
           

    //         location=`/payment/checkout/?item=${variant.slug}&color=${selectedColor}&size=${selectedSize}&quantity=${selectedQuantity}`
    //     })
    //     }


    if('{{request.user}}'!=='AnonymousUser'){
        document.getElementById('addcart').addEventListener('click', function() {
            var selectedSize;
            var selectedQuantity = document.getElementById('quantity').value;
            var selectedColor = variant.color;
        
            propertSize.forEach(function(element) {
                if (element.classList.contains('aktiv')) {
                    selectedSize = element.getAttribute('value');
                }
            });
            
            let body = {
                "cart": cartID,
                "variant": variantID,
                "quantity": selectedQuantity,
                "size": selectedSize,
            }
            
            async function myAsyncFunction() {
                try {
                    let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
                    let data = await fetch('http://127.0.0.1:8000/api/addtocart/', {
                        method: 'POST',
                        headers: {
                            "Content-Type": "application/json",
                            'X-CSRFToken': csrfToken
                        },
                        body: JSON.stringify(body)
                    });
                    console.log(data);
            
                    let items = await data.json();
                    // Elde edilen verileri kullanabilirsiniz
                    console.log(items);
                } catch (error) {
                    console.error('Error:', error);
                }
            }
            myAsyncFunction();            


            location=`/payment/cart/` 
        });
        
        }

    });