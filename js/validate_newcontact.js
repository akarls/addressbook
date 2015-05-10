document.getElementById("new_contact").addEventListener('submit', function(event) {
  var field_firstname = document.getElementById('name').value;
  var field_lastname = document.getElementById('surname').value;
  var field_email = document.getElementById('email').value;
  var pattern = /^([a-zA-Z0-9_.-])+@([a-zA-Z0-9_.-])+\.([a-zA-Z])+([a-zA-Z])+/;
  var isValid = pattern.test(field_email);

  if (field_firstname == "") {
    alert("Fyll i ett namn!");
	    event.preventDefault();
  }
  if (field_lastname == "") {
    alert("Fyll i ett efternamn!");
	    event.preventDefault();
  }

  if (isValid == false) {
    alert("Eposten är ifylld inkorrekt!");
    event.preventDefault();
  }
});

