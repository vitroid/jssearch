<script>
    import SessionTableRow from "./sessiontablerow.svelte";

    export let title
    export let sessions
    export let timebins
    export let slots

</script>

<div>
    <table>
        <tbody>
            <tr class='header'>
                <th colspan={sessions.length + 1} class='corner'>
                    {title}
                </th>
            </tr>
            <tr class='header'>
                <th></th>
                {#each sessions as session}
                <th class='col'>{session}</th>
                {/each}
            </tr>
            {#each timebins as starttime, i}
            <SessionTableRow
                {sessions}
                {starttime}
                slot={slots[i]}
                on:search />
            {/each}
        </tbody>
    </table>
</div>

<style>
    div {
        padding: 5px;
        margin: 0;
        /* border: solid 1px #888;
        border-radius: 10px; */
    }
    table {
        margin: 0px;
    }
    th.col {
        text-align: center;
        padding: 2px 2px 0;
        width: 22px;
        font-size:90%;
    }
    tr.header{
        background-color: #fff;
    }
    th.corner {
        width: 64px;
        font-size: 120%;
        /* padding: 10px 10px 0; */
    }
</style>
