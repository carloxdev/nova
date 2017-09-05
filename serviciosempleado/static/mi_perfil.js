/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/
var url_expediente_personal_bypage = window.location.origin  + "/api-capitalhumano/archivopersonal_bypage/"
var url_expediente_capacitacion_bypage = window.location.origin  + "/api-capitalhumano/archivocapacitacion_bypage/"
var url_archivo =  window.location.origin + "/api-capitalhumano/archivo/"
var url_profile =  window.location.origin + "/api-seguridad/profile/"

// OBJS
var grid_personal = null
var grid_capacitacion = null
var filtros = null
var tarjeta_resultados = null
var personalizacion = null
var popup = null

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {
    filtros = new Filtros()
    tarjeta_resultados = new TarjetaResultados()

})

/*-----------------------------------------------*\
            OBJETO: Tarjeta Resultados
\*-----------------------------------------------*/

function TarjetaResultados(){
    this.personalizacion = new Personalizacion()
    this.popup = new Popup()
    grid_personal = new GridPersonal()
}

/*-----------------------------------------------*\
            OBJETO: Filtros
\*-----------------------------------------------*/

function Filtros(){

    this.$numero_empleado = $('#numero_empleado')
}
Filtros.prototype.get_Values = function (_page) {
    return {
        page: _page,
        relacion_personal__numero_empleado: this.$numero_empleado.val(),
   }
}
Filtros.prototype.get_ValuesCap = function (_page) {
    return {
        page: _page,
        relacion_capacitacion__numero_empleado: this.$numero_empleado.val(),
   }
}

/*-----------------------------------------------*\
            OBJETO: Modal actualizacion
\*-----------------------------------------------*/

