% include('includes/header.tpl')
<div style="width: 50%">
	<form style="float: left" id="activeform" method="POST" action="/devolver">
		<h1>Devolución parcial</h1>
		<p>Monto: <strong>$ {{amount}}</strong></p>
		<label for="amount">Monto a devolver:</label>
		<input id="amount" name="amount" type="text" required /><div class="line"></div>
			
		<input name="parcial" class="btn-primary btn-sm" type="submit" value="Devolver" />
		<input name="id" class="btn-primary btn-sm" type="hidden" value="{{id}}" />
		<div class="line"></div>
		<p><a href="/list">Volver a listado</a></p>
	</form>


	<form style="float: right" id="activeform" method="POST" action="/devolver">
		<h1>Devolución total</h1>
		<p>Monto: <strong>$ {{amount}}</strong></p>		
		<input name="total" class="btn-primary btn-sm" type="submit" value="Devolver" />
		<input name="id" class="btn-primary btn-sm" type="hidden" value="{{id}}" />
	</form>
</div>

% include('includes/footer.tpl')		