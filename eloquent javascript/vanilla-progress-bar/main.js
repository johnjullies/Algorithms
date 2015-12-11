var bar = document.querySelector(".progress div");
addEventListener("scroll", function() {
	var max = document.body.scrollHeight - innerHeight;
	var percent = (pageYOffset / max) * 100;
	bar.style.width = percent + "%";
});