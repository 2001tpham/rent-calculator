document.addEventListener('DOMContentLoaded', function() {

    //TABS
    const createProfileTab = document.querySelector('#tab-create-profileid');
    const expenseTab = document.querySelector('#tab-expenseid');
    const resultsTab = document.querySelector('#tab-resultsid');

    const createProfileApp = document.querySelector('#app-create-profileid');
    const expensesApp = document.querySelector('#app-expenseid');
    const resultsApp = document.querySelector('#app-resultsid');

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