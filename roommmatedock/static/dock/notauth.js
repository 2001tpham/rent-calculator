document.addEventListener('DOMContentLoaded', function() {
    const loggedOutButton = document.querySelectorAll('.logged-out-nav-btn');

    loggedOutButton.forEach(loggedOutButton => {
        loggedOutButton.addEventListener('mouseover', function() {
            loggedOutButton.classList.add('active');
        })
        loggedOutButton.addEventListener('mouseout', function() {
            loggedOutButton.classList.remove('active');
        })
    })
})