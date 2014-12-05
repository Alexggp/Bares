$(document).ready(function(){


//bar_list is the list of bars given by django, sorted by price
    bar_list=[];    
    clstate=true;                                                                               //true= caña, false= litro
    tapastate=false;                                                                            //tapa or no tapa
    


// Geolocation
    
    var numIcon = L.Icon.extend({
        options: {
            shadowUrl: '/static/js/leaflet-0.7.3/images/marker-shadow.png',
            iconSize:     [35, 42],
            shadowSize:   [50, 64],
            iconAnchor:   [17, 40],
            shadowAnchor: [14, 64]
            }
        });
    

    
    minimap = L.map('minimap');
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(minimap); 
    markerDrag = L.marker([0,0],{draggable:true}); //marker draggable to locate the new bar in the minimap
    
    map = L.map('map', {zoomControl: false});
    map.addControl( L.control.zoom({position: 'bottomleft'}) )
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map); 
    markersLayer = L.layerGroup().addTo(map);   //layer with all markers in the map    
    markers_blueLayer= L.layerGroup().addTo(map);   //layer to stand out the selected bar in the map with a blue marker
    map.locate({setView: true, maxZoom: 16});    
 
 
 
 
 
  //  map.on('click',function(e) {
  //                                                                                            For debugging
  //                  console.log(e.latlng.lat,e.latlng.lng);
  //  });    

    

    function onLocationFound(e) {
        
        var radius =e.accuracy / 2;
        L.marker(e.latlng).addTo(map);
        L.circle(e.latlng, radius).addTo(map);
        map.setView(e.latlng, 16);
        minimap.setView(e.latlng, 18);
        
       
        markerDrag.setLatLng(e.latlng).addTo(minimap);
        LatLngOnForm(e.latlng);
        
        get_bar_list()      
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
        stopLoading();
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
    
    
   //this function takes the location and sends a GET petition to django to take the bar_list value
   function get_bar_list(){
        
        var dataD =  map.getBounds();     
        var dataDic={'East':dataD.getEast(),'West':dataD.getWest(),'North':dataD.getNorth(),'South':dataD.getSouth()} 
        var responseAjaxGET= $.ajax({
            type: "GET",
            url: "/init",     
            data: dataDic,       
            success: function(data){
                    if (data=='error'){alert("Error de inicializacion!")}
                    else{
                        bar_list=jQuery.parseJSON(data);                       
                        bar_list = _.sortBy(bar_list, function(obj){ return obj.fields.price;});                            
                        paintBars();
                    }
            }
        }); 
    
    
    };
    

    
    
    
    function paintBars(){          //this function creates markers on the map
        markersLayer.clearLayers();
        markers_blueLayer.clearLayers();
        list=getFilteredList();
        for (i = 0; i < list.length; i++){
            var n = i+1;
            var numberedIcon = new numIcon({iconUrl: '/static/images/markers/number_'+n+'.png'})
            var marker = new L.marker([list[i].fields.latitude, list[i].fields.longitude],{
                        title:list[i].fields.name+' '+list[i].fields.price+'€',
                        icon:numberedIcon
                        })   
            marker.on('click',function(e) {
                    var latlng=this.getLatLng();
                    var barfound = _.find(list, function(obj){ 
                                        return obj.fields.latitude == latlng.lat && obj.fields.longitude == latlng.lng; });
                    fillBarInfo(barfound);
                    selectBarList(barfound); 
            });
            markersLayer.addLayer(marker);
        }
        $('#barList ol').html('');
        paintDescarted(list);
        fillBarList(list);
        stopLoading();
    }
    
    function paintDescarted(list){            // Paints bars out of the #barList ol like circles on the map
    
    descartedList = _.reject(bar_list, function(obj){ return  _.find(list, function(bar){return obj.pk == bar.pk; }) });
    for (i = 0; i < descartedList.length; i++){
            var n = i+1;
            var numberedIcon = new numIcon({iconUrl: '/static/images/markers/number_'+n+'.png'})
            var circle = new L.circle([descartedList[i].fields.latitude, descartedList[i].fields.longitude],5,{
                                            title:descartedList[i].fields.name+' '+descartedList[i].fields.price+'€',
                                            color: 'black',
                                            fillColor: '#FF8000',
                                            fillOpacity: 1
                                        })   
            circle.on('click',function(e) {
                    var latlng=this.getLatLng();
                    var barfound = _.find(bar_list, function(obj){ 
                                        return obj.fields.latitude == latlng.lat && obj.fields.longitude == latlng.lng; });
                    fillBarInfo(barfound);
                    selectBarList(barfound); 
            });
            markersLayer.addLayer(circle);
        }
    }
    
    
    function fillBarList(list){         //this function lists the bars on the left side of the map inside the div "barList"
        for (i in list){
            if (clstate){
                $('#barList ol').append('<li class="barli" id='+list[i].pk+'>'+list[i].fields.name+' <span>'+list[i].fields.price+'€'+'</span></li>');
            }else{
                $('#barList ol').append('<li  class="barli" id='+list[i].pk+'>'+list[i].fields.name+' <span>'+list[i].fields.litre+'€'+'</span></li>');
            }
        }
        
        
        $( '#barList li' ).click(function( event ) {
          var pk=this.id;
          var barfound = _.find(list, function(obj){return obj.pk == pk; });
          fillBarInfo(barfound);                //in style.js
          selectBarList(barfound);
                     
        });
   
   };
   
   
   function fillBarInfo(bar){       //this function prints the info of the objet bar given as a parameter
        setBarInfo();
        $('#barInfoContainer').html('<h3>'+bar.fields.name+'</h3><h6>'+bar.fields.street+'</h6> Caña: '+bar.fields.price+'€')
        if (bar.fields.litre!=0){$('#barInfoContainer').append('<br>Litro: '+bar.fields.litre+'€')}
        if (bar.fields.tapa){$('#barInfoContainer').append('<br>Ponen tapa')}else{$('#barInfoContainer').append('<br>No ponen tapa')}
       
        var responseAjaxGET= $.ajax({
            type: "GET",
            url: "/images",     
            data: {'bar_id':bar.pk},       
            success: function(data){
                $('#barAlbum').html('');
                var img_list=jQuery.parseJSON(data);
                for (i in img_list){
                    console.log(img_list);
                    $('#barAlbum').append(                                
                                '<a href=/media/'+img_list[i].fields.image+' title='+bar.fields.name+'>'+
                                '<img class="barImg" src=/media/'+img_list[i].fields.image+'>'+
                                '</a>'
                    );
                    
                   
                }
                
            	
            }
            
        });        
   };
   
    
    $("#addBarForm").validate({         //Takes data form, validates and sends it to the view with ajax
        rules: {
            nameForm: { required: true, minlength: 2},
            priceForm: { required: true},
            litreForm: { required: false},
            tapaForm: { required: false},
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
                            "litreForm":$('#litreForm').val(),
                            "tapaForm":$('#tapaForm').is(':checked'),
                            "latForm":$('#latForm').val(),
                            "lonForm":$('#lonForm').val()}       
            var responseAjaxPost= $.ajax({
                type: "POST",
                url: "/addBar",
                data: dataDic,
                success: function(data){
                        if (data=='error'){alert("Este bar ya existe!")}
                        else{
                            get_bar_list()                         

                        }
                }
            });          
        }
    });  
    
  
    $( '#beerIcon' ).click(function( event ) {                                  //changes clstate and the png icon
         if($('#beerIcon').attr('src') == "/static/images/beer_glass.png") {
           $('#beerIcon').attr('src',"/static/images/beer_jar.png");
           clstate=false;
        } else {
           $('#beerIcon').attr('src',"/static/images/beer_glass.png");
           clstate=true;           
        }
        paintBars();
    });
    $( '#plateIcon' ).click(function( event ) {                                 //changes tapastate and the png icon
        if($('#plateIcon').attr('src') == "/static/images/plate_false.png") {
            $('#plateIcon').attr('src',"/static/images/plate_true.png");
            tapastate=true;
        } else {
            $('#plateIcon').attr('src',"/static/images/plate_false.png");
            tapastate=false;           
        }
        paintBars();
    });
    
    function getFilteredList(){   //check tapastate and clstate and filters bar_list, it returns the correct list of bars
        var current_bar_list;
        
        if (tapastate){
            current_bar_list = _.filter(bar_list, function(obj){ return obj.fields.tapa == true; });
        }else{
            current_bar_list = bar_list;
        }
        if(!clstate) {
            var filtered_bar_list = _.filter(current_bar_list, function(obj){ return obj.fields.litre != "0"; });
            filtered_bar_list = _.sortBy(filtered_bar_list, function(obj){ return obj.fields.litre;});
            return filtered_bar_list.slice(0, 10);
        }else{
            return current_bar_list.slice(0, 10);
        }
    
    
    }
    
    
    var frm = $('#barImageForm');
    frm.submit(function () {
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: new FormData( this ),
            processData: false,
            contentType: false,
            success: function (data) {
                console.log(data);
            },
            error: function(data) {
                console.log("Something went wrong!");
            }
        });
        return false;
    });
    
    $('.popup-gallery').magnificPopup({
                delegate: 'a',
                type: 'image',
                tLoading: 'Loading image #%curr%...',
                mainClass: 'mfp-img-mobile',
                gallery: {
                    enabled: true,
                    navigateByImgClick: true,
                    preload: [0,1] // Will preload 0 - before current, and 1 after the current image
                },
                image: {
                    tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
                    titleSrc: function(item) {
	                    return item.el.attr('title');
                    }
                }
    });
                
                
                


    
});
    


