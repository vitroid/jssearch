<script>
    // ボタンに内容が書かれているタイプ。受賞講演のみに使用
    import { _ } from 'svelte-i18n';
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
                sessions={rooms}
                button_titles={button_titles[i]}
                ids={ids[i]}
                {starttime}
                on:search />
            {/each}
            <!-- export let sessions
            export let button_titles=[]
            // export let timebin
            export let starttime
            export let slot -->
            <tr>
                <th>
                    15:40
                </th>
                <td class="event">
                    {$_("JSCC general meeting")}
                </td>
            </tr>
        </tbody>
    </table>
    <table>
        <tbody>
            <tr class='header'>
                <th></th>
                <th class='corner'>
                    {$_("Hotel Okura Fukuoka")}
                </th>
            </tr>
            <tr>
                <th>
                    17:30
                </th>
                <td class="event">
                    {$_("Banquet")}
                </td>
            </tr>
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
    .event {
        width: 240px;
        text-align: center;
    }
</style>
