<script>
    // import { project } from "./jscc71.svelte";
    import PosterTableRows from "./postertablerows.svelte";

    export let title;
    export let sessions;

</script>

<div>
    <table>
        <tbody>
            <tr class='header'>
                <th colspan='11' class='corner'>
                    {title}
                </th>
            </tr>
            <tr class='header'>
                <th></th>
                {#each [0,1,2,3,4,5,6,7,8,9] as i}
                <th class='col'>{i}</th>
                {/each}
            </tr>
            {#each sessions as session}
            <PosterTableRows label={session.label} items={session.items} on:search />
            {/each}
        </tbody>
    </table>
</div>

<style>
    div {
        padding: 5px;
        margin: 0px;
        /* border: solid 1px #888;
        border-radius: 10px; */
    }
    table {
        margin: 0px;
        /* background-color: #ddd; */
    }
    th.col {
        text-align: center;
        padding: 2px 2px 0;
        width: 22px;
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
