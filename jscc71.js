//2021
var bins = ["", "9:20", "9:40", "10:00", "10:20", "11:00", "11:20", "11:40",
            "12:00", "13:40", "14:00", "14:20", "14:40", "15:20", "15:40", "16:00", "16:20"];
var bins2 = ["", "9:20", "9:40", "10:00", "10:20", "15:20", "15:40", "16:00", "16:20"];
//2021
var sc=[
  ["PA1", "^PA1-"],
  ["PB1", "^PB1-"],
  ["PC1", "^PC1-"],
  ["PD1", "^PD1-"],
  ["PE1", "^PE1-"],
  ["PF1", "^PF1-"],
  ["PA2", "^PA2-"],
  ["PB2", "^PB2-"],
  ["PC2", "^PC2-"],
  ["PD2", "^PD2-"],
  ["PE2", "^PE2-"],
  ["PF2", "^PF2-"],

  ["2Aa", "^2Aa-"],
  ["2Ab", "^2Ab-"],
  ["2B", "^2B-"],
  ["2C", "^2C-"],
  ["2D", "^2D-"],
  ["2Fa", "^2Fa-"],
  ["2Fb", "^2Fb-"],

  ["3Aa", "^3Aa-"],
  ["3Ab", "^3Ab-"],
  ["3B", "^3B-"],
  ["3C", "^3C-"],
  ["3D", "^3D-"],
  ["3E", "^3E-"],
  ["3Fa", "^3Fa-"],
  ["3Fb", "^3Fb-"],

  ["4Aa", "^4Aa-"],
  ["4Ab", "^4Ab-"],
  ["4C", "^4C-"],
  ["4E", "^4D-"],
  ["4Fa", "^4Fa-"],
  ["4Fb", "^4Fb-"],

  ["受賞講演", "^Aw-"],
  ["S1", "^S1-"],
  ["S2", "^S2-"],
  ["S3", "^S3-"],
  ["S4", "^S4-"],
];



function gid(id){
	return document.getElementById(id);
}

/*2020 new*/
function sessionstable(sessions, ends, bin){
  var buf= ["<table><tbody>"];
  buf.push("<tr class='header'><th class='corner'>Oral</th>");
  for(let j in sessions){
    buf.push("<th class='col'>",sessions[j],"</th>");
  }
  buf.push("</tr>");
  for(var i=1; i<=ends; i++){
    var si=i+"";
    if (i<10){
      si = "0"+si;
    }
    buf.push("<tr class='row'><th class='row'>",si,"</th>");
    for(let j in sessions){
      var id = sessions[j]+"-"+si;
      buf.push("<td class='row' id='v",id,"' onclick='onesearch(this)'></td>");
    }
    buf.push("<th class='right'>",bin[i],"</th>");
    buf.push("</tr>");
  }
  buf.push("</tbody></table>");
  return buf.join("");
}

function sympotable(sessions, ends, bin){
  var buf= ["<table><tbody>"];
  buf.push("<tr class='header'><th colspan='"+(sessions.length+1)+"' class='corner'>Symposia</th></tr><tr class='header'><th></th>");
  for(let j in sessions){
    buf.push("<th class='col'>",sessions[j],"</th>");
  }
  buf.push("</tr>");
  for(var i=1; i<=ends; i++){
    var si=i+"";
    if (i<10){
      si = "0"+si;
    }
    buf.push("<tr class='row'><th class='row'>",si,"</th>");
    for(let j in sessions){
      var id = sessions[j]+"-"+si;
      var tim = "";
      if (id in bin){
        tim = bin[id].substr(0,5);
      }
      buf.push("<td class='row' id='v",id,"' onclick='onesearch(this)'>"+tim+"</td>");
    }
    // buf.push("<th class='right'>",bins[i],"</th>");
    buf.push("</tr>");
  }
  buf.push("</tbody></table>");
  return buf.join("");
}

function awardtable(awards, bin){
  var buf= ["<table><tbody>"];
  buf.push("<tr class='header'><th colspan='2' class='cornerw'>Award lectures</th>");
  buf.push("</tr>");
  for(var i=0; i<awards.length; i++){
    buf.push("<tr class='row'>");
    var id = awards[i];
    var tim = "";
    if (id in bin){
      tim = bin[id];
    }
    buf.push("<th class='roww' id='v",id,"' onclick='onesearch(this)'>"+id+"</td>");
    buf.push("<th class='time'>"+tim+"</th>");

    // buf.push("<th class='right'>",bins[i],"</th>");
    buf.push("</tr>");
  }
  buf.push("</tbody></table>");
  return buf.join("");
}


function awardtable2(awards, bin){
  var buf= ["<table><tbody>"];
  buf.push("<tr class='header'><th colspan='2' class='cornerw'>Award lectures</th>");
  buf.push("</tr>");
  for(var i=0;i<awards.length; i++){
    var row=awards[i];
    buf.push("<tr class='row'>");
    for(var j=0;j<row.length; j++){
      var id = row[j];
      buf.push("<td class='row' id='v",id,"' onclick='onesearch(this)'>"+id+"</td>");
    }
    var tim = bin[i];
    buf.push("<th class='time'>"+tim+"</th>");
    // buf.push("<th class='right'>",bins[i],"</th>");
    buf.push("</tr>");
  }
  buf.push("</tbody></table>");
  return buf.join("");
}


