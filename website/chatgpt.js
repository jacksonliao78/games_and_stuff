// Get the form element
var form = document.querySelector("form");

// Listen for submit events on the form
form.addEventListener("submit", function(event) {
  // Prevent the form from being submitted
  event.preventDefault();

  // Get the values of the name, email, and message fields
  var name = document.querySelector("input[name='name']").value;
  var email = document.querySelector("input[name='email']").value;
  var message = document.querySelector("textarea[name='message']").value;

  // Log the values to the console
  console.log("Name: " + name);
  console.log("Email: " + email);
  console.log("Message: " + message);

  // Clear the form fields
  document.querySelector("input[name='name']").value = "";
  document.querySelector("input[name='email']").value = "";
  document.querySelector("textarea[name='message']").value = "";
});
