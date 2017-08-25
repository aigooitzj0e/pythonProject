$(document).ready(function(){
	
	$(".next_link").on("click", function(e){

		var currentActiveImage = $(".image_shown");
		var nextActiveImage = currentActiveImage.next();

		if(nextActiveImage.length == 0)
		{
			nextActiveImage = $(".carousel_inner img").first();
		}
		currentActiveImage.removeClass("image_shown").addClass("image_hidden").css("z-index", -10);
		nextActiveImage.addClass("image_shown").removeClass("image_hidden").css("z-index", 20);
		$(".carousel_inner img").not([currentActiveImage, nextActiveImage]).css("z-index",1);

		e.preventDefault();
	});

	$(".prev_link").on("click", function(e){

		var currentActiveImage = $(".image-shown");
		var nextActiveImage = currentActiveImage.prev();

		if(nextActiveImage.length == 0)
		{
			nextActiveImage = $(".carousel_inner img").last();

		}
		currentActiveImage.removeClass("image_shown").addClass("image_hidden").css("z-index", -10);
		nextActiveImage.addClass("image_shown").removeClass("image_hidden").css("z-index", 20);
		$(".carousel_inner img").not([currentActiveImage, nextActiveImage]).css("z-index", 1);

		e.preventDefault();

	})
});