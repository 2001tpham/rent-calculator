document.addEventListener('DOMContentLoaded', function() {
    //MESSAGES CLOSE BUTTON
    const closeMessage = document.querySelector('#close-messages');
    const messageContainer = document.querySelectorAll('.message-container');

    closeMessage.onclick = () => {
        messageContainer.forEach(messageContainer => {
            messageContainer.classList.add('active');

        messageContainer.addEventListener('animationend', function() {
            messageContainer.style.display = 'none';
        }, {once: true});

        })
    }
})