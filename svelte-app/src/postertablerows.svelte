<script>
    import PosterTableRow from "./postertablerow.svelte";
    export let label;
    export let items;

    let rows;

    $: {
        let rowset = new Set()
        items.forEach(function(i){
            rowset.add(Math.trunc(i / 10))
        });
        rows = Array.from(rowset);
    }
</script>

{#each rows as row, _}
<PosterTableRow label={label} row={row} {items} on:search />
{/each}