function Popup(){

    this.$formulario = $('#formulario')
    this.$numero_empleado = $('#numero_empleado')
    this.$asunto = $('#id_asunto')
    // this.$departamento = $('#id_departamento')
    this.$descripcion = $('#id_descripcion')
    this.$archivo = $('#id_archivo')
    this.$created_by = $('#id_created_by')
    this.$boton_limpiar = $('#boton_limpiar')
    this.$boton_enviar = $('#boton_enviar')
    this.$formulario = $('#formulario')
    this.$modal_actualizar = $('#modal_actualizar')

    this.init_Events()
    this.init_Components()

}
Popup.prototype.init_Components = function(){

    this.$asunto.select2(appnova.get_ConfigSelect2())
}
Popup.prototype.init_Events = function(){
    
    this.$boton_limpiar.on("click", this , this.limpiar_Campos)
    this.$boton_enviar.on("click", this, this.enviar_Solicitud)
}
Popup.prototype.enviar_Solicitud = function (e){
    id_solicitud = ''
    extension = tarjeta_resultados.popup.validar_Archivo(e.data.$archivo.val())
    if (tarjeta_resultados.popup.validar_Campos() != 'True'){
        if (extension == ".pdf"){
            var promesa = $.ajax({
                     url: url_solicitud,
                     method: "POST",
                     headers: { "X-CSRFToken": appnova.galletita },
                     data: {
                            'numero_empleado' : e.data.$numero_empleado.val(),
                            'clave_departamento' : 107,
                            'asunto' : e.data.$asunto.val(),
                            'descripcion' : e.data.$descripcion.val(),
                            'observaciones': '--',
                            'created_by' : url_profile+e.data.$created_by.val()+"/",
                     },
                     success: function (_response) {
                            id_solicitud = _response.pk
                     },
                     error: function (_response) {
                            alertify.error("Ocurrio error al guardar")
                     }
                })
            promesa.then(function(){
                tarjeta_resultados.popup.guardar_Archivo(id_solicitud)
            })
        }else if(extension==""){
            e.data.$formulario.append('<div class="alert alert-danger nova-margin" id="id_error"><span class="icon mdi mdi-close-circle-o"></span><strong>Debe adjuntar el archivo correspondiente.</strong></div>')
        }
        else{
            e.data.$formulario.append('<div class="alert alert-danger nova-margin" id="id_error"><span class="icon mdi mdi-close-circle-o"></span><strong>Solo se permiten archivos pdf.</strong></div>')
        }
    }
}
Popup.prototype.guardar_Archivo = function (_id_solicitud){

        var data = new FormData()
        tarjeta_resultados.popup.$formulario.find(':input').each(function() {
                var elemento= this;
                if(elemento.type === 'file'){
                     if(elemento.value !== ''){
                                for(var i=0; i< $('#'+elemento.id).prop("files").length; i++){
                                    data.append('archivo', $('#'+elemento.id).prop("files")[i]);
                             }
                            
                                data.append('tipo_archivo', "sol")
                                data.append('content_object', url_solicitud+_id_solicitud+"/")
                                data.append('created_by', url_profile+tarjeta_resultados.popup.$created_by.val()+"/")
                        }              
                 }
         })

         $.ajax({
                 url: url_archivo,
                 method: "POST",
                 headers: { "X-CSRFToken": appnova.galletita },
                 contentType: false,
                 processData: false,
                 data: data,
                 success: function (_response) {

                        alertify.success("Se ha guardado el archivo")
                        tarjeta_resultados.popup.hidden_Modal()
                        
                 },
                 error: function (_response) {
                        alertify.error("Ocurrio error al guardar archivo")

                        $.ajax({
                             url: url_solicitud +_id_solicitud+"/",
                             method: "DELETE",
                             headers: { "X-CSRFToken": appnova.galletita },
                             success: function (_response) {
                                
                             },
                             error: function (_response) {
                                alertify.error("No se ha podido eliminar el registro")
                             }
                        })
                 }
            })
}
Popup.prototype.hidden_Modal = function () {

    this.$modal_actualizar.modal('hide')
    this.$asunto.data('select2').val(0)
    this.$descripcion.val("")
    this.$archivo.val("")
}
Popup.prototype.limpiar_Campos = function (e){
    e.data.$asunto.data('select2').val(0)
    e.data.$descripcion.val("")
    e.data.$archivo.val("")
    tarjeta_resultados.popup.clear_Estilos()
}
Popup.prototype.validar_Campos = function () {
    bandera = 'False'
    $('#id_error').detach()
    if(this.$asunto.data('select2').val() == ""){
        this.$asunto.data('select2').$selection.addClass("nova-has-error");
        bandera = 'True'
    }
    else{
        this.$asunto.data('select2').$selection.removeClass("nova-has-error");
    }
    if(this.$descripcion.val() == ""){
        this.$descripcion.addClass("nova-has-error")
        bandera = 'True'
    }
    else{
        this.$descripcion.removeClass("nova-has-error")
    }
    if(this.$archivo.val() == ""){
        this.$archivo.addClass("nova-has-error")
        bandera = 'True'
    }
    else{
        this.$archivo.removeClass("nova-has-error")
    }
    if (bandera == 'True' ){
        this.$formulario.append('<div class="alert alert-danger nova-margin" id="id_error"><span class="icon mdi mdi-close-circle-o"></span><strong>Completa los campos correspondientes</strong></div>')
    }
    else{
        $('#id_error').detach()
    }

    return bandera
}
Popup.prototype.clear_Estilos = function () {

   this.$asunto.data('select2').$selection.removeClass("nova-has-error");
   this.$descripcion.removeClass("nova-has-error")
   this.$formulario.get(0).reset()
   this.$archivo.removeClass("nova-has-error")
   $('#id_error').detach()
}
Popup.prototype.validar_Archivo = function (_archivo) {
        extension = (_archivo.substring(_archivo.lastIndexOf("."))).toLowerCase();
        return extension
}


/*-----------------------------------------------*\
            OBJETO: Personalizacion del tab
\*-----------------------------------------------*/

