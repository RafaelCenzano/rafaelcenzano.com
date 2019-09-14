// Set the date we're counting down to
var countUpDate = new Date("Sep 1, 2017 0:0:0").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();
    
  // Find the distance between now and the count down date
  var distance = now - countUpDate;
    
  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var years = Math.floor(days / 365);
  var months = Math.floor((days / 29) - (years * 12))
  
  var pluralOrNot = "year ";
  if (years > 0) {
    pluralOrNot = "years ";
  }
  var pluralOrNotMonth = "month ";
  if (months > 0) {
    pluralOrNotMonth = "months ";
  }

  // Output the result in an element with id="demo"
  document.getElementById("jyl").innerHTML = "~ " + years + pluralOrNot + months + pluralOrNotMonth + " ~";
}, 1000);