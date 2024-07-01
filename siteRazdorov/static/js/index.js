(() => {
$(function(){
  // Маски
  $('input[name="PHONE"]').mask("+7 (999)-999-99-99"); // Телефон
})

function getIPFromAmazon() {
  fetch('https://checkip.amazonaws.com/')
    .then((res) => res.text())
    .then((data) => localStorage.setItem("IPClient", data));
}
getIPFromAmazon();

function getReferSite(){
  let referSite = new URL(document.referrer).hostname;
  let locationHost = window.location.host;

  	if (localStorage.getItem("referSite"))
    {
      if (referSite != locationHost && referSite != localStorage.getItem("referSite")){
        localStorage.setItem("referSite", referSite);
      }
      else{
      }
    }

  else{
   localStorage.setItem("referSite", referSite);
  }

}
getReferSite()

function getNamePage(){
    var namePage = document.getElementById('namePage');
    if (namePage.value == 'None'){
    namePage.value = window.location.pathname;
    }
}
getNamePage()



})();