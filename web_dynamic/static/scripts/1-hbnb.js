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
});
