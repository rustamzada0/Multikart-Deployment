// let form = document.querySelector('#login-form')

// form.addEventListener('submit', async function(event) {
//     event.preventDefault();
//     console.log('here');

//     let postData = {
//         username: form.emailorusername.value,
//         password: form.password.value 
//     }

//     let data = await fetch('http://localhost:8000/api/token/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(postData)
//     });
//     if (data.ok){
//         let response = await data.json()
//         localStorage.setItem("access_token", response["access"]);
//         localStorage.setItem("refresh_token", response["refresh"]);
//         // window.location = '/account/profile'
//     }
// });














// let loginBtn = document.querySelector("#loginBtn")

// loginBtn.addEventListener("click", async function() {
//     event.preventDefault();
//     let usernameOrEmail = document.querySelector("#usernameOrEmail").value;
//     let password = document.querySelector("#password").value

//     let body = {
//         "username": usernameOrEmail,
//         "password": password
//     }

//     let url = `http://127.0.0.1:8000/api/token/`;
//     let data = await fetch(url, {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//         },
//         body: JSON.stringify(body)
//     });

//     if (data.ok) {
//         let response = await data.json();
//         localStorage.setItem("access_token", response["access"]);
//         localStorage.setItem("refresh_token", response["refresh"]);

//         window.location.href = `http://127.0.0.1:8000/account/profile/`; 
//     } else {
//         console.log("OLmur");
//     }
// })
