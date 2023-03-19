document.addEventListener('DOMContentLoaded', function() {
    const modalBody = document.querySelectorAll('.modal-body');
    
    const replyModal = document.querySelector('#reply-modalid');
    const replyModalButton = document.querySelector('#reply-buttonid');
    const replyModalClose = document.querySelector('#reply-closeid');

    replyModalButton.addEventListener('click', function() {
        modalBody.forEach(modalBody => {
            modalBody.classList.remove('active');
        })
        replyModal.style.display = 'flex';
    })

    replyModalClose.addEventListener('click', function() {
        modalBody.forEach(modalBody => {
            modalBody.classList.add('active');
        })
        
        replyModal.addEventListener('animationend', function() {
            modalBody.forEach(modalBody => {
                if (modalBody.classList.contains('active')) {
                    replyModal.style.display = 'none';
                }
            })        
        })        
    })

    window.onclick = function(event) {
        if (event.target == replyModal) {
            replyModal.style.display = 'none';
        }
    }
})