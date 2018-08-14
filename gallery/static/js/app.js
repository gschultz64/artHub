// Change Active Class on Navigation Links
var pathname = window.location.pathname;
if (pathname !== '/') {
  $("#home").removeClass("active");
  if (pathname === '/login/') {
    $('#login').addClass('active');
  } else if (window.location.toString().includes('/user/')
    && window.location.toString().includes('/upload/')) {
    $('#upload').addClass('active');
  } else if (pathname === '/chat/') {
    $('#chat').addClass('active');
  } else if (pathname === '/signup/') {
    $('#signup').addClass('active');
  } else if (window.location.toString().includes('/user/')){
    $('#profile').addClass('active');
  } 
}
$('.like-btn').on('click', function (e) {
  
  e.preventDefault();
  var element = $(this);
  $.ajax({
    url: '/like_img/',
    method: 'GET',
    data: {
      media_id: element.attr('data-id')
    },
    success: function (response) {
      element.html('Likes: ' + response)
    }
  })
})