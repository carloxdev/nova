/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

var url_empleados = window.location.origin + "/api-ebs/viewempleadosfull/"

//OBJS
var organigrama = null
var tarjeta_filtros = null

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function(){
   tarjeta_filtros = new TarjetaFiltros()
   //organigrama = new Organigrama()
})

/*-----------------------------------------------*\
            OBJETO: TARJETA FILTROS
\*-----------------------------------------------*/


function TarjetaFiltros(){

   this.$organizaciones = $('#id_organizaciones')

   this.init_Components()
}
TarjetaFiltros.prototype.init_Components = function () {
   this.$organizaciones.select(this.get_ConfSelect2())
}
TarjetaFiltros.prototype.get_ConfSelect2 = function () {
    return {
        width: '100%'
    }
}
TarjetaFiltros.prototype.llenar_Select = function(){

}


/*-----------------------------------------------*\
            OBJETO: ORGANIGRAMA
\*-----------------------------------------------*/


function Organigrama(){
   this.init_Components()
}
Organigrama.prototype.init_Components = function () {

    this.crear_Diagrama()
}
Organigrama.prototype.crear_Diagrama = function (){

   $("#diagram").kendoDiagram({
      dataSource: new kendo.data.HierarchicalDataSource({
         data: this.get_Data(),
         schema: {
            model: {
               children: "items"
            }
         }
      }),
      layout: {
         type: "layered"
      },
      shapeDefaults: {
         visual: this.visual_Template()
      },
      connectionDefaults: {
         stroke: {
            color: "#979797",//Color gris
            width: 2
         }
      }
   });

   var diagram = $("#diagram").getKendoDiagram()
   diagram.bringIntoView(diagram.shapes)

}
Organigrama.prototype.get_Data = function (){

   var data =[]
   
   data= [{
            firstName: "Antonio",
            lastName: "Moreno",
            title: "Team Lead",
            colorScheme: "#1696d3",//Color azul
            items: [{
               firstName: "Elizabeth",
               lastName: "Brown",
               title: "Design Lead",
               colorScheme: "#ef6944",
               items: [{
                  firstName: "Ann",
                  lastName: "Devon",
                  title: "UI Designer",
                  colorScheme: "#ef6944"
               }]
            }, {
               firstName: "Diego",
               lastName: "Roel",
               title: "QA Engineer",
               colorScheme: "#ee587b",
               items: [{
                  firstName: "Fran",
                  lastName: "Wilson",
                  title: "QA Intern",
                  colorScheme: "#ee587b"
               }]
            }, {
               firstName: "Felipe",
               lastName: "Izquiedro",
               title: "Senior Developer",
               colorScheme: "#75be16",
               items: [{
                  firstName: "Daniel",
                  lastName: "Tonini",
                  title: "Developer",
                  colorScheme: "#75be16"
               }]
            }]
         }]
   return data
}
Organigrama.prototype.visual_Template = function (){

   var var_template = function (options){
      var dataviz = kendo.dataviz
      var g = new dataviz.diagram.Group()
      var dataItem = options.dataItem

      g.append(new dataviz.diagram.Rectangle({
         width: 210,
         height: 75,
         stroke: {
            width: 0
         },
         fill: {
            gradient: {
               type: "linear",
               stops: [{
                  color: dataItem.colorScheme,
                  offset: 0,
                  opacity: 0.5
               }, {
                  color: dataItem.colorScheme,
                  offset: 1,
                  opacity: 1
               }]
            }
         }
      }))

      g.append(new dataviz.diagram.TextBlock({
         text: dataItem.firstName + " " + dataItem.lastName,
         x: 85,
         y: 20,
         fill: "#fff" //Color blanco
      }))

      g.append(new dataviz.diagram.TextBlock({
         text: dataItem.title,
         x: 85,
         y: 40,
         fill: "#fff"
      }))

      return g
   }

   return var_template
}