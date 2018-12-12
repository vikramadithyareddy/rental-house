
  var delay = 100;
  var infowindow = new google.maps.InfoWindow();
  var latlng = new google.maps.LatLng(17.3850, 78.4867);
  var mapOptions = {
    zoom: 15,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  var geocoder = new google.maps.Geocoder();
  var map = new google.maps.Map(document.getElementById("map"), mapOptions);
  var bounds = new google.maps.LatLngBounds();

  function geocodeAddress(address, next) {
    geocoder.geocode({address:address}, function (results,status)
      {
         if (status == google.maps.GeocoderStatus.OK) {
          var p = results[0].geometry.location;
          var lat=p.lat();
          var lng=p.lng();
          createMarker(address,lat,lng);
        }
        else {
           if (status == google.maps.GeocoderStatus.OVER_QUERY_LIMIT) {
            nextAddress--;
            delay++;
          } else {
                        }
        }
        next();
      }
    );
  }
 function createMarker(add,lat,lng) {
   var contentString = add;
   var marker = new google.maps.Marker({
     position: new google.maps.LatLng(lat,lng),
     map: map,
           });

  google.maps.event.addListener(marker, 'click', function() {
     infowindow.setContent(contentString);
     infowindow.open(map,marker);
   });

   bounds.extend(marker.position);

 }
  var locations = [
           'hyderabad', 'India'

  ];
  var nextAddress = 0;
  function theNext() {
    if (nextAddress < locations.length) {
      setTimeout('geocodeAddress("'+locations[nextAddress]+'",theNext)', delay);
      nextAddress++;
    } else {
      map.fitBounds(bounds);
    }
  }
 theNext();
