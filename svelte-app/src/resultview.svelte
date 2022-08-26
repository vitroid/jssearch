<script>
    import PageNavi from "./pagenavi.svelte";
    import View from "./view.svelte";
    export let results = [];

    const max=10;
    let npage = 0;
    let currentPage = 0;
    let subset = [];

    function moveto(page){
        subset = []
        currentPage = page;
        for(let i=0; i<max; i++){
            const record = page*max+i;
            if (record < results.length){
                subset.push(results[record]);
            }
        }
    }

    export function move_up(){
        if (currentPage > 0){
            moveto(currentPage-1);
        }
    }

    export function move_down(){
        if (currentPage < npage-1){
            moveto(currentPage+1);
        }
    }




    $: {
        // when the results are changed, i.e. new query
        npage = Math.ceil(results.length / max);
        moveto(0);
    }


    function handler(event){
        // when page navi is pressed
        subset = [];
        const page = event.detail.text;
        console.log("move to ", page)
        moveto(page);
    }


</script>

{#each Array(npage) as _, pagenum}
<PageNavi page={pagenum} on:pagenavi={handler} highlight={currentPage == pagenum}/>
{/each}

<table>
    <tbody>
        {#each subset as record}
        <View {record} />
        {/each}
    </tbody>
</table>

<style>

</style>
