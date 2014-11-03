$(document).ready(function(){

    map = L.map('map').setView([40.4405295, -3.6927629], 15);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);  
       
    
    (function paintBars(){
        for (i in bar_list){
            var marker = L.marker([bar_list[i].fields.latitude, bar_list[i].fields.longitude]).addTo(map);    
            marker.bindPopup(bar_list[i].fields.name+'<br>'+bar_list[i].fields.price+'€').openPopup();        
        }
    })();
        
    
});

