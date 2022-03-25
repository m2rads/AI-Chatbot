const menu = document.getElementById("menu-display")
/* 
    Gets the menu items from the api
    and populate the menu section 
*/ 
const Populate = async () => {
    menu.innerHTML = '';
    fetch('/api')
    .then(response => response.json())
    .then(data => {
        // console.log(data)
        let menuItems = JSON.stringify(data['menu'])
        // console.log(menuItems)
        let menuArr = JSON.parse(menuItems)
        Object.entries(menuArr).forEach(item => {
            menu.innerHTML += `
                <div id='${item[0]}' class="category">
                    <h3>${item[0]}</h3>
            `
            item[1].forEach(item => {
                menu.innerHTML += `
                    <div class="items">
                        <p>${item['name']}</p>
                        <h6>${item['price']}</h6>
                        <!-- <a href="#">+</a> -->
                    </div>
                `
            })
            menu.innerHTML += `
                    </div>
                `
        })
    })
}

Populate()
