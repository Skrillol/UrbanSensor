function iniciarMap(){
    var coord = {lat:-33.4275384 ,lng: -70.6112534};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 12,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}