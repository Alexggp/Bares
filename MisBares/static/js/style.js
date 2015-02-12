$(document).ready(function(){


//sets relative positions and behaviour of divs


//the following statements sets css position for diferent divs


    center("#loading");  //defined below
    $("footer").css("left",$(window).width()/2-$("footer").width()/2);
    $("#logIcon").css("left",$(window).width()-$("#logIcon").width()-7);
    $("#addIcon").css("left",$(window).width()-$("#logIcon").width()-75);



    $( "#barInfo" ).panel({                     //When barInfo closes
        close: function( event, ui ) {
        
        markers_blueLayer.clearLayers();                 //delete selections on map
        $('#selectable li').removeClass( "selectedLi" );
        $('#selectable li').addClass( "barli" );
        
        }
    });




    $( '#addIcon' ).click(function( event ) {       //Displays the form to add bar, centered on the window
        $( '#addBarContainer' ).show();
        $( '#background').show();
        $( '#minimap').show();
        
        center("#addBarContainer");                                  
        minimap.invalidateSize();
        
    });
    $( '#background' ).click(function(event){           //Closes addBar by clicking on the background or
        $( '.hidable' ).hide();                                     //sending information
       
    });
    $('#cameraIcon').click(function( event ){        //Displays the form to add bar images, centered on the window
        $('#addImage').show();
        $( '#background').show();
        center("#addImage"); 
    });
    
    $('#pencilIcon').click(function(event){           //Displays the form to update bar, centered on the window
        $('#changeBar').show();
        $( '#background').show();
        center("#changeBar"); 
    });
    

});


function center(obj){                                               //Center divs 
        $(obj).css("left",$(window).width()/2-$(obj).width()/2);
        $(obj).css("top",$(window).height()/2-$(obj).height()/2);
    }


function stopLoading(){                                             //Deletes the loading gif
    $("#loading").remove();
    $("#background").hide();
}

var numIcon_blue = L.Icon.extend({                  // new marker to stand out the selected bar on the map
    options: {
        shadowUrl: '/static/js/leaflet-0.7.3/images/marker-shadow.png',
        iconSize:     [35, 42],
        shadowSize:   [50, 64],
        iconAnchor:   [17, 40],
        shadowAnchor: [14, 64]
        }
    });


function selectBarList(bar){     //Stands out the selected bar on the map and the barList, or delets the selection
    var obj=$('#'+bar.pk);
    markers_blueLayer.clearLayers();                    //"barli" = unselected class bar on barList
    if (obj.hasClass("barli")){                         //"selectedLi" = selected class bar on barList
        $( '#barList li' ).removeClass( "selectedLi" );
        $( '#barList li' ).addClass( "barli" );
        obj.removeClass( "barli" );
        obj.addClass( "selectedLi" );
        
        
        var Icon = new numIcon_blue({iconUrl: '/static/images/marker_blue.png'})
        var marker = new L.marker([bar.fields.latitude, bar.fields.longitude],{
                        title:bar.fields.name+' '+bar.fields.price+'€',
                        icon:Icon
                        }) 
        marker.on('click',function(e) {                         //It deletes the selection too
                    $('#'+bar.pk).removeClass( "selectedLi" );
                    $('#'+bar.pk).addClass( "barli" );
                    markers_blueLayer.clearLayers();
                    $( "#barInfo" ).panel( "close" );
            });
        markers_blueLayer.addLayer(marker);
    }else if (obj.hasClass("selectedLi")){
            $( "#barInfo" ).panel( "close" );
            obj.removeClass( "selectedLi" );
            obj.addClass( "barli" );
            
    }
    else{       // bars out of #10 bar list (barList), marked with circles...
    
        $( '#barList li' ).removeClass( "selectedLi" );
        $( '#barList li' ).addClass( "barli" );
        var Icon = new numIcon_blue({iconUrl: '/static/images/marker_blue.png'})
        var marker = new L.marker([bar.fields.latitude, bar.fields.longitude],{
                        title:bar.fields.name+' '+bar.fields.price+'€',
                        icon:Icon
                        }) 
        marker.on('click',function(e) {                        
                    markers_blueLayer.clearLayers();
                    $('#barInfo').hide();
            });
        markers_blueLayer.addLayer(marker);
    }
};

