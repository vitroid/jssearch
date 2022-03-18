<script>
    import ResultView from "./resultview.svelte";
    // import { move_up, move_down } from "./resultview.svelte";
    import { data } from "./index.svelte";
    export let search = "";

    $: {
        do_find(search);
    }

    let st = "";
    let lastquery = "";
    let results = [];
    let resultView;

    function do_find(v){
        console.log(v);
        if (lastquery == v)
            return;
        lastquery = v;
    	results = find(v);
    }
    function key(event){        
	    switch(event.key){
		    case "ArrowUp" : resultView.move_up();break;
    		case "ArrowDown" : resultView.move_down();break;
    	}
    }

    function ignore_case(){
    	var a = arguments;
        return "[" + a[0] + a[0].toUpperCase() + "]"
    }

    function find(query){

        if(!query){return []}

        var aimai;
        var reg;
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
            var s = data[i].con;
        reg.lastIndex = 0; // because reg remembers the last place
            var res = reg.exec(s);
            if(!res){continue}
            var len = res[0].length;
            var idx = res.index;
            if(idx != -1){
                result.push([i,idx,len]);
            }
        }
        if(result.length < 2){
            st = result.length +" item found.";
        }
        else{
            st = result.length +" items found.";
        }
        var end = new Date().getTime();

        console.log("Find:"+ (end-start) + " ms");
        return result;
    }

</script>

<div>
    <input type="text" id="q" on:keydown={key} autocomplete="off" placeholder="Search" bind:value={search} />
    {st}
    <ResultView results={results} bind:this={resultView} />
</div>

