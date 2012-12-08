var saveMember = function(member_id, class_id){	

	json = {'class_id' : class_id, 
			'member_name' : $('#memberName').val(),
			'access' : $('input[name=access]:checked').val(),
			'abstract' : $('#abstract').is(':checked') ? 1 : 0,
			'final' : $('#final').is(':checked') ? 1 : 0,
			'member_type' : $('#type option:selected').val()};
	if(member_id == -1)
		member_id = 'new';
	$.post('/api/class/' + class_id + '/member/' + member_id + '/', json, function(data){
			$.mobile.changePage( "/model/class/" + class_id + "/", {
            	panel: "main"
            });
	});
}

var deleteMember = function(member_id, class_id){
	$.ajax({
    url: '/api/class/' + class_id + '/member/' + member_id + '/',
    type: 'DELETE',
    success: function(result) {
        $.mobile.changePage( "/model/class/" + class_id + "/", {
            	panel: "main"
            });
    }
});}
