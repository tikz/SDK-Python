% include('includes/header.tpl')

%if status == -1:
	<div class="alert alert-success"><p>Pago correcto</p></div>
%else:
	<div class="alert alert-danger"><p>Error al realizar el pago</p></div>
%end


<p><a href="/list">Volver al listado</a></p>
% include('includes/footer.tpl')