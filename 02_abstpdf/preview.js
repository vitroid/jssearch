function authorlists(record){
    var speakermark = "〇";
    if ( record["award.apply"] ){
	speakermark = "◎";
    }
    else if ( record["award2.apply"] ){
	speakermark = "★";
    }

    var namesj = [];
    var namese = [];

    var namej = record["happyo.name"];
    var namee = record["happyo.namee"];

    if ( record["happyo.speak"] ){
	namej = speakermark + namej;
	namee = speakermark + namee;
    }

    var affil = record["happyo.affil"];
    namej += "<sup>"+affil+"</sup>";
    namee += "<sup>"+affil+"</sup>";

    namesj.push(namej);
    namese.push(namee);

    for( var i=1;i<=record["array.count"];i++){
	var tag = "array." + i + "happyo.namee";

	namej = record["array." + i + "happyo.name"];
	namee = record["array." + i + "happyo.namee"];
	if ( namee == "" )
	    break;

	if ( record["array." + i + "happyo.speak"] ){
	    namej = speakermark + namej;
	    namee = speakermark + namee;
	}

	var affil = record["array." + i + "happyo.affil"];
	namej += "<sup>"+affil+"</sup>";
	namee += "<sup>"+affil+"</sup>";

	namesj.push(namej);
	namese.push(namee);

    }

    var auj = namesj.join("・");
    var aue = namese.join(", ");

    var affilsj = [];
    var affilse = [];

    for( var i=1; i<10; i++){
	var affilj = record["affil" + i];
	var affile = record["affil" + i + "e"];
	if ( ! affile ) break;
	affilsj.push("<sup>" + i + "</sup>" + affilj);
	affilse.push("<sup>" + i + "</sup>" + affile);
    }
    auj = "(" + affilsj.join("・") + ") " + auj;
    aue = "(" + affilse.join(", ") + ") " + aue;

    return [auj, aue];
}

function replacer(x){
    if (x.match(/^<\/*su[pb \/]>$/))
	return x;
    console.log(x);
    return "";
}


function cleanse(text){
    // remove harmful HTML tags
    return text.replace(/(<[^>]*>)/g, replacer)
}


function build(record){
    var title = cleanse(record["titlee"])
    var titlj = cleanse(record["title"])
    var abste = cleanse(record["abstracte"])
    var abstj = cleanse(record["abstract"])
    var caption = record["caption"]
    var label = record["id"]  // should be the presentation ID
    var figure = record["figure"]
    if ( record["code"] )
    label = record["code"];
    // var figure = record["resized"]

    var english = record["style"] === "2" || record["style"] === "4";

    var aus = authorlists(record);

    if ( figure ){
	var frame = document.createElement("div");
	var img = document.createElement("img");
	//img.src = "attach/" + figure + ".body"; //seems OK
	img.src = "figure.jpg"
	img.className = "preview";
	frame.appendChild(img);

	frame.innerHTML += marked("**Figure** " + caption);
    }

    document.getElementById("label").innerHTML = label;
    if (english) {
	console.log(document)
	console.log(document.getElementById("title_main"));
	document.getElementById("title_main").innerHTML = marked(title);
	document.getElementById("author_main").innerHTML = aus[1];
	document.getElementById("abst_main").innerHTML = marked(abste);
    }
    else {
	document.getElementById("title_main").innerHTML = marked(titlj);
	document.getElementById("author_main").innerHTML = aus[0];
	document.getElementById("abst_main").innerHTML = marked(abstj);
	document.getElementById("title_sub").innerHTML = marked(title);
	document.getElementById("author_sub").innerHTML = aus[1];
	document.getElementById("abst_sub").innerHTML = marked("**Abstract:** " + abste);
    }
    if (figure){
	document.getElementById("abst_main").appendChild(frame);
    }
}
