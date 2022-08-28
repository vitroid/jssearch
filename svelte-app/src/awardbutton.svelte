<script>
    import { createEventDispatcher,onMount } from 'svelte';
    import { directory } from "./directory.js";
    import { all_talks,marks } from './stores.js';
	const dispatch = createEventDispatcher();

    export let id
    export let title=""

    let active = false
    let bgcolor = "#888"
    let color = "#000"

    onMount(() => {
        const status = $marks[id]
        if (status){
            bgcolor = "#0075ff";
            color="#fff"
        }
        else{
            bgcolor = "#f0f0f0";
            color="#000"
        }
        active = all_talks.has(id)
        if ( ! active ){
            bgcolor = "#f8f8f8"
        }
	});

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

<button bind:this={directory[id]} disabled={!active} on:click={buttonPressed} style="background-color: {bgcolor}; color: {color}; ">
    {@html title}
</button>

<style>
    button {
        min-width: 120px;
        width: 100%;
    }
    button:disabled{
        border: 0;
    }
</style>
