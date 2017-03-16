% include('includes/header.tpl')

<div class="w-section"></div>
<div id="m-status" style="margin-bottom: 300px">

	<div class="block">
	<img class="logo" src="https://developers.todopago.com.ar/site/sites/all/themes/todopagodev_theme/logo.png" alt="Todopago" /><div class="clearfix"></div>
	<form method="POST" action="/login_action">
		<input required name="user" type="text" placeholder="Usuario Todopago" /><div></div>
		<input required name="pwd" type="password" placeholder="Contraseña Todopago" /><div></div>
		<input class="btn-default" type="submit" value="Obtener credenciales" />
	
		<div>Modo:
			<label for="test">
				<input type="radio" name="mode" id="test" value="test" checked /> Test
			</label>

			<label for="production">
				<input type="radio" name="mode" id="production" value="prod" /> Producción
			</label>
		</div>
	</form>
	</div>
</div>
% include('includes/footer.tpl')