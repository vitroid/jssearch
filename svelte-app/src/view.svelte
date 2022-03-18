<script>
    import { data } from "./index.svelte";
    // import { marks } from "./mark.js";
    import { directory } from "./directory.js";
    import Checkbox from "./checkbox.svelte";

    export let record;

    let rec;
    let head;
    let len;

    let pdf;
    let link; //for zoom link
    let s;
    let pre;
    let lab;
    let au;
    let index;
    let snippet;
    // let checked;

    function makeSnippet(body,idx,len){
        var start = idx - 20;
        return [
            body.substring(start,idx)
            ,body.substr(idx,len)
            ,body.substr(idx+len,50)
        ];
    }

    $: {
        rec = record[0]
        head = record[1]
        len = record[2]

        pdf = data[rec].pdf
        link = ""; //for zoom link
        snippet = ""
        s = ""
        pre = data[rec].pre
        lab = data[rec].lab
        index = data[rec].con

        // preformatted html cannot be rendered in svelte.
        let titles = data[rec].inf
        au = []
        for(let i=0; i<titles.length; i+=2){
            au.push([titles[i], titles[i+1]])
        }
        snippet = makeSnippet(index, head, len)
        // checked = $marks.has(lab);
    }

    // function cbclick ( event ){
    //     console.log(event)
    //     let id = event.srcElement.id
    //     if (event.srcElement.checked){
    //         $marks.add(id)
    //         // directoryにはスケジュール表の要素が設定されている。
    //         directory[id].style.backgroundColor = "#0075ff";
    //         directory[id].style.color = "#fff";
    //     }
    //     else{
    //         $marks.delete(id)
    //         directory[id].style.backgroundColor = "#f0f0f0";
    //         directory[id].style.color = "#000";
    //     }   
    // }

</script>

<tr class='r'>
    <td class='i'>
        <a href={pdf} target='_blank'>
            <img src={pre} width='200' height='200' alt="thumbnail" />
        </a>
    </td>
    <td class='d'>
        <span style='float:left'>
            <Checkbox id={lab}/>
        </span>
        {link}
        <br />
        {#each au as tiau}
        <span class="ti">{tiau[0]}</span><br />{tiau[1]}<br />
        {/each}
        {s}
        <div class='m'>...
            {snippet[0]}<b>{snippet[1]}</b>{snippet[2]}
        </div>
    </td>
</tr>

<style>
    span.ti{
        font-weight:bold;
    }

    tr.r:nth-child(odd){
        background-color: #e0e0e0;
    }

    @media screen and (min-width: 550px) {
        tr.r{
            display: flex;           /* flexコンテナ化 */
            flex-direction: row;
            justify-content: flex-start;
        }
    }

    @media screen and (max-width: 550px) {
        tr.r {
            display: flex;
            flex-direction: column-reverse;
            align-items: center;
        }
        td.i { justify-content: center; }
    }
    tr.r{
        margin: 0px;
    }
    b{
        color:#666600;
        background-color:#ffffdd;
        font-weight:bold;
        border:1px solid #bbbb00;
        margin:0 2px 0 2px;
        padding:0 2px 0 2px;
    }
    div.m{
        color: #808080;
        background-color: #fff;
    }
</style>