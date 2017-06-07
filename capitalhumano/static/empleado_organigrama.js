/*-----------------------------------------------*\
               GLOBAL VARIABLES
\*-----------------------------------------------*/

var url_organigrama = window.location.origin + "/api-ebs/vieworganigrama/"
var url_datos = window.location.origin + "/organigrama/json/"

//OBJS
var organigrama = null
var tarjeta_filtros = null
var organizacion = 0

/*-----------------------------------------------*\
               LOAD
\*-----------------------------------------------*/

$(document).ready(function(){
   organigrama = new Organigrama()
   tarjeta_filtros = new TarjetaFiltros()
   //organigrama.crear_Diagrama()
         
})

/*-----------------------------------------------*\
               OBJETO: TARJETA FILTROS
\*-----------------------------------------------*/


function TarjetaFiltros(){

   this.$organizaciones = $('#id_organizaciones')
   this.$empresas = $('id_empresas')

   this.init_Components()
   this.init_Events()
}
TarjetaFiltros.prototype.init_Components = function () {
   this.$organizaciones.select2(this.get_ConfSelect2())
   this.$empresas.select2(this.get_ConfSelect2())
}
TarjetaFiltros.prototype.init_Events = function () {
   this.$organizaciones.on("change", this, organigrama.empleados_Organizacion)
   //this.$empresas.on("change", this, organigrama.buscar_Empleados)
}
TarjetaFiltros.prototype.get_ConfSelect2 = function () {
   return {
      width: '100%'
   }
}
/*-----------------------------------------------*\
               OBJETO: ORGANIGRAMA
\*-----------------------------------------------*/


function Organigrama(){
}
Organigrama.prototype.empleados_Organizacion = function(e){

  organizacion = e.data.$organizaciones.val()

   $.ajax({
            url: url_organigrama,
            data: {
              asig_organizacion_clave:organizacion
            },
            dataType: "json",
            type: "GET",
            contentType: "application/json; charset=utf-8",
            context: this,
            success: function (response) {

              cont = 0
              for (var i = 0; i < response.length; i++) {
                cont+=1
              }

              if (cont == 0)
                organigrama.mostrar_Mensaje(cont)
              else{
                organigrama.mostrar_Mensaje(cont)
                organigrama.buscar_Empleados(organizacion)
              }
              
            },
            error: function (response) {

                         alert("Ocurrio error al consultar ")
                  }

    })
}
Organigrama.prototype.buscar_Empleados = function (_organizacion){

   var url = url_datos + _organizacion + "/"

   $.ajax({
            url: url,
            data: {},
            dataType: "json",
            type: "GET",
            contentType: "application/json; charset=utf-8",
            context: this,
            success: function (response) {

              console.log(JSON.stringify(response))
              organigrama.crear_Diagrama(response)
            },
            error: function (response) {

                         alert("Ocurrio error al consultar")
                  }

    })
}
Organigrama.prototype.crear_Diagrama = function(_response){
  $('#content-data').orgchart({
    'data' : _response,
    'depth': 4,
    'nodeTitle': 'puesto',
    'nodeFoto':'foto',
    'nodeNombre': 'nombre',
    'nodeNumEmpleado':'num_empleado',
    'nodeCompania':'compania',
    'nodeDepartamento':'departamento',
    'toggleSiblingsResp': true,
    'zoom': false,
    'pan': true
  })
}
Organigrama.prototype.get_Data = function(){

var datasource2 =
{ "nombre":"VILLEGAS RASCON CLAUDIA ANGELICA",
  "foto":"usuarios/fotos/imagen2.png",
  "puesto":"COORDINADOR",
  "num_empleado": "202000",
  "compania":"SIC",
  "departamento": "TECNOLOGIA DE INFORMACION",
  "children":[
    {"nombre":"JIMENEZ HERRERA ZAIRA","puesto":"AUXILIAR"},
    {"nombre":"AVENDAÑO CRUZ LUIS ALBERTO","puesto":"JEFE",
      "children":[
        {"nombre":"MARTINEZ GUTIERREZ EDWIN","puesto":"TECNICO ESPECIALISTA"}
        ],
    },
    {"nombre":"MARTINEZ HERNANDEZ JORGE JESUS","puesto":"JEFE",
      "children":[
        {"nombre":"ARIAS ZACARIAS ZACHARIEL","puesto":"ANALISTA"},
        {"nombre":"CASTRO CASTILLO JANET","puesto":"ANALISTA"},
        {"nombre":"CRUZ GOXCON MIGUEL ANGEL","puesto":"TECNICO ESPECIALISTA"},
        {"nombre":"CORDOVA QUIROZ NADIA","puesto":"ANALISTA"},
        {"nombre":"MARTINEZ JIMENEZ CARLOS ANDRES","puesto":"ANALISTA"}
        ],
    }
  ],
}
  return datasource2
}
Organigrama.prototype.mostrar_Mensaje = function (_total){

   if(_total == 0){
      document.getElementById('container-mensaje').innerHTML='La organización no cuenta con empleados'
      $('#contenedor').hide()

   }else{
      document.getElementById('container-mensaje').innerHTML=' '
      $('#contenedor').show()
   }
}
