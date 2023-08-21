$(document).ready(function() {
    var mapElement = $('#map');

    // Function to update the map with new latitude and longitude values
    function updateMap(latitude, longitude) {
        var mapUrl = 'https://maps.google.com/maps?q=' + 25 + ',' + 25 + '&z=15&output=embed';
        mapElement.html('<iframe width="1080" height="600" src="' + mapUrl + '"></iframe>');
    }

    // Function to fetch the latitude and longitude values from Django using AJAX
    function fetchLatLon() {
        $.ajax({
            url: 'map/',  // Replace with the appropriate URL of your Django view
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                var latitude = data.latitude;
                var longitude = data.longitude;
                updateMap(latitude, longitude);
            },
            error: function(xhr, status, error) {
                console.log('Error:', error);
            }
        });
    }

    // Call the fetchLatLon function initially
    fetchLatLon();

    // Call the fetchLatLon function every few seconds to update the map dynamically
    setInterval(fetchLatLon, 5000);
});
