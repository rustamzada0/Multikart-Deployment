let formContainer = document.getElementById("formContainer")
let create_btn = document.getElementsByClassName('subscribe-form')[0]

create_btn.addEventListener("submit", async function(e){
    e.preventDefault()

    let csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    
    let data = await fetch(`${location.origin}/api/subs/`,{
        method: "POST",
        headers:{
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "X-CSRFToken":csrfToken            
        },
        body : JSON.stringify({
            "email":e.target.email.value
        })
    })

    let response = await data.json();

    if (data.ok){
        alert('Subscribe Successfully!')
        location=`/home`
    }
})


