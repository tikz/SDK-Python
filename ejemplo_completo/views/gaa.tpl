% include('includes/header.tpl')

%if statusCode == -1:
	<div class="alert alert-success"><p><strong>GAA correcto</strong></p></div>
%else:
	<div class="alert alert-danger"><p><strong>Error al realizar el GAA</strong></p></div>
%end

<h1>Respuesta de servicio</h1>
<pre>
{{result}}
</pre>

<p><a href="/list">Volver al listado</a></p>
% include('includes/footer.tpl')