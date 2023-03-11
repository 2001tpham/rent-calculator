document.addEventListener('DOMContentLoaded', function() {

    //Dropdown menu button
    // const dropdownButton = document.querySelector('#dropdown-main-btnid');
    // const dropdownMenu = document.querySelector('#dropdown-menu-containerid');
    // dropdownButton.addEventListener('click', function() {
    //     dropdownMenu.classList.toggle('open-menu');
    // })

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
    
    //Dropdown for profile
    const dropDownProfileButton = document.querySelector('#hover-profile-dropdownid');
    const dropDownProfileMenu = document.querySelector('#dropdown-profile-containerid');

    dropDownProfileButton.addEventListener('mouseover', function() {
        dropDownProfileMenu.classList.add('open-menu');

    })

    dropDownProfileButton.addEventListener('mouseout', function() {
        dropDownProfileMenu.classList.remove('open-menu');
        
    })
    
    dropDownProfileMenu.addEventListener('mouseover', function() {
        dropDownProfileMenu.classList.add('open-menu');
    })

    dropDownProfileMenu.addEventListener('mouseout', function() {
        dropDownProfileMenu.classList.remove('open-menu');
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
    
    const profileOption = document.querySelector('#hover-profile-dropdownid');

        profileOption.addEventListener('mouseover', function() {
            profileOption.classList.add('active');
        })
        
        profileOption.addEventListener('mouseout', function() {
            profileOption.classList.remove('active');
        })

        

})