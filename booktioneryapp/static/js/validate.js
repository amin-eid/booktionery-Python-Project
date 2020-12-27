var check = function() {
  if (document.getElementById('password').value ==
    document.getElementById('confirm').value) {
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = 'passwords are matching';
  } else {
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'passwords are not matching';
  }
}