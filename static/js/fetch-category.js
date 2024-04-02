const categoryFunction = async function () {
    const urlParams = new URLSearchParams(window.location.search);
    const categoryValue = urlParams.get("category");
    const colorValue = urlParams.get("colors");
    const brandValue = urlParams.get("brand");
    const priceMinValue = urlParams.get("priceMin");
    const priceMaxValue = urlParams.get("priceMax");
    const size = urlParams.get("size");

    const itemsContainer = document.getElementById("itemsContainer");

    if (categoryValue || colorValue || brandValue || priceMinValue || priceMaxValue || size) {
        let url = `http://20.215.225.225/api/filter/?`;

        if (categoryValue) {
            url += `category=${categoryValue}`;
        }

        if (colorValue) {
            if (categoryValue) {
                url += `&`;
            }
            url += `color=${colorValue}`;
        }

        if (brandValue) {
            if (categoryValue || colorValue) {
                url += `&`;
            }
            url += `brand=${brandValue}`;
        }

        if (priceMinValue) {
            if (categoryValue || colorValue || brandValue) {
                url += `&`;
            }
            url += `price_min=${priceMinValue}`;
        }

        if (priceMaxValue) {
            if (categoryValue || colorValue || brandValue || priceMinValue) {
                url += `&`;
            }
            url += `price_max=${priceMaxValue}`;
        }

        if (size) {
            if (categoryValue || colorValue || brandValue || priceMinValue || priceMaxValue) {
                url += `&`;
            }
            url += `size=${size}`;
        }

        let data = await fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            }
        });

        let items = await data.json();

        itemsContainer.innerHTML = ""

        for (let item of items) {
            const actualPrice = item.variant.actual_price;
            const productPrice = item.variant.product.price;
            const priceHTML = actualPrice < productPrice
                ? `<h4>${actualPrice}</h4> <del>${productPrice}</del>`
                : `<h4>${productPrice}</h4>`;
            console.log(item.image);            
            itemsContainer.innerHTML += `
            <div class="col-xl-3 col-6 col-grid-box">
                <div class="product-box">
                    <div class="img-wrapper">
                        <div class="front">
                            <a href="/product/${item.variant.get_absolute_url}"><img src="${item.image}" class="img-fluid blur-up lazyload bg-img" alt=""></a>
                        </div>
                        <div class="back">
                            <a href="/product/${item.variant.get_absolute_url}"><img src="${item.image}" class="img-fluid blur-up lazyload bg-img" alt=""></a>
                        </div>
                    <div class="cart-info cart-wrap">
                        <a href="javascript:void(0)" value="${item.variant.id}"  class="addToWishlist" title="Add to Wishlist">
                            <i class="ti-heart" aria-hidden="true"></i>
                        </a>
                        <a href="#" data-toggle="modal" data-target="#quick-view" title="Quick View">
                            <i class="ti-search" aria-hidden="true"></i>
                        </a> 
                    </div>
                </div>
                <div class="product-detail">
                    <div>
                            <div class="rating">
                            </div>
                            <a href="product-page(no-sidebar).html">
                                <h6>${item.variant.product.title_en}</h6>
                            </a>
                            <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley
                                of type and scrambled it to make a type specimen book
                            </p>
                            ${priceHTML}
                            
                        </div>
                    </div>
                </div>
            </div>
            `
        }

        addItemToWishlist();

    }
    else {
        let url = `http://20.215.225.225/api/filter/`;

        let data = await fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                // "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MDY3NTg0LCJpYXQiOjE2OTgwNjM5ODQsImp0aSI6ImZiZjMxYzI0NmI5MzRmOGJhMmDxMTE0ZTQ5MmNiNDAwIiwidXNlcl9pZCI6MX0.Pffk8KBrL7uR0FT6H-_vTOfzEv56JkMsUL5F8QDz_OU"
            }
        });

        let items = await data.json();
        let itemsContainer = document.getElementById("itemsContainer")

        itemsContainer.innerHTML = ""

        for (let item of items) {
            const actualPrice = item.variant.actual_price;
            const productPrice = item.variant.product.price;
            const priceHTML = actualPrice < productPrice
                ? `<h4>${actualPrice}</h4> <del>${productPrice}</del>`
                : `<h4>${productPrice}</h4>`;

            itemsContainer.innerHTML += `
                <div class="col-xl-3 col-6 col-grid-box">
                    <div class="product-box">
                        <div class="img-wrapper">
                            <div class="front">
                                <a href="/product/${item.variant.get_absolute_url}"><img src="${item.image}" class="img-fluid blur-up lazyload bg-img" alt=""></a>
                            </div>
                            <div class="back">
                                <a href="/product/${item.variant.get_absolute_url}"><img src="${item.image}" class="img-fluid blur-up lazyload bg-img" alt=""></a>
                            </div>
                        <div class="cart-info cart-wrap">
                            <a href="javascript:void(0)" value="${item.variant.id}"  class="addToWishlist" title="Add to Wishlist">
                                <i class="ti-heart" aria-hidden="true"></i>
                            </a>
                            <a href="#" data-toggle="modal" data-target="#quick-view" title="Quick View">
                                <i class="ti-search" aria-hidden="true"></i>
                            </a> 
                        </div>
                    </div>
                    <div class="product-detail">
                        <div>
                            <div class="rating"><i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i> <i class="fa fa-star"></i></div>
                                <a href="product-page(no-sidebar).html">
                                    <h6>${item.variant.product.title_en}</h6>
                                </a>
                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley
                                    of type and scrambled it to make a type specimen book
                                </p>
                                ${priceHTML}
                                
                            </div>
                        </div>
                    </div>
                </div>
                `
        }
        
        addItemToWishlist();

    }
};

