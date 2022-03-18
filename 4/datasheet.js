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
    //var figure = record["figure"]
    var figure = record["resized"]

    var english = record["style"] === "2" || record["style"] === "4";

    var aus = authorlists(record);

    var frame = ""
    if (figure){
	frame = "<div><img src='"+figure+"' class='preview' />" +  marked("**Figure** " + caption) + "</div>"
    }

    //difference from preview.js
    // make a table for additional data
    var subject = record["subject"]
    var keyword1 = record["keyword1r"]
    var keyword2 = record["keyword2r"]
    var keyword1t = record["keyword1t"]
    var keyword2t = record["keyword2t"]
    var keyword3 = record["keyword3"]
    var style = record["style"]
    var ordern = record["order.num"]
    var orderd = record["order.den"]
    var priorn = record["priority.num"]
    var priord = record["priority.den"]
    var award = record["award.apply"]
    var award2 = record["award2.apply"]
    var comment = record["comment"]
    var abst = record["abst"]

    // make them labels
    var subjects={
        1:"A 錯体の合成と性質 (Syntheses and Characterization of Coordination Compounds)",
        2:"B 錯体の構造と電子状態 (Geometrical and Electronic Structures of Coordination Compounds)",
        3:"C 錯体の反応 (Reactions of Coordination Compounds)",
        4:"D 有機金属錯体 (Organometallic Complexes)",
        5:"E 生物無機化学 (Complexes related to Bioinorganic Chemistry)",
        6:"F 錯体の機能と応用 (Functionalities and Applications of Coordination Compounds)"}
    subject = subjects[subject]

    var kw={
      1: "構造化学 / structural chemistry",
      2: "立体化学 / stereochemistry",
      3: "溶液化学 / solution chemistry",
      4: "分光学的性質 / spectroscopic properties",
      5: "電気化学 / electrochemistry",
      6: "理論計算・分子軌道 / theoretical calculations & MO",
      7: "電子状態 / electronic states",
      8: "単核錯体 / mononuclear complexes",
      9: "多核錯体 / polynuclear complexes",
      10: "集積型錯体 / metal-assembled complexes",
      11: "超分子錯体 / supramolecular complexes",
      12: "金属酸化物・ヘテロポリ酸 / metal oxides & heteropolyacids",
      13: "金属間相互作用 / metal-metal interactions",
      14: "非共有結合性相互作用 / noncovalent interactions",
      15: "ホスト-ゲスト / host-guest chemistry",
      16: "光化学 / photochemistry",
      17: "磁気的性質 / magnetic properties",
      18: "蛋白質・酵素 / proteins & enzymes",
      19: "DNA / DNA",
      20: "医薬 / medicines",
      21: "酵素モデル / enzyme models",
      22: "自己組織化 / self-assemblies",
      23: "分子認識 / molecular recognition",
      24: "液晶 / liquid crystals",
      25: "吸着特性 / adsorption properties",
      26: "細孔 / pores",
      27: "酸化反応 / oxidation reactions",
      28: "還元反応 / reduction reactions",
      29: "分解・切断反応 / decomposition & cleavage reactions",
      30: "水和・加水分解反応 / hydration & hydrolysis",
      31: "小分子活性化 / activation of small molecules",
      32: "触媒 / catalysts",
      33: "センサー / sensors",
      34: "表面・界面（膜） / surfaces & interfaces (membranes)",
      35: "スイッチング / switching behaviors",
      36: "分子磁性 / molecular magnetism",
      37: "電導性 / electroconductivity",
      38: "誘電体 / dielectric",
      39: "EL素子 / EL devices",
	40: "その他（具体的に） / others (in concrete terms)"
    }

    var styles = {
        1: "口頭(日本語一般講演)(Oral Presentation; Japanese Talk)",
        2: "Oral Presentation; English Talk",
        3: "ポスター(日本語) (Poster Presentation; in Japanese)",
	4: "Poster Presentation; in English",
    }
    style = styles[style];
    
    var keywords = kw[keyword1]
    if ( keyword1t != "" ){
	keywords += " ( " + keyword1t + " ) "
    }
    keywords += " | " + kw[keyword2]
    if ( keyword2t != "" ){
	keywords += " ( " + keyword2t + " ) "
    }
    keywords += " | " + keyword3
    
    priority = ""
    if ( priorn ) priority = priord + "件中の" + priorn + "番目"
    order = ""
    if ( ordern ) order = orderd + "件中の" + ordern + "番目"

    if ( award == 2 ){
	award = "応募する (I apply)"
    }
    else {
	award = ""
    }
    if ( award2 == 2 ){
	award2 = "応募する (I apply)"
    }
    else {
	award2 = ""
    }
    
    var el = []
    el.push("<table><tbody>")
    el.push("<tr><th>ID</th><td>"+label+"</td></tr>")
    el.push("<tr><th>討論主題</th><td>"+subject+"</td></tr>")
    el.push("<tr><th>キーワード</th><td>"+keywords+"</td></tr>")
    el.push("<tr><th>発表形式</th><td>"+style+"</td></tr>")
    el.push("<tr><th>口頭発表の優先度</th><td>"+priority+"</td></tr>")
    el.push("<tr><th>発表順序</th><td>"+order+"</td></tr>")
    el.push("<tr><th>ポスター賞</th><td>"+award+"</td></tr>")
    el.push("<tr><th>学生講演賞</th><td>"+award2+"</td></tr>")
    el.push("<tr><th>Comment</th><td>"+comment+"</td></tr>")
    el.push("</tbody></table><p>" + marked(abst) + "</p>")
    appendix = el.join("")
    document.getElementById("appendix").innerHTML = appendix;
    // end difference



    
    document.getElementById("label").innerHTML = label;
    if (english) {
	console.log(document)
	console.log(document.getElementById("title_main"));
	document.getElementById("title_main").innerHTML = marked(title);
	document.getElementById("author_main").innerHTML = aus[1];
	document.getElementById("abst_main").innerHTML = frame + marked(abste);
    }
    else {
	document.getElementById("title_main").innerHTML = marked(titlj);
	document.getElementById("author_main").innerHTML = aus[0];
	document.getElementById("abst_main").innerHTML = frame + marked(abstj);
	document.getElementById("title_sub").innerHTML = marked(title);
	document.getElementById("author_sub").innerHTML = aus[1];
	document.getElementById("abst_sub").innerHTML = marked("**Abstract:** " + abste);
    }
}
