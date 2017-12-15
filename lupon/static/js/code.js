// THIS IS OUR JS CODE FILE
console.log('java script is active');
window.onload = function () {
    console.log('page has loaded bitch');
    document.getElementById('add_task').addEventListener("click",intercept);
    console.log('dom manipulated')
}



function intercept() {
    alert('action was intercepted');
}

