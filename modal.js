
var modals = document.getElementsByClassName('bg-modal');
var btns = document.getElementsByClassName("button");
var spans = document.getElementsByClassName("close-modal");

for(let i=0;i<btns.length;i++){
    btns[i].onclick = function() {
       modals[i].style.display = "flex";
    }
 }
 for(let i=0;i<spans.length;i++){
     spans[i].onclick = function() {
        modals[i].style.display = "none";
     }
  }