categoryFunction()


const colors = document.getElementsByClassName("colors");

for (var i = 0; i < colors.length; i++) {
    colors[i].addEventListener("click", (e) => {
        const clickedColor = e.target.dataset.color;
        const urlParams = new URLSearchParams(window.location.search);
        const url = new URL(window.location.href);
        const currentColor = urlParams.get("colors");

        if (currentColor === clickedColor) {

            url.searchParams.delete('colors');
            e.target.classList.remove('active');
        } else {
            url.searchParams.set('colors', clickedColor);

        }

        window.history.replaceState(null, null, url);
        categoryFunction();
    })
}


const priceInputs = document.querySelectorAll('#priceMin, #priceMax');

priceInputs.forEach(input => {
    input.addEventListener('input', function () {
        filterByPrice();
    });
});


function filterByPrice() {
    const priceMinInput = document.getElementById('priceMin');
    const priceMaxInput = document.getElementById('priceMax');

    const urlParams = new URLSearchParams(window.location.search);
    urlParams.set('priceMin', priceMinInput.value);
    urlParams.set('priceMax', priceMaxInput.value);

    window.history.replaceState(null, null, `?${urlParams.toString()}`);

    categoryFunction();
}


const sizeCheckboxes = document.querySelectorAll('.size-checkbox');

sizeCheckboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function () {
        updateSizeFilters(this);
    });
});


function updateSizeFilters(checkedCheckbox) {
    sizeCheckboxes.forEach(checkbox => {
        if (checkbox !== checkedCheckbox) {
            checkbox.checked = false;
        }
    });

    const urlParams = new URLSearchParams(window.location.search);
    urlParams.set('size', checkedCheckbox.checked ? checkedCheckbox.value : '');

    window.history.replaceState(null, null, buildUpdatedUrl(urlParams));

    categoryFunction();
}


function buildUpdatedUrl(urlParams) {
    const currentUrl = window.location.href;
    const baseUrl = currentUrl.split('?')[0];

    return `${baseUrl}?${urlParams.toString()}`;
}


const brandCheckboxes = document.querySelectorAll('.brand-checkbox');

brandCheckboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function () {
        updateBrandFilters(this);
    });
});


function updateBrandFilters(checkedCheckbox) {
    brandCheckboxes.forEach(checkbox => {
        if (checkbox !== checkedCheckbox) {
            checkbox.checked = false;
        }
    });

    const urlParams = new URLSearchParams(window.location.search);
    urlParams.set('brand', checkedCheckbox.checked ? checkedCheckbox.value : '');

    window.history.replaceState(null, null, buildUpdatedUrl(urlParams));

    categoryFunction();
}


// var addToWishlistButton = document.getElementById("addToWishlist");

// if (addToWishlistButton) {
//     addToWishlistButton.addEventListener("click", async function() {
//         console.log('salam');
//     });
// }

let userID = document.getElementById("userID").value;

function addItemToWishlist() {
    document.querySelectorAll(".addToWishlist").forEach(element => {
        element.addEventListener("click", async function () {
            try {
                let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
                const data = await fetch(`http://20.215.225.225/api/add-to-wishlist/?user_id=${userID}&variant_id=${this.getAttribute('value')}`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        'X-CSRFToken': csrfToken

                    }
                });

                if (!data.ok) {
                    throw new Error(`HTTP error! Status: ${data.status}`);
                }

                const response = await data.json();
                console.log('Response:', response);

                if (response.detail === "This item is already in the wishlist") {
                    alert(response.detail);
                } else {
                    location = `/account/wishlist`;
                }
            } catch (error) {
                console.error('Error:', error);
            }
        });
    });
}
