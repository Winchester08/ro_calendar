$(document).ready(function (){

  $(".abrirm").click(function(){
    //alert("Abriendo Modal");
    $('#myModal').modal('show');
});
$("#cierra").click(function(){
  $('#myModal').modal('hide');
})
$(".close").click(function(){

  $('#myModal').modal('hide');
})

});

