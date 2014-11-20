$(document).ready(function(){

    



    map = L.map('map').setView([40.4405295, -3.6927629], 15);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);  
       
    
    //bar_list is the list of bars given by django, sorted by price
    bar_list = _.sortBy(bar_list, function(obj){ return obj.fields.price;});    
    
    (function paintBars(){          //this function creates markers on the map
        for (i in bar_list){
            var marker = new L.marker([bar_list[i].fields.latitude, bar_list[i].fields.longitude],{
                        title:bar_list[i].fields.name+' '+bar_list[i].fields.price+'€'
                        }).addTo(map);    
            marker.on('click',function(e) {
                    var latlng=this.getLatLng();
                    var barfound = _.find(bar_list, function(obj){ 
                                        return obj.fields.latitude == latlng.lat && obj.fields.longitude == latlng.lng; });
                    fillBarInfo(barfound);
            });
        }
    })();
    
   (function fillBarList(){         //this function list the bars on the left side of the map inside the div "barList"
        for (i in bar_list){
            $('#barList ul').append('<li id='+bar_list[i].pk+'>'+bar_list[i].fields.name+' <span>'+bar_list[i].fields.price+'€'+'</li>');
        }
   
   })();
   
   $( '#barList li' ).click(function( event ) {
      var pk=this.id;
      var barfound = _.find(bar_list, function(obj){ 
                                        return obj.pk == pk; });
      fillBarInfo(barfound);
    });
   
   function fillBarInfo(bar){       //this function print the info of the objet bar given as a parameter
        $('#barInfo').html('<h3>'+bar.fields.name+'</h3> Precio de la caña: '+bar.fields.price+'€')
   };
   

    $("#addBarForm").validate({
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
                            "priceForm":$('#priceForm').val(),
                            "latForm":$('#latForm').val(),
                            "lonForm":$('#lonForm').val()}
                            
            var responseAjax= $.ajax({
                type: "POST",
                url: "/addBar",
                data: dataDic,
                success: function(json){console.log(json)}
            });          
        }
    });  
    
});

