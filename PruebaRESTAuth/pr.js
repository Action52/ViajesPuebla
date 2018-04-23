var urlRestRegister = "http://127.0.0.1:8000/rest-auth/registration/"; //POST
var urlRestInicioSesion = "http://127.0.0.1:8000/rest-auth/login/"; //POST
function UserObject(myUsername, myPassword1, myPassword2, myEmail, csrftoken) {

    this.username = myUsername;
    this.password1 = myPassword1;
    this.password2 = myPassword2;
    this.email = myEmail;
    this.csrftoken = '{{ csrf_token }}';
    this.toJsonString = function () { return JSON.stringify(this); }; //Parsear a JSON el objeto
};

function UserLoginObject(myUsername, myPassword1, myEmail) {
    this.username = myUsername;
    this.password = myPassword1;
    this.email = myEmail;
    this.csrftoken = '{{ csrf_token }}';
    this.toJsonString = function () { return JSON.stringify(this); }; //Parsear a JSON el objeto
};

function pruebaRegister(){
  try
  {
  	var myData = new UserObject(
      $("#username").val(),
      $("#password1").val(),
      $("#password2").val(),
      $("#email").val()
    );

  	 jQuery.ajax({
           type: "POST",
           url: urlRestRegister,
           data: myData.toJsonString(), //Lo convertimos a json para que el back lo reciba así
           crossDomain: true,
           headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
           },
           success: function (response) {
                alert(response);
           },

           error: function(XMLHttpRequest, textStatus, errorThrown) {
             alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
           }


       });

   }
   catch(error)
   {
    alert(error);
   }
}

function iniciarSesion(){
  try
  {
    var myData = new UserLoginObject(
      $("#usernameIS").val(),
      $("#passwordIS").val(),
      $("#email").val()
    );

     jQuery.ajax({
           type: "POST",
           url: urlRestInicioSesion,
           data: myData.toJsonString(), //Lo convertimos a json para que el back lo reciba así
           crossDomain: true,
           headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
           },
           success: function (response) {
                alert(JSON.stringify(response));
           },
           error: function(XMLHttpRequest, textStatus, errorThrown) {
             alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
           }


       });

   }
   catch(error)
   {
    alert(error);
   }
}
