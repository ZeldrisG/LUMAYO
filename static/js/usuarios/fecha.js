var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();
 if(dd<10){
        dd='0'+dd
    } 
    if(mm<10){
        mm='0'+mm
    } 

yyyy2 = yyyy-100;
minFecha2 = yyyy2+'-'+mm+'-'+dd;
document.getElementById("datefield2").setAttribute("min", minFecha2);
yyyy = yyyy-18;
maxFecha = yyyy+'-'+mm+'-'+dd;
document.getElementById("datefield2").setAttribute("max", maxFecha);

