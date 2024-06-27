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

//function selectOffice(){
//    let rostov = document.getElementById('RND');
//    let msk = document.getElementById('MSK');
//    let rostov = document.getElementById('SPB');
//    let select = document.getElementById('city');
//    console.log('Зашел в функцию');
//    select.addEventListener('change', function(e) {
//        if (select.value == '1'){
//            console.log('Выбран Ростов');
//            rostov.style.display = "Block";
//            msk.style.display = "None";
//            spb.style.display = "None";
//
//        }
//        else if (select.value == '2'){
//            msk.style.display = "Block";
//            rostov.style.display = "None";
//            spb.style.display = "None";
//            console.log('Выбран МСК');
//
//        }
//        else if (select.value == '3'){
//            spb.style.display = "Block";
//            msk.style.display = "None";
//            rostov.style.display = "None";
//            console.log('Выбран СПБ');
//        }
//        else{
//        console.log('елсе');
//        }
//
//	}
//}
//
//selectOffice()

})();