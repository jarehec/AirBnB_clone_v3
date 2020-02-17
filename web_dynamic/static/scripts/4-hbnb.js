$(document).ready(function () {
    const amenities = {};
    let places = [];
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
			success: function (place) {
				// places = []
				$.get( "http://0.0.0.0:5001/api/v1/users/", function(users) {
					for (let i = 0; i < place.length; i++) {
						for (let j = 0; j < users.length; j++) {
							if (users[j].id === place[i].user_id) {
								// first_name = users[j].first_name
								// last_name = users[j].last_name
								places.push(
									`<article>
				<div class="title">
					<h2>
					\#${ place[i].name }
					</h2>
					<div class="price_by_night">
					\$${ place[i].price_by_night }
					</div>
					</div>
					<div class="information">
					<div class="max_guest">
					<i class="fa fa-users fa-3x" aria-hidden="true"></i>
					<br />
					${ place[i].max_guest } Guests
					</div>
					<div class="number_rooms">
					<i class="fa fa-bed fa-3x" aria-hidden="true"></i>
					<br />
					${ place[i].number_rooms } Bedrooms
					</div>
					<div class="number_bathrooms">
					<i class="fa fa-bath fa-3x" aria-hidden="true"></i>
					<br />
					${ place[i].number_bathrooms } Bathroom
					</div>
					</div>
					<!-- **********************
					USER
					**********************  -->
					<div class="user">
					<strong>Owner: ${ users[j].first_name } ${ users[j].last_name }</strong>
					</div>
					<div class="description">
					${ place[i].description }
					</div>
					</article>
							`);
							}
						}
					}
					$("section.places").append(places.join(''))
				})
			}
		});
    // console.log(places);
    $('.container .filters button').click(function () {
        $.ajax(
                {
                        url: 'http://0.0.0.0:5001/api/v1/places_search/',
                        type: 'POST',
                        dataType: 'json',
                        contentType: "application/json",
                        data: JSON.stringify({}),
                        success: function (place) {
			    let newPlace = {};
			    // console.log(place);
			    for (let l = 0; l < place.length; l++) {
				// console.log(place[0].id)
				// console.log(place[l].id)
				// console.log("http://0.0.0.0:5001/api/v1/places/" + place[l].id + "/amenities");
                                $.get( "http://0.0.0.0:5001/api/v1/places/" + place[l].id + "/amenities", function(place_amenities) {
                                        // for (let i = 0; i < place.length; i++) {
				    // console.log(place_amenities);
                                                // for (let j = 0; j < place_amenities.length; j++) {
						    for (let k = 0; k < Object.keys(amenities).length; k++) {
							// console.log("INSIDE FOR LOOP!!!");
place_amenities.forEach(dict => { if (Object.keys(amenities)[k] === dict.id) { newPlace[place[l].id]=place[l]; } }) // else { delete newPlace[place[l].id]; } } )
						}
				})
			    }
			    console.log(newPlace);
			    console.log(typeof(newPlace));
			    for (let key in newPlace) {console.log(newPlace[key])};
//			    Object.entries(newPlace).forEach( (k, v) => { console.log(k); console.log(v); } );
//			    console.log(Object.values(newPlace));
//			    console.log(newPlaceList);
		}
		}
	);
})
});
