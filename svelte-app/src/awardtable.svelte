<script>
    // ボタンに内容が書かれているタイプ。受賞講演のみに使用
    import SessionTableRow2 from "./awardtablerow.svelte";

    export let title
    export let rooms
    export let timebins
    export let button_titles
    export let ids

</script>

<div>
    <table>
        <tbody>
            <tr class='header'>
                <th></th>
                <th colspan={rooms.length} class='corner'>
                    {title}
                </th>
            </tr>
            <tr class='header'>
                <th></th>
                {#each rooms as session}
                <th class='col'>{session}</th>
                {/each}
            </tr>
            {#each timebins as starttime, i}
            <SessionTableRow2
                button_titles={button_titles[i]}
                ids={ids[i]}
                {starttime}
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
        width: 100%;
        display: flex;
        justify-content: center;
    }
    table {
        margin: 0px;
        /* min-width: 640px; */
        table-layout: fixed;
    }
    th.col {
        text-align: center;
        padding: 2px 2px 0;
        font-size:90%;
    }
    tr.header{
        background-color: #fff;
    }
    th.corner {
        font-size: 120%;
        /* padding: 10px 10px 0; */
    }
</style>
