document.addEventListener('DOMContentLoaded', function() {
    //MAIN BUTTONS
    const landingButtonMain = document.querySelector('.main-button-white');

    landingButtonMain.addEventListener('mouseover', function() {
        landingButtonMain.classList.add('active');
    })

    landingButtonMain.addEventListener('mouseout', function() {
        landingButtonMain.classList.remove('active');
    })  
})