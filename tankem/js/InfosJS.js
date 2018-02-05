$(function (){
	getState();
})
function getState(){
	$.ajax({
		type:"POST",
		url:"ajaxInfos.php",
		data:{}
	})
		.done(function (response) {
			var resultat = JSON.parse(response);
			document.getElementById("editNom").value = resultat.NAME;
			document.getElementById("editPrenom").value = resultat.SURNAME;
			document.getElementById("editColor").value = resultat.COULEURTANK;
			document.getElementById("editEmail").value = resultat.EMAIL;
			document.getElementById("editUsername").value = resultat.USERNAME;
		

		})
}