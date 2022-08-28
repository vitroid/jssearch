<script>
    import AsyncTableColumn from "./asynctablecolumn.svelte";

    export let table
    export let colnames
    export let title
</script>

<div class="container2">
    <h3>{title}</h3>
    <div class="container">
        {#each table as column, i}
        <div class="column">
            <AsyncTableColumn {column} label={colnames[i]} on:search/>
        </div>
        {/each}
    </div>
</div>

<style>
    .container2 {
        display: flex;
        justify-content: start;
        flex-direction: column;
        margin: 5px;
    }
    h3 {
        text-align: center;
    }
    .container {
        display: flex;
        justify-content: start;
        flex-direction: row;
    }
</style>
