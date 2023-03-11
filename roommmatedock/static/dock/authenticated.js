document.addEventListener('DOMContentLoaded', function() {
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

    const profileOption = document.querySelector('#hover-profile-dropdownid');

    profileOption.addEventListener('mouseover', function() {
        profileOption.classList.add('active');
    })
    
    profileOption.addEventListener('mouseout', function() {
        profileOption.classList.remove('active');
    })
})