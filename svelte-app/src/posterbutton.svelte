<script>
    import { createEventDispatcher,onMount } from 'svelte';
    import { directory } from "./directory.js";
    import { marks } from './stores.js';
	const dispatch = createEventDispatcher();

    export let label;
    export let row;
    export let order;
    export let items;


    let active = true;
    let color = "#888";
    let id;

    onMount(() => {
        const status = $marks[id]
        if (status){
            color = "#0075ff";
        }
        else{
            color = "#f0f0f0";
        }
        let item = row*10+order;
        active = items.has(item);
        if ( ! active ){
            color = "#f8f8f8"
        }
	});

    $: {
        id=label + row + order;
        let item = row*10+order;
        active = items.has(item);
        // const status = $marks[id]

        // if (status){
        //     directory[id].style.backgroundColor = "#0075ff";
        //     directory[id].style.color = "#fff";
        // }
        // else{
        //     directory[id].style.backgroundColor = "#f0f0f0";
        //     directory[id].style.color = "#000";
        // }
    }

	function buttonPressed() {
        // invoke signal
		dispatch('search', {
			text: id
		});
	}

    export function mark() {
        console.log(id, "marked")
    }

</script>

<button bind:this={directory[id]} disabled={!active} on:click={buttonPressed} style="background-color: {color}">
    <!-- {id} -->
</button>

<style>
    button {
        width: 20px;
        height: 20px;
    }
    button:disabled{
        border: 0;
    }
</style>
