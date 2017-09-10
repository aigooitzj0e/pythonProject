
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

// Log/Reg Validation Messages

	$('#post-form').submit(function(e){
		e.preventDefault(); //Prevents the form from doing its normal thing when submitted
		console.log('form submitted');
	});

	$('#email').change(function(){
		var email = $(this).val();
		console.log(email);
		$.ajax ({
			url: 'ajax/validate_email/',
			data: {
				'email': email
			},
			dataType: 'json',
			success: function (data) {
				console.log(data.is_taken);
				if (data.is_taken == false) {
					// alert("This email is not registered");
					$('#email').addClass('error')
				}
				else {
					$('#email').removeClass('error')
				}
			}
		});
	});

	// $('#first_name').change(function(){
	// 	var firstName = $(this).val();
	// 	if (firstName.length < 2) {
	// 		$(this).css('border-color', "red");
	// 	}
	// 	else {
	// 		$(this).css('border-color', 'inherit')
	// 	}
	// })


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
