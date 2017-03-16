% include('includes/header.tpl')

<div class="w-section"></div>
<div id="m-status" style="margin-bottom: 300px">
	<div class="block">
		<table id="tablelist" class="full tablesorter">
			<thead>
			<tr>
				<th class="header">Operación</th>
				<th class="header">Estado</th>
				<th class="header">SAR</th>
				<th class="header">Pagar</th>
				<th class="header">GAA</th>
				<th class="header">getByOperationId</th>
				<th class="header">Devolver</th>	
			</tr>
			</thead>

			<tbody>
			%for row in rows:
			  <tr>
			    <td>{{row[2]}}</td>
			    <td>{{row[1]}}</td>
			    <td><a href="/sar?id={{row[0]}}" class="btn site btn-sm">SAR</a></td>
			    <td><a href="/pagar?id={{row[0]}}" class="btn site btn-sm">Pagar</a></td>
			    <td><a href="/gaa?id={{row[0]}}" class="btn site btn-sm">GAA</a></td>
			    <td><a href="/getstatus?id={{row[0]}}" class="btn success btn-sm">getByOperationId</a></td>
			    <td><a href="/devolucion_form?id={{row[0]}}" class="btn warning site btn-sm">Devolver</a></td>
			  </tr>
			%end
			</tbody>

			<tfoot>
				<tr>
					<td colspan="7">		    	
						<a href="/new" class="btn info">Nuevo</a>
					</td>
				</tr>
				<tr>
					<td colspan="7">		    	
						<a href="/login_form" class="btn info">Cambiar credenciales</a>
					</td>


				</tr>
			</tfoot>
		</table>
	</div>
% include('includes/footer.tpl')