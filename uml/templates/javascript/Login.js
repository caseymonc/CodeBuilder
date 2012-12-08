// JavaScript Document

var login = function(url){
	username = $('#email').val();
	password = $('#password').val();
	data = {'email' : username, 'password' : password}	
	$.post('/api/login/', data, function(data){
		window.location = '/model/';
	});
}
