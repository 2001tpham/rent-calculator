document.addEventListener('DOMContentLoaded', function() {
    //MAIN BUTTONS
    const landingButtonMain = document.querySelector('.main-button-white');

    landingButtonMain.addEventListener('mouseover', function() {
        landingButtonMain.classList.add('active');
    })

    landingButtonMain.addEventListener('mouseout', function() {
        landingButtonMain.classList.remove('active');
    })
    
    const landingButtonBlue = document.querySelectorAll('.main-button');

    landingButtonBlue.forEach(function(landingButtonBlue) {
        landingButtonBlue.addEventListener('mouseover', function() {
            landingButtonBlue.classList.add('active');
        })
    
        landingButtonBlue.addEventListener('mouseout', function() {
            landingButtonBlue.classList.remove('active');
        })
    })
})