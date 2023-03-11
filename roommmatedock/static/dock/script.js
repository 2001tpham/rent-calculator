document.addEventListener('DOMContentLoaded', function() {

    //DROPDOWN MENU OPTIONS
    const dropdownOption = document.querySelectorAll('.dropdown-menu-option');

    dropdownOption.forEach(dropdownOption => {
        dropdownOption.addEventListener('mouseover', function() {
            dropdownOption.classList.add('active');
        })
        
        dropdownOption.addEventListener('mouseout', function() {
            dropdownOption.classList.remove('active');
        })
    })

    //Dropdown for Tools
    const dropDownToolsButton = document.querySelector('#hover-tools-dropdownid');
    const dropDownToolsMenu = document.querySelector('#dropdown-tools-containerid');

    dropDownToolsButton.addEventListener('mouseover', function() {
        dropDownToolsMenu.classList.add('open-menu');

    })

    dropDownToolsButton.addEventListener('mouseout', function() {
        dropDownToolsMenu.classList.remove('open-menu');
    })
    
    dropDownToolsMenu.addEventListener('mouseover', function() {
        dropDownToolsMenu.classList.add('open-menu');
    })

    dropDownToolsMenu.addEventListener('mouseout', function() {
        dropDownToolsMenu.classList.remove('open-menu');
    })
    
    //NAV BAR
    //BRAND
    const brand = document.querySelector('.nav-brand');

    brand.addEventListener('mouseover', function() {
        brand.classList.add('active');
    })

    brand.addEventListener('mouseout', function() {
        brand.classList.remove('active');
    })

    //NAV OPTIONS
    const navOption = document.querySelectorAll('.nav-option');

    navOption.forEach(navOption => {
        navOption.addEventListener('mouseover', function() {
            navOption.classList.add('active');
        })
        
        navOption.addEventListener('mouseout', function() {
            navOption.classList.remove('active');
        })
    })
    
})