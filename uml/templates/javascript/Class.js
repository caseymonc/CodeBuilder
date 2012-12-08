var saveClass = function(class_id){	
	var extend = $('#extends option:selected').val();
	var interfaces = ''; 
	$('#implements option:selected').each(function(i, selected){ 
		if(i != 0){
			interfaces += ',';
		}	  
		interfaces += $(selected).val(); 
	});

	json = {'class_id' : class_id, 
			'class_name' : $('#className').val(),
			'access' : $('input[name=access]:checked').val(),
			'abstract' : $('#abstract').is(':checked') ? 1 : 0,
			'final' : $('#final').is(':checked') ? 1 : 0};

	if(extend != '' && extend != undefined)
		json.class_extends = extend;
	if(interfaces.length > 0){
		json.interfaces = interfaces
	}
	if(class_id == -1)
		class_id = 'new';
	$.post('/api/class/' + class_id + '/', json, function(data){
			if(class_id != 'new')
				$('#class-' + class_id).text($('#className').val())
			else{
				$('#classes').append('<li><a href="class/'+ data.class_id +'" data-transition="fade" data-panel="main" id="class-'+ data.class_id +'">'+ data.class_name +'</a></li>');
				$('#classes').listview('refresh');
				$.mobile.changePage( "/model/class/" + data.class_id + "/", {
                	panel: "main"
                });
			}
	});
}

var deleteClass = function(class_id){
	$.ajax({
    url: '/api/class/' + class_id + '/',
    type: 'DELETE',
    success: function(result) {
        $('#class-' + class_id).remove();
		$('#classes').listview('refresh');
		$.mobile.changePage( "/model/", {panel: "main"});
    }
});}
