$(document).ready(function(){
    minimap = L.map('minimap');
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(minimap); 
    markerDrag = L.marker([0,0],{draggable:true}); //marker draggable to locate the new bar in the minimap
    
    map = L.map('map');
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map); 
    markersLayer = L.layerGroup();   //layer with all markers in the map
   
    
    //bar_list is the list of bars given by django, sorted by price
    bar_list = _.sortBy(bar_list, function(obj){ return obj.fields.price;});    
    paintBars();
    
    
    
    function paintBars(){          //this function creates markers on the map
        for (i in bar_list){
            var marker = new L.marker([bar_list[i].fields.latitude, bar_list[i].fields.longitude],{
                        title:bar_list[i].fields.name+' '+bar_list[i].fields.price+'€'
                        })   
            marker.on('click',function(e) {
                    var latlng=this.getLatLng();
                    var barfound = _.find(bar_list, function(obj){ 
                                        return obj.fields.latitude == latlng.lat && obj.fields.longitude == latlng.lng; });
                    fillBarInfo(barfound);
            });
            markersLayer.addLayer(marker);
        }
        markersLayer.addTo(map);
        $('#barList ul').html('');
        fillBarList();
    }
    
    
   function fillBarList(){         //this function lists the bars on the left side of the map inside the div "barList"
        for (i in bar_list){
            $('#barList ul').append('<li id='+bar_list[i].pk+'>'+bar_list[i].fields.name+' <span>'+bar_list[i].fields.price+'€'+'</li>');
        }
        
        
        $( '#barList li' ).click(function( event ) {
          var pk=this.id;
          var barfound = _.find(bar_list, function(obj){ 
                                            return obj.pk == pk; });
          fillBarInfo(barfound);
        });
   
   };
   
   
   
   function fillBarInfo(bar){       //this function prints the info of the objet bar given as a parameter
        $('#barInfo').html('<h3>'+bar.fields.name+'</h3><h6>'+bar.fields.street+'</h6> Precio de la caña: '+bar.fields.price+'€')
   };
   
    
    $("#addBarForm").validate({         //Takes data form, validates and sends it to the view with ajax
        rules: {
            nameForm: { required: true, minlength: 2},
            priceForm: { required: true},
            latForm: { required:true},
            lonForm: { required:true}
        },
        messages: {
            nameForm: "Introduzca el nombre del Bar",
            priceForm: "Introduzca un precio",
        },
        submitHandler: function(form){
            var dataDic =   {"nameForm":$('#nameForm').val(),
                            "streetForm":$('#streetForm').html(),
                            "priceForm":$('#priceForm').val(),
                            "latForm":$('#latForm').val(),
                            "lonForm":$('#lonForm').val()}
                            
            var responseAjax= $.ajax({
                type: "POST",
                url: "/addBar",
                data: dataDic,
                success: function(data){
                        if (data=='error'){alert("Este bar ya existe!")}
                        else{
                            bar_list=jQuery.parseJSON(data);                       
                            bar_list = _.sortBy(bar_list, function(obj){ return obj.fields.price;}); 
                            markersLayer.clearLayers();
                            paintBars();
                        }
                }
            });          
        }
    });  
    
    // Geolocation
        
    map.locate();
    minimap.locate();

    function onLocationFound(e) {
        
        var radius = e.accuracy / 2;
        L.marker(e.latlng).addTo(map);
        L.circle(e.latlng, radius).addTo(map);
        map.setView(e.latlng, 17);
        minimap.setView(e.latlng, 18);
        
       
        markerDrag.setLatLng(e.latlng).addTo(minimap);
        LatLngOnForm(e.latlng);
              
    }

    markerDrag.on('dragend', function(e) { 
            LatLngOnForm(markerDrag.getLatLng());
        }); 
        
    function LatLngOnForm(latlng){ //fills authomatic values in the form
            $('#latForm').val(latlng.lat.toFixed(7));
            $('#lonForm').val(latlng.lng.toFixed(7));
            
            
            var addressInfo = searchAddress(latlng.lat,latlng.lng);
            
            var data=addressInfo.display_name.split(', ');

            $('#nameForm').val(data[0]);
            $('#streetForm').html(data[1]);
    }

    // geolocation error message
    map.on('locationfound', onLocationFound);
    minimap.on('locationfound', onLocationFound);

            function onLocationError(e) {
        alert(e.message);
    }

    map.on('locationerror', onLocationError);
    minimap.on('locationerror', onLocationError);
    
    
    
    function searchAddress(lat,long) {  //takes the address from nominatim
          var datos;
              $.ajax({
                url: 'http://open.mapquestapi.com/nominatim/v1/reverse.php?format=json&lat='+lat+'&lon='+long,
                dataType: 'json',
                async: false,            
                success: function(data) {
                  datos = data;
                }
              });
          if (datos==undefined){ return ""}
          
          return datos;
    };
    
    
    
});


