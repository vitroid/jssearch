<script>
    import SessionButton from "./sessionbutton.svelte";
    export let sessions
    // export let timebin
    export let starttime
    export let slot

</script>

<tr class='row'>
    <th class='row'>
        {slot}
    </th>
    {#each sessions as session}
    <td class="row">
    <SessionButton id={session+"-"+("00"+slot).slice(-2)} on:search />
    </td>
    {/each}
    <th class='row'>
        {starttime}
    </th>
</tr>

<style>
    td.row {
        text-align: center;
        padding: 2px 2px 0;
        width: 22px;
    }
</style>
