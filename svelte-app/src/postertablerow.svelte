<script>
    import PosterButton from "./posterbutton.svelte";
    export let label;
    export let row;
    export let items;

</script>

<tr class='row'>
    <th class='row'>
        {label}{row}
    </th>
    {#each [0,1,2,3,4,5,6,7,8,9] as i}
    <td class="row">
    <PosterButton order={i} row={row} label={label} items={items} on:search />
    </td>
    {/each}
</tr>

<style>
    td.row {
        text-align: center;
        padding: 2px 2px 0;
        width: 22px;
    }
</style>
