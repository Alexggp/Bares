function mostrarOcultar(id_abrir,id_cerrar){
      id_abrir.style.display = '';
      id_cerrar.style.display='none';
    }


var req = new XMLHttpRequest();
var revista;
var noticia;

function EstadoCambiado(){

  var puntuacion = document.getElementById("puntuacion" + noticia);
  puntuacion.innerHTML =  req.responseText;
}

function haciaRevista(codigo,id_n){

  noticia=id_n.toString();
  req.open('GET','/aRevista/'+codigo+'/'+noticia,true);
  if (codigo=='-1')
    req.onreadystatechange = EstadoCambiado;
  req.send(null);
  
}


function Enviado(){

  var div= document.getElementById('comentarios')
  var caja = document.getElementById('lista_comentarios')
  if (div.style.display=='none'){
    div.style.display = '';
  }
    if (req.response==''){
      div.style.display = 'none';
    }
  caja.innerHTML =  req.responseText;
}

function enviar(destino){
  var valor = document.getElementById("parrafo").value;
  if (valor){
    req.open('POST','/comentar',true);  
    req.send('del=False&texto=' + valor + '&destino='+destino);
    req.onreadystatechange = Enviado;
  }
}

function eliminar(id,destino){
  id=id.toString();
  req.open('POST','/comentar',true);  
  req.send('del=True&id=' + id + '&destino='+destino);  
  req.onreadystatechange = Enviado;
}
