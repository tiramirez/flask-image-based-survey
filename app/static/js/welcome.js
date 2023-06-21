
$(document).ready(function(){

$("#next0").click(function(){
  $("div#text0").hide();
  $("div#text1").show();
  $("div#title-instructions").show();
});

$("#next1").click(function(){
  $("div#text1").hide();
  $("div#text2").show();
});

$("#next1b").click(function(){
  $("div#text1").hide();
  $("div#text2").show();
});

$("#next1c").click(function(){
  $("div#text1").hide();
  $("div#text2").show();
});

$("#back1").click(function(){
  $("div#text1").hide();
  $("div#text0").show();
  $("div#title-instructions").hide();
});

$("#next2").click(function(){
  $("div#text2").hide();
  $("div#text3").show();
});

$("#next2b").click(function(){
  $("div#text2").hide();
  $("div#text3").show();
});

$("#back2").click(function(){
  $("div#text2").hide();
  $("div#text1").show();
});

$("#next3").click(function(){
  $("div#text3").hide();
  $("div#text4").show();
});

$("#next3b").click(function(){
  $("div#text3").hide();
  $("div#text4").show();
});

$("#back3").click(function(){
  $("div#text3").hide();
  $("div#text2").show();
});

$("#back4").click(function(){
  $("div#text4").hide();
  $("div#text3").show();
});

$("#next4").click(function(){
  $("div#text4").hide();
  $("div#text5").show();
});

$("#back5").click(function(){
  $("div#text5").hide();
  $("div#text4").show();
});



$("#next-responsive-0").click(function(){
  $("div#text-responsive-0").hide();
  $("div#text-responsive-1").show();
});

$("#next-responsive-1").click(function(){
  $("div#text-responsive-1").hide();
  $("div#text-responsive-2").show();
});

$("#back-responsive-1").click(function(){
  $("div#text-responsive-1").hide();
  $("div#text-responsive-0").show();
});

$("#next-responsive-2").click(function(){
  $("div#text-responsive-2").hide();
  $("div#text-responsive-3").show();
});

$("#back-responsive-2").click(function(){
  $("div#text-responsive-2").hide();
  $("div#text-responsive-1").show();
});

$("#next-responsive-3").click(function(){
  $("div#text-responsive-3").hide();
  $("div#text-responsive-4").show();
});

$("#back-responsive-3").click(function(){
  $("div#text-responsive-3").hide();
  $("div#text-responsive-2").show();
});

$("#next-responsive-4").click(function(){
  $("div#text-responsive-4").hide();
  $("div#text-responsive-5").show();
});

$("#back-responsive-4").click(function(){
  $("div#text-responsive-4").hide();
  $("div#text-responsive-3").show();
});

$("#back-responsive-5").click(function(){
  $("div#text-responsive-5").hide();
  $("div#text-responsive-4").show();
});

});  