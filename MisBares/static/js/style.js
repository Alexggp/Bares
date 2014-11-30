$(document).ready(function(){



//sets relative positions and behaviour of divs

    $("#loading").css("left",$(window).width()/2-$("#loading").width()/2);
    $("#loading").css("top",$(window).height()/2-$("#loading").height()/2);


    $("footer").css("left",$(window).width()/2-$("footer").width()/2);




    $("#authentication").css("left",$(window).width()-$("#authentication").width());
    $("#addIcon").css("left",$(window).width()-$("#authentication").width()-75);

    setIconsPosition();

    $( '#auxBarList' ).click(function( event ) {  
        $( '#auxBarList' ).hide();
        $('#barList').show();         
        setIconsPosition();

    });
    $('#barList').click(function(event){
        if(event.target != this) return false;
        $( '#auxBarList' ).show();
        $('#barList').hide();       
        setIconsPosition();
    });

    $('#barInfo').click(function(event){
        if(event.target != this) return false;
        $('#barInfo').hide();
        $("#authentication").show();
        $("#addIcon").show();
        setIconsPosition();
        
    });



    $( '#addIcon' ).click(function( event ) {  
        $( '#addBarContainer' ).show();
        $( '#background').show();
        $( '#minimap').show();
        
        $("#addBarContainer").css("left",$(window).width()/2-$("#addBarContainer").width()/2);
        $("#addBarContainer").css("top",$(window).height()/2-$("#addBarContainer").height()/2);
        minimap.invalidateSize();
        
    });
    $( '#background, #addBarClose,#sendAddBar' ).click(function(event){
        $( '#addBarContainer' ).hide();
        $( '#background').hide();
    });
});


function stopLoading(){
    $("#loading").remove();
    $("#backgroundLoad").remove();
}

function setIconsPosition(){
    if ($('#barList').css("display")== "none"){
        $("#beerIcon").css("left",30); 
        $("#plateIcon").css("left",75);
    }else{

        $("#beerIcon").css("left",$('#barList').width()+30); 
        $("#plateIcon").css("left",$('#barList').width()+75);
    };   
};

function setBarInfo(){ 
                                                 //called by fillBarInfo()
    $('#barInfo').css("left",$(window).width()-$('#barInfo').width());   
    $('#barInfo').show();
    $("#authentication").hide();
    $("#addIcon").hide();
};

