<script>
    import SessionButton from "./sessionbutton.svelte";
    export let sessions
    export let button_titles=[]
    // export let timebin
    export let starttime
    export let ids

</script>

<tr class='row'>
    <th class='row'>
        {starttime}
    </th>
    {#each sessions as session, i}
    <td class="row">
    <SessionButton id={ids[i]} title={button_titles[i]} on:search />
    <!-- <SessionButton on:search /> -->
    </td>
    {/each}
</tr>

<style>
    td.row {
        text-align: center;
        padding: 0;
        width: 22px;
    }
</style>
