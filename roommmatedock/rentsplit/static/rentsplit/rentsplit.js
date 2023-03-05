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
    const expenseClose = document.querySelector('#expenses-closeid');

    expenseModalButton.addEventListener('click', function(){
        expenseModal.style.display = 'flex';
    })

    expenseClose.addEventListener('click', function() {
        expenseModal.style.display = 'none';
    })

    expenseModal.addEventListener('click', function() {
        expenseModal.style.display = 'none';
    })
    
    //MODAL FOR RENT
    const rentModal = document.querySelector('#rent-modalid');
    const rentModalButton = document.querySelector('#rent-buttonid');
    const rentModalClose = document.querySelector('#rent-closeid');

    rentModalButton.addEventListener('click', function() {
        rentModal.style.display = 'flex';
    })

    rentModalClose.addEventListener('click', function() {
        rentModal.style.display = 'none';
    })

    rentModal.addEventListener('click', function() {
        rentModal.style.display = 'none';
    })

    //MODAL FOR EXPENSE CARD
    const expenseCardModal = document.querySelector('#expense-card-modalid');
    const expenseCardButton = document.querySelector('#expense-card');
    const expenseCardClose = document.querySelector('#expense-card-closeid');

    expenseCardButton.addEventListener('click', function() {
        expenseCardModal.style.display = 'flex';
    })

    expenseCardClose.addEventListener('click', function() {
        expenseCardModal.style.display = 'none';
    })

    expenseCardModal.addEventListener('click', function() {
        expenseCardModal.style.display = 'none';
    })
})