function Personalizacion(){
    this.$personales = $('#personales')
    this.$capacitaciones = $('#capacitaciones')
    this.$li_personales = $('#per')
    this.$li_capacitaciones = $('#cap')
    this.init_Events()
}
Personalizacion.prototype.init_Components = function(){
}
Personalizacion.prototype.init_Events = function(){
    
    this.$personales.on("click", this , this.mostrar_Personales)
    this.$capacitaciones.on("click", this , this.mostrar_Capacitaciones)
    this.$li_personales.on("click", this , this.mostrar_Personales)
    this.$li_capacitaciones.on("click", this , this.mostrar_Capacitaciones)
}
Personalizacion.prototype.mostrar_Personales = function(e){
     
    e.data.$capacitaciones.removeClass('nova-active-tab')
    e.data.$personales.addClass('nova-active-tab')
    e.data.$li_capacitaciones.removeClass('active')
    e.data.$li_personales.addClass('active')
    $("#grid_resultados").empty()
    grid_personal.init()
}
Personalizacion.prototype.mostrar_Capacitaciones = function(e){
    
    e.data.$personales.removeClass('nova-active-tab')
    e.data.$capacitaciones.addClass('nova-active-tab')
    e.data.$li_personales.removeClass('active')
    e.data.$li_capacitaciones.addClass('active')
    $("#grid_resultados").empty()
    grid_capacitacion = new GridCapacitacion()
}


/*-----------------------------------------------*\
            OBJETO: Grid personal
\*-----------------------------------------------*/

