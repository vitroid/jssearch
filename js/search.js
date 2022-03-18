{
	$_ = String.prototype;

	$_.mReplace = function(pat,flag){
		var temp = this;
		if(!flag){flag=""}
		for(var i in pat){
			var re = new RegExp(i,flag);
			temp = temp.replace(re,pat[i])
		}
		return temp;
	};
}

{
	$_ = Date.prototype;

	$_.format = "yyyy-mm-dd HH:MM:SS";
	$_.formatTime = function(format){
		var yy;
		var o = {
			yyyy : ((yy = this.getYear()) < 2000)? yy+1900 : yy,
			mm   : this.getMonth() + 1,
			dd   : this.getDate(),
			HH   : this.getHours(),
			MM   : this.getMinutes(),
			SS   : this.getSeconds()
		}
		for(var i in o){
			if (o[i] < 10) o[i] = "0" + o[i];
		}
		return (format) ? format.mReplace(o) : this.format.mReplace(o);
	}
}

gid("q").focus();
gid('q').addEventListener('compositionend', (event) => {
							do_find(gid('q').value);
  console.log(`generated characters were: ${event.data}`);
});

var start = new Date().getTime();
var bodylist = [];
var st = gid("stat");
var re = gid("result");
var nv = gid("navi");
var tt = gid("timetable");

var max = 10;
var KC = {
	enter: 13,
	left : 37,
	right: 39,
	up   : 38,
	down : 40
};

function ignore_case(){
	var a = arguments;
	return "[" + a[0] + a[0].toUpperCase() + "]"
}
function do_find(v){
	if(this.lastquery == v){return}
	this.lastquery = v;
	var re = find(v);
	pagenavi(re);
	view(re)
  pagenavi(re);
}
function key(c){
	switch(c){
		case KC.up   : mv(-1);break;
		case KC.down : mv(1);break;
	}
}
function find(v){
	var query = v;
	if(!v){return []}
	var aimai;
	if(query){
		aimai = query.replace(/[a-z]/g,ignore_case);
		try{
			reg = new RegExp(aimai,"g");
		}catch(e){
			reg = /(.)/g;
		}
	}else{
		reg = /(.)/g;
	}
	var start = new Date().getTime();
	var result = [];
	for(var i=0;i<data.length;i++){
		var s = bodylist[i];
    reg.lastIndex = 0; // because reg remembers the last place
		var res = reg.exec(s);
		if(!res){continue}
		var len = res[0].length;
		var idx = res.index;
		if(idx != -1){
			result.push([i,idx,len]);
		}
	}
	//if(result.length){
		st.innerHTML = result.length +" items found.";
	//}
	var end = new Date().getTime();

	console.log("Find:"+ (end-start) + " ms");
	return result;
}
function time2date(time){
	if(!this.cache){this.cache = {}};
	if(this.cache[time]) return this.cache[time];
	var d = new Date(time*1000);
	this.cache[time] = d.formatTime("yyyy-mm-dd");
	return this.cache[time];
}
function snippet(body,idx,len){
	var start = idx - 20;
	return [
		body.substring(start,idx),
		,"<b>"
		,body.substr(idx,len)
		,"</b>"
		,body.substr(idx+len,50),
	].join("");
}
function pagenavi(result){
	var len = result.length;
	var ct = Math.ceil(len/max);
	var buf = [];
	for(var i=0;i<ct;i++){
		buf.push(
			"<span onclick='view(\"\","
			,i+1
			,");sw(",i,")'>"
			,i+1
			,"</span>"
		);
	}
	nv.innerHTML = buf.join("");
	sw(0);
}
function sw(t){
	var span = nv.getElementsByTagName("span");
	for(var i=0;i<span.length;i++){
		span[i].className = (i==t)?"selected":"";
	}
}
function mv(to){
	var span = nv.getElementsByTagName("span");
	var current;
	if(!span.length){return}
	for(var i=0;i<span.length;i++){
		if(span[i].className == "selected"){
			current = i;break;
		}
	}
	var moveto = current+to;
	if(moveto < 0){moveto += span.length}
	if(moveto > span.length-1){moveto=0}
	sw(moveto);
	view("",moveto+1)
}
/*2020 new*/
function cbclick(checkbox){
    //If it is checked.
    if(checkbox.checked){
      checked.add(checkbox.id);
      gid("v"+checkbox.id).style.backgroundColor = "#0075ff";
      gid("v"+checkbox.id).style.color = "#fff";
    }
    //If it has been unchecked.
    else{
      checked.delete(checkbox.id);
      gid("v"+checkbox.id).style.backgroundColor = "#f0f0f0";
      gid("v"+checkbox.id).style.color = "#000";
    }
    var s = Array.from(checked).join(" ");
    //fv.innerHTML = s;
    window.localStorage.checked = s;
}
/*2020 new*/
function query(v){
  document.getElementById("q").value = v;
  do_find(v);
}
function onesearch(bin){
  query(bin.id.substring(1)); //elim first v
}

function view(result,offset){
	if(!offset){offset = 1}
	if(!result){
		result = this.last;
	}else{
		this.last = result;
	}
	//var r = result.reverse();
  var r = result;
	var buf = ["<table>"];
	var count = 0;
  var checkmark;
	for(var i=(offset-1)*max;i<r.length;i++){
		count++;
		if(count > max){break}
		var num = r[i][0];
		var idx = r[i][1];
		var len = r[i][2];
		with(data[num]){
      var link;
      if(typ == "zoom"){
        link = "<a class='zm' href='"+zoom[roo].URL+"'>"+zoom[roo].room+"</a>";
      }
      else{//remo
        link = "<a class='rm' href='"+remo[roo][0]+"'>"+remo[roo][1]+"</a>";
      }
      if (checked.has(lab)){
        checkmark=" checked";
      }
      else{
        checkmark="";
      }
      var au=inf; //list of title and authorlist
      var s = "";
      for ( var j=0; j<au.length; j+=2){
        s += "<span class='ti'>" + au[j] + "</span><br />" + au[j+1] + "<br />"
      }
			buf.push(
		       "<tr class='r'><td class='i'><a href='",pdf,"' target='_blank'><img src='",pre,"' width='200' height='200' /></a></td>",
		       "<td class='d'><span style='float:left'><input type='checkbox' id='",lab,"' onclick='cbclick(this)' ",checkmark,"></span><span class='l'>",lab,"</span>",link,"<br />", s, "<div class='m'>..."
		       ,snippet(bodylist[num],idx,len)
		       ,"</m></td></tr>"
			);
		}
	}
	buf.push("</table>");
	re.innerHTML = buf.join("");
}


//for debug
//fv.innerHTML = window.localStorage.checked;


for(var i=0;i<data.length;i++){
	bodylist.push(data[i].con);
}
//var bodyidx = bodylist.join("<>");
var end = new Date().getTime();

console.log("Index:"+ (end-start) + " ms");
