<script>
    import { _ } from 'svelte-i18n';
    import AwardButton from "./awardbutton.svelte";
    export let button_titles=[]
    // export let timebin
    export let starttime
    export let ids

</script>

<tr class='row'>
    <th class='row'>
        {starttime}
    </th>
    {#each ids as id, i}
    <td class="row">
    <AwardButton {id} title={$_(button_titles[i])} on:search />
    </td>
    {/each}
</tr>

<style>
    td.row {
        text-align: center;
        padding: 0;
    }
</style>
