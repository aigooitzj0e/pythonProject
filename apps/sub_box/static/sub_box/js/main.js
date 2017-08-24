
//  Login MODAL

$(document).ready(function() {
	$(".call_modal").click(function() {
		$(".modal").fadeIn();
		$(".modal_main").show();
	});
	$(".close").click(function() {
		$(".modal").fadeOut();
		$(".modal_main").fadeOut();
	});

// Add Logo Hovers Here





// member page
	$("#Indica").click(function(){
		$("#strainpics").css("background-image", "url('http://localhost:8000/static/sub_box/img/indica.jpg')");
	});
	$("#Hybrid").click(function(){
		$("#strainpics").css("background-image", "url('http://localhost:8000/static/sub_box/img/hybrid.jpg')");
	});
	$("#Sativa").click(function(){
		$("#strainpics").css("background-image", "url('http://localhost:8000/static/sub_box/img/sativa.jpg')");
	});
});
