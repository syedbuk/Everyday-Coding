
function playsound(key){

    switch (key) {
       
        

        case:'w':
            var tom1 = new Audio('sounds/tom-1.mp3');
            tom1.play();
            break;

        case:'a':
            var tom2 = new Audio('sounds/tom-2.mp3');
            tom2.play();
            break;
        case:'s':
            var tom3 = new Audio('sounds/tom-3.mp3');
            tom3.play();
            break;
        case:'d':
            var tom4 = new Audio('sounds/tom-4.mp3');
            tom4.play();
            break;          




document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click',function(event){

        var buttonInnerHTML = this.innerHTML;

        playsound(buttonInnerHTML);

    })