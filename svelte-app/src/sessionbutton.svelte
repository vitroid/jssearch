<script>
    import { createEventDispatcher,onMount } from 'svelte';
    import { directory } from "./directory.js";
    import { all_talks,marks } from './stores.js';
	const dispatch = createEventDispatcher();

    export let id

    let active = false
    let color = "#888"

    onMount(() => {
        const status = $marks[id]
        if (status){
            color = "#0075ff";
        }
        else{
            color = "#f0f0f0";
        }
        active = all_talks.has(id)
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

<button bind:this={directory[id]} disabled={!active} on:click={buttonPressed} style="background-color: {color}">
    <!-- {@html id} -->
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