function postertable(title, sessions){
  var buf= ["<table><tbody>"];
  buf.push("<tr class='header'><th colspan='11' class='corner'>"+title+"</th></tr><tr class='header'><th></th>");
  for(var i=0; i<10; i++){
    buf.push("<th class='col'>",i,"</th>");
  }
  buf.push("</tr>");

  for(var key in sessions){
    var value = sessions[key];
    for(var i=0; i<value; i+=10){
      var si = key + Math.trunc(i/10);
      buf.push("<tr class='row'><th class='row'>",si,"</th>");
      for(var j=0;j<10;j++){
        var id = si + j;
        buf.push("<td class='row' id='v",id,"' onclick='onesearch(this)'></td>");
      }
      buf.push("</tr>");
    }
  }
  buf.push("</tbody></table>");
  return buf.join("");
}

var sessions2=["2Aa","2Ab","2B","2C","2D",     "2Fa","2Fb"];
var sessions3=["3Aa","3Ab","3B","3C","3D","3E","3Fa","3Fb"];
var sessions4=["4Aa","4Ab",     "4C",     "4E","4Fa","4Fb"];
var sympos  = ["S1", "S2", "S3", "S4"];
var awards3 = [["Aw-01","-"],["Aw-02","-"],["Aw-03","Aw-04"]]
var abin3 = ["14:30","15:20","16:30"]
var awards4 = [["Aw-05","Aw-06"],["Aw-07","Aw-08"],["Aw-09","Aw-10"]]
var abin4 = ["11:00","13:20","14:10"]
var posters1 = {"PA1-":74, "PB1-":15, "PC1-":16, "PD1-":14, "PE1-":10, "PF1-":42};
var posters2 = {"PA2-":74, "PB2-":15, "PC2-":16, "PD2-":13, "PE2-":11, "PF2-":42};

function day1_panel(timebin){
  return postertable("Poster1: 9:30-12:00", posters1) + postertable("Poster2: 12:30-15:00", posters2) + sympotable(sympos, 7, timebin);
}

function day2_panel(timebin){
  return sessionstable(sessions2, 16, bins);
}

function day3_panel(timebin){
  return sessionstable(sessions3, 8, bins) + awardtable2(awards3, abin3);
}

function day4_panel(timebin){
  return sessionstable(sessions4, 8, bins2) + awardtable2(awards4, abin4);
}

function ad_panel(){
  var s = [];
  s.push("<div class='intro'>画像をクリックすると広告が表示され、企業名をクリックすると HP が開きます。</div><table class='c'><tbody>");
  for(var i=0; i<ads.length; i++){
    var a = ads[i]
    s.push('<tr><td class="fr"><a href="'+a.pdf+'" target="_blank"><img src="'+a.tn+'" /></a></td><td>')
    var sps=[]
    for(var j=0;j<a.sp.length; j++){
      sp = a.sp[j]
      sps.push("<div class='lk'><a class='l' href='"+sp.url+"'>"+sp.name+"</a></div>")
    }
    s.push(sps.join('<br />'));
    s.push('</td></tr>');
  }
  s.push("</tbody></table>")
  return s.join("");
}

function make_timetable(){
  var timebin={};
  // Award.jsには、"tim"というフィールドがあって、時間を書いてある。
  for(let i in data){
    if ("tim" in data[i]){
      timebin[data[i]["lab"]] = data[i]["tim"];
    }
  }
  console.log(timebin)
  gid("day1_panel").innerHTML = day1_panel(timebin);
  gid("day2_panel").innerHTML = day2_panel(timebin);
  gid("day3_panel").innerHTML = day3_panel(timebin);
  gid("day4_panel").innerHTML = day4_panel(timebin);
  gid("ad_panel").innerHTML   = ad_panel();
  /* set bg color dynamically*/
  for(let i in data){
    // 2020 comment out until program is decided.
    var v = gid("v"+data[i]["lab"]);
    if (v) v.style.backgroundColor = "#f0f0f0";
  }
}


function shortcuts(){
  s = [];
  for(let i in sc){
    s.push('<span class="lk2" onclick="query(\''+sc[i][1]+'\')">'+sc[i][0]+'</span> ');
  }
  gid('sc').innerHTML = s.join("");
}

make_timetable();
shortcuts();

// get from local storage
var checked;
if (window.localStorage.hasOwnProperty("checked")){
  checked = new Set(window.localStorage.checked.split(" "));
}
else{
  checked = new Set();
}
// set initial timetable
var labels=Array.from(checked);
for(let label in labels){
  var field = gid("v"+labels[label]);
  if (field){
    field.style.backgroundColor = "#0075ff";
  }
}
