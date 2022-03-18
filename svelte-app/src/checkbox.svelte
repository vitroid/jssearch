<script>
    import { marks } from "./mark.js";
    import { directory } from "./directory.js";
	// import { onMount } from 'svelte';

    export let id;


    let _this;
    let status = marks[id];
	// onMount( () => {
    //     status = $marks.has(id);
	// });

    function cbclick ( event ){
        // let id = event.srcElement.id
        status = marks[id]
        if (status){
            // $marks.delete(id)
            directory[id].style.backgroundColor = "#f0f0f0";
            directory[id].style.color = "#000";
            _this.style.backgroundColor = "#f0f0f0";
            marks[id] = false;
        }
        else{
            // $marks.add(id)
            // directoryにはスケジュール表の要素が設定されている。
            directory[id].style.backgroundColor = "#0075ff";
            directory[id].style.color = "#fff";
            _this.style.backgroundColor = "#0075ff";
            marks[id] = true;
        }
    }

</script>

{#if marks[id]}
<button class="on" id={id} on:click={cbclick} bind:this={_this}>
{id}
</button>
{:else}
<button class="off" id={id} on:click={cbclick} bind:this={_this}>
{id}
</button>
{/if}


<style>
    button {
        font-size:150%;
        font-weight:bold;
        text-decoration: none;
        border-radius: 10px 10px 10px;
    }
    button.on {
        color: #fff;
        background-color:#0075ff;
    }
    button.off {
        color: #000;
        background-color:#f0f0f0;
    }
</style>