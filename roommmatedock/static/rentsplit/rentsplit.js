document.addEventListener('DOMContentLoaded', function() {

    //TABS
    const userTab = document.querySelector('#tab-userid');
    const expenseTab = document.querySelector('#tab-expenseid');
    const resultsTab = document.querySelector('#tab-resultsid');

    const userApp = document.querySelector('#app-userid');
    const expensesApp = document.querySelector('#app-expenseid');
    const resultsApp = document.querySelector('#app-resultsid');

    //Default show Create Profile
    userApp.style.display = 'flex';
    expensesApp.style.display = 'none';
    resultsApp.style.display = 'none';

    userTab.addEventListener('click', function() {
        userApp.style.display = 'flex';
        expensesApp.style.display = 'none';
        resultsApp.style.display = 'none';
    })

    expenseTab.addEventListener('click', function() {
        userApp.style.display = 'none';
        expensesApp.style.display = 'flex';
        resultsApp.style.display = 'none';
    })

    resultsTab.addEventListener('click', function() {
        userApp.style.display = 'none';
        expensesApp.style.display = 'none';
        resultsApp.style.display = 'flex';
    })

    //MODAL FOR EXPENSES
    const expenseModal = document.querySelector('#expense-modalid');
    const expenseModalButton = document.querySelector('#expense-modal-openid');
    const expenseClose = document.querySelector('#expense-closeid');

    expenseModalButton.addEventListener('click', function(){
        expenseModal.style.display = 'flex';
    })

    expenseClose.addEventListener('click', function() {
        expenseModal.style.display = 'none';
    })

    window.onclick = function(event) {
        if (event.target == expenseModal) {
            expenseModal.style.display = 'none';
        }
    }
    

})