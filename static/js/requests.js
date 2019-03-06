$('#signup').submit(function(e) {
  e.preventDefault();
  var data = {
        username : $('input[name=username]').val(),
        email : $('input[name=email]').val(),
        password : $('input[name=password]').val(),
    };
    $.ajax({
      url: '/signup',
      type: 'POST',
      dataType: 'text json',
      headers: {'X-CSRFToken': $.cookie('csrftoken')},
      contentType: 'application/json',
      processData: false,
      data: JSON.stringify(data),
      success: function(data){
        window.location.href = '/login'
      },
      error: function(data){
        console.log('error!');
      },
    });
});

$('#login').submit(function(e) {
  e.preventDefault();
  var data = {
        username : $('input[name=username]').val(),
        password : $('input[name=password]').val(),
    };
    console.log(data);
    $.ajax({
      url: '/signin',
      type: 'POST',
      dataType: 'text json',
      headers: {'X-CSRFToken': $.cookie('csrftoken')},
      contentType: 'application/json',
      processData: false,
      data: JSON.stringify(data),
      success: function(data){
        console.log(data);
        window.location.href = '/profile'
      },
      error: function(data){
        console.log(data);
      },
    });
});
$('#logout').click(function(e) {
  e.preventDefault();
    $.ajax({
      url: 'logout_profile',
      type: 'POST',
      dataType: 'text json',
      headers: {'X-CSRFToken': $.cookie('csrftoken')},
      contentType: 'application/json',
      processData: false,
      success: function(data){
        window.location.href = '/login'
      },
      error: function(data){
        console.log('Error!');
      },
    });
});
