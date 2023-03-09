document.addEventListener('DOMContentLoaded', function() {
        //Create Profile Modal



        //Create Profile Add User Button
        const addUserButton = document.querySelector('#add-user-in-form');

        addUserButton.addEventListener('click', function() {
            var userField = document.createElement('input');
            userField.setAttribute('type', 'text');
            userField.setAttribute('name', 'users[]');
            userField.classList.add('input-field');
    
            var createProfileFields = document.querySelector('#create-profile-form-fields');
            createProfileFields.appendChild(userField);
        })

        const createProfileModal = document.querySelector('#create-profile-modal');
        const createProfileModalButton = document.querySelector('#create-profile-button');
        const createProfileModalClose = document.querySelector('#create-profile-close');
    
        createProfileModalButton.addEventListener('click', function() {
            createProfileModal.style.display = 'flex';
        })
    
        createProfileModalClose.addEventListener('click', function() {
            createProfileModal.style.display = 'none';
        })
    
        window.addEventListener('click', function(event) {
            if (event.target == createProfileModal) {
                createProfileModal.style.display = 'none';
            }
        })
    
})