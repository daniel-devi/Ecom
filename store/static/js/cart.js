console.log("HEllo World")
var updateBttn = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBttn.length; i++) {
    updateBttn[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('user: ', user)
        if (user === 'AnonymousUser'){
                console.log('Not loggin IN')
            }
        else{
            updateUserOrder(productId, action)
        }
        console.log('productid: ', productId, 'action: ', action)
    })
}


function updateUserOrder(productId, action){

    var url =   '/update_item/'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFTOKEN': csrftoken
        },
        body:JSON.stringify({
            'productId': productId, 'action':action})
    })


    .then((response =>{
        return response.json()
    }
        ))

    
    .then((data =>{
        console.log('data:', data)
        location.reload()
    }
        ))
    
}
