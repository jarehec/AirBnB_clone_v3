$(document).ready(function () {
	const amenities = {};
	$('input[type="checkbox"]').click(function () {
		const amenityId = $(this).attr('data-id');
		const amenityName = $(this).attr('data-name');
		if ($(this).prop('checked') === true) {
			amenities[amenityId] = amenityName;
		} else if ($(this).prop('checked') === false) {
			delete amenities[amenityId];
		}
		const amenityList = Object.values(amenities).join(', ');
		if (amenityList.length > 30) {
			$('.amenities h4').text(amenityList.substring(0, 29) + '...');
		} else {
			$('.amenities h4').text(amenityList);
		}
		if ($.isEmptyObject(amenities)) {
			$('.amenities h4').html('&nbsp;');
		}
	});
	$.ajax(
		{
			url: 'http://0.0.0.0:5001/api/v1/status/',
			type: 'GET',
			dataType: 'json',
			success: function (response) {
				if (response.status === 'OK') {
					$('DIV#api_status').addClass('available');
				} else {
					$('DIV#api_status').removeClass('available');
				}
			},
			error: function (error) {
				$('DIV#api_status').removeClass('available');
			}
		});
	$.ajax(
		{
			url: 'http://0.0.0.0:5001/api/v1/places_search/',
			type: 'POST',
			dataType: 'json',
			contentType: "application/json",
			data: JSON.stringify({}),
			success: function (response) {
				console.log(response[0].name)
				$( "section.places" ).html('<article>\
				<div class="title">\
					<h2>' +
					JSON.stringify(response[0].name) +
					'</h2>\
					$("h2").text(response[0].name)\
					<div class="price_by_night">\
					{{ place.price_by_night }}\
					</div>\
					</div>\
					<div class="information">\
					<div class="max_guest">\
					<i class="fa fa-users fa-3x" aria-hidden="true"></i>\
					<br />\
					{{ place.max_guest }} Guests\
					</div>\
					<div class="number_rooms">\
					<i class="fa fa-bed fa-3x" aria-hidden="true"></i>\
					<br />\
					{{ place.number_rooms }} Bedrooms\
					</div>\
					<div class="number_bathrooms">\
					<i class="fa fa-bath fa-3x" aria-hidden="true"></i>\
					<br />\
					{{ place.number_bathrooms }} Bathroom\
					</div>\
					</div>\
					<!-- **********************\
					USER\
					**********************  -->\
					<div class="user">\
					<strong>Owner: {{ users[place.user_id] }}</strong>\
					</div>\
					<div class="description">\
					{{ place.description }}\
					</div>\
					</article>\
				');
			}
		});
});
