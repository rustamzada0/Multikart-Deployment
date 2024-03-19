window.addEventListener('load', async function(){
    let userID = document.getElementById("userID").value
    let data = await fetch(`http://127.0.0.1:8000/api/carts/?user_id=${userID}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    });
    let carts = await data.json();
    let tableContainer = document.getElementById("tableContainer")

    let toti = 0
    for (let cart of carts) {
        toti += cart.total_price
        tableContainer.innerHTML += `
        <tbody>
            <tr>
                <td>
                    <a href="/product/${cart.variant.get_absolute_url}"><img src="${cart.variant.is_main_image}" alt=""></a>
                </td>
                <td><a href="/product/${cart.variant.get_absolute_url}">${cart.variant.title}</a>
                    <div class="mobile-cart-content row">
                        <div class="col-xs-3">
                            <div class="qty-box">
                                <div class="input-group">
                                    <input type="text" name="quantity" class="form-control input-number"
                                        value="1">
                                </div>
                            </div>
                        </div>
                        <div class="col-xs-3">
                            <h2 class="td-color">${cart.variant.actual_price}</h2>
                        </div>
                        <div class="col-xs-3">
                            <h2 class="td-color"><a href="#" class="icon"><i class="ti-close"></i></a>
                            </h2>
                        </div>
                    </div>
                </td>
                <td>
                    <h2>$${cart.variant.actual_price}</h2>
                </td>
                
                <td>
                    <div class="qty-box">
                        <div class="input-group">

                            <h2>${cart.quantity}</h2>

                        </div>
                    </div>
                </td>
                <td><button  data-product=${cart.id}  class="btn btn-solid remove" ><i data-product=${cart.id} class="ti-close"></i></button></td>
                <td>
                    <h2 id="total_price" class="td-color">$${cart.total_price}</h2>
                </td>
            </tr>
        </tbody>
        `
       
        }
        const removeBtn=document.getElementsByClassName("remove");
        console.log(removeBtn);
        for(var i=0;i<removeBtn.length;i++){

            removeBtn[i].addEventListener("click", async function(e){
                try {
                    let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

                    await fetch(`http://127.0.0.1:8000/api/delete/${e.target.dataset.product}`, {
                        method: "DELETE",
                        headers: {
                            "Content-Type": "application/json",
                            'X-CSRFToken': csrfToken
                        }

                    });
                    e.target.parentNode.parentNode.parentNode.remove()
                
                    // toti-= parseFloat(e.target.parentNode.parentNode.parentNode.childNodes[5].children[0].innerText.replace("$",""))
                    // let totiContainer = document.getElementById("toti")
                    
                    // totiContainer.innerHTML = `
                
                    //     <h2>$${toti}</h2>
                
                    // `
                } catch (error) {
                    console.error("Error deleting cart:", error);
                }
            })
            }

    // let totiContainer = document.getElementById("toti")
    // totiContainer.innerHTML += `

    //     <h2>$${toti}</h2>

    // `


})

