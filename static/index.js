//abababa
var position=0;
var regexinput = null
var Pageinfo = null
var dict = {



};


 $("#backbutton").click(function(){

 goBack();

 });


$("#startbutton").click(function(){

Pageinfo = "inputpage";
$("#backbutton").toggle();
$(".startpage").toggle();
$(".inputpage").toggle();

});


$("#input1").click(function(){ //First INPUT CLICKED
regexinput=1;
Pageinfo = "outputdfapage";

$(".inputpage").toggle();
  $(".outputpage").toggle();
  $("#dfabutton").toggle();
    $("#pdabutton").toggle();
      $("#cfgbutton").toggle();


  showOutput("/static/images/DFA1.png");
  $("#stringinput1").toggle();
  $("#backward").toggle();
  $("#readnext").toggle();
  $("#trace").toggle();
  $("#regex1input").toggle();


});

$("#input2").click(function(){ //SECOND INPUT CLICKED
regexinput=2;
Pageinfo = "outputdfapage";

$(".inputpage").toggle();
  $(".outputpage").toggle();
  $("#dfabutton").toggle();
    $("#pdabutton").toggle();
      $("#cfgbutton").toggle();


  showOutput("/static/images/DFA2.png");
  $("#stringinput2").toggle();
  $("#backward").toggle();
  $("#readnext").toggle();
  $("#trace").toggle();
  $("#regex2input").toggle();

});




$("#pdabutton").click(function(){ // when user clicks pda button it will show the output

if (regexinput === 1){
  showOutput("/static/images/PDA1.png");
} else {
  showOutput("/static/images/PDA2.png");
}
})

$("#dfabutton").click(function(){ //shows the output of the dfa
position = 0;
  if (regexinput === 1){
    showOutput("/static/images/DFA1.png");
  } else {
    showOutput("/static/images/DFA2.png");
  }
});

$("#cfgbutton").click(function(){ //shows the output of the dfa
position = 0;
  if (regexinput === 1){
    showOutput("/static/images/number1cfg.jpg");
  } else {
    showOutput("/static/images/number2cfg.jpg");
  }
});



$("#trace").click(function(){
  var stringinput = $("#stringinput").val();
  if ($("#stringinput").val() === "")  {
    alert("Please make sure you have inputted a string.");
  } else {
  if (regexinput === 1){
    showOutput("/static/images/DFA1.png");
  } else {
    showOutput("/static/images/DFA2.png");
  }

  TraceRegex1(stringinput);
}
});

function goBack(){

  if (Pageinfo === "outputdfapage"){
    if (regexinput === 1)
    {
      $("#stringinput1").toggle();
        $("#regex1input").toggle();
    }else {
       $("#stringinput2").toggle();
         $("#regex2input").toggle();
    }
  $("#backward").toggle();
  $("#readnext").toggle();
  $("#trace").toggle();
  $("#dfabutton").toggle();
    $("#pdabutton").toggle();
      $("#cfgbutton").toggle();


    Pageinfo = "inputpage";
    $(".outputpage").toggle();
    $(".inputpage").toggle();
}
  else if (Pageinfo === "inputpage") {
      Pageinfo = null;
      $("#backbutton").toggle();
    $(".inputpage").toggle();
    $(".startpage").toggle();
  }
}


// $("#readnext").click(function(){
//
// if ($("#stringinput").val() === "")  {
//   alert("Please make sure you have inputted a string.");
// } else {
// readnext();
// }
// });





function showOutput(directory){

  $(".outputpage #output").attr("src",directory)




}


// function traceOutput(directory){
//   $(".outputpage #output").attr("src","/static/images/states/regex1/"+directory+".png")
// }
//
// function readnext(){ //abababa
//
// traceOutput(dict[position][0]);
// console.log(dict[position][0]);
// if (position === 0){
//   position +=3;
// }else{
//   position++;
// }
//
// }


// function backwards(){ //abababa
//   if (position === 3){
//     position -=3;
//   }else{
//     position--;
//   }
//
// traceOutput(dict[position][0]);
// console.log(dict[position][0]);
//
// }




// function TraceRegex1(string){ //abababa
// var idx = 3;
// dict[0]=[0,"startstate"];
// for (let i of string)
// {
//   dict[idx]=[idx,i];
//   idx++;
//
// }
// }
