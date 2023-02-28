document.addEventListener('DOMContentLoaded', function() {

    //TABS
    const createProfileTab = document.querySelector('#tab-guest-create-profileid');
    const expenseTab = document.querySelector('#tab-guest-expenseid');
    const resultsTab = document.querySelector('#tab-guest-resultsid');

    const createProfileApp = document.querySelector('#app-guest-create-profileid');
    const expensesApp = document.querySelector('#app-guest-expenseid');
    const resultsApp = document.querySelector('#app-guest-resultsid');

    //Default show Create Profile
    createProfileApp.style.display = 'flex';
    expensesApp.style.display = 'none';
    resultsApp.style.display = 'none';

    createProfileTab.addEventListener('click', function() {
        createProfileApp.style.display = 'flex';
        expensesApp.style.display = 'none';
        resultsApp.style.display = 'none';
    })

    expenseTab.addEventListener('click', function() {
        createProfileApp.style.display = 'none';
        expensesApp.style.display = 'flex';
        resultsApp.style.display = 'none';
    })

    resultsTab.addEventListener('click', function() {
        createProfileApp.style.display = 'none';
        expensesApp.style.display = 'none';
        resultsApp.style.display = 'flex';
    })




})