
//alert("Welcome to Miranda's Webpage!");

function changeImg(){
	var image = document.getElementById("shapes");
	
	if (image.src.match("shapes.png")){
		image.src = "shapes2.png";
		image.alt = "Shapes Project 2";
	}
	else{
		image.src = "shapes.png";
		image.alt = "Shapes Project 1";
	}
}

