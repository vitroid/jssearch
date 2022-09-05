<script lang="ts">
    export let table
    let stable
    $: {
        stable = smart_table(table)
        stable = merge_rows(stable)
        stable = compress(stable)
    }

    function smart_table(table){
        // automatic colspan
        // assume table is a 2-d array
        let newtable = []
        for (let r=0; r< table.length; r++)        {
            newtable[r] = []
        }
        for(let c=0; c < table[0].length; c++)        {
            for (let r=0; r< table.length; r++)            {
                newtable[r][c] = {value:table[r][c]}
            }
        }
        return newtable;
    }

    function merge_rows(table){
        // automatic rowspan
        // assume table is a 2-d array

        for(let c=0; c < table[0].length; c++)        {
            let cur = "&&&&&"
            let cnt = 0
            let firstrow = 0
            for (let r=0; r< table.length; r++)            {
                if ( cur == table[r][c].value ){
                    table[r][c].value = "〃"
                    cnt ++
                }
                else {
                    if ( cur != "&&&&&" ){
                        table[firstrow][c] = {...table[firstrow][c], rowspan:cnt}
                    }
                    cur = table[r][c].value
                    cnt = 1
                    firstrow = r
                }
            }
            table[firstrow][c] = {...table[firstrow][c], rowspan:cnt}
        }
        return table;
    }

    function compress(table)
    {
        // remove merged items
        let newtable = []
        for (let r=0; r< table.length; r++) {
            newtable[r] = []
            for(let c=0; c < table[0].length; c++) {
                if ( table[r][c].value != "〃" ){
                    newtable[r] = [...newtable[r], table[r][c]]
                }
            }
        }
        return newtable
    }
</script>

<table>
    <tbody>
        {#each stable as row, j}
        <tr class={"row"+j}>
            {#each row as col, i}
            <td rowspan={col.rowspan}>
                {@html col.value}
            </td>
            {/each}
        </tr>
        {/each}
    </tbody>
</table>

<style>
    table {
        margin-left: auto;
        margin-right: auto;
        background-color: #ddd;
    }
    tr {
        /* border: 1px solid #888; */
        background-color: #fff;
        margin: 0;
    }
    td {
        text-align: center;
    }
    .row0 {
        font-weight: bold;
    }
</style>
