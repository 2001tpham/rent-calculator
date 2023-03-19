document.addEventListener('DOMContentLoaded', function() {
    const settingsForm = document.querySelectorAll('.settings-form');

    settingsForm.forEach(function(settingsForm) {
        if (!settingsForm.classList.contains('hidden')) {
            settingsForm.classList.add('hidden');
        }
    })

    //PROFILE NAME CHANGE
    const changeName = document.querySelector('#settings-change-name');
    const formName = document.querySelector('#settings-form-name');

    changeName.onclick = function() {
        formName.classList.remove('hidden');
    }

    //PROFILE NAME CHANGE
    const changeDesc = document.querySelector('#settings-change-description');
    const formDesc = document.querySelector('#settings-form-description');

    changeDesc.onclick = function() {
        formDesc.classList.remove('hidden');
    }

    //DELETE PROFILE
    const deleteModal = document.querySelector('#delete-modal');
    const deleteButton = document.querySelector('#delete-profile-button');
    const deleteClose = document.querySelector('#delete-modal-close');
    const deleteCancel = document.querySelector('#delete-modal-cancel');
    const ModalBody = document.querySelectorAll('modal-body');

    deleteButton.addEventListener('click', function() {
        ModalBody.forEach(ModalBody => {
            ModalBody.classList.remove('active');
        })
        deleteModal.style.display = 'flex';
    })
    
    deleteClose.addEventListener('click', function() {
        ModalBody.forEach(ModalBody => {
            ModalBody.classList.add('active');
        })
        
        deleteModal.addEventListener('animationend', function() {
            deleteModal.style.display = 'none';
        })
    })
    
    deleteCancel.addEventListener('click', function() {
        ModalBody.forEach(ModalBody => {
            ModalBody.classList.add('active');
        })
        
        deleteModal.addEventListener('animationend', function() {
            ModalBody.forEach(ModalBody => {
                if (ModalBody.classList.contains('active')) {
                    deleteModal.style.display = 'none';
                }
            })        })
    })
    
    window.addEventListener('click', function(event) {
        if (event.target == deleteModal) {
            deleteModal.style.display = 'none';
        }
    })
})