
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

// Register MODAL

	$(".reg_change").click(function() {
		$(".modal").fadeOut();
		$(".modal_main").fadeOut();
		$(".reg_modal").delay(500).fadeIn();
		$(".reg_modal_main").show();
	});
	$(".reg_close").click(function() {
		$(".reg_modal").fadeOut();
		$(".reg_modal_main").fadeOut();
	});

// Add Logo Hovers Here

});
