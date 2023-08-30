document.addEventListener('DOMContentLoaded', function() {

    const logoutLink = document.querySelector('#logout-link');
    logoutLink.addEventListener('click', function(event) {
        event.preventDefault();
        logout();
    });
});

function logout() {
    fetch('/logout')
        .then(response => {
            if (response.ok) {
                window.location.href = '/';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
