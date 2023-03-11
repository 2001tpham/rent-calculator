document.addEventListener('DOMContentLoaded', function() {
    //MAIN BUTTONS
    
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