% include('includes/header.tpl')

%if statusCode == '2011':
	<div class="alert alert-success"><p>Devolución {{tipoDevolucion}} correcta</p></div>
%else:
	<div class="alert alert-danger"><p>Error al hacer la devolución {{tipoDevolucion}}</p></div>
%end

<h1>Respuesta del servicio:</h1>
<pre>
{{result}}
</pre>

<p><a href="/list">Volver al listado</a></p>
% include('includes/footer.tpl')		