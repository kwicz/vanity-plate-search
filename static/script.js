

// function queryResults(input, plateStatus, dateLastChecked, previousStatus, previousStatusDate) {
//   dmv2u.json.
// }

$(document).ready(function() {
  $("#plateSearchInput").change(function(){
    const input = $("#plateSearchInput").val();
    console.log("input: ", input);
    $.ajax({
      url: 'dmv2u.json', 
      success: function(result) {
        console.log("result: ", result[1]);
      },
      error: function (jqXHR, textStatus, errorThrown) {
        console.log("error: ", jqXHR.responseText, textStatus, errorThrown);
      }
    });
  });    
});

// $("#search-form-button").submit(function(event){
//   event.preventDefault();
//   const input = $("$plateSearchInput").val();
//   const plateStatus = $("$plateStatus").val();
//   const dateLastChecked = $("$dateLastChecked").val();
//   const previousStatus = $("$previousStatus").val();
//   const previousStatusDate = $("$previousStatusDate").val();
//   queryResults(input, plateStatus, dateLastChecked, previousStatus, previousStatusDate);
// 