document.addEventListener('DOMContentLoaded', function() {
    const modalBody = document.querySelectorAll('.modal-body');
    
    const addMessageModal = document.querySelector('#messageboard-modalid');
    const addMessageModalButton = document.querySelector('#messageboard-button');
    const addMessageModalClose = document.querySelector('#messageboard-closeid');

    addMessageModalButton.addEventListener('click', function() {
        modalBody.forEach(modalBody => {
            modalBody.classList.remove('active');
        })
        addMessageModal.style.display = 'flex';
    })

    addMessageModalClose.addEventListener('click', function() {
        modalBody.forEach(modalBody => {
            modalBody.classList.add('active');
        })
        
        addMessageModal.addEventListener('animationend', function() {
            modalBody.forEach(modalBody => {
                if (modalBody.classList.contains('active')) {
                    addMessageModal.style.display = 'none';
                }
            })        
        })        
    })

    window.onclick = function(event) {
        if (event.target == addMessageModal) {
            addMessageModal.style.display = 'none';
        }
    }

})