function GridPersonal() {

    this.$id = $("#grid_resultados")
    this.kfuente_datos = null

    this.kgrid = null
    this.init()
}
GridPersonal.prototype.init = function () {

    // Definicion del pais, formato modena, etc..
    kendo.culture("es-MX")

    // Se inicializa la fuente da datos (datasource)
    this.kfuente_datos = new kendo.data.DataSource(this.get_DataSourceConfig())
    
    // Se inicializa y configura el grid:
    this.kgrid = this.$id.kendoGrid(this.get_Configuracion())
}
GridPersonal.prototype.get_DataSourceConfig = function () {
    return {

        serverPaging: true,
        pageSize: 10,
        transport: {
            read: {
                url: url_expediente_personal_bypage,
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read"){
                    return  filtros.get_Values(data.page)
                }
            }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                fields: this.get_Campos()
            }
        },
        error: function (e) {
            alertify.error("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }    
}
GridPersonal.prototype.get_Campos = function () {
    
    return {
        agrupador : { type: "string" },
        fecha : { type: "date"},
        vigencia_inicio : { type: "string" },
        vigencia_fin : { type: "string" },
        tipo_documento : { type: "string" },
        archivo : { type: "string" },
        created_by : { type: "string" },
        created_date : { type: "date" },
    }
}
GridPersonal.prototype.get_Configuracion = function () {

    return {
        dataSource: this.kfuente_datos,
        columnMenu: true,
        groupable: false,
        sortable: false,
        editable: false,
        resizable: true,
        selectable: true,
        columns: this.get_Columnas(),
        scrollable: true,
        pageable: true,
        noRecords: {
            template: "<div class='nova-grid-empy'> No se encontraron registros </div>"
        },
        dataBound: this.set_Icons,
    }
}
GridPersonal.prototype.get_Columnas = function () {

    return [  
        { field: "archivo", 
            title: "Archivo", 
            width:"60px" ,
            template: '<a class="btn btn-default nova-url" href="#=archivo#" target="_blank" id="documento"><i class="icon icon-left icon mdi mdi-file icon-black"></i></a>'
        },
        { field: "tipo_documento", title: "Tipo documento",  width:"150px"},
        { field: "agrupador", title: "Agrupador", width:"100px"},
        { field: "vigencia_inicio",title: "Vigencia inicio",width:"100px"},
        { field: "vigencia_fin", title: "Vigencia fin", width:"100px" },
        { field: "created_by", title: "Creado por", width:"150px" },
        { field: "created_date", title: "Fecha de creación", width:"150px", format: "{0:dd/MM/yyyy}" },

    ]
}
GridPersonal.prototype.buscar = function() {

    this.kfuente_datos.page(1)
}

/*-----------------------------------------------*\
            OBJETO: Grid capacitacion
\*-----------------------------------------------*/

function GridCapacitacion() {

    this.$id = $("#grid_resultados")
    this.kfuente_datos = null

    this.kgrid = null
    this.init()
}
GridCapacitacion.prototype.init = function () {

    // Definicion del pais, formato modena, etc..
    kendo.culture("es-MX")

    // Se inicializa la fuente da datos (datasource)
    this.kfuente_datos = new kendo.data.DataSource(this.get_DataSourceConfig())
    
    // Se inicializa y configura el grid:
    this.kgrid = this.$id.kendoGrid(this.get_Configuracion())
}
GridCapacitacion.prototype.get_DataSourceConfig = function () {
    return {

        serverPaging: true,
        pageSize: 10,
        transport: {
            read: {
                url: url_expediente_capacitacion_bypage,
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read"){
                    return  filtros.get_ValuesCap(data.page)
                }
            }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                fields: this.get_CamposCap()
            }
        },
        error: function (e) {
            alertify.error("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }    
}
GridCapacitacion.prototype.get_CamposCap = function () {
    return {
        curso : { type: "string" },
        archivo : { type: "string" },
        agrupador: { type: "string" },
        area: { type: "string" },
        proveedor : { type: "string"},
        modalidad : { type: "string" },
        costo : { type: "string" },
        moneda : { type: "integer" },
        fecha_inicio : { type: "string" },
        fecha_fin : { type: "string" },
        fecha_vencimiento: { type: "date" },
        duracion : { type: "string" },
        observaciones : { type: "string" },
        created_by : { type: "string" },
        created_date : { type: "date" },
    }
}
GridCapacitacion.prototype.get_Configuracion = function () {

    return {
        dataSource: this.kfuente_datos,
        columnMenu: true,
        groupable: false,
        sortable: false,
        editable: false,
        resizable: true,
        selectable: true,
        columns: this.get_Columnas(),
        scrollable: true,
        pageable: true,
        noRecords: {
            template: "<div class='nova-grid-empy'> No se encontraron registros </div>"
        },
        dataBound: this.aplicar_Estilos
    }
}
GridCapacitacion.prototype.get_Columnas = function () {

    return [  
        { field: "archivo", 
            title: "Archivo", 
            width:"70px" ,
            template: '<a class="btn btn-default nova-url" href="#=archivo#" target="_blank" id="documento"><i class="icon icon-left icon mdi mdi-file"></i></a>'
        },
        { field: "curso", title: "Curso", width:"150px"},
        { field: "agrupador", title: "Agrupador", width:"100px"},
        { field: "area", title: "Area", width:"100px"},
        { field: "proveedor", title: "Proveedor", width:"150px"},
        { field: "modalidad",title: "Modalidad",width:"100px"},
        { field: "costo", title: "Costo", width:"100px" },
        { field: "moneda",title: "Moneda",width:"100px"},
        { field: "fecha_inicio", title: "Fecha inicio", width:"100px" },
        { field: "fecha_fin",title: "Fecha fin",width:"100px"},
        { field: "fecha_vencimiento", title: "Fecha vencimiento", width:"100px", format: "{0:dd/MM/yyyy}" },
        { field: "duracion", title: "Duración", width:"100px",template: '#=duracion# hrs' },
        { field: "observaciones", title: "Observaciones", width:"200px" },
        { field: "created_by", title: "Creado por", width:"150px" },
        { field: "created_date", title: "Fecha de creación", width:"150px", format: "{0:dd/MM/yyyy}" },

    ]
}
GridCapacitacion.prototype.aplicar_Estilos = function (e) {

    columns = e.sender.columns
    dataItems = e.sender.dataSource.view()
    fecha_hoy = new Date()

    for (var j = 0; j < dataItems.length; j++) {
        fecha_vencimiento = dataItems[j].get("fecha_vencimiento")
        row = e.sender.tbody.find("[data-uid='" + dataItems[j].uid + "']")
        row.removeClass("k-alt");
        if(fecha_vencimiento != null){
  
            if (fecha_vencimiento.getTime() <= fecha_hoy.getTime()) {
                row.addClass("fecha-vencida")
            }
        }
    }
}
GridCapacitacion.prototype.buscar = function() {

    this.kfuente_datos.page(1)
}

