Activate=document.querySelector(".button")



function voice(){
  var recogniton = new webkitSpeechRecognition();
  recogniton.lang="en-GB";
  recogniton.onresult=function(event){
    console.log(event);
    document.getElementById("speechtotext").value=
    event.results[0][0].transcript;
  }
  recogniton.start();



}

Activate.addEventListener("click" , () =>{
  window.location.pathname='/alfred'
})
