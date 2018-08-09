// Change Active Class on Navigation Links
var pathname = window.location.pathname;
if (pathname !== '/') {
  $("#home").removeClass("active");
  if (pathname === '/login/') {
    $('#login').addClass('active');
  } else if (pathname === '/upload') {
    $('#upload').addClass('active');
  } else if (pathname === '/profile') {
    $('#profile').addClass('active');
  }
}
