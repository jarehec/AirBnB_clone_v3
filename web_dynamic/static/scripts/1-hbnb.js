$(document).ready(function() {
	let amenities = {}
	$('input[type="checkbox"]').click(function(){
		let amenity_id = $(this).attr('data-id');
		let amenity_name = $(this).attr('data-name');
		if($(this).prop("checked") == true){
			amenities[amenity_id] = amenity_name;
			$('.amenities h4').text(Object.values(amenities).join(", "));
			console.log(JSON.stringify(amenities));
		}
		else if($(this).prop("checked") == false){
			delete amenities[amenity_id];
			$('.amenities h4').text(Object.values(amenities).join(", "));
			console.log(JSON.stringify(amenities));
		}
	});
})
