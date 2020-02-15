$(document).ready(function() {
	let amenities = {}
	$('input[type="checkbox"]').click(function(){
		if($(this).is(":checked")){
			alert("Checkbox is checked.");
		}
		else if($(this).is(":not(:checked)")){
			alert("Checkbox is unchecked.");
		}
	});
